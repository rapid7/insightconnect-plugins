import komand
from .schema import AddIssueLabelInput, AddIssueLabelOutput, Input, Output, Component
# Custom imports below


class AddIssueLabel(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_issue_label',
                description=Component.DESCRIPTION,
                input=AddIssueLabelInput(),
                output=AddIssueLabelOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
