import insightconnect_plugin_runtime
from .schema import CreateIncidentInput, CreateIncidentOutput, Component, Output, Input

# Custom imports below
from komand_cherwell.util.utils import set_field_values


class CreateIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_incident",
            description=Component.DESCRIPTION,
            input=CreateIncidentInput(),
            output=CreateIncidentOutput(),
        )

    def run(self, params={}):
        # Will now take template id
        # And a set of key values to change in the template
        # This will then be packed up and sent off.
        fields_to_change = params.get(Input.FIELDS_TO_CHANGE)
        business_object_id = params.get(Input.BUSINESS_OBJECT_ID)

        # Template lookup
        bo_template = {"busObId": business_object_id, "includeRequired": True, "includeAll": True}

        template = self.connection.api.get_businessobjecttemplate(bo_template)

        # Set values for template
        bof = set_field_values(template, fields_to_change)

        # Create body for incident
        busOb = {
            "fields": bof,
            "busObId": business_object_id,
        }

        response = self.connection.api.create_incident(busOb)

        return {Output.SUCCESS: True, Output.RAW_RESPONSE: response}
