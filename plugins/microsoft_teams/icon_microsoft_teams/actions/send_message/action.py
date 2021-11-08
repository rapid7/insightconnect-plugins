import komand
from .schema import SendMessageInput, SendMessageOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_teams.util.teams_utils import (
    get_teams_from_microsoft,
    get_channels_from_microsoft,
    send_message,
)
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean
from icon_microsoft_teams.util.words_utils import add_words_values_to_message


class SendMessage(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="send_message",
            description=Component.DESCRIPTION,
            input=SendMessageInput(),
            output=SendMessageOutput(),
        )

    def run(self, params={}):
        message = params.get(Input.MESSAGE)
        team = params.get(Input.TEAM_NAME)
        channel = params.get(Input.CHANNEL_NAME)

        team_id = ""
        channel_id = ""

        if team and channel:
            teams = get_teams_from_microsoft(self.logger, self.connection, team)
            if teams and isinstance(teams, list):
                team_id = teams[0].get("id")
                channels = get_channels_from_microsoft(self.logger, self.connection, team_id, channel)
                if channels and isinstance(channels, list):
                    channel_id = channels[0].get("id")

        message = send_message(
            self.logger,
            self.connection,
            message,
            team_id,
            channel_id,
            thread_id=params.get(Input.THREAD_ID, None),
            chat_id=params.get(Input.CHAT_ID),
        )

        message = remove_null_and_clean(message)
        message = add_words_values_to_message(message)

        return {Output.MESSAGE: message}
