import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ListContainersInput, ListContainersOutput, Input, Output, Component

# Custom imports below
from icon_azure_blob_storage.util.constants import DEFAULT_MAX_RESULTS, DEFAULT_TIMEOUT, Container, ContainerProperties
from insightconnect_plugin_runtime.helper import clean


class ListContainers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_containers",
            description=Component.DESCRIPTION,
            input=ListContainersInput(),
            output=ListContainersOutput(),
        )

    def run(self, params: dict = None):
        prefix = params.get(Input.PREFIX, "")
        max_results = params.get(Input.MAX_RESULTS)
        timeout = params.get(Input.TIMEOUT)
        include = params.get(Input.INCLUDE, [])
        if not params:
            raise PluginException(
                cause="No input parameters provided.", assistance="Please provide at least one input parameter."
            )
        if max_results and (max_results < 1 or max_results > DEFAULT_MAX_RESULTS):
            self.logger.info(
                f"Provided max_results = {max_results} is incorrect. Setting max_results = {DEFAULT_MAX_RESULTS}"
            )
            max_results = DEFAULT_MAX_RESULTS
        if timeout and (timeout < 1 or timeout > DEFAULT_TIMEOUT):
            self.logger.info(f"Provided timeout = {timeout} is incorrect. Setting timeout = {DEFAULT_TIMEOUT}s")
            timeout = DEFAULT_TIMEOUT

        json_response = self.connection.api_client.list_containers(
            prefix=prefix,
            max_results=max_results,
            include=include,
            timeout=timeout,
            additional_headers=params.get(Input.ADDITIONAL_HEADERS, {}),
        )
        return self.clean_containers_list_output(clean(json_response))

    @staticmethod
    def clean_containers_list_output(json_response: dict) -> dict:
        new_json_response = {
            Output.MAX_RESULTS: json_response.get("MaxResults", ""),
            Output.PREFIX: json_response.get("Prefix", ""),
            Output.CONTAINERS: json_response.get("Containers", {}).get("Container", []),
        }
        if isinstance(new_json_response.get(Output.CONTAINERS), dict):
            new_json_response[Output.CONTAINERS] = [new_json_response.get(Output.CONTAINERS)]
        for index, container in enumerate(new_json_response.get(Output.CONTAINERS, [])):
            new_container = {
                Container.NAME: container.get("Name", ""),
                Container.DELETED: container.get("Deleted", ""),
                Container.PROPERTIES: container.get("Properties", {}),
                Container.METADATA: container.get("Metadata", {}),
            }

            new_properties = {
                ContainerProperties.LAST_MODIFIED: new_container.get(Container.PROPERTIES, {}).get("Last-Modified", ""),
                ContainerProperties.PUBLIC_ACCESS: new_container.get(Container.PROPERTIES, {}).get("PublicAccess", ""),
                ContainerProperties.ETAG: new_container.get(Container.PROPERTIES, {}).get("Etag", ""),
            }

            new_container[Container.PROPERTIES] = new_properties
            new_json_response[Output.CONTAINERS][index] = new_container
        return clean(new_json_response)
