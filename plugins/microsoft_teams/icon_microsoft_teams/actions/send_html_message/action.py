import insightconnect_plugin_runtime
from .schema import SendHtmlMessageInput, SendHtmlMessageOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_teams.util.teams_utils import (
    get_teams_from_microsoft,
    get_channels_from_microsoft,
    send_html_message,
)
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean
from icon_microsoft_teams.util.words_utils import add_words_values_to_message


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

        teams = get_teams_from_microsoft(self.logger, self.connection, params.get(Input.TEAM_NAME))
        team_id = teams[0].get("id")
        channels = get_channels_from_microsoft(self.logger, self.connection, team_id, params.get(Input.CHANNEL_NAME))

        message = send_html_message(
            self.logger,
            self.connection,
            message,
            team_id,
            channels[0].get("id"),
            thread_id=params.get(Input.THREAD_ID, None),
        )

        message = remove_null_and_clean(message)
        message = add_words_values_to_message(message)

        return {Output.MESSAGE: message}
