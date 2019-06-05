import komand
from .schema import ListTasksInput, ListTasksOutput
# Custom imports below
import json
import requests


class ListTasks(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_tasks',
                description='Returns list of tasks',
                input=ListTasksInput(),
                output=ListTasksOutput())

    def run(self, params={}):
        server = self.connection.server
        
        if params.get('offset', ''):
            offset = params.get('offset', '')
            limit = params.get('limit', '')
            if limit:
                endpoint = server + "/tasks/list/%d/%d" % (limit, offset)
            else:
                endpoint = server + "/tasks/list"
        elif params.get('limit', ''):
            limit = params.get('limit', '')
            endpoint = server + "/tasks/list/%d" % (limit)
        else:
            endpoint = server + "/tasks/list"

        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            response = r.json()
            result = {'tasks': response}
            return result

        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        return {"tasks": [self.connection.test()]}

