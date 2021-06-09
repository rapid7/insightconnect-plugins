import komand
from .schema import SslReportInput, SslReportOutput

# Custom imports below
import json
import requests


class SslReport(komand.Action):

    API_URL = "https://www.threatminer.org/ssl.php?api=True&rt=2"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="ssl_report",
            description="Fetches information related to a certificate",
            input=SslReportInput(),
            output=SslReportOutput(),
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
        params = {"q": "42a8d5b3a867a59a79f44ffadd61460780fe58f2"}
        response = requests.get(self.API_URL, params=params)
        if response.status_code != 200:
            raise Exception("%s (HTTP status: %s)" % (response.text, response.status_code))

        return {"status_code": response.status_code}
