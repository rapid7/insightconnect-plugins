import komand
import json
import requests
from .schema import PatchIncidentInput, PatchIncidentOutput


class PatchIncident(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='patch_incident',
                description='Patches a single incident.',
                input=PatchIncidentInput(),
                output=PatchIncidentOutput())

    def run(self, params={}):
        org_id = params.get("organization_id")
        inc_id = params.get("incident_id")
        patch = params.get("patch")

        url = self.connection.API_BASE + "/orgs/{org_id}/incidents/{inc_id}".format(org_id=org_id,
                                                                                    inc_id=inc_id)

        patch = json.dumps(patch)

        self.logger.info("Patching incident %s..." % inc_id)
        try:
            response = self.connection.SESSION.patch(url=url, data=patch)
            patch_status = response.json()
            patch_status = komand.helper.clean(patch_status)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error: %s" % error)
            raise

        return {"patch_status": patch_status}

    def test(self):
        """TODO: Test action"""
        return {}
