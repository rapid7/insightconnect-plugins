import insightconnect_plugin_runtime
from .schema import LookupIncidentInput, LookupIncidentOutput, Component, Output, Input

# Custom imports below


class LookupIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_incident",
            description=Component.DESCRIPTION,
            input=LookupIncidentInput(),
            output=LookupIncidentOutput(),
        )

    def run(self, params={}):
        business_object_id = params.get(Input.BUSINESS_OBJECT_ID)
        public_id = params.get(Input.PUBLIC_ID)

        response = self.connection.api.get_incident(business_object_id, public_id)

        return {Output.SUCCESS: True, Output.RAW_RESPONSE: response}
