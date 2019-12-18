import komand
import requests
from .schema import DeleteIncidentInput, DeleteIncidentOutput


class DeleteIncident(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_incident',
                description='Deletes an incident.',
                input=DeleteIncidentInput(),
                output=DeleteIncidentOutput())

    def run(self, params={}):
        org_id = params.get("organization_id")
        inc_id = params.get("incident_id")

        url = self.connection.API_BASE + "/orgs/{org_id}/incidents/{inc_id}".format(org_id=org_id,
                                                                                    inc_id=inc_id)

        self.logger.info("Creating incident for organization %s..." % org_id)
        try:
            response = self.connection.SESSION.delete(url=url)
            status = response.json()
            status = komand.helper.clean(status)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error: %s" % error)
            raise

        return {"status": status}

    def test(self):
        """TODO: Test action"""
        return {}
