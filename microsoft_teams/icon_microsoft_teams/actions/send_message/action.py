import komand
from .schema import SendMessageInput, SendMessageOutput, Input, Output, Component
# Custom imports below
from icon_microsoft_teams.util.teams_utils import get_teams_from_microsoft, get_channels_from_microsoft, send_message
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean


class SendMessage(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_message',
                description=Component.DESCRIPTION,
                input=SendMessageInput(),
                output=SendMessageOutput())

    def run(self, params={}):
        team_name = params.get(Input.TEAM_NAME)
        channel_name = params.get(Input.CHANNEL_NAME)
        message = params.get(Input.MESSAGE)

        teams = get_teams_from_microsoft(self.logger, self.connection, team_name)
        team_id = teams[0].get("id")
        channels = get_channels_from_microsoft(self.logger, self.connection, team_id, channel_name)
        channel_id = channels[0].get("id")

        message = send_message(self.logger, self.connection, message, team_id, channel_id)

        clean_message = remove_null_and_clean(message)

        return {Output.MESSAGE: clean_message}
