import komand
# Custom imports below
import requests

from .schema import AvReportInput, AvReportOutput


class AvReport(komand.Action):

    API_URL = "https://www.threatminer.org/av.php?api=True&rt=2"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="av_report",
            description="AV Report",
            input=AvReportInput(),
            output=AvReportOutput(),
        )

    def run(self, params={}):
        query = params.get("query")

        try:
            response = requests.get(self.API_URL, params={"q": query}, timeout=10)
            return {"response": response.json()}

        except requests.exceptions.HTTPError as error:
            self.logger.error(
                f"Requests: HTTPError: status code {str(error.response.status_code)} for { params.get('query')}"
            )

    def test(self):
        params = {"q": "Trojan.Enfal"}
        response = requests.get(self.API_URL, params=params, timeout=10)
        if int(response.status_code) != 200:
            raise AssertionError(f"{response.text} (HTTP status: {response.status_code})")

        return {"status_code": response.status_code}
