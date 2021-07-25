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
        clean_params = helper.clean(params)
        index = clean_params.get(Input.INDEX)
        id_ = clean_params.get(Input.ID)
        version = clean_params.get(Input.VERSION)
        document = clean_params.get(Input.DOCUMENT)
        parent = clean_params.get(Input.PARENT)

        query_params = {
            "version_type": clean_params.get(Input.VERSION_TYPE),
            "routing": clean_params.get(Input.ROUTING),
            "timeout": clean_params.get(Input.TIMEOUT),
        }
        if version:
            query_params["version"] = str(version)
        if parent:
            query_params["parent"] = str(parent)

        results = self.connection.client.index(
            index=index, _id=id_, _type=clean_params.get(Input.TYPE), params=query_params, document=document
        )
        if results:
            return {Output.INDEX_RESPONSE: insightconnect_plugin_runtime.helper.clean(results)}

        raise PluginException(
            cause="Document was not indexed. ", assistance="Please check provided data and try again."
        )
