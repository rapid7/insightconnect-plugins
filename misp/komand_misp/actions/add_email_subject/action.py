import komand
from .schema import AddEmailSubjectInput, AddEmailSubjectOutput
# Custom imports below


class AddEmailSubject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_email_subject',
                description='Add email subject to event',
                input=AddEmailSubjectInput(),
                output=AddEmailSubjectOutput())

    def run(self, params={}):
        client = self.connection.client
        dist = {
            "This Organization": "0",
            "This Community": "1",
            "Connected Communities": "2",
            "All Communities": "3"
        }
        proposal = params.get("proposal")

        try:
            event = client.get_event(params.get('event'))
            sub = client.add_email_subject(event, email=params.get('subject'),
                                           category='Payload delivery', to_ids=True,
                                           comment=params.get('comment'),
                                           distribution=dist[params.get('distribution')],
                                           proposal=proposal)
        except:
            self.logger.error(event)
            return {"status": False}

        return {"status": True}

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        self.logger.info(output)
        return {"status": True}
