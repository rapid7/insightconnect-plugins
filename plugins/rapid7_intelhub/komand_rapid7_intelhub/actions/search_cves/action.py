import insightconnect_plugin_runtime
from .schema import SearchCvesInput, SearchCvesOutput, Input, Output, Component
from insightconnect_plugin_runtime.helper import clean

# Custom imports below
from komand_rapid7_intelhub.util.api import IntelHubAPI
from komand_rapid7_intelhub.util.helpers import map_cve


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

        cves = [map_cve(item) for item in response.get("data", [])]

        total_count = response.get("total_count", len(cves))
        pagination = {
            "page": response.get("page", page),
            "page_size": response.get("page_size", page_size),
            "total_count": total_count,
            "total_pages": (total_count + page_size - 1) // page_size if page_size > 0 else 0,
        }

        return {
            Output.CVES: cves,
            Output.PAGINATION: clean(pagination),
        }
