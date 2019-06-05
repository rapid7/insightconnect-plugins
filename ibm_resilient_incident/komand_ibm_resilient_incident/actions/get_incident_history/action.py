import komand
import requests
from .schema import GetIncidentHistoryInput, GetIncidentHistoryOutput


class GetIncidentHistory(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_incident_history',
                description='Gets history about an incident.',
                input=GetIncidentHistoryInput(),
                output=GetIncidentHistoryOutput())

    def run(self, params={}):
        org_id = params.get("organization_id")
        inc_id = params.get("incident_id")

        url = self.connection.API_BASE + "/orgs/{org_id}/incidents/{inc_id}/history".format(org_id=org_id,
                                                                                            inc_id=inc_id)

        self.logger.info("Retrieving history for incident %s..." % inc_id)
        try:
            response = self.connection.SESSION.get(url)
            history = response.json()
            history = komand.helper.clean(history)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error: %s" % error)
            raise

        return {"incident_history": history}

    def test(self):
        """TODO: Test action"""
        return {}
