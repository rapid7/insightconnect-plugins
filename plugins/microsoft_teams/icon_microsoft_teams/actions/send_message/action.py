import insightconnect_plugin_runtime
from .schema import SendMessageInput, SendMessageOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean
from icon_microsoft_teams.util.words_utils import add_words_values_to_message
from insightconnect_plugin_runtime.exceptions import PluginException


class SendMessage(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="send_message",
            description=Component.DESCRIPTION,
            input=SendMessageInput(),
            output=SendMessageOutput(),
        )

    def run(self, params={}):
        message_content = params.get(Input.MESSAGE)
        team_name = params.get(Input.TEAM_NAME)
        channel_name = params.get(Input.CHANNEL_NAME)
        chat_id = params.get(Input.CHAT_ID)
        thread_id = params.get(Input.THREAD_ID)

        team_id = ""
        channel_id = ""

        if team_name and channel_name:
            teams = self.connection.client.get_teams(team_name)
            if teams and isinstance(teams, list):
                team_id = teams[0].get("id")
                channels = self.connection.client.get_channels(team_id, channel_name)
                if channels and isinstance(channels, list):
                    channel_id = channels[0].get("id")

        if not chat_id and not team_id and not channel_id:
            raise PluginException(
                cause="No chat ID or team ID with channel ID was provided.",
                assistance="Please provide the chat ID to send the chat message or the team and channel details "
                "(name or GUID) to send the message to a specific channel.",
            )

        if chat_id:
            result = self.connection.bot.send_chat_message(chat_id, message_content)
        else:
            result = self.connection.bot.send_channel_message(
                team_id=team_id,
                channel_id=channel_id,
                message=message_content,
                content_type="text",
                thread_id=thread_id,
            )

        # Build a message-like output from the bot response
        output_message = {
            "body": {"contentType": "text", "content": message_content},
            "id": result.get("id", ""),
        }
        output_message = remove_null_and_clean(output_message)
        output_message = add_words_values_to_message(output_message)

        return {Output.MESSAGE: output_message}
