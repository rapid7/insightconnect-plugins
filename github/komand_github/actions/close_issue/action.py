import komand
from .schema import CloseIssueInput, CloseIssueOutput, Input, Output, Component
# Custom imports below


class CloseIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='close_issue',
                description=Component.DESCRIPTION,
                input=CloseIssueInput(),
                output=CloseIssueOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
