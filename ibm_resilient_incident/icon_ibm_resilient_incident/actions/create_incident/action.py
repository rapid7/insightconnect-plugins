import komand
import json
import requests
from .schema import CreateIncidentInput, CreateIncidentOutput


class CreateIncident(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_incident',
                description='Creates an incident.',
                input=CreateIncidentInput(),
                output=CreateIncidentOutput())

    def run(self, params={}):
        org_id = params.get("organization_id")
        incident = params.get("incident")

        url = self.connection.API_BASE + "/orgs/{org_id}/incidents".format(org_id=org_id)

        incident = json.dumps(incident)

        self.logger.info("Creating incident for organization %s..." % org_id)
        try:
            response = self.connection.SESSION.post(url=url, data=incident)
            new_incident = response.json()
            new_incident = komand.helper.clean(new_incident)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error: %s" % error)
            raise

        return {"incident": new_incident}

    def test(self):
        """TODO: Test action"""
        return {}
