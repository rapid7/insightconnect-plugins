import komand
import requests
from .schema import GetIncidentsInput, GetIncidentsOutput


class GetIncidents(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_incidents',
                description='Gets a list of open and closed incidents.',
                input=GetIncidentsInput(),
                output=GetIncidentsOutput())

    def run(self, params={}):
        org_id = params.get("organization_id")
        url = self.connection.API_BASE + "/orgs/{org_id}/incidents".format(org_id=org_id)

        self.logger.info("Retrieving incidents...")
        try:
            response = self.connection.SESSION.get(url)
            incidents = response.json()
            incidents = komand.helper.clean(incidents)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error: %s" % error)
            raise

        return {"incidents": incidents}

    def test(self):
        """TODO: Test action"""
        return {}
