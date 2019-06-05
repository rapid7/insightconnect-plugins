import komand
from .schema import GetJobDetailsInput, GetJobDetailsOutput
# Custom imports below
import requests


class GetJobDetails(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_job_details',
                description='List the details of a given job, identified by its ID',
                input=GetJobDetailsInput(),
                output=GetJobDetailsOutput())

    def run(self, params={}):
        """TODO: Run action"""
        client = self.connection.client

        _id = params.get('job_id')
        url = '{}/{}/{}'.format(self.connection.url, 'api/job', _id)
        self.logger.info('URL: %s', url)

        try:
            resp = requests.get(url)
            try:
                out = resp.json()
            except ValueError:
                self.logger.error(resp.content.decode())
                raise
        except ValueError:
            self.logger.error('No JSON returned')
            raise ValueError
        except:
            raise

        return out

    def test(self):
        """TODO: Test action"""
        client = self.connection.client

        try:
            out = client.get_analyzers()
        except CortexException:
            self.logger.error('Failed to test getting analyzers')
            raise

        artifact = { "data": "Test", "attributes": { "dataType": "Test", "filename": "Test", "tlp": 1 } }
        return { "status": "In Progress", "date": 1111111, "id": "Test", "artifact": artifact, "analyzerId": "Test" }
