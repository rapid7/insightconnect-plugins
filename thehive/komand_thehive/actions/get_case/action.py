import komand
from .schema import GetCaseInput, GetCaseOutput
# Custom imports below
import requests


class GetCase(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_case',
                description='Retrieve a case by ID',
                input=GetCaseInput(),
                output=GetCaseOutput())

    def run(self, params={}):
        client = self.connection.client

        try:
            case = client.get_case(params.get('id'))
            case.raise_for_status()
        except requests.exceptions.HTTPError:
            self.logger.error(case.json())
            raise
        except:
            self.logger.error('Failed to get case')
            raise

        return {'case': case.json()}
