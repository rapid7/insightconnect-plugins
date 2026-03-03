import insightconnect_plugin_runtime
from .schema import GetCveInput, GetCveOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

# Custom imports below
from komand_rapid7_intelhub.util.api import IntelHubAPI


class GetCve(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_cve",
            description=Component.DESCRIPTION,
            input=GetCveInput(),
            output=GetCveOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        cve_id = params.get(Input.CVE_ID)
        # END INPUT BINDING - DO NOT REMOVE

        api = IntelHubAPI(self.connection, self.logger)

        try:
            response = api.get_cve(cve_id=cve_id)
        except Exception as e:
            self.logger.info(f"CVE {cve_id} not found or error occurred: {str(e)}")
            return {
                Output.CVE: {},
                Output.FOUND: False,
            }

        if not response:
            return {
                Output.CVE: {},
                Output.FOUND: False,
            }

        # Direct CVE endpoint returns the CVE object directly
        cve_data = response

        cve = {
            "cve_id": cve_data.get("cve_id", ""),
            "title": cve_data.get("title", ""),
            "description": cve_data.get("description", ""),
            "severity": cve_data.get("severity", ""),
            "cvss_score": cve_data.get("cvss_score") or cve_data.get("cvss", {}).get("score"),
            "cvss_vector": cve_data.get("cvss_vector") or cve_data.get("cvss", {}).get("vector"),
            "published_date": cve_data.get("published_date", ""),
            "modified_date": cve_data.get("modified_date", ""),
            "references": cve_data.get("references", []),
            "affected_products": cve_data.get("affected_products", []),
        }

        return {
            Output.CVE: clean(cve),
            Output.FOUND: True,
        }
