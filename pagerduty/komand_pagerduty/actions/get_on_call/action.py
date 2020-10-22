import komand
from .schema import GetOnCallInput, GetOnCallOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class GetOnCall(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_on_call',
                description=Component.DESCRIPTION,
                input=GetOnCallInput(),
                output=GetOnCallOutput())

    def run(self, params={}):
        # TODO: Implement run function
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
            except Exception as e:
                self.logger.info(f"User ID not available: {str(e)}")
                pass

        users = []
        for user_id in user_ids:
            user_response = self.connection.api_connection.get(f"https://api.pagerduty.com/users/{user_id}")
            users.append(user_response.json().get("user"))

        return {Output.USERS: komand.helper.clean(users)}
