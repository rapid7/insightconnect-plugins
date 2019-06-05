import komand
from .schema import LookupUrlInput, LookupUrlOutput
# Custom imports below
from copy import copy
from json.decoder import JSONDecodeError


class LookupUrl(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup_url',
                description='Lookup a URL',
                input=LookupUrlInput(),
                output=LookupUrlOutput())

    def run(self, params={}):
        # Copy and update the base request to avoid mutating the original
        self.request = copy(self.connection.request)
        self.request.url, self.request.method = self.request.url + "/intelligence", "GET"

        # Pagination flag and results placeholder
        self.continue_paging, self.results = True, list()
        # Update the request with the supplied domain, page size, and offset
        self.request.params.update({
            "url": "{url}".format(url=params.get("url")),
            "limit": 1000,
            "offset": 0
        })

        while self.continue_paging:
            response = self.connection.session.send(self.request.prepare(), verify=False)

            if response.status_code not in range(200, 299):
                raise Exception(
                    "Error: Received %d HTTP status code from ThreatStream. Please verify your ThreatStream server "
                    "status and try again. If the issue persists please contact support. "
                    "Server response was: %s" % (response.status_code, response.text))

            try:
                response_data = response.json()
            except JSONDecodeError:
                raise Exception("Error: Received an unexpected response from ThreatStream "
                                "(non-JSON or no response was received). Response was: %s" % response.text)

            # Check pagination indicator. A "null" value means no more pages.
            if not response_data["meta"]["next"]:
                self.continue_paging = False

            self.request.params["offset"] += 1000
            self.results.extend(response_data["objects"])

        self.results = komand.helper.clean(self.results)
        return {"results": self.results}

    def test(self):
        # TODO: Implement test function
        return {}
