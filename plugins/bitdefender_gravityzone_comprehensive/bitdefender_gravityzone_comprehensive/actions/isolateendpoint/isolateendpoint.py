import insightconnect_plugin_runtime
from .schema import CreateIsolateEndpointTaskInput, CreateIsolateEndpointTaskOutput, Component, Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException


class CreateIsolateEndpointTask(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_isolate_endpoint_task",
            description=Component.DESCRIPTION,
            input=CreateIsolateEndpointTaskInput(),
            output=CreateIsolateEndpointTaskOutput()
        )

    def run(self, params={}):
        api_key = self.connection.api_key
        base_url = self.connection.base_url
        
        # Isolation actions route explicitly to the incidents JSON-RPC URL path
        api_url = f"{base_url.rstrip('/')}/api/v1.2/jsonrpc/incidents"

        # Extract target endpoint array from standard inputs
        endpoint_ids = params.get(Input.ENDPOINT_IDS, [])

        if not endpoint_ids:
            raise PluginException(
                cause="Missing required arguments.",
                assistance="You must supply at least one endpoint ID to initiate isolation."
            )

        # Build structural JSON-RPC params wrapper
        rpc_params = {
            "endpointIds": endpoint_ids
        }

        payload = {
            "jsonrpc": "2.0",
            "method": "createIsolateEndpointTask",
            "params": rpc_params,
            "id": "insightconnect-isolate-request"
        }

        self.logger.info(f"Submitting isolation task for {len(endpoint_ids)} endpoint target(s).")

        try:
            response = self.connection.session.post(
                api_url,
                json=payload,
                verify=True
            )
            response.raise_for_status()
            response_json = response.json()

        except Exception as e:
            raise PluginException(
                cause="Communication failure while attempting endpoint isolation request.",
                assistance="Verify authorization access rules and routing paths inside GravityZone context.",
                data=str(e)
            )

        if "error" in response_json:
            error_obj = response_json.get("error", {})
            raise PluginException(
                cause=f"Bitdefender API rejected the isolation request: {error_obj.get('message', 'Unknown Error')}",
                assistance="Ensure all target IDs are valid 24-character hex strings and the key has Incident permissions.",
                data=error_obj
            )

        # The API can return an explicit boolean (true) on success or an array containing parent task IDs
        rpc_result = response_json.get("result")
        success = False
        task_ids = []

        if isinstance(rpc_result, bool):
            success = rpc_result
        elif isinstance(rpc_result, list):
            success = True
            task_ids = rpc_result

        return {
            Output.SUCCESS: success,
            Output.TASK_IDS: task_ids
        }