import insightconnect_plugin_runtime

from .schema import Component, Input, Output, SslHostsInput, SslHostsOutput

# Custom imports below


class SslHosts(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ssl_hosts",
            description=Component.DESCRIPTION,
            input=SslHostsInput(),
            output=SslHostsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        query = params.get(Input.QUERY, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.RESPONSE: self.connection.api_client.ssl_hosts(query, report=False)}
