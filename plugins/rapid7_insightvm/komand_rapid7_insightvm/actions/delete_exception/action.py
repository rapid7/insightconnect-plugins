import insightconnect_plugin_runtime
from .schema import DeleteExceptionInput, DeleteExceptionOutput, Component

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class DeleteException(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_exception",
            description=Component.DESCRIPTION,
            input=DeleteExceptionInput(),
            output=DeleteExceptionOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)

        id_ = params["exception_id"]

        endpoint = endpoints.VulnerabilityException.vulnerability_exception(self.connection.console_url, id_)
        response = resource_helper.resource_request(endpoint=endpoint, method="delete")
        return response
