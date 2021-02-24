from icon_domaintools_phisheye.util.helper import Helper

import komand
from komand.exceptions import PluginException
from .schema import DomainListInput, DomainListOutput, Input, Output, Component


class DomainList(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domain_list",
            description=Component.DESCRIPTION,
            input=DomainListInput(),
            output=DomainListOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.QUERY)
        days_back = params.get(Input.DAYS_BACK, None)

        if query not in self.connection.terms:
            raise PluginException(
                cause="Query term not enabled in PhishEye product.",
                assistance=f"Add term to PhishEye and try again, or use one of the allowed terms: {self.connection.terms}.",
            )

        response = Helper.make_request(self.connection.api.phisheye, self.logger, query, days_back)
        output = {
            Output.DOMAINS: response["response"]["domains"],
            Output.TERM: response["response"]["term"],
        }

        if "date" in response["response"]:
            output["date"] = response["response"]["date"]

        return output
