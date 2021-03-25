import komand
import requests
import xmltodict
from .schema import DownloadDomainRiskListInput, DownloadDomainRiskListOutput


class DownloadDomainRiskList(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="download_domain_risk_list",
            description="This action returns a risk list of domains matching a filtration rule",
            input=DownloadDomainRiskListInput(),
            output=DownloadDomainRiskListOutput(),
        )

    def run(self, params={}):
        try:
            risklist = params.get("list")
            query_headers = self.connection.headers
            query_params = {"format": "xml/stix/1.2", "gzip": "false", "list": risklist}
            results = requests.get(
                "https://api.recordedfuture.com/v2/domain/risklist",
                params=query_params,
                headers=query_headers,
            )
            return dict(xmltodict.parse(results.text))
        except Exception as e:
            self.logger.error("Error: " + str(e))
