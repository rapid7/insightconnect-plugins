import komand
from .schema import JobsInput, JobsOutput
# Custom imports below


class Jobs(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='jobs',
                description='Return every report generated at the end of indexing process',
                input=JobsInput(),
                output=JobsOutput())

    def run(self, params={}):
        jobs = self.connection.api.jobs()
        return {'jobs': jobs}
