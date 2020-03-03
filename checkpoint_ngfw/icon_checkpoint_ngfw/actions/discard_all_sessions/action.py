import komand
from .schema import DiscardAllSessionsInput, DiscardAllSessionsOutput, Output, Component
# Custom imports below


class DiscardAllSessions(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='discard_all_sessions',
                description=Component.DESCRIPTION,
                input=DiscardAllSessionsInput(),
                output=DiscardAllSessionsOutput())

    def run(self, params={}):
        self.connection.discard_all_sessions()
        self.connection.logout()
        return {Output.SUCCESS: True}
