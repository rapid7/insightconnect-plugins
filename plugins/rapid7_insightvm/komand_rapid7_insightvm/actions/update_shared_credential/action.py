import insightconnect_plugin_runtime
from .schema import UpdateSharedCredentialInput, UpdateSharedCredentialOutput, Input, Output, Component
from ...util import endpoints
from ...util.resource_requests import ResourceRequests
from ...util.update_shared_credential_util import make_payload, get_account_input


class UpdateSharedCredential(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_shared_credential",
            description=Component.DESCRIPTION,
            input=UpdateSharedCredentialInput(),
            output=UpdateSharedCredentialOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.SharedCredential.update_shared_credential(
            self.connection.console_url, params.get(Input.ID)
        )
        account = params.get("account")
        account_input = get_account_input(account)
        payload = make_payload(params, account_input)
        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=payload)

        return {Output.LINKS: response.get("links")}
