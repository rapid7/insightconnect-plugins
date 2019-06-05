import komand
import requests
from .schema import GetIncidentTasksInput, GetIncidentTasksOutput


class GetIncidentTasks(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_incident_tasks',
                description='Gets the list of tasks for the incident.',
                input=GetIncidentTasksInput(),
                output=GetIncidentTasksOutput())

    def run(self, params={}):
        org_id = params.get("organization_id")
        inc_id = params.get("incident_id")

        url = self.connection.API_BASE + "/orgs/{org_id}/incidents/{inc_id}/tasks".format(org_id=org_id,
                                                                                            inc_id=inc_id)

        self.logger.info("Retrieving tasks for incident %s..." % inc_id)
        try:
            response = self.connection.SESSION.get(url)
            tasks = response.json()
            tasks = komand.helper.clean(tasks)
        except (requests.ConnectionError, requests.HTTPError, KeyError, ValueError) as error:
            self.logger.error("Error: %s" % error)
            raise

        return {"tasks": tasks}

    def test(self):
        """TODO: Test action"""
        return {}
