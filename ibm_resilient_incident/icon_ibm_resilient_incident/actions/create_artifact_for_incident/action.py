import komand
import json
import requests
from .schema import CreateArtifactForIncidentInput, CreateArtifactForIncidentOutput


class CreateArtifactForIncident(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_artifact_for_incident',
                description='Creates a new artifact on an incident.',
                input=CreateArtifactForIncidentInput(),
                output=CreateArtifactForIncidentOutput())

    def run(self, params={}):
        org_id = params.get("organization_id")
        inc_id = params.get("incident_id")
        artifact = params.get("artifact")

        url = self.connection.API_BASE + "/orgs/{org_id}/incidents/{inc_id}/artifacts".format(org_id=org_id,
                                                                                              inc_id=inc_id)

        artifact = json.dumps(artifact)

        self.logger.info("Creating artifact on incident %s..." % inc_id)
        try:
            response = self.connection.SESSION.post(url=url, data=artifact)
            new_artifact = response.json()[0]
            new_artifact = komand.helper.clean(new_artifact)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error: %s" % error)
            raise

        return {"artifact": new_artifact}

    def test(self):
        """TODO: Test action"""
        return {}
