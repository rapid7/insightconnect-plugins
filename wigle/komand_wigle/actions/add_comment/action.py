import komand
from .schema import AddCommentInput, AddCommentOutput
# Custom imports below
from komand_wigle.util.utils import clear_empty_values


class AddComment(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_comment',
                description='Add a comment to the network',
                input=AddCommentInput(),
                output=AddCommentOutput())

    def run(self, params={}):
        self.logger.info('AddComment: Sending a comment to the server ...')

        params = {
            'netid': params.get('netid', ''),
            'comment': params.get('comment', '')
        }
        params = clear_empty_values(params)
        response = self.connection.call_api(
            'post', 'network/comment', data=params
        )
        return response

    def test(self):
        return {
          "comment": "Appended by anon on 2018-08-29 01:05:54:\n\nA comment",
          "netid": "00:1D:73:0B:4F:B0"
        }
