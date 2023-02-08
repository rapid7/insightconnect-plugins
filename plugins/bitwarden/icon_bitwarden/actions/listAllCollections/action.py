import insightconnect_plugin_runtime
from .schema import ListAllCollectionsInput, ListAllCollectionsOutput, Output, Component
from insightconnect_plugin_runtime.helper import clean

# Custom imports below


class ListAllCollections(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="listAllCollections",
            description=Component.DESCRIPTION,
            input=ListAllCollectionsInput(),
            output=ListAllCollectionsOutput(),
        )

    def run(self, params={}) -> dict:
        self.logger.info("[ACTION] Getting a list of collections...")

        return {Output.COLLECTIONS: clean(self.connection.api_client.list_all_collections())}
