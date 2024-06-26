import insightconnect_plugin_runtime
from .schema import BuildJobInput, BuildJobOutput, Input, Output

# Custom imports below
from requests import Request
from urllib.parse import urljoin, urlparse
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_jenkins.util.util import extract_job_number, extract_build_number


class BuildJob(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="build_job",
            description="Start a build job",
            input=BuildJobInput(),
            output=BuildJobOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        name = params.get(Input.NAME)
        parameters = params.get(Input.PARAMETERS, {}) or None
        # END INPUT BINDING - DO NOT REMOVE

        try:
            # Build endpoint URL and cutoff parameters from that
            endpoint = self.connection.server.build_job_url(name, parameters)

            # Send request with parameters as 'data' instead of in URL as it's in package
            response = self.connection.server.jenkins_request(
                Request("POST", urljoin(endpoint, urlparse(endpoint).path), data=parameters)
            )

            # Get job details
            job_info = self.connection.server.get_job_info(name)

            return {
                Output.JOB_NUMBER: extract_job_number(response),
                Output.BUILD_NUMBER: extract_build_number(job_info),
            }
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
