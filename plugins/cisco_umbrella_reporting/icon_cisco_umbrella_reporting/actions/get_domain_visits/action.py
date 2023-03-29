# Custom imports below
from urllib import parse

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from .schema import Component, GetDomainVisitsInput, GetDomainVisitsOutput, Input, Output
from icon_cisco_umbrella_reporting.util.constants import ORDER_PARAMETER_MAPPING, LIMIT_DEFAULT_VALUE


class GetDomainVisits(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_domain_visits",
            description=Component.DESCRIPTION,
            input=GetDomainVisitsInput(),
            output=GetDomainVisitsOutput(),
        )

    def run(self, params={}):
        address = params.get(Input.ADDRESS, "")
        limit = params.get(Input.LIMIT, LIMIT_DEFAULT_VALUE)
        from_time = params.get(Input.FROM, "")
        order = params.get(Input.ORDER, "")
        verdict = params.get(Input.VERDICT, [])
        threats = params.get(Input.THREATS, [])
        threat_types = params.get(Input.THREATTYPES, [])
        data = clean(
            {
                "domains": parse.urlparse(address).hostname,
                "from": from_time,
                "order": ORDER_PARAMETER_MAPPING.get(order.lower(), "desc"),
                "verdict": ",".join(map(str.lower, verdict)),
                "threats": ",".join(threats),
                "threattypes": ",".join(threat_types),
            }
        )
        return {Output.DOMAIN_VISITS: self.connection.client.destinations_most_recent_request(data, limit)}
