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
        retry_on_conflict = params.get(Input.RETRY_ON_CONFLICT)
        wait_for_active_shards = params.get(Input.WAIT_FOR_ACTIVE_SHARDS)
        version = params.get(Input.VERSION)

        query_params = {
            "refresh": params.get(Input.REFRESH),
            "source": params.get(Input.SOURCE),
            "routing": params.get(Input.ROUTING),
            "parent": params.get(Input.PARENT),
            "timeout": params.get(Input.TIMEOUT),
        }

        if retry_on_conflict:
            query_params["retry_on_conflict"] = str(retry_on_conflict)
        if wait_for_active_shards:
            query_params["wait_for_active_shards"] = str(wait_for_active_shards)
        if version:
            query_params["version"] = str(version)

        results = self.connection.client.update(
            index=params.get(Input.INDEX),
            _id=params.get(Input.ID),
            _type=params.get(Input.TYPE),
            params=helper.clean(query_params),
            script=params.get(Input.SCRIPT),
        )

        if not results:
            raise PluginException(
                cause="Document was not updated", assistance="Please check provided data and try again."
            )
        else:
            return {Output.UPDATE_RESPONSE: helper.clean(results)}
