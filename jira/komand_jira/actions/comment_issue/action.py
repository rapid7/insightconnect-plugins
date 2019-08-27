import komand
from .schema import CommentIssueInput, CommentIssueOutput
# Custom imports below


class CommentIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='comment_issue',
            description='Comment on Issue',
            input=CommentIssueInput(),
            output=CommentIssueOutput())

    def run(self, params={}):
        """Run action"""
        id_ = params['id']
        issue = self.connection.client.issue(id=id_)

        if not issue:
            raise Exception('Error: No issue found with ID: ' + id_)

        comment = self.connection.client.add_comment(issue=issue, body=params['comment'])
        self.logger.info("Returned comment: %s", dir(comment))
        return {'comment_id': comment.id}
