import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import SearchSecurityIncidentInput, SearchSecurityIncidentOutput, Input, Output, Component

# Custom imports below
from icon_servicenow.util.security_incident_helper import convert_security_incident_fields
from insightconnect_plugin_runtime.helper import return_non_empty


class SearchSecurityIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_security_incident",
            description=Component.DESCRIPTION,
            input=SearchSecurityIncidentInput(),
            output=SearchSecurityIncidentOutput(),
        )

    def run(self, params={}):
        search_params = {
            "sysparm_query": params.get(Input.QUERY),
            "sysparm_limit": (
                params.get(Input.LIMIT) if params.get(Input.LIMIT) and params.get(Input.LIMIT) > 0 else None
            ),
            "sysparm_offset": (
                params.get(Input.OFFSET) if params.get(Input.OFFSET) and params.get(Input.OFFSET) >= 0 else None
            ),
            "sysparm_fields": params.get(Input.FIELDS),
        }

        response = self.connection.request.make_request(
            endpoint=self.connection.security_incident_url,
            method="GET",
            params=return_non_empty(search_params),
        )

        try:
            result = response.get("resource", {}).get("result", [])
        except AttributeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

        return {
            Output.SECURITY_INCIDENTS: [
                convert_security_incident_fields(return_non_empty(security_incident)) for security_incident in result
            ]
        }
