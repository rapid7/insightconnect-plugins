import komand
from .schema import JobInput, JobOutput
import time



class Job(komand.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='job',
            description='Trigger on new jobs',
            input=JobInput(),
            output=JobOutput())

        self.status = 'failed'
        self.last_job_id = ''

    def steps(self, job_id):
        url = self.connection.credentials.base_url + '/v2/jobs/' + job_id + '/steps'
        result = self.connection.session().get(url)

        return result.json()

    def poll(self, init=False):
        offset = 0
        params = {
            'status': self.status,
            'desc': ['created_at', 'job_id'],
            'limit': 50,
            'offset': offset,
        }
        url = self.connection.credentials.base_url + '/v2/jobs'
        result = self.connection.session().get(url, params=params)
        jobs = result.json()['jobs']

        last_job_id = ''

        self.logger.info('Looking for messages from id=%s with status=%s', self.last_job_id, self.status)

        for job in jobs:

            if last_job_id == '':
                last_job_id = job['job_id']

            if init or job['job_id'] == self.last_job_id:
                break

            job['steps'] = self.steps(job['job_id'])
            self.send(job)

        self.last_job_id = last_job_id

    def run(self, params={}):
        """Run the trigger"""
        self.status = params['status']

        self.poll(True)

        while True:
            self.poll()
            time.sleep(30)

    def test(self):
        # TODO: Implement test function
        return {}
