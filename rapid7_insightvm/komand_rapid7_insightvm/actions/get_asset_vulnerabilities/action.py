import komand
from .schema import GetAssetVulnerabilitiesInput, GetAssetVulnerabilitiesOutput, Input, Output
# Custom imports below
import asyncio
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_helper import ResourceHelper


class GetAssetVulnerabilities(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_asset_vulnerabilities',
                description='Get vulnerabilities found on an asset. Can only be used if the asset has first been scanned (via Komand or other means)',
                input=GetAssetVulnerabilitiesInput(),
                output=GetAssetVulnerabilitiesOutput())

    def run(self, params={}):
        resource_helper = ResourceHelper(self.connection.session, self.logger)
        asset_id = params.get(Input.ASSET_ID)
        risk_score = params.get(Input.GET_RISK_SCORE, False)
        endpoint = endpoints.VulnerabilityResult.vulnerabilities_for_asset(self.connection.console_url, asset_id)

        resources = resource_helper.paged_resource_request(endpoint=endpoint,
                                                           method='get')
        if not risk_score:
            return {Output.VULNERABILITIES: resources}
        else:
            print("temp")

    def get_vulnerabilities(self, resources):
        endpoint = endpoints.Vulnerability.vulnerability(self.connection.console_url)