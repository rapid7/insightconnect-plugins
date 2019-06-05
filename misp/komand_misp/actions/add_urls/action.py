import komand
from .schema import AddUrlsInput, AddUrlsOutput
# Custom imports below


class AddUrls(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_urls',
                description='Add URLs to event',
                input=AddUrlsInput(),
                output=AddUrlsOutput())

    def run(self, params={}):

        dist = {
            "This Organization": "0",
            "This Community": "1",
            "Connected Communities": "2",
            "All Communities": "3"
        }

        urls = params.get("urls")
        client = self.connection.client
        event = client.get_event(params.get("event"))
        d = dist.get(params.get("distribution"))
        proposal = params.get("proposal")


        try:
            for url in urls:
                client.add_url(event, url, category='Network activity', to_ids=False,
                               comment=(params.get("comment") or None), distribution=d, proposal=proposal)
            return {"status": True}
        except Exception as e:
            self.logger.error("An error has occurred adding one or more URLs. Error: {}".format(e))
            return {"status": False}

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        self.logger.info(output)
        return {"status": True}
