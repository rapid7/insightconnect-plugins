import insightconnect_plugin_runtime
from .schema import SearchCvesInput, SearchCvesOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

# Custom imports below
from komand_rapid7_intelhub.util.api import IntelHubAPI


class SearchCves(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_cves",
            description=Component.DESCRIPTION,
            input=SearchCvesInput(),
            output=SearchCvesOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        search = params.get(Input.SEARCH, "")
        page = params.get(Input.PAGE, 1)
        page_size = params.get(Input.PAGE_SIZE, 10)
        cvss_score = params.get(Input.CVSS_SCORE, "")
        exploitable = params.get(Input.EXPLOITABLE)
        epss_score = params.get(Input.EPSS_SCORE, "")
        cisa_kev = params.get(Input.CISA_KEV)
        last_updated = params.get(Input.LAST_UPDATED, "")
        # END INPUT BINDING - DO NOT REMOVE

        api = IntelHubAPI(self.connection, self.logger)

        try:
            response = api.search_cves(
                search=search,
                page=page,
                page_size=page_size,
                cvss_score=cvss_score,
                exploitable=exploitable,
                epss_score=epss_score,
                cisa_kev=cisa_kev,
                last_updated=last_updated,
            )
        except Exception as e:
            raise PluginException(
                cause="Failed to search CVEs",
                assistance=f"Error: {str(e)}",
            )

        cves = []
        raw_data = response.get("data", [])
        for item in raw_data:
            cve = {
                "cve_id": item.get("cve_id", ""),
                "title": item.get("title", ""),
                "description": item.get("description", ""),
                "severity": item.get("severity", ""),
                "cvss_score": item.get("cvss_score") or item.get("cvss", {}).get("score"),
                "published_date": item.get("published_date", ""),
            }
            cves.append(clean(cve))

        pagination = {
            "page": response.get("page", page),
            "page_size": response.get("page_size", page_size),
            "total_count": response.get("total_count", len(cves)),
            "total_pages": response.get("total_pages", 1),
        }

        return {
            Output.CVES: cves,
            Output.PAGINATION: clean(pagination),
        }
