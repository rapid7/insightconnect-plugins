import komand
from .schema import SendMessageInput, SendMessageOutput, Input, Output, Component
# Custom imports below
from icon_microsoft_teams.util import pymsteams


class SendMessage(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_message',
                description=Component.DESCRIPTION,
                input=SendMessageInput(),
                output=SendMessageOutput())

    def run(self, params={}):
        message = params.get(Input.MESSAGE)
        webhook = self.connection.webhook

        teams_message_card = pymsteams.connectorcard(webhook)
        teams_message_card.text(message)

        teams_message_card.send()

        return {Output.SUCCESS: True}
