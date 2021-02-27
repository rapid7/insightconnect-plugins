import insightconnect_plugin_runtime
from .schema import CreateServiceRequestInput, CreateServiceRequestOutput, Input, Output, Component
# Custom imports below


class CreateServiceRequest(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_service_request',
                description=Component.DESCRIPTION,
                input=CreateServiceRequestInput(),
                output=CreateServiceRequestOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
