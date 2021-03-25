import komand
from .schema import AvSampleInput, AvSampleOutput

# Custom imports below
import requests
import json


class AvSample(komand.Action):

    API_URL = "https://www.threatminer.org/av.php?api=True&rt=1"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="av_sample",
            description="Fetches information related to a virus",
            input=AvSampleInput(),
            output=AvSampleOutput(),
        )

    def run(self, params={}):
        query = params.get("query")

        try:
            response = requests.get(self.API_URL, params={"q": query})
            return {"response": response.json()}

        except requests.exceptions.HTTPError as e:
            self.logger.error(
                "Requests: HTTPError: status code %s for %s",
                str(e.status_code),
                params.get("query"),
            )

    def test(self):
        params = {"q": "Trojan.Enfal"}
        response = requests.get(self.API_URL, params=params)
        if response.status_code != 200:
            raise Exception("%s (HTTP status: %s)" % (response.text, response.status_code))

        return {"status_code": response.status_code}
