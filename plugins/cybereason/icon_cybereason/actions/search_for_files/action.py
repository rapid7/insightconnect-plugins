import insightconnect_plugin_runtime
from .schema import SearchForFilesInput, SearchForFilesOutput, Input, Output, Component

# Custom imports below
from icon_cybereason.util.api import CybereasonAPI


class SearchForFiles(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_for_files",
            description=Component.DESCRIPTION,
            input=SearchForFilesInput(),
            output=SearchForFilesOutput(),
        )

    def run(self, params={}):
        return {
            Output.RESPONSE: self.connection.api.file_search(
                CybereasonAPI.parse_server_filter(params.get(Input.SERVER_FILTER)),
                CybereasonAPI.parse_file_filter(params.get(Input.FILE_FILTER)),
            )
        }
