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
        # check that the incident exists
        # if so update incident
        business_object_id = params.get(Input.BUSINESS_OBJECT_ID)
        public_id = params.get(Input.PUBLIC_ID)
        fields_to_update = params.get(Input.FIELDS_TO_UPDATE)
        update_data = []
        incident = self.connection.api.get_incident(busobid=business_object_id, publicid=public_id)
        if incident:
            for field in incident.get("fields", []):
                if field.get("displayName") in fields_to_update:
                    field["dirty"] = True
                    field["value"] = fields_to_update.get(field.get("displayName"), "")
                    update_data.append(field)

            business_object = {
                "fields": update_data,
                "busObId": business_object_id,
                "busObPublicId": public_id,
            }
            response = self.connection.api.update_incident(business_object)
            return {Output.SUCCESS: True, Output.RAW_RESPONSE: response}
        else:
            return {Output.SUCCESS: False, Output.RAW_RESPONSE: {}}
