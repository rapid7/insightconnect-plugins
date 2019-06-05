import komand
from .schema import UpdateIncidentInput, UpdateIncidentOutput, Input
# Custom imports below


class UpdateIncident(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_incident',
                description='Updates an incident within Cherwell',
                input=UpdateIncidentInput(),
                output=UpdateIncidentOutput())

    def run(self, params={}):
        # check that the incident exists
        # if so update incident
        business_object_id = params.get(Input.BUSINESS_OBJECT_ID)
        public_id = params.get(Input.PUBLIC_ID)
        fields_to_update = params.get(Input.FIELDS_TO_UPDATE)
        update_data = []
        incident = self.connection.api.get_incident(busobid=business_object_id, publicid=public_id)
        if incident:
            for field in incident["fields"]:
                if field["displayName"] in fields_to_update:
                    field["dirty"] = True
                    field["value"] = fields_to_update[field["displayName"]]
                    update_data.append(field)

            business_object = {
                    "fields": update_data,
                    "busObId": business_object_id,
                    "busObPublicId": public_id,
            }
            response = self.connection.api.update_incident(business_object)
            return {"success": True, "raw_response": response}
        else:
            return {"success": False, "raw_response": {}}
