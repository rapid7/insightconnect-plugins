import komand
from .schema import DeleteTaskInput, DeleteTaskOutput
# Custom imports below
import json
import requests


class DeleteTask(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_task',
                description='Removes the given task from the database and deletes the results',
                input=DeleteTaskInput(),
                output=DeleteTaskOutput())

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get('task_id', '')
        endpoint = server + "/tasks/delete/" + str(task_id)
        
        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            response = r.json()
            response['message'] = 'Task deleted'
            del response['status']
            return response
        
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['error'] = False
        out['error_value'] = 'No error'
        out['message'] = 'Test passed'
        return out