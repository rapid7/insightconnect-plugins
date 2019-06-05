import komand
import requests
from .schema import GetIndividualIncidentInput, GetIndividualIncidentOutput


class GetIndividualIncident(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_individual_incident',
                description='Gets an individual incident.',
                input=GetIndividualIncidentInput(),
                output=GetIndividualIncidentOutput())

    def run(self, params={}):
        org_id = params.get("organization_id")
        inc_id = params.get("incident_id")
        url = self.connection.API_BASE + "/orgs/{org_id}/incidents/{inc_id}".format(org_id=org_id,
                                                                                    inc_id=inc_id)

        self.logger.info("Retrieving incident %s..." % inc_id)
        try:
            response = self.connection.SESSION.get(url)
            incident = response.json()
            incident = komand.helper.clean(incident)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error: %s" % error)
            raise

        return {"incident": incident}

    def test(self):
        """TODO: Test action"""
        return {}
