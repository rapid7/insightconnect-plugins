import insightconnect_plugin_runtime
from .schema import GetUserInput, GetUserOutput, Input, Output, Component

# Custom imports below


class GetUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user",
            description=Component.DESCRIPTION,
            input=GetUserInput(),
            output=GetUserOutput(),
        )

    def run(self, params={}):
        user_id = params.get(Input.ID)
        response = self.connection.client.get_user(user_id=user_id)

        return {
            Output.AVATAR_URL: response.get("avatar_url", "None"),
            Output.BIO: response.get("bio", "None"),
            Output.CREATED_AT: response.get("created_at", "None"),
            Output.ID: response.get("id", -1),
            Output.LINKEDIN: response.get("linkedin", "None"),
            Output.LOCATION: response.get("location", "None"),
            Output.NAME: response.get("name", "None"),
            Output.ORGANIZATION: response.get("organization", "None"),
            Output.SKYPE: response.get("skype", "None"),
            Output.STATE: response.get("state", "None"),
            Output.TWITTER: response.get("twitter", "None"),
            Output.USERNAME: response.get("username", "None"),
            Output.WEB_URL: response.get("web_url", "None"),
            Output.WEBSITE_URL: response.get("website_url", "None"),
        }
