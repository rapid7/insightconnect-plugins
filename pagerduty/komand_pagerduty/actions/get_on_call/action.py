import insightconnect_plugin_runtime
from .schema import GetOnCallInput, GetOnCallOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import asyncio


class GetOnCall(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_on_call',
                description=Component.DESCRIPTION,
                input=GetOnCallInput(),
                output=GetOnCallOutput())

    def run(self, params={}):
        """Get list of users"""

        response = self.connection.api_connection.get("https://api.pagerduty.com/oncalls")
        try:
            response.raise_for_status()
        except Exception as e:
            raise PluginException(cause="Failed to get on call users",
                                  assistance="Unknown error. Please see the following for more information.",
                                  data=response.text)
        response_object = response.json()

        user_ids = []
        for oncall_object in response_object.get("oncalls"):
            try:
                user_ids.append(oncall_object["user"]["id"])
            except KeyError as e:
                self.logger.info(f"User ID not available: {str(e)}")
                pass

        users = asyncio.run(self.async_get_users(user_ids))

        return {Output.USERS: insightconnect_plugin_runtime.helper.clean(users)}

    async def async_get_users(self, user_ids: list) -> list:
        connection = self.connection.async_connection
        async with connection.get_async_session() as async_session:
            tasks: [asyncio.Future] = []
            for user_id in user_ids:
                url = f"https://api.pagerduty.com/users/{user_id}"
                tasks.append(asyncio.ensure_future(connection.async_request(session=async_session, url=url,
                                                                             method="get")))
                user_objects = await asyncio.gather(*tasks)
                # extract "users" value from object
                users = list()
                for user in user_objects:
                    users.append(user.get('user'))
                return users
