import insightconnect_plugin_runtime
from .schema import GetEndpointDetailsByHostnameInput, GetEndpointDetailsByHostnameOutput, Input, Output, Component
# Custom imports below


class GetEndpointDetailsByHostname(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_endpoint_details_by_hostname',
                description=Component.DESCRIPTION,
                input=GetEndpointDetailsByHostnameInput(),
                output=GetEndpointDetailsByHostnameOutput())

    def run(self, params={}):
        hostname = params.get(Input.HOSTNAME)
        results = self.connection.xdr_api.get_endpoint_information_by_hostname(hostname)
        endpoints = results.get("reply")
        return {Output.ENDPOINTS: endpoints}
