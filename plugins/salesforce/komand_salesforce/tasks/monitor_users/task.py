import insightconnect_plugin_runtime
from .schema import MonitorUsersInput, MonitorUsersOutput, MonitorUsersState, Component

# Custom imports below
from datetime import datetime, timedelta, timezone
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_salesforce.util.exceptions import ApiException
from komand_salesforce.util.helpers import clean, convert_to_camel_case


class MonitorUsers(insightconnect_plugin_runtime.Task):
    USER_LOGIN_QUERY = "SELECT LoginTime, UserId, LoginType, LoginUrl, SourceIp, Status, Application, Browser FROM LoginHistory WHERE LoginTime >= {start_timestamp} AND LoginTime < {end_timestamp}"
    USERS_QUERY = "SELECT Id, FirstName, LastName, Email, Alias, IsActive FROM User WHERE UserType = 'Standard'"
    UPDATED_USER_QUERY = "SELECT Id, FirstName, LastName, Email, Alias, IsActive FROM User WHERE Id = '{user_id}' AND UserType = 'Standard'"
    USERS_NEXT_PAGE_ID = "users_next_page_id"
    USER_LOGIN_NEXT_PAGE_ID = "user_login_next_page_id"
    LAST_USER_UPDATE_COLLECTION_TIMESTAMP = "last_user_update_collection_timestamp"
    NEXT_USER_COLLECTION_TIMESTAMP = "next_user_collection_timestamp"
    NEXT_USER_LOGIN_COLLECTION_TIMESTAMP = "next_user_login_collection_timestamp"
    LAST_USER_LOGIN_COLLECTION_TIMESTAMP = "last_user_login_collection_timestamp"

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

                    updated_users = []
                    for user_id in user_ids:
                        updated_user = self.connection.api.query(
                            self.UPDATED_USER_QUERY.format(user_id=user_id), None
                        ).get("records", [])
                        if updated_user:
                            updated_users.extend(updated_user)
                    records.extend(self.add_data_type_field(updated_users, "User Update"))

                if get_users:
                    response = self.connection.api.query(self.USERS_QUERY, users_next_page_id)
                    users_next_page_id = response.get("next_page_id")
                    if users_next_page_id:
                        state[self.USERS_NEXT_PAGE_ID] = users_next_page_id
                        has_more_pages = True
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
                    records.extend(self.add_data_type_field(response.get("records", []), "User Login"))
                return convert_to_camel_case(clean(records)), state, has_more_pages, 200, None
            except ApiException as error:
                return [], state, False, error.status_code, error
        except Exception as error:
            return [], state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

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
            record["dataType"] = field_value
        return records
