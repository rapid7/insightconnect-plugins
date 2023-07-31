import json
from typing import Union

import insightconnect_plugin_runtime
from .schema import MonitorUsersInput, MonitorUsersOutput, MonitorUsersState, Component

from datetime import datetime, timedelta, timezone
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_salesforce.util.exceptions import ApiException


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
    def run(self, params={}, state={}):  # noqa: C901
        has_more_pages = False
        try:
            now = self.get_current_time()
            get_users = False
            get_user_login_history = False
            last_24_hours = now - timedelta(hours=24)

            remove_duplicates = state.pop(self.REMOVE_DUPLICATES, True)  # true as a default
            users_next_page_id = state.pop(self.USERS_NEXT_PAGE_ID, None)
            user_login_next_page_id = state.pop(self.USER_LOGIN_NEXT_PAGE_ID, None)
            updated_users_next_page_id = state.pop(self.UPDATED_USERS_NEXT_PAGE_ID, None)

            user_update_end_timestamp = now

            # group of timestamps for retrieving updated users data
            user_update_start_timestamp = user_update_end_timestamp - timedelta(hours=24)
            user_update_last_collection = user_update_end_timestamp

            # group of timestamps for retrieving login history data
            user_login_end_timestamp = now
            user_login_start_timestamp = user_login_end_timestamp - timedelta(hours=24)

            if not state:
                self.logger.info("First run")
                state[self.LAST_USER_UPDATE_COLLECTION_TIMESTAMP] = str(user_update_last_collection)

                get_users = True
                state[self.NEXT_USER_COLLECTION_TIMESTAMP] = str(now + timedelta(hours=24))

                get_user_login_history = True
                state[self.NEXT_USER_LOGIN_COLLECTION_TIMESTAMP] = str(now + timedelta(hours=1))
                state[self.LAST_USER_LOGIN_COLLECTION_TIMESTAMP] = str(user_login_end_timestamp)
            elif users_next_page_id or user_login_next_page_id or updated_users_next_page_id:
                self.logger.info("Getting next page of results...")
                if users_next_page_id:
                    get_users = True
                if user_login_next_page_id:
                    get_user_login_history = True

            else:
                self.logger.info("Subsequent run")

                is_valid_state, key = self._is_valid_state(state)
                if not is_valid_state:
                    return (
                        [],
                        state,
                        False,
                        400,
                        PluginException(
                            preset=PluginException.Preset.BAD_REQUEST, data=f"Invalid timestamp format for {key}"
                        ),
                    )

                user_update_start_timestamp = self._get_recent_timestamp(
                    state, last_24_hours, self.LAST_USER_UPDATE_COLLECTION_TIMESTAMP
                )
                state[self.LAST_USER_UPDATE_COLLECTION_TIMESTAMP] = str(user_update_last_collection)
                next_user_collection_timestamp = state.get(self.NEXT_USER_COLLECTION_TIMESTAMP)
                if next_user_collection_timestamp and self.compare_timestamp(
                    now, self.convert_to_datetime(next_user_collection_timestamp)
                ):
                    get_users = True
                    state[self.NEXT_USER_COLLECTION_TIMESTAMP] = str(now + timedelta(hours=24))

                next_user_login_collection_timestamp = state.get(self.NEXT_USER_LOGIN_COLLECTION_TIMESTAMP)
                if next_user_login_collection_timestamp and self.compare_timestamp(
                    now, self.convert_to_datetime(next_user_login_collection_timestamp)
                ):
                    get_user_login_history = True
                    state[self.NEXT_USER_LOGIN_COLLECTION_TIMESTAMP] = str(now + timedelta(hours=1))
                    user_login_start_timestamp = self._get_recent_timestamp(
                        state, last_24_hours, self.LAST_USER_LOGIN_COLLECTION_TIMESTAMP
                    )
                    state[self.LAST_USER_LOGIN_COLLECTION_TIMESTAMP] = str(user_login_end_timestamp)

            try:
                records = []

                if not users_next_page_id and not user_login_next_page_id or updated_users_next_page_id:
                    self.logger.info(
                        f"Get updated users - start: {user_update_start_timestamp} end: {user_update_last_collection}"
                    )
                    response = self.connection.api.query(
                        self.UPDATED_USERS_QUERY.format(
                            start_timestamp=user_update_start_timestamp.isoformat(),
                            end_timestamp=user_update_last_collection.isoformat(),
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
                    self.logger.info(
                        f"Get user login history - start: {user_login_start_timestamp} end: {user_login_end_timestamp}"
                    )
                    response = self.connection.api.query(
                        self.USER_LOGIN_QUERY.format(
                            start_timestamp=user_login_start_timestamp.isoformat(),
                            end_timestamp=user_login_end_timestamp.isoformat(),
                        ),
                        user_login_next_page_id,
                    )
                    users_login = response.get("records", [])
                    user_login_next_page_id = response.get("next_page_id")
                    if user_login_next_page_id:
                        state[self.USER_LOGIN_NEXT_PAGE_ID] = user_login_next_page_id
                        has_more_pages = True

                    self.logger.info(f"{len(users_login)} users login history added to output")
                    records.extend(self.add_data_type_field(users_login, "User Login"))

                if remove_duplicates is True:
                    records = self.remove_duplicates(records)

                return records, state, has_more_pages, 200, None
            except ApiException as error:
                return [], state, False, error.status_code, error
        except Exception as error:
            return [], state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def _is_valid_state(self, state: dict) -> Union[bool, str]:
        for key, value in state.items():
            try:
                self.convert_to_datetime(value)
            except ValueError:
                try:
                    state[key] = str(self.convert_to_datetime_from_old_format(value))
                except ValueError:
                    state[key] = str(self.get_current_time())
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
        return max(stored_timestamp, fallback_timestamp)

    def remove_duplicates(self, records: list) -> list:
        """
         Remove duplicate entries from the provided list of records.

        Args:
            records (list): A list containing the records to be de-duplicated.

        Returns:
            list: A list containing only the unique records from the input list.
        """
        unique_records = {json.dumps(event, sort_keys=True): event for event in records}
        unique_records = list(unique_records.values())
        if len(records) != len(unique_records):
            self.logger.info(
                f"Removed {len(records) - len(unique_records)} duplicate from a total of {len(records)} duplicate records."
            )
        return unique_records

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

    def convert_to_datetime_from_old_format(self, timestamp: str) -> datetime:
        return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f%z")
