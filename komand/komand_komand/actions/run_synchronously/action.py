import komand
from .schema import RunSynchronouslyInput, RunSynchronouslyOutput
# Custom imports below
import requests
import time



class RunSynchronously(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run_synchronously',
                description='Run a workflow and wait for results',
                input=RunSynchronouslyInput(),
                output=RunSynchronouslyOutput())

    def run(self, params={}):
        """Run a job"""
        uid = params.get('workflow_uid')
        timeout = params.get('timeout')
        completion_checks = params.get("completion_checks")

        check_interval = RunSynchronously.get_check_interval(timeout, completion_checks)


        # Get UID for workflow if name was used
        if not uid:
            uid = self.connection.lookup_workflow_name(params['workflow_name'])
            if not uid:
                raise Exception('invalid workflow name provided')

        # Execute workflow
        url = self.connection.credentials.base_url + '/v2/workflows/' + uid + '/events'
        r = self.connection.session().post(url, json=params['input'])

        # Check status code of executed workflow
        if r.status_code != requests.codes.ok:
            raise Exception('Failure to create job, bad request code: ' + str(r.status_code) + str(r.text))

        job = r.json()

        # Try/except here in case of API changes
        try:
            uid = job['job_id']
            job_url = job['job_url']
        except KeyError:
            raise Exception('Failed to get job ID and/or URL from asynchronous job')
        else:

            job = self.connection.get_job(uid)

            # List of statuses where the job has stopped for one reason or another
            done_statuses = ['succeeded', 'failed', 'dismissed', 'cancelled']

            # First let's make sure we have a job
            while not job:
                self.logger.info('Job not created yet, polling until existence')
                time.sleep(1)
                job = self.connection.get_job(uid)

            # Out of while loop, so let's let the user know we got the job
            self.logger.info('Got job! Checking status...')

            count = 0
            while job['status'] not in done_statuses:
                self.logger.info('Current job status: %s' % job['status'])
                count += 1

                if (count > completion_checks) and (timeout is not 0):
                    raise Exception('Timeout waiting for job: %s' + job['job_id'])

                time.sleep(check_interval)
                job = self.connection.get_job(uid)

            if not job:
                raise Exception('No job found: ' + uid)

            job['url'] = job_url
            return job

    @staticmethod
    def get_check_interval(timeout, completion_checks):
        """Determines amount of seconds to sleep given total timeout period and amount of checks to make"""
        if timeout is 0:
            return 5
        else:
            return timeout / completion_checks

    def test(self):
        # TODO: Implement test function
        return {}
