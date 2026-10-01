import insightconnect_plugin_runtime
from .schema import SendMessageByGuidInput, SendMessageByGuidOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean
from icon_microsoft_teams.util.words_utils import add_words_values_to_message


class SendMessageByGuid(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="send_message_by_guid",
            description=Component.DESCRIPTION,
            input=SendMessageByGuidInput(),
            output=SendMessageByGuidOutput(),
        )

    def run(self, params={}):
        team_guid = params.get(Input.TEAM_GUID)
        channel_guid = params.get(Input.CHANNEL_GUID)
        is_html = params.get(Input.IS_HTML)
        message_content = params.get(Input.MESSAGE)

        content_type = "html" if is_html else "text"

        result = self.connection.bot.send_channel_message(
            team_id=team_guid,
            channel_id=channel_guid,
            message=message_content,
            content_type=content_type,
        )

        output_message = {
            "body": {"contentType": content_type, "content": message_content},
            "id": result.get("id", ""),
        }
        output_message = remove_null_and_clean(output_message)
        output_message = add_words_values_to_message(output_message)

        return {Output.MESSAGE: output_message}
