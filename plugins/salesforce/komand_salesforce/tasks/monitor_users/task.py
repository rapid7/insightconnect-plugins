from typing import Tuple

import insightconnect_plugin_runtime
from .schema import MonitorUsersInput, MonitorUsersOutput, MonitorUsersState, Component

from datetime import datetime, timedelta, timezone
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.telemetry import monitor_task_delay
from komand_salesforce.util.exceptions import ApiException

DEFAULT_CUTOFF_HOURS = 24 * 7
INITIAL_LOOKBACK = 24

exp_frmt = "%Y-%m-%d %H:%M:%S.%f%z"  # the format the state should be in
old_frmt = "%Y-%m-%dT%H:%M:%S.%f%z"  # an old backwards compatible state
bugged_frmt = "%Y-%m-%d %H:%M:%S%z"  # str value without the microseconds - SOAR-18202
SUPPORTED_STR_TYPES = [exp_frmt, old_frmt, bugged_frmt]


class MonitorUsers(insightconnect_plugin_runtime.Task):
    USER_LOGIN_QUERY = "SELECT LoginTime, UserId, LoginType, LoginUrl, SourceIp, Status, Application, Browser FROM LoginHistory WHERE LoginTime >= {start_timestamp} AND LoginTime < {end_timestamp}"
    USERS_QUERY = "SELECT Id, FirstName, LastName, Email, Alias, IsActive FROM User WHERE UserType = 'Standard'"
    UPDATED_USER_QUERY = "SELECT Id, FirstName, LastName, Email, Alias, IsActive FROM User WHERE Id = '{user_id}' AND UserType = 'Standard'"
    UPDATED_USERS_QUERY = "SELECT Id, FirstName, LastName, Email, Alias, IsActive FROM User WHERE UserType = 'Standard' AND LastModifiedDate >= {start_timestamp} AND LastModifiedDate < {end_timestamp}"
    USERS_NEXT_PAGE_ID = "users_next_page_id"
    USER_LOGIN_NEXT_PAGE_ID = "user_login_next_page_id"
    UPDATED_USERS_NEXT_PAGE_ID = "updated_users_next_page_id"
    LAST_USER_UPDATE_COLLECTION_TIMESTAMP = "last_user_update_collection_timestamp"
    NEXT_USER_COLLECTION_TIMESTAMP = "next_user_collection_timestamp"
    NEXT_USER_LOGIN_COLLECTION_TIMESTAMP = "next_user_login_collection_timestamp"
    LAST_USER_LOGIN_COLLECTION_TIMESTAMP = "last_user_login_collection_timestamp"
    REMOVE_DUPLICATES = "remove_duplicates"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_users",
            description=Component.DESCRIPTION,
            input=MonitorUsersInput(),
            output=MonitorUsersOutput(),
            state=MonitorUsersState(),
        )

    # pylint: disable=unused-argument
    @monitor_task_delay(
        timestamp_keys=[
            LAST_USER_UPDATE_COLLECTION_TIMESTAMP,
            LAST_USER_LOGIN_COLLECTION_TIMESTAMP,
        ],
        default_delay_threshold="2d",
    )
    def run(self, params={}, state={}, custom_config={}):  # noqa: C901
        self.connection.api.enable_rate_limiting = False
        has_more_pages = False
        try:
            now = self.get_current_time()
            get_users = False
            get_user_login_history = False

            cut_off_time, start_time = self._get_timings(now, custom_config, state)

            remove_duplicates = state.pop(self.REMOVE_DUPLICATES, True)
            users_next_page_id = state.pop(self.USERS_NEXT_PAGE_ID, None)
            user_login_next_page_id = state.pop(self.USER_LOGIN_NEXT_PAGE_ID, None)
            updated_users_next_page_id = state.pop(self.UPDATED_USERS_NEXT_PAGE_ID, None)

            user_update_start_timestamp = start_time
            user_update_last_collection = now
            user_login_start_timestamp = start_time
            user_login_end_timestamp = now

            if not state:
                get_users, get_user_login_history = self._handle_first_run(
                    state, now, user_update_last_collection, user_login_end_timestamp
                )
            elif users_next_page_id or user_login_next_page_id or updated_users_next_page_id:
                get_users, get_user_login_history = self._handle_next_page(
                    users_next_page_id, user_login_next_page_id
                )
            else:
                (
                    get_users,
                    get_user_login_history,
                    user_update_start_timestamp,
                    user_login_start_timestamp,
                ) = self._handle_subsequent_run(
                    state,
                    cut_off_time,
                    now,
                    user_update_last_collection,
                    user_login_end_timestamp,
                )

            try:
                return self._process_records(
                    get_users,
                    get_user_login_history,
                    users_next_page_id,
                    user_login_next_page_id,
                    updated_users_next_page_id,
                    user_update_start_timestamp,
                    user_update_last_collection,
                    user_login_start_timestamp,
                    user_login_end_timestamp,
                    remove_duplicates,
                    state,
                    has_more_pages,
                )
            except ApiException as error:
                self.logger.info(f"An API Exception has been raised. Status code: {error.status_code}. Error: {error}")
                self.connection.api.unset_token()
                return [], state, False, error.status_code, error
        except Exception as error:
            self.logger.info(f"An Exception has been raised. Error: {error}")
            self.connection.api.unset_token()
            return [], state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def _handle_first_run(self, state, now, user_update_last_collection, user_login_end_timestamp):
        self.logger.info("First run")
        get_users = True
        get_user_login_history = True
        state[self.NEXT_USER_COLLECTION_TIMESTAMP] = self.convert_dt_to_string(now + timedelta(hours=24))
        state[self.LAST_USER_UPDATE_COLLECTION_TIMESTAMP] = self.convert_dt_to_string(user_update_last_collection)
        state[self.NEXT_USER_LOGIN_COLLECTION_TIMESTAMP] = self.convert_dt_to_string(now + timedelta(hours=1))
        state[self.LAST_USER_LOGIN_COLLECTION_TIMESTAMP] = self.convert_dt_to_string(user_login_end_timestamp)
        return get_users, get_user_login_history

    def _handle_next_page(self, users_next_page_id, user_login_next_page_id):
        self.logger.info("Getting next page of results...")
        get_users = bool(users_next_page_id)
        get_user_login_history = bool(user_login_next_page_id)
        return get_users, get_user_login_history

    def _handle_subsequent_run(
            self, state, cut_off_time, now, user_update_last_collection, user_login_end_timestamp
    ):
        self.logger.info("Subsequent run")
        valid_state, key = self._make_valid_state(state)
        if not valid_state:
            self.logger.info(
                f"Bad request error occurred. Invalid timestamp format for {key}. Got value {state[key]}"
            )
            raise PluginException(
                preset=PluginException.Preset.BAD_REQUEST, data=f"Invalid timestamp format for {key}"
            )

        get_users = False
        get_user_login_history = False

        user_update_start_timestamp = self._get_recent_timestamp(
            state, cut_off_time, self.LAST_USER_UPDATE_COLLECTION_TIMESTAMP
        )
        state[self.LAST_USER_UPDATE_COLLECTION_TIMESTAMP] = self.convert_dt_to_string(user_update_last_collection)

        next_user_collection_timestamp = state.get(self.NEXT_USER_COLLECTION_TIMESTAMP)
        if next_user_collection_timestamp and self.compare_timestamp(
                now, self.convert_to_datetime(next_user_collection_timestamp)
        ):
            get_users = True
            state[self.NEXT_USER_COLLECTION_TIMESTAMP] = self.convert_dt_to_string(now + timedelta(hours=24))

        user_login_start_timestamp = None
        next_user_login_collection_timestamp = state.get(self.NEXT_USER_LOGIN_COLLECTION_TIMESTAMP)
        if next_user_login_collection_timestamp and self.compare_timestamp(
                now, self.convert_to_datetime(next_user_login_collection_timestamp)
        ):
            get_user_login_history = True
            state[self.NEXT_USER_LOGIN_COLLECTION_TIMESTAMP] = self.convert_dt_to_string(now + timedelta(hours=1))
            user_login_start_timestamp = self._get_recent_timestamp(
                state, cut_off_time, self.LAST_USER_LOGIN_COLLECTION_TIMESTAMP
            )
            state[self.LAST_USER_LOGIN_COLLECTION_TIMESTAMP] = self.convert_dt_to_string(user_login_end_timestamp)
        else:
            user_login_start_timestamp = None

        return get_users, get_user_login_history, user_update_start_timestamp, user_login_start_timestamp

    def _process_records(
            self,
            get_users,
            get_user_login_history,
            users_next_page_id,
            user_login_next_page_id,
            updated_users_next_page_id,
            user_update_start_timestamp,
            user_update_last_collection,
            user_login_start_timestamp,
            user_login_end_timestamp,
            remove_duplicates,
            state,
            has_more_pages,
    ):
        records = []

        if not users_next_page_id and not user_login_next_page_id or updated_users_next_page_id:
            msg = f"Get updated users - start: {user_update_start_timestamp} end: {user_update_last_collection}"
            if updated_users_next_page_id:
                msg += f", next page ID: {updated_users_next_page_id}"
            self.logger.info(msg)
            response = self.connection.api.query(
                self.UPDATED_USERS_QUERY.format(
                    start_timestamp=user_update_start_timestamp.isoformat(timespec="microseconds"),
                    end_timestamp=user_update_last_collection.isoformat(timespec="microseconds"),
                ),
                updated_users_next_page_id,
            )
            updated_users_next_page_id = response.get("next_page_id")
            updated_users = response.get("records")
            if updated_users_next_page_id:
                state[self.UPDATED_USERS_NEXT_PAGE_ID] = updated_users_next_page_id
                has_more_pages = True

            self.logger.info(f"{len(updated_users)} updated users added to output")
            records.extend(self.add_data_type_field(updated_users, "User Update"))

        if get_users:
            self.logger.info("Get all internal users")
            response = self.connection.api.query(self.USERS_QUERY, users_next_page_id)
            users = response.get("records", [])
            users_next_page_id = response.get("next_page_id")
            if users_next_page_id:
                state[self.USERS_NEXT_PAGE_ID] = users_next_page_id
                has_more_pages = True

            self.logger.info(f"{len(users)} internal users added to output")
            records.extend(self.add_data_type_field(users, "User"))

        if get_user_login_history:
            msg = (
                f"Get user login history - start: {user_login_start_timestamp} end: {user_login_end_timestamp}"
            )
            if user_login_next_page_id:
                msg += f", next page ID: {user_login_next_page_id}"
            self.logger.info(msg)
            response = self.connection.api.query(
                self.USER_LOGIN_QUERY.format(
                    start_timestamp=user_login_start_timestamp.isoformat(timespec="microseconds"),
                    end_timestamp=user_login_end_timestamp.isoformat(timespec="microseconds"),
                ),
                user_login_next_page_id,
            )
            users_login = response.get("records", [])
            user_login_next_page_id = response.get("next_page_id")

            if remove_duplicates is True:
                users_login = self.remove_duplicates_user_login_history(users_login)

            if user_login_next_page_id:
                state[self.USER_LOGIN_NEXT_PAGE_ID] = user_login_next_page_id
                has_more_pages = True

            self.logger.info(f"{len(users_login)} users login history added to output")
            records.extend(self.add_data_type_field(users_login, "User Login"))
        self.connection.api.unset_token()
        return records, state, has_more_pages, 200, None

    def _make_valid_state(self, state: dict) -> Tuple[bool, str]:
        # it looks like we used to store the timestamp in the state with the `T` delimiter and then swapped when we
        # started to do str(datetime) which does not have this delimiter but then swap it back and forward throughout
        # the task logic. Allow the state to have any and a time without the microseconds also.
        last_attempt = len(SUPPORTED_STR_TYPES) - 1
        for key, value in state.items():
            for attempt_x, str_format in enumerate(SUPPORTED_STR_TYPES):
                try:
                    dt_value = datetime.strptime(value, str_format)
                    state[key] = self.convert_dt_to_string(dt_value)
                    break  # we're happy with this state value now move to the next one
                except ValueError:
                    if attempt_x != last_attempt:
                        continue  # try the next type
                return False, key
        return True, ""

    def _get_recent_timestamp(self, state: dict, fallback_timestamp: datetime, key: str) -> datetime:
        """
        Obtain a timestamp, assuring it's not anterior to a given fallback_timestamp.

        Extracts the timestamp from `state` utilizing `key`. Should it be
        antedated in comparison to `fallback_timestamp`, we opt for
        `fallback_timestamp` to ensure recentness in data processing.

        :param state: A dictionary anticipated to store our timestamps.
        :param fallback_timestamp: A datetime object representing the absolute
                                   oldest permissible timestamp.
        :param key: The key used to extract our timestamp from `state`.
        :return: A datetime object that is assured to be no older than
                 `fallback_timestamp`.
        """
        stored_timestamp = self.convert_to_datetime(state.get(key, fallback_timestamp))
        new_ts = max(stored_timestamp, fallback_timestamp)

        if new_ts != stored_timestamp:
            self.logger.info(
                f"State stored timestamp is: {stored_timestamp}, "
                f"returning {new_ts} to keep within our fallback period."
            )
        return new_ts

    def _get_timings(self, now: datetime, custom_config: dict, state: dict) -> Tuple[datetime, datetime]:
        """
        If custom_config values have been passed to the task use these to calculate lookback and cut off
        values otherwise default to a lookback and cut off being 24 hours.

        Args:
            now (datetime): datetime object that holds the current time
            custom_config (dict): dictionary containing values passed from the SDK to calculate timing values.
            state (dict): existing state of the integration used to fine tune the logger.

        Returns:
            cut_off_time (datetime): datetime that will be used to stop time values going back beyond a set date.
            lookback_time (datetime): datetime to use on the first run to carry out a backfill of data.
        """
        cut_off_timings, lookback_time = custom_config.get("cutoff", {}), custom_config.get("lookback")

        cut_off_date, cut_off_hours = cut_off_timings.get("date"), cut_off_timings.get("hours", DEFAULT_CUTOFF_HOURS)
        cut_off_time = (
            datetime(**cut_off_date, tzinfo=timezone.utc) if cut_off_date else now - timedelta(hours=cut_off_hours)
        )

        log_msg = f"Cut off time being applied: {cut_off_time}"
        if lookback_time:
            start_time = datetime(**lookback_time, tzinfo=timezone.utc)
            additional_msg = f", along with custom lookback of {start_time}"
        else:
            start_time = now - timedelta(hours=INITIAL_LOOKBACK)
            additional_msg = f", along with lookback time of {INITIAL_LOOKBACK} hours ({start_time})"

        if not state:  # we only care about lookback time if there's no state.
            log_msg += additional_msg
        self.logger.info(log_msg)
        return cut_off_time, start_time

    def remove_duplicates_user_login_history(self, records: list) -> list:
        """
        Remove duplicate entries from the provided list of records based on a hash of non-time fields.

        Args:
            records (list): A list containing the records to be de-duplicated.

        Returns:
            list: A list containing only the unique records from the input list.
        """
        unique_records = []
        seen_hashes = []

        for record in records:
            hash_record = self._get_non_time_fields_hash(record)
            if hash_record not in seen_hashes:
                unique_records.append(record)
                seen_hashes.append(hash_record)

        if len(records) != len(unique_records):
            self.logger.info(
                f"Removed {len(records) - len(unique_records)} duplicate from a total of {len(records)} duplicate records."
            )
        return unique_records

    def _get_non_time_fields_hash(self, record):
        """
        Calculate a hash based on the non-time fields of a record.

        Args:
            record (dict): A dictionary containing the record data with fields to be used for hash calculation.

        Returns:
            int: A hash value representing the non-time fields of the record.
        """
        return hash(
            str(record.get("userId", ""))
            + str(record.get("LoginType", ""))
            + str(record.get("LoginUrl", ""))
            + str(record.get("SourceIp", ""))
            + str(record.get("Status", ""))
            + str(record.get("Application", ""))
            + str(record.get("Browser", ""))
        )

    @staticmethod
    def get_current_time() -> datetime:
        return datetime.now(timezone.utc)

    @staticmethod
    def compare_timestamp(first_timestamp: datetime, second_timestamp: datetime) -> bool:
        return first_timestamp >= second_timestamp

    @staticmethod
    def convert_to_datetime(timestamp: str) -> datetime:
        return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f%z")

    @staticmethod
    def add_data_type_field(records: list, field_value: str) -> list:
        for record in records:
            record["DataType"] = field_value
        return records

    @staticmethod
    def convert_dt_to_string(timestamp: datetime) -> str:
        # Force microseconds to keep microseconds in the string but remove the `T`
        return timestamp.isoformat(timespec="microseconds").replace("T", " ")
