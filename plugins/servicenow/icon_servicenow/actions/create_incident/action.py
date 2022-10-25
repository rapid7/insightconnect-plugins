import insightconnect_plugin_runtime

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import CreateIncidentInput, CreateIncidentOutput, Input, Output, Component


class CreateIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_incident",
            description=Component.DESCRIPTION,
            input=CreateIncidentInput(),
            output=CreateIncidentOutput(),
        )

    def run(self, params={}):
        data = {
            "caller_id": params.get(Input.CALLER),
            "category": params.get(Input.CATEGORY),
            "subcategory": params.get(Input.SUBCATEGORY),
            "business_service": params.get(Input.BUSINESS_SERVICE),
            "cmdb_ci": params.get(Input.CONFIGURATION_ITEM),
            "contact_type": params.get(Input.CONTACT_TYPE),
            "state": params.get(Input.STATE),
            "impact": params.get(Input.IMPACT),
            "urgency": params.get(Input.URGENCY),
            "priority": params.get(Input.PRIORITY),
            "assignment_group": params.get(Input.ASSIGNMENT_GROUP),
            "assigned_to": params.get(Input.ASSIGNED_TO),
            "short_description": params.get(Input.SHORT_DESCRIPTION),
            "description": params.get(Input.DESCRIPTION),
        }

        data.update(params.get(Input.ADDITIONAL_FIELDS, {}))

        response = self.connection.request.make_request(
            endpoint=self.connection.incident_url, method="post", payload=data
        )

        try:
            result = response["resource"].get("result")
        except KeyError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text) from e

        sys_id = result.get("sys_id", "")
        number = result.get("number", "")

        if sys_id is None:
            raise PluginException(
                cause="Error: Create Incident failed - no system_id returned.", assistance=f"Response: {response.text}"
            )

        return {
            Output.SYSTEM_ID: sys_id,
            Output.NUMBER: number,
            Output.INCIDENT_URL: f"{self.connection.base_url}task.do?sys_id={sys_id}",
        }
