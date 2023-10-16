import insightconnect_plugin_runtime
from .schema import GetOnCallInput, GetOnCallOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_pagerduty.util.util import normalize_user


class GetOnCall(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_on_call",
            description=Component.DESCRIPTION,
            input=GetOnCallInput(),
            output=GetOnCallOutput(),
        )

    def run(self, params={}):
        schedule_id = params.get("schedule_id")

        if schedule_id is None:
            self.logger.warning("Please ensure a valid 'schedule_id' is provided")
            raise PluginException(
                cause="Missing required paramaters", assistance="Please ensure a valid 'schedule_id' is provided"
            )

        user_ids = []
        for oncall_object in self.connection.api.get_on_calls(schedule_id).get("schedule", {}).get("users", []):
            try:
                if oncall_object.get("deleted_at", None):
                    self.logger.info(oncall_object)
                    self.logger.warning(
                        f"The following user {oncall_object.get('id')} is part of the schedule but has been deleted"
                    )
                else:
                    user_ids.append(oncall_object["id"])
            except KeyError as e:
                self.logger.warning(f"User ID not available: {str(e)}")
                continue

        if not user_ids and schedule_id:
            self.logger.warning(
                f"No users found for the provided schedule ID - {schedule_id}. "
                "Please make sure that the schedule used is correct."
            )

        list_of_users = []
        for user_id in user_ids:
            try:
                user_info = self.connection.api.get_user_by_id(user_id).get("user", {})
            except Exception as e:
                self.logger.warning(f"No information was found for the user - {user_id}")
                continue

            if user_info:
                list_of_users.append(normalize_user(user_info))

        return {"users": list_of_users}
