import insightconnect_plugin_runtime
from .schema import UpdateIncidentInput, UpdateIncidentOutput, Input, Output, Component
# Custom imports below


class UpdateIncident(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_incident',
                description=Component.DESCRIPTION,
                input=UpdateIncidentInput(),
                output=UpdateIncidentOutput())

    def run(self, params={}):
        url = f'{self.connection.incident_url}/{params.get(Input.SYSTEM_ID)}'
        payload = params.get(Input.UPDATE_DATA)
        method = "put"

        response = self.connection.request.make_request(url, method, payload=payload)

        if response.get("status", 0) in range(200, 299):
            success = True
        else:
            success = False

        return {
            Output.SUCCESS: success
        }
