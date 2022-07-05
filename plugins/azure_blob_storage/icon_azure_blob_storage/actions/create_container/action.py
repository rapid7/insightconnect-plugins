import insightconnect_plugin_runtime
from .schema import CreateContainerInput, CreateContainerOutput, Input, Output, Component


# Custom imports below


class CreateContainer(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_container",
            description=Component.DESCRIPTION,
            input=CreateContainerInput(),
            output=CreateContainerOutput(),
        )

    def run(self, params: dict = None):
        self.connection.api_client.create_container(
            container_name=params.get(Input.CONTAINER_NAME), additional_headers=params.get(Input.ADDITIONAL_HEADERS, {})
        )
        return {Output.SUCCESS: True, Output.MESSAGE: "Container creation was successfully submitted."}
