import insightconnect_plugin_runtime
from .schema import UpdateDocumentInput, UpdateDocumentOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class UpdateDocument(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_document",
            description=Component.DESCRIPTION,
            input=UpdateDocumentInput(),
            output=UpdateDocumentOutput(),
        )

    def run(self, params={}):
        index = params.get(Input.INDEX)
        type_ = params.get(Input.TYPE)
        id_ = params.get(Input.ID)
        retry_on_conflict = params.get(Input.RETRY_ON_CONFLICT)
        wait_for_active_shards = params.get(Input.WAIT_FOR_ACTIVE_SHARDS)
        refresh = params.get(Input.REFRESH)
        source = params.get(Input.SOURCE)
        version = params.get(Input.VERSION)
        routing = params.get(Input.ROUTING)
        parent = params.get(Input.PARENT)
        timeout = params.get(Input.TIMEOUT)
        script = params.get(Input.SCRIPT)

        params = {}
        if retry_on_conflict:
            params["retry_on_conflict"] = str(retry_on_conflict)
        if wait_for_active_shards:
            params["wait_for_active_shards"] = str(wait_for_active_shards)
        if refresh:
            params["refresh"] = refresh
        if source:
            params["source"] = source
        if version:
            params["version"] = str(version)
        if routing:
            params["routing"] = routing
        if parent:
            params["parent"] = parent
        if timeout:
            params["timeout"] = timeout

        results = self.connection.client.update(index, type_, id_, script, params)

        if not results:
            raise PluginException(
                cause="Document was not updated",
                assistance="Please check provided data and try again."
            )
        else:
            return {
                Output.UPDATE_RESPONSE: insightconnect_plugin_runtime.helper.clean(results)
            }

