import insightconnect_plugin_runtime
from .schema import SendMessageByGuidInput, SendMessageByGuidOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_teams.util.teams_utils import send_html_message, send_message
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

        if is_html:
            message = send_html_message(self.logger, self.connection, message_content, team_guid, channel_guid)
        else:
            message = send_message(self.logger, self.connection, message_content, team_guid, channel_guid)

        clean_message = remove_null_and_clean(message)
        clean_message = add_words_values_to_message(clean_message)

        return {Output.MESSAGE: clean_message}
