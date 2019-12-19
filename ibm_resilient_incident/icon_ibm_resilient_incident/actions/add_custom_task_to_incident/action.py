import komand
import json
import requests
from .schema import AddCustomTaskToIncidentInput, AddCustomTaskToIncidentOutput


class AddCustomTaskToIncident(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_custom_task_to_incident',
                description='Adds a custom task to the incident.',
                input=AddCustomTaskToIncidentInput(),
                output=AddCustomTaskToIncidentOutput())

    def run(self, params={}):
        org_id = params.get("organization_id")
        inc_id = params.get("incident_id")
        url = self.connection.API_BASE + "/orgs/{org_id}/incidents/{inc_id}/tasks".format(org_id=org_id,
                                                                                          inc_id=inc_id)
        json_body = params.get("body")
        json_body = json.dumps(json_body)

        try:
            response = self.connection.SESSION.post(url=url, data=json_body)
            identifier = response.json()["id"]

            if response.status_code != 200:
                self.logger.error("Error occurred - check the JSON body and ensure the data is correct.")

        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error %d: %s" % (response.status_code, error))
            raise

        return {"identifier": identifier}

    def test(self):
        """TODO: Test action"""
        return {}
