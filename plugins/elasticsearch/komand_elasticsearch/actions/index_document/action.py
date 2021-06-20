import insightconnect_plugin_runtime
from .schema import IndexDocumentInput, IndexDocumentOutput, Output, Input, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class IndexDocument(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="index_document",
            description=Component.DESCRIPTION,
            input=IndexDocumentInput(),
            output=IndexDocumentOutput(),
        )

    def run(self, params={}):
        index = params.get(Input.INDEX)
        type_ = params.get(Input.TYPE)
        id_ = params.get(Input.ID)
        version_type = params.get(Input.VERSION_TYPE)
        version = params.get(Input.VERSION)
        document = params.get(Input.DOCUMENT)
        routing = params.get(Input.ROUTING)
        parent = params.get(Input.PARENT)
        timeout = params.get(Input.TIMEOUT)

        params = {}
        if version_type:
            params["version_type"] = version_type
        if version:
            params["version"] = str(version)
        if routing:
            params["routing"] = routing
        if parent:
            params["parent"] = str(parent)
        if timeout:
            params["timeout"] = timeout

        if not id_:
            results = self.connection.client.index(index, type_, document, params)
        else:
            results = self.connection.client.index(index, type_, id_, document, params)

        if not results:
            raise PluginException(
                cause="Document was not indexed. ",
                assistance="Please check provided data and try again."
            )
        else:
            return {
                Output.INDEX_RESPONSE: insightconnect_plugin_runtime.helper.clean(results)
            }
