import insightconnect_plugin_runtime
from .schema import RunSynchronouslyInput, RunSynchronouslyOutput
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import requests
import time


class RunSynchronously(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_synchronously",
            description="Run a workflow and wait for results",
            input=RunSynchronouslyInput(),
            output=RunSynchronouslyOutput(),
        )

    def run(self, params={}):
        """Run a job"""
        uid = params.get("workflow_uid")
        timeout = params.get("timeout")
        completion_checks = params.get("completion_checks")

        check_interval = RunSynchronously.get_check_interval(timeout, completion_checks)

        # Get UID for workflow if name was used
        if not uid:
            uid = self.connection.lookup_workflow_name(params["workflow_name"])
            if not uid:
                raise PluginException(
                    cause="Invalid workflow name provided", assistance="Please provide a valid workflow name"
                )

        # Execute workflow
        url = self.connection.credentials.base_url + "/v2/workflows/" + uid + "/events"
        response = self.connection.session().post(url, json=params["input"])

        # Check status code of executed workflow
        if response.status_code != requests.codes.ok:
            raise PluginException(
                cause="Failure to create job", assistane=f"Response: {str(response.status_code) + str(response.text)}"
            )
        job = response.json()

        # Try/except here in case of API changes
        try:
            uid = job["job_id"]
            job_url = job["job_url"]
        except KeyError:
            raise PluginException(cause="Failed to get job ID and/or URL from asynchronous job")
        else:

            job = self.connection.get_job(uid)

            # List of statuses where the job has stopped for one reason or another
            done_statuses = ["succeeded", "failed", "dismissed", "cancelled"]

            # First let's make sure we have a job
            while not job:
                self.logger.info("Job not created yet, polling until existence")
                time.sleep(1)
                job = self.connection.get_job(uid)

            # Out of while loop, so let's let the user know we got the job
            self.logger.info("Got job! Checking status...")

            count = 0
            while job["status"] not in done_statuses:
                self.logger.info(f"Current job status: {job.get('status')}")
                count += 1

                if (count > completion_checks) and (timeout != 0):
                    raise PluginException(cause="Timeout waiting for job", assistance=f"Job ID: {job.get('job_id')}")

                time.sleep(check_interval)
                job = self.connection.get_job(uid)

            if not job:
                raise PluginException(cause="No job found", assistance=f"ID: {uid}")

            job["url"] = job_url
            return job

    @staticmethod
    def get_check_interval(timeout, completion_checks):
        """Determines amount of seconds to sleep given total timeout period and amount of checks to make"""
        if timeout == 0:
            return 5
        else:
            return timeout / completion_checks

    def test(self):
        # TODO: Implement test function
        return {}
