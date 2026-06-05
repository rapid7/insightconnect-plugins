import insightconnect_plugin_runtime
from .schema import GetEndpointsListInput, GetEndpointsListOutput, Component, Input, Output
# Always import PluginException for consistent error handling in InsightConnect
from insightconnect_plugin_runtime.exceptions import PluginException


class GetEndpointsList(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_endpoints_list",
            description=Component.DESCRIPTION,
            input=GetEndpointsListInput(),
            output=GetEndpointsListOutput()
        )

    def run(self, params={}):
        # 1. Retrieve connection details (API Key, Base URL, etc.) from the connection component
        # This assumes your connection class sets self.api_key and self.base_url (or a client wrapper)
        api_key = self.connection.api_key
        base_url = self.connection.base_url  # Example: "https://cloud.gravityzone.bitdefender.com"
        
        # Bitdefender JSON-RPC endpoint for the network/computers service
        # (Ensure your base_url formatting logic matches what's configured in connection.py)
        api_url = f"{base_url.rstrip('/')}/api/v1.0/jsonrpc/network/computers"

        # 2. Extract inputs defined in your plugin.spec.yaml schema
        parent_id = params.get(Input.PARENT_ID)
        is_managed = params.get(Input.IS_MANAGED)
        page = params.get(Input.PAGE, 1)
        per_page = params.get(Input.PER_PAGE, 100)
        
        # Build Bitdefender API filters dictionary if passed
        filters = {}
        if params.get(Input.NAME_FILTER):
            filters["name"] = params.get(Input.NAME_FILTER)

        # 3. Construct Bitdefender parameter structure (corresponds to their documentation)
        rpc_params = {
            "page": page,
            "perPage": per_page
        }
        
        if parent_id:
            rpc_params["parentId"] = parent_id
        if is_managed is not None:
            rpc_params["isManaged"] = is_managed
        if filters:
            rpc_params["filters"] = filters

        # 4. Construct JSON-RPC 2.0 compliant payload envelope
        payload = {
            "jsonrpc": "2.0",
            "method": "getEndpointsList",
            "params": rpc_params,
            "id": "insightconnect-request-id"
        }

        self.logger.info(f"Fetching endpoints list from Bitdefender API. Page: {page}")

        try:
            # Execute the request utilizing the HTTP client helper established in connection.py
            # Or fall back to python requests directly using the base64 API key setup:
            # (Note: InsightConnect prefers passing this through a reusable session object in connection.py)
            response = self.connection.session.post(
                api_url,
                json=payload,
                verify=True
            )
            
            # Check for generic HTTP errors
            response.raise_for_status()
            response_json = response.json()

        except Exception as e:
            raise PluginException(
                cause="Failed to communicate with the Bitdefender GravityZone API.",
                assistance="Please verify your Base URL configuration and network connectivity.",
                data=str(e)
            )

        # 5. Handle Bitdefender JSON-RPC error responses
        if "error" in response_json:
            error_obj = response_json.get("error", {})
            raise PluginException(
                cause=f"Bitdefender API returned an error: {error_obj.get('message', 'Unknown Error')}",
                assistance="Check your input parameters such as parentId, pagination limits, and API key permissions.",
                data=error_obj
            )
            
