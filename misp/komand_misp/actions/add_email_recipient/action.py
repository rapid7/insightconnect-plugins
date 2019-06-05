import komand
from .schema import AddEmailRecipientInput, AddEmailRecipientOutput
# Custom imports below


class AddEmailRecipient(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_email_recipient',
                description='Add email recipient to event',
                input=AddEmailRecipientInput(),
                output=AddEmailRecipientOutput())

    def run(self, params={}):
        client = self.connection.client
        dist = {
            "This Organization": "0",
            "This Community": "1",
            "Connected Communities": "2",
            "All Communities": "3"
        }

        try:
            event = client.get_event(params.get('event')),
            proposal = params.get("proposal")

            if isinstance(event, tuple):
                event = event[0]

            recip = client.add_email_dst(event, email=params.get('recipient'),
                                         category='Payload delivery', to_ids=True,
                                         comment=params.get('comment'),
                                         distribution=dist[params.get('distribution')],
                                         proposal=proposal)
        except:
            self.logger.error(recip)
            return {"status": False}

        return {"status": True}

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        self.logger.info(output)
        return {"status": True}
