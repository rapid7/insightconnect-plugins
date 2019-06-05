import komand
from .schema import CloseCaseInput, CloseCaseOutput, Component
# Custom imports below
import requests


class CloseCase(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='close_case',
                description=Component.DESCRIPTION,
                input=CloseCaseInput(),
                output=CloseCaseOutput())

    def run(self, params={}):

        client = self.connection.client
        case_id = params.get('id')
        summary = params.get('summary')
        resolution_status = params.get('resolution_status')
        impact_status = params.get('impact_status')
        url = '{}/api/case/{}'.format(client.url, case_id)
        data = {'summary': summary, 'resolutionStatus': resolution_status, 'impactStatus': impact_status}

        try:
            user = requests.delete(url, json=data, auth=(self.connection.username, self.connection.password), verify=self.connection.verify)
            user.raise_for_status()
        except requests.exceptions.HTTPError:
            self.logger.error(user.json())
            return {'type': 'NotFound', 'message': 'NotClosed'}
        except:
            self.logger.error('Failed to close case')
            raise

        return {'type': 'Found', 'message': 'Closed'}
