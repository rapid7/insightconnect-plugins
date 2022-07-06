import insightconnect_plugin_runtime
from .schema import DeleteContainerInput, DeleteContainerOutput, Input, Output, Component


# Custom imports below


class DeleteContainer(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_container",
            description=Component.DESCRIPTION,
            input=DeleteContainerInput(),
            output=DeleteContainerOutput(),
        )

    def run(self, params: dict = None):
        self.connection.api_client.delete_container(
            container_name=params.get(Input.CONTAINER_NAME), additional_headers=params.get(Input.ADDITIONAL_HEADERS, {})
        )
        return {Output.SUCCESS: True, Output.MESSAGE: "Container deletion was successfully submitted."}
