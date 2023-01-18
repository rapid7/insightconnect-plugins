import insightconnect_plugin_runtime
from .schema import VulnSearchInput, VulnSearchOutput, Input, Output, Component

# Constants below
MAX_SIZE = 500
AVG_SIZE = 200


class VulnSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="vuln_search", description=Component.DESCRIPTION, input=VulnSearchInput(), output=VulnSearchOutput()
        )

    def run(self, params={}):
        asset_crit = params.get(Input.ASSET_CRITERIA)
        vuln_crit = params.get(Input.VULN_CRITERIA)
        size = params.get(Input.SIZE, AVG_SIZE)
        sort_criteria = params.get(Input.SORT_CRITERIA, {})
        parameters = []

        for key, value in sort_criteria.items():
            parameters.append(("sort", f"{key},{value}"))

        if size > MAX_SIZE:
            self.logger.info(f"'{size}' too large, set to max size of 500.")
            size = MAX_SIZE
        if size <= 0:
            self.logger.info(f"'{size}' must be greater than zero, set to average size of 200.")
            size = AVG_SIZE
        parameters.append(("size", size))
        if asset_crit or vuln_crit:
            body = {"asset": asset_crit, "vulnerability": vuln_crit}
            resources = self.connection.ivm_cloud_api.call_api("vulnerabilities", "POST", params, body)
        else:
            resources = self.connection.ivm_cloud_api.call_api("vulnerabilities", "POST", parameters)

        vulns = resources.get("data", [])

        return {Output.VULNERABILITIES: vulns}
