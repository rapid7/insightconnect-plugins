import insightconnect_plugin_runtime
from .schema import GetOnCallInput, GetOnCallOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import asyncio


class GetOnCall(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_on_call",
            description=Component.DESCRIPTION,
            input=GetOnCallInput(),
            output=GetOnCallOutput(),
        )

    def run(self, params={}):
        schedule_id = params.get(Input.SCHEDULE_ID, None)
        user_ids = []
        for oncall_object in self.connection.api.get_on_calls(schedule_id).get("oncalls", []):
            try:
                user_ids.append(oncall_object["user"]["id"])
            except KeyError as e:
                self.logger.warning(f"User ID not available: {str(e)}")
                continue

        if not user_ids and schedule_id:
            self.logger.warning(
                f"No users found for the provided schedule ID - {schedule_id}. "
                "Please make sure that the schedule used is correct."
            )

        users = asyncio.run(self.async_get_users(user_ids))
        return {Output.USERS: insightconnect_plugin_runtime.helper.clean(users)}

    async def async_get_users(self, user_ids: [str]) -> list:
        connection = self.connection.async_connection
        async with connection.get_async_session() as async_session:
            tasks: [asyncio.Future] = []
            for user_id in user_ids:
                url = f"https://api.pagerduty.com/users/{user_id}"
                tasks.append(
                    asyncio.ensure_future(connection.async_request(session=async_session, url=url, method="get"))
                )
            user_objects = await asyncio.gather(*tasks)
            users = [u.get("user") for u in user_objects]

            return users
