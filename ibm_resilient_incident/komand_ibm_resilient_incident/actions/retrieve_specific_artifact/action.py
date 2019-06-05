import komand
import requests
from .schema import RetrieveSpecificArtifactInput, RetrieveSpecificArtifactOutput


class RetrieveSpecificArtifact(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_specific_artifact',
                description='Retrieves a specific incident artifact.',
                input=RetrieveSpecificArtifactInput(),
                output=RetrieveSpecificArtifactOutput())

    def run(self, params={}):
        org_id = params.get("organization_id")
        inc_id = params.get("incident_id")
        artifact_id = params.get("artifact_id")

        url = self.connection.API_BASE + "/orgs/{org_id}/incidents/{inc_id}/artifacts/{artifact_id}".format(org_id=org_id,
                                                                                                            inc_id=inc_id,
                                                                                                            artifact_id=artifact_id)

        self.logger.info("Retrieving artifact for incident %s..." % inc_id)
        try:
            response = self.connection.SESSION.get(url)
            artifact = response.json()
            artifact = komand.helper.clean(artifact)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error: %s" % error)
            raise

        return {"artifact": artifact}

    def test(self):
        """TODO: Test action"""
        return {}
