import insightconnect_plugin_runtime
import github

from insightconnect_plugin_runtime.helper import clean
from komand_github.util.util import handle_gihub_exceptions
from komand_github.actions.user.schema import UserInput, UserOutput, Input, Output, Component


class User(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="user", description=Component.DESCRIPTION, input=UserInput(), output=UserOutput()
        )

    def run(self, params={}):
        username = params.get(Input.USERNAME)

        try:
            github_user = self.connection.github_user
            user_info = github_user.get_user(username)
        except github.GithubException as err:
            handle_gihub_exceptions(err)
            
        user = clean(
            {
                "avatar": getattr(user_info, "avatar_url"),
                "bio": getattr(user_info, "bio"),
                "email": getattr(user_info, "email"),
                "name": getattr(user_info, "name"),
                "url": getattr(user_info, "html_url"),
            }
        )
        return {
            Output.AVATAR: user.get("avatar", ""),
            Output.BIO: user.get("bio", ""),
            Output.EMAIL: user.get("email", ""),
            Output.NAME: user.get("name", ""),
            Output.URL: user.get("url", ""),
        }
