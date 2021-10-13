import insightconnect_plugin_runtime
from .schema import IndexDocumentInput, IndexDocumentOutput, Output, Input, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime import helper


class IndexDocument(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="index_document",
            description=Component.DESCRIPTION,
            input=IndexDocumentInput(),
            output=IndexDocumentOutput(),
        )

    def run(self, params={}):
        version = params.get(Input.VERSION)
        parent = params.get(Input.PARENT)

        query_params = {
            "version_type": params.get(Input.VERSION_TYPE),
            "routing": params.get(Input.ROUTING),
            "timeout": params.get(Input.TIMEOUT),
        }

        if version:
            query_params["version"] = str(version)
        if parent:
            query_params["parent"] = str(parent)

        results = self.connection.client.index(
            index=params.get(Input.INDEX),
            _id=params.get(Input.ID),
            _type=params.get(Input.TYPE),
            params=helper.clean(query_params),
            document=params.get(Input.DOCUMENT),
        )

        if results:
            return {Output.INDEX_RESPONSE: helper.clean(results)}

        raise PluginException(
            cause="Document was not indexed. ", assistance="Please check provided data and try again."
        )
