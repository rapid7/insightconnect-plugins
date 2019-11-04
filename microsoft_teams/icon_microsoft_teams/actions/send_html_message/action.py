import komand
from .schema import SendHtmlMessageInput, SendHtmlMessageOutput, Input, Output, Component
# Custom imports below
from icon_microsoft_teams.util.teams_utils import get_teams_from_microsoft, get_channels_from_microsoft, send_html_message
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean


class SendHtmlMessage(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_html_message',
                description=Component.DESCRIPTION,
                input=SendHtmlMessageInput(),
                output=SendHtmlMessageOutput())

    def run(self, params={}):
        team_name = params.get(Input.TEAM_NAME)
        channel_name = params.get(Input.CHANNEL_NAME)
        message = params.get(Input.MESSAGE_CONTENT)

        teams = get_teams_from_microsoft(self.logger, self.connection, team_name)
        team_id = teams[0].get("id")
        channels = get_channels_from_microsoft(self.logger, self.connection, team_id, channel_name)
        channel_id = channels[0].get("id")

        message = send_html_message(self.logger, self.connection, message, team_id, channel_id)

        clean_message = remove_null_and_clean(message)

        return {Output.MESSAGE: clean_message}
