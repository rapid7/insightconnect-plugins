import insightconnect_plugin_runtime
from .schema import GetDomainVisitsInput, GetDomainVisitsOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below
from urllib import parse


class GetDomainVisits(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_domain_visits',
            description=Component.DESCRIPTION,
            input=GetDomainVisitsInput(),
            output=GetDomainVisitsOutput())

    def run(self, params={}):
        if params.get(Input.MOST_RECENT, True):
            address = params.get(Input.ADDRESS)
            if not address:
                raise PluginException(
                    cause="Input error.",
                    assistance="The 'domain' input is required when 'Most Recent' input is true."
                )
            return {
                Output.DOMAIN_VISITS: self.connection.client.destinations_most_recent_request(
                    parse.urlparse(address).hostname
                ).get('requests', [])
            }

        return {
            Output.DOMAIN_VISITS: self.connection.client.security_activity_report().get('requests', [])
        }
