import insightconnect_plugin_runtime
from .schema import MonitorUsersInput, MonitorUsersOutput, MonitorUsersState, Component

# Custom imports below
from datetime import datetime, timedelta, timezone
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_salesforce.util.exceptions import ApiException
from komand_salesforce.util.helpers import clean, convert_to_camel_case

from ...util.event import UserEvent


class MonitorUsers(insightconnect_plugin_runtime.Task):
    USER_LOGIN_QUERY = "SELECT LoginTime, UserId, LoginType, LoginUrl, SourceIp, Status, Application, Browser FROM LoginHistory WHERE LoginTime >= {start_timestamp} AND LoginTime < {end_timestamp}"
    USERS_QUERY = "SELECT Id, FirstName, LastName, Email, Alias, IsActive FROM User WHERE UserType = 'Standard'"
    UPDATED_USER_QUERY = "SELECT Id, FirstName, LastName, Email, Alias, IsActive FROM User WHERE Id = '{user_id}' AND UserType = 'Standard'"
    UPDATED_USERS_QUERY = "SELECT Id, FirstName, LastName, Email, Alias, IsActive FROM User WHERE UserType = 'Standard' AND Id IN ({user_ids})"
    USERS_NEXT_PAGE_ID = "users_next_page_id"
    USER_LOGIN_NEXT_PAGE_ID = "user_login_next_page_id"
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
        self.connection.api.enable_rate_limiting = False
        has_more_pages = False
        try:
            now = self.get_current_time()
            get_users = False
            get_user_login_history = False

            remove_duplicates = state.pop(self.REMOVE_DUPLICATES, True)  # true as a default
            users_next_page_id = state.get(self.USERS_NEXT_PAGE_ID)
            state.pop(self.USERS_NEXT_PAGE_ID, None)
            user_login_next_page_id = state.get(self.USER_LOGIN_NEXT_PAGE_ID)
            state.pop(self.USER_LOGIN_NEXT_PAGE_ID, None)

            user_update_end_timestamp = now
            user_update_start_timestamp = (user_update_end_timestamp - timedelta(hours=24)).isoformat(
                timespec="milliseconds"
            )
            user_update_last_collection = (user_update_end_timestamp + timedelta(milliseconds=1)).isoformat(
                timespec="milliseconds"
            )
            user_update_end_timestamp = user_update_end_timestamp.isoformat(timespec="milliseconds")

            user_login_end_timestamp = now
            user_login_start_timestamp = user_login_end_timestamp - timedelta(hours=24)

            if not state:
                self.logger.info("First run")
                state[self.LAST_USER_UPDATE_COLLECTION_TIMESTAMP] = user_update_last_collection

                get_users = True
                state[self.NEXT_USER_COLLECTION_TIMESTAMP] = str(now + timedelta(hours=24))

                get_user_login_history = True
                state[self.NEXT_USER_LOGIN_COLLECTION_TIMESTAMP] = str(now + timedelta(hours=1))
                state[self.LAST_USER_LOGIN_COLLECTION_TIMESTAMP] = str(user_login_end_timestamp)
            elif users_next_page_id or user_login_next_page_id:
                self.logger.info("Getting next page of results...")
                if users_next_page_id:
                    get_users = True
                if user_login_next_page_id:
                    get_user_login_history = True
            else:
                self.logger.info("Subsequent run")
                user_update_start_timestamp = state.get(self.LAST_USER_UPDATE_COLLECTION_TIMESTAMP)
                state[self.LAST_USER_UPDATE_COLLECTION_TIMESTAMP] = user_update_last_collection
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
                    user_login_start_timestamp = self.convert_to_datetime(
                        state.get(self.LAST_USER_LOGIN_COLLECTION_TIMESTAMP)
                    )
                    state[self.LAST_USER_LOGIN_COLLECTION_TIMESTAMP] = str(user_login_end_timestamp)

            try:
                records = []

                if not users_next_page_id and not user_login_next_page_id:
                    user_ids = self.connection.api.get_updated_users(
                        {
                            "start": user_update_start_timestamp,
                            "end": user_update_end_timestamp,
                        }
                    ).get("ids", [])
                    self.logger.info(f"Found {len(user_ids)} updated users")
                    if user_ids:
                        user_ids_quoted = ["'" + x + "'" for x in user_ids]
                        concatenated_ids = ",".join(user_ids_quoted)
                        updated_users = self.connection.api.query(
                            self.UPDATED_USERS_QUERY.format(user_ids=concatenated_ids), None
                        ).get("records", [])

                        self.logger.info(f"{len(updated_users)} updated users added to output")
                        records.extend(self.add_data_type_field(updated_users, "User Update"))

                if get_users:
                    response = self.connection.api.query(self.USERS_QUERY, users_next_page_id)
                    users_next_page_id = response.get("next_page_id")
                    if users_next_page_id:
                        state[self.USERS_NEXT_PAGE_ID] = users_next_page_id
                        has_more_pages = True

                    self.logger.info(f"{len(response.get('records'))} users added to output")
                    records.extend(self.add_data_type_field(response.get("records", []), "User"))

                if get_user_login_history:
                    response = self.connection.api.query(
                        self.USER_LOGIN_QUERY.format(
                            start_timestamp=user_login_start_timestamp.isoformat(),
                            end_timestamp=user_login_end_timestamp.isoformat(),
                        ),
                        user_login_next_page_id,
                    )
                    user_login_next_page_id = response.get("next_page_id")
                    if user_login_next_page_id:
                        state[self.USER_LOGIN_NEXT_PAGE_ID] = user_login_next_page_id
                        has_more_pages = True

                    self.logger.info(f"{len(response.get('records'))} users login added to output")
                    records.extend(self.add_data_type_field(response.get("records", []), "User Login"))

                if remove_duplicates is True:
                    records = self.remove_duplicates(records)

                records = [record.__dict__ for record in records]

                return convert_to_camel_case(clean(records)), state, has_more_pages, 200, None
            except ApiException as error:
                return [], state, False, error.status_code, error
        except Exception as error:
            return [], state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def remove_duplicates(self, records: list) -> list:
        """
         Remove duplicate entries from the provided list of records.

        Args:
            records (list): A list containing the records to be de-duplicated.

        Returns:
            list: A list containing only the unique records from the input list.
        """
        unique_records = list(dict.fromkeys(records))
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
        event_records = []
        for record in records:
            record["dataType"] = field_value
            event_records.append(UserEvent(**record))
        return event_records
