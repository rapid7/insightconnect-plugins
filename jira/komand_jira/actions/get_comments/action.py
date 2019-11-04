import komand
from .schema import GetCommentsInput, GetCommentsOutput

# Custom imports below
from ...util import *
from komand.exceptions import PluginException


class GetComments(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_comments',
            description='Get Comments',
            input=GetCommentsInput(),
            output=GetCommentsOutput())

    def run(self, params={}):
        """Run action"""
        issue = self.connection.client.issue(id=params['id'])

        if not issue:
            raise PluginException(cause=f"No issue found with ID: {params['id']}.",
                                  assistance='Please provide a valid issue ID.')

        comments = issue.fields.comment.comments or []

        results = list(map(lambda comment: normalize_comment(comment, logger=self.logger), comments))
        results = komand.helper.clean(results)

        count = len(results)

        return {'count': count, 'comments': results}
