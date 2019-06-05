import komand
from .schema import BuildJobInput, BuildJobOutput
# Custom imports below


class BuildJob(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='build_job',
                description='Start a build job',
                input=BuildJobInput(),
                output=BuildJobOutput())

    def run(self, params={}):
        name = params.get('name')
        parameters = params.get('parameters')

        job_number = self.connection.server.build_job(name, parameters)
        build_number = self.connection.server.get_job_info(name)['lastCompletedBuild']['number']

        return {'job_number': job_number, 'build_number': build_number}

    def test(self):
        user = self.connection.server.get_whoami()
        return {'user': user}
