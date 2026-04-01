import insightconnect_plugin_runtime
from .schema import (
    SendHtmlMessageInput,
    SendHtmlMessageOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from icon_microsoft_teams.util.teams_utils import (
    get_teams_from_microsoft,
    get_channels_from_microsoft,
    send_html_message,
)
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean
from icon_microsoft_teams.util.words_utils import add_words_values_to_message
from insightconnect_plugin_runtime.exceptions import PluginException


class SendHtmlMessage(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="send_html_message",
            description=Component.DESCRIPTION,
            input=SendHtmlMessageInput(),
            output=SendHtmlMessageOutput(),
        )

    def run(self, params={}):
        message = params.get(Input.MESSAGE_CONTENT)
        team = params.get(Input.TEAM_NAME, None)
        channel = params.get(Input.CHANNEL_NAME, None)
        chat_id = params.get(Input.CHAT_ID, None)
        team_id = None
        channel_id = None

        if team and channel:
            teams = get_teams_from_microsoft(self.logger, self.connection, team)
            team_id = teams[0].get("id")
            channels = get_channels_from_microsoft(self.logger, self.connection, team_id, channel)
            channel_id = channels[0].get("id")

        if not chat_id and not team_id and not channel_id:
            raise PluginException(
                cause="No chat ID or team ID with channel ID was provided.",
                assistance="Please provide the chat ID to send the chat message or the team and channel details(name or"
                " GUID) to send the message to a specific channel.",
            )
        message = send_html_message(
            self.logger,
            self.connection,
            message,
            team_id,
            channel_id,
            thread_id=params.get(Input.THREAD_ID, None),
            chat_id=chat_id,
        )

        message = remove_null_and_clean(message)
        message = add_words_values_to_message(message)

        return {Output.MESSAGE: message}
