import komand
from .schema import RebootTaskInput, RebootTaskOutput
# Custom imports below
import json
import requests


class RebootTask(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='reboot_task',
                description='Add a reboot task to database from an existing analysis ID',
                input=RebootTaskInput(),
                output=RebootTaskOutput())

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get('task_id', '')
        endpoint = server + "/tasks/reboot/%d" % (task_id)

        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            response = r.json()
            return response

        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['task_id'] = 0
        out['reboot_id'] = 0
        return out