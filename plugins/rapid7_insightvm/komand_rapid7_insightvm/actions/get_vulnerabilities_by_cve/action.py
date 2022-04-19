import insightconnect_plugin_runtime
from .schema import GetVulnerabilitiesByCveInput, GetVulnerabilitiesByCveOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetVulnerabilitiesByCve(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_vulnerabilities_by_cve",
            description="Get vulnerabilities details associated with a CVE",
            input=GetVulnerabilitiesByCveInput(),
            output=GetVulnerabilitiesByCveOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        cve_id = params.get("cve_id")
        endpoint = endpoints.Vulnerability.vulnerability_checks(self.connection.console_url)
        self.logger.info(f"Using {endpoint}...")
        params = {"search": cve_id}

        results = resource_helper.paged_resource_request(endpoint=endpoint, method="get", params=params)

        # Get unique vulnerability IDs
        vuln_ids = set()
        for r in results:
            vuln_ids.add(r["vulnerability"])
        self.logger.info(f"Received {len(vuln_ids)} vulnerability IDs from search, getting details...")
        # Get vulnerability details
        vulns = []
        for v in vuln_ids:
            endpoint = endpoints.Vulnerability.vulnerability(self.connection.console_url, v)
            response = resource_helper.resource_request(endpoint=endpoint)
            vulns.append(response)

        return {"vulnerabilities": vulns}
