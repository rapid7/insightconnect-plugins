import komand
import requests
import xmltodict
from .schema import DownloadIPAddressesRiskListInput, DownloadIPAddressesRiskListOutput


class DownloadIPAddressesRiskList(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="download_IP_addresses_risk_list",
            description="This action is used to fetch a risk list of the IP addresses that match a specified filtration rule",
            input=DownloadIPAddressesRiskListInput(),
            output=DownloadIPAddressesRiskListOutput(),
        )

    def run(self, params={}):
        try:
            risklist = params.get("list")
            query_headers = {"X-RFToken": self.connection.token}
            query_params = {"format": "xml/stix/1.2", "gzip": "false", "list": risklist}
            results = requests.get(
                "https://api.recordedfuture.com/v2/ip/risklist",
                params=query_params,
                headers=query_headers,
            )
            return dict(xmltodict.parse(results.text))
        except Exception as e:
            self.logger.error("Error: " + str(e))
