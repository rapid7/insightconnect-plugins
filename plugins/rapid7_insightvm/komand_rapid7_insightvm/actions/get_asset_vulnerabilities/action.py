import insightconnect_plugin_runtime
from .schema import GetAssetVulnerabilitiesInput, GetAssetVulnerabilitiesOutput, Input, Output

# Custom imports below
import asyncio
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
from operator import itemgetter


class GetAssetVulnerabilities(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_asset_vulnerabilities",
            description="Get vulnerabilities found on an asset. Can only be used if the asset has first been scanned (via Komand or other means)",
            input=GetAssetVulnerabilitiesInput(),
            output=GetAssetVulnerabilitiesOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        asset_id = params.get(Input.ASSET_ID)
        risk_score = params.get(Input.GET_RISK_SCORE, False)

        endpoint = endpoints.VulnerabilityResult.vulnerabilities_for_asset(self.connection.console_url, asset_id)
        resources = resource_helper.paged_resource_request(endpoint=endpoint, method="get")
        if not risk_score:
            return {Output.VULNERABILITIES: resources}
        else:
            resources = self.get_vulnerabilities(resources)
            return {Output.VULNERABILITIES: resources}

    async def async_get_vulnerabilities(self, vuln_ids: list) -> list:
        """
        Prepares a list of vulnerability ids for asynchronous API calls
        :param vuln_ids: A list of vulnerability ids
        :return: A list of vulnerability details
        """
        connection = self.connection.async_connection
        async with connection.get_async_session() as async_session:
            tasks: [asyncio.Future] = []
            for vuln_id in vuln_ids:
                endpoint = endpoints.Vulnerability.vulnerability(self.connection.console_url, vuln_id)
                tasks.append(
                    asyncio.ensure_future(
                        connection.async_request(session=async_session, endpoint=endpoint, method="get")
                    )
                )
            vulnerabilities = await asyncio.gather(*tasks)
            return vulnerabilities

    def get_vulnerabilities(self, resources: list) -> list:
        """
        Finds risk scores for a list of asset_vulnerabilities and attaches them
        :param resources: A list of asset_vulnerabilities
        :return: A list of asset_vulnerabilities with risk scores
        """
        vuln_ids = list()
        risk_score = list()
        for resource in resources:
            try:
                vuln_ids.append(resource["id"])
            except KeyError:
                self.logger.error(f"The following resource did not have an ID:\n{resource}")
                continue

        vulnerabilities = asyncio.run(self.async_get_vulnerabilities(vuln_ids))

        for vulnerability in vulnerabilities:
            risk_score.append({"id": vulnerability["id"], "riskScore": vulnerability["riskScore"]})

        sorted_resources = self.add_risk_scores_to_resources(resources, risk_score)
        return sorted_resources

    @staticmethod
    def add_risk_scores_to_resources(resources: list, risk_scores: list) -> list:
        """
        Sorts asset_vulnerabilities and appends risk scores to them. Returns asset_vulnerabilities list
        sorted by risk score descending
        :param resources: A list of asset_vulnerabilities
        :param risk_scores: A list of risk scores
        :return: A sorted list of asset_vulnerabilities with risk scores attached
        """
        sorted_resources = sorted(resources, key=itemgetter("id"))
        sorted_risk_score = sorted(risk_scores, key=itemgetter("id"))
        for i in range(0, len(sorted_resources), 1):
            sorted_resources[i]["riskScore"] = sorted_risk_score[i]["riskScore"]

        sorted_resources = sorted(sorted_resources, key=itemgetter("riskScore"), reverse=True)
        return sorted_resources
