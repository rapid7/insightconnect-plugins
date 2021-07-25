import insightconnect_plugin_runtime
from .schema import UpdateDocumentInput, UpdateDocumentOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime import helper


class UpdateDocument(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_document",
            description=Component.DESCRIPTION,
            input=UpdateDocumentInput(),
            output=UpdateDocumentOutput(),
        )

    def run(self, params={}):
        clean_params = helper.clean(params)
        index = clean_params.get(Input.INDEX)
        id_ = clean_params.get(Input.ID)
        retry_on_conflict = clean_params.get(Input.RETRY_ON_CONFLICT)
        wait_for_active_shards = clean_params.get(Input.WAIT_FOR_ACTIVE_SHARDS)
        version = clean_params.get(Input.VERSION)

        query_params = {
            "refresh": clean_params.get(Input.REFRESH),
            "source": clean_params.get(Input.SOURCE),
            "routing": clean_params.get(Input.ROUTING),
            "parent": clean_params.get(Input.PARENT),
            "timeout": clean_params.get(Input.TIMEOUT),
        }
        if retry_on_conflict:
            query_params["retry_on_conflict"] = str(retry_on_conflict)
        if wait_for_active_shards:
            query_params["wait_for_active_shards"] = str(wait_for_active_shards)
        if version:
            query_params["version"] = str(version)

        results = self.connection.client.update(
            index=index,
            _id=id_,
            _type=clean_params.get(Input.TYPE),
            params=query_params,
            script=clean_params.get(Input.SCRIPT),
        )

        if not results:
            raise PluginException(
                cause="Document was not updated", assistance="Please check provided data and try again."
            )
        else:
            return {Output.UPDATE_RESPONSE: insightconnect_plugin_runtime.helper.clean(results)}
