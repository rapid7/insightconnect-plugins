import komand
from .schema import CreateIssueCommentInput, CreateIssueCommentOutput, Input, Output, Component
# Custom imports below


class CreateIssueComment(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_issue_comment',
                description=Component.DESCRIPTION,
                input=CreateIssueCommentInput(),
                output=CreateIssueCommentOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
