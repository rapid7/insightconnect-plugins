import komand
from .schema import RunAsynchronouslyInput, RunAsynchronouslyOutput
# Custom imports below
import requests


class RunAsynchronously(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run_asynchronously',
                description='Run a workflow without waiting for results',
                input=RunAsynchronouslyInput(),
                output=RunAsynchronouslyOutput())

    def run(self, params={}):
        """Run a job"""
        uid = params.get('workflow_uid')

        if not uid:
            uid = self.connection.lookup_workflow_name(params['workflow_name'])
            if not uid:
                raise Exception('invalid workflow name provided')

        url = self.connection.credentials.base_url + '/v2/workflows/' + uid + '/events'
        r = self.connection.session().post(url, json=params['input'])

        if r.status_code != requests.codes.ok:
            raise Exception('Failure to create job, bad request code: ' + str(r.status_code) + str('text'))

        job = r.json()
        return {'job_id': job['job_id'], 'url': job['job_url']}

    def test(self):
        # TODO: Implement test function
        return {}
