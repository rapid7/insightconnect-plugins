import komand
from .schema import LookupIncidentInput, LookupIncidentOutput
# Custom imports below


class LookupIncident(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup_incident',
                description='Lookup an Cherwell incident',
                input=LookupIncidentInput(),
                output=LookupIncidentOutput())

    def run(self, params={}):
        business_object_id = params["business_object_id"]
        public_id = params["public_id"]

        response = self.connection.api.get_incident(business_object_id, public_id)

        return {
            "success": True,
            "raw_response": response
        }
