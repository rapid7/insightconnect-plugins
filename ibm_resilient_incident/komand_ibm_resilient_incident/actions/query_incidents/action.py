import komand
import requests
from .schema import QueryIncidentsInput, QueryIncidentsOutput


class QueryIncidents(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='query_incidents',
                description='Query for incidents.',
                input=QueryIncidentsInput(),
                output=QueryIncidentsOutput())

    def run(self, params={}):
        org_id = params.get("organization_id")
        query = params.get("query")

        url = self.connection.API_BASE + "/orgs/{org_id}/incidents/query".format(org_id=org_id)

        self.logger.info("Querying...")
        try:
            response = self.connection.SESSION.post(url=url, data=query)
            incidents = response.json()
            incidents = komand.helper.clean(incidents)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error: %s" % error)
            raise

        return {"incidents": incidents}

    def test(self):
        """TODO: Test action"""
        return {}
