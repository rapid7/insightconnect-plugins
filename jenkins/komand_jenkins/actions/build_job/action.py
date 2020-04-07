import komand
from .schema import BuildJobInput, BuildJobOutput, Input, Output
# Custom imports below


class BuildJob(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='build_job',
                description='Start a build job',
                input=BuildJobInput(),
                output=BuildJobOutput())

    def run(self, params={}):
        name = params.get(Input.NAME)
        parameters = params.get(Input.PARAMETERS)

        job_number = self.connection.server.build_job(name, parameters)
        build_number = self.connection.server.get_job_info(name)['lastCompletedBuild']['number']

        return {Output.JOB_NUMBER: job_number, Output.BUILD_NUMBER: build_number}
