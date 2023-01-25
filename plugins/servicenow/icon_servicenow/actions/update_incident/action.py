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
        data = {}
        data_fields = {
            "caller_id": Input.CALLER,
            "category": Input.CATEGORY,
            "subcategory": Input.SUBCATEGORY,
            "business_service": Input.BUSINESS_SERVICE,
            "cmdb_ci": Input.CONFIGURATION_ITEM,
            "contact_type": Input.CONTACT_TYPE,
            "state": Input.STATE,
            "impact": Input.IMPACT,
            "urgency": Input.URGENCY,
            "priority": Input.PRIORITY,
            "assignment_group": Input.ASSIGNMENT_GROUP,
            "assigned_to": Input.ASSIGNED_TO,
            "short_description": Input.SHORT_DESCRIPTION,
            "description": Input.DESCRIPTION,
        }

        # Only update fields which have a valid value to avoid causing previously populated fields to reset to defaults
        for field, value in data_fields.items():
            update_value = params.get(value)
            if update_value:
                data[field] = update_value

        # Additional fields are an optional dictionary of key/value pairs and may include fields not specified above
        data.update(params.get(Input.ADDITIONAL_FIELDS))

        response = self.connection.request.make_request(
            endpoint=f"{self.connection.incident_url}/{params.get(Input.SYSTEM_ID)}", method="put", payload=data
        )

        if response.get("status", 0) in range(200, 299):
            success = True
        else:
            success = False

        return {Output.SUCCESS: success}
