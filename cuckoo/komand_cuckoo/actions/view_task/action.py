import komand
from .schema import ViewTaskInput, ViewTaskOutput
# Custom imports below
import json
import requests


class ViewTask(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='view_task',
                description='Returns details on the task associated with the specified ID',
                input=ViewTaskInput(),
                output=ViewTaskOutput())

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get('task_id', '')
        endpoint = server + "/tasks/view/" + str(task_id)

        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            response = r.json()
            """
            result = {'task': {}}
            keys = response['task'].keys()

            for key in keys:
                if response['task'][key] is not None:
                    result['task'][key] = response['task'][key]

            option_list = []
            for option in response['task']['options']:
                option_list.append({
                        'option': option,
                        'value': response['task']['options'][option]
                    })
            result['task']['options'] = option_list
            """
            return response

        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['task'] = {'message':'Test passed'}
        return out
