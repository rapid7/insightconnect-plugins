import insightconnect_plugin_runtime

from .schema import Component, EmailDomainInput, EmailDomainOutput, Input, Output

# Custom imports below


class EmailDomain(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="email_domain",
            description=Component.DESCRIPTION,
            input=EmailDomainInput(),
            output=EmailDomainOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        email = params.get(Input.EMAIL, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.RESPONSE: self.connection.api_client.email(email, report=False)}
