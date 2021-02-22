import insightconnect_plugin_runtime

from .schema import UpdateIncidentInput, UpdateIncidentOutput, Input, Output, Component


# Custom imports below


class UpdateIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_incident",
            description=Component.DESCRIPTION,
            input=UpdateIncidentInput(),
            output=UpdateIncidentOutput(),
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

        data.update(params.get(Input.ADDITIONAL_FIELDS))

        response = self.connection.request.make_request(
            endpoint=f"{self.connection.incident_url}/{params.get(Input.SYSTEM_ID)}", method="put", payload=data
        )

        if response.get("status", 0) in range(200, 299):
            success = True
        else:
            success = False

        return {Output.SUCCESS: success}
