import insightconnect_plugin_runtime
from .schema import SendHtmlMessageInput, SendHtmlMessageOutput, Input, Output, Component

# Custom imports below
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
        message_content = params.get(Input.MESSAGE_CONTENT)
        team_name = params.get(Input.TEAM_NAME)
        channel_name = params.get(Input.CHANNEL_NAME)
        thread_id = params.get(Input.THREAD_ID)

        teams = self.connection.client.get_teams(team_name)
        if not teams:
            raise PluginException(
                cause="Team not found.",
                assistance=f"Please verify '{team_name}' is a valid team name.",
            )
        team_id = teams[0].get("id")

        channels = self.connection.client.get_channels(team_id, channel_name)
        if not channels:
            raise PluginException(
                cause="Channel not found.",
                assistance=f"Please verify '{channel_name}' is a valid channel name.",
            )
        channel_id = channels[0].get("id")

        result = self.connection.bot.send_channel_message(
            team_id=team_id,
            channel_id=channel_id,
            message=message_content,
            content_type="html",
            thread_id=thread_id,
        )

        output_message = {
            "body": {"contentType": "html", "content": message_content},
            "id": result.get("id", ""),
        }
        output_message = remove_null_and_clean(output_message)
        output_message = add_words_values_to_message(output_message)

        return {Output.MESSAGE: output_message}
