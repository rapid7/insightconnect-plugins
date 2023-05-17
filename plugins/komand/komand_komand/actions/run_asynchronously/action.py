import insightconnect_plugin_runtime
from .schema import RunAsynchronouslyInput, RunAsynchronouslyOutput
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import requests


class RunAsynchronously(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_asynchronously",
            description="Run a workflow without waiting for results",
            input=RunAsynchronouslyInput(),
            output=RunAsynchronouslyOutput(),
        )

    def run(self, params={}):
        """Run a job"""
        uid = params.get("workflow_uid")

        if not uid:
            uid = self.connection.lookup_workflow_name(params["workflow_name"])
            if not uid:
                raise PluginException(
                    cause="Invalid workflow name provided", assistance="Please provide a valid workflow name"
                )

        url = self.connection.credentials.base_url + "/v2/workflows/" + uid + "/events"
        response = self.connection.session().post(url, json=params["input"])

        if response.status_code != requests.codes.ok:
            raise PluginException(
                cause="Failure to create job", assistane=f"Response: {str(response.status_code) + str(response.text)}"
            )

        job = response.json()
        return {"job_id": job["job_id"], "url": job["job_url"]}

    def test(self):
        # TODO: Implement test function
        return {}
