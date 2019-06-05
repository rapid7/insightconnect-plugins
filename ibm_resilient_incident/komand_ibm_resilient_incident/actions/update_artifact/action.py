import komand
import json
import requests
from .schema import UpdateArtifactInput, UpdateArtifactOutput


class UpdateArtifact(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_artifact',
                description='Saves changes to an artifact.',
                input=UpdateArtifactInput(),
                output=UpdateArtifactOutput())

    def run(self, params={}):
        org_id = params.get("organization_id")
        inc_id = params.get("incident_id")
        artifact_id = params.get("artifact_id")
        artifact = params.get("artifact")

        url = self.connection.API_BASE + "/orgs/{org_id}/incidents/{inc_id}/artifacts/{artifact_id}".format(org_id=org_id,
                                                                                                            inc_id=inc_id,
                                                                                                            artifact_id=artifact_id)

        artifact = json.dumps(artifact)

        self.logger.info("Updating artifact %s..." % artifact_id)
        try:
            response = self.connection.SESSION.put(url=url, data=artifact)
            updated_artifact = response.json()
            updated_artifact = komand.helper.clean(updated_artifact)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error: %s" % error)
            raise

        return {"artifact": updated_artifact}

    def test(self):
        """TODO: Test action"""
        return {}
