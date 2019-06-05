import komand
from .schema import DeleteJobInput, DeleteJobOutput
# Custom imports below
from cortex4py.api import CortexException


class DeleteJob(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_job',
                description='Delete an existing job, identified by its ID',
                input=DeleteJobInput(),
                output=DeleteJobOutput())

    def run(self, params={}):
        """TODO: Run action"""
        client = self.connection.client

        try:
            status = client.delete_job(params.get('job_id'))
        except CortexException:
            self.logger.error('Failed to delete job: %s. It may not exist.', params.get('job_id'))
            status = False

        return { 'status': status }

    def test(self):
        """TODO: Test action"""
        client = self.connection.client

        try:
             out = client.get_analyzers()
        except CortexException:
            self.logger.error('Failed to test getting analyzers')
            raise

        return { 'status': True }
