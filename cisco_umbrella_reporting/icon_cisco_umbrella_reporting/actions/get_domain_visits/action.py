import insightconnect_plugin_runtime
from .schema import GetDomainVisitsInput, GetDomainVisitsOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below


class GetDomainVisits(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_domain_visits',
            description=Component.DESCRIPTION,
            input=GetDomainVisitsInput(),
            output=GetDomainVisitsOutput())

    def run(self, params={}):
        if params.get(Input.MOST_RECENT, True):
            if not params.get(Input.DOMAIN):
                raise PluginException(
                    cause="Input error.",
                    assistance="When input 'Most Recent' is true domain input is required."
                )
            return {
                Output.DOMAIN_VISITS: self.connection.client.destinations_most_recent_request(
                    params.get(Input.DOMAIN)
                ).get('requests', [])
            }

        return {
            Output.DOMAIN_VISITS: self.connection.client.security_activity_report().get('requests', [])
        }
