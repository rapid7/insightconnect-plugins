import komand
from .schema import DeleteIncidentInput, DeleteIncidentOutput, Input, Output, Component
# Custom imports below


class DeleteIncident(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_incident',
                description=Component.DESCRIPTION,
                input=DeleteIncidentInput(),
                output=DeleteIncidentOutput())

    def run(self, params={}):
        url = f'{self.connection.incident_url}/{params.get(Input.SYSTEM_ID)}'
        method = "delete"

        response = self.connection.request.make_request(url, method)

        if response.get("status", 0) in range(200, 299):
            success = True
        else:
            success = False

        return {
            Output.SUCCESS: success
        }
