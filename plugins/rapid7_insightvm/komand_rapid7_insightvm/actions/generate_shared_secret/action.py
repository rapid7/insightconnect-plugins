import insightconnect_plugin_runtime
from .schema import GenerateSharedSecretInput, GenerateSharedSecretOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_helpers import V1Session
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GenerateSharedSecret(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="generate_shared_secret",
            description="Generates a shared secret for use with pairing a scan engine using the Engine -> Console communication direction",
            input=GenerateSharedSecretInput(),
            output=GenerateSharedSecretOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        v1_session = V1Session(self.connection.session, self.logger)
        time_to_live = params.get("time_to_live")
        endpoint = endpoints.SharedSecret.generate_shared_secret(self.connection.console_url, time_to_live)

        # Auth to APIv1 and make the request, then deauth
        v1_session.v1_authenticate(self.connection.console_url)
        try:
            response = resource_helper.resource_request(endpoint=endpoint, method="put")
        finally:
            v1_session.v1_deauthenticate(self.connection.console_url)

        return {"shared_secret": response["keyString"]}
