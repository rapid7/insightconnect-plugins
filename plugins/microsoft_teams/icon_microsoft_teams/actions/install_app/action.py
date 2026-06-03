import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import InstallAppInput, InstallAppOutput, Input, Output, Component


class InstallApp(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="install_app",
            description=Component.DESCRIPTION,
            input=InstallAppInput(),
            output=InstallAppOutput(),
        )

    def run(self, params={}):
        team_id = params.get(Input.TEAM_ID, "").strip()
        chat_id = params.get(Input.CHAT_ID, "").strip()
        app_id = params.get(Input.APP_ID, "").strip()

        if not team_id and not chat_id:
            raise PluginException(
                cause="No target specified.",
                assistance="Please provide either a Team ID or a Chat ID to install the app into.",
            )

        if team_id and chat_id:
            raise PluginException(
                cause="Both Team ID and Chat ID were provided.",
                assistance="Please provide only one of Team ID or Chat ID, not both.",
            )

        if team_id:
            self.connection.client.install_app_in_team(team_id, app_id)
        else:
            self.connection.client.install_app_in_chat(chat_id, app_id)

        return {Output.SUCCESS: True}
