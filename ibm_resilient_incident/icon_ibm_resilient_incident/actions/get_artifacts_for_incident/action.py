import komand
import requests
from .schema import GetArtifactsForIncidentInput, GetArtifactsForIncidentOutput


class GetArtifactsForIncident(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_artifacts_for_incident',
                description='Gets the list of artifacts associated with the specified incident.',
                input=GetArtifactsForIncidentInput(),
                output=GetArtifactsForIncidentOutput())

    def run(self, params={}):
        org_id = params.get("organization_id")
        inc_id = params.get("incident_id")

        url = self.connection.API_BASE + "/orgs/{org_id}/incidents/{inc_id}/artifacts".format(org_id=org_id,
                                                                                              inc_id=inc_id)

        self.logger.info("Retrieving artifacts for incident %s..." % inc_id)
        try:
            response = self.connection.SESSION.get(url)
            artifacts = response.json()
            artifacts = komand.helper.clean(artifacts)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error: %s" % error)
            raise

        return {"artifacts": artifacts}

    def test(self):
        """TODO: Test action"""
        return {}
