import komand
from .schema import CreateCaseInput, CreateCaseOutput, Component
# Custom imports below
import requests
from thehive4py.models import Case, CaseTask


class CreateCase(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_case',
                description=Component.DESCRIPTION,
                input=CreateCaseInput(),
                output=CreateCaseOutput())

    def run(self, params={}):

        client = self.connection.client

        self.logger.info('Input: %s', params)
        task = CaseTask(
                            title=params.get('task').get('title', None),
                            description=params.get('task').get('description', None),
                            flag=params.get('task').get('flag', False),
                            owner=params.get('task').get('owner', None),
                            status=params.get('task').get('status', None),
                            startDate=params.get('task').get('startDate', None)
        )

        case = Case(
                        title=params.get('title', None),
                        tlp=params.get('tlp', 2),
                        flag=params.get('flag', False),
                        tags=params.get('tags', []),
                        description=params.get('description', None),
                        tasks=[task],
                        customFields=params.get('customFields', None)
        )

        try:
            new_case = client.create_case(case)
            new_case.raise_for_status()
        except requests.exceptions.HTTPError:
            self.logger.error(new_case.json())
            raise
        except:
            self.logger.error('Failed to create case')
            raise

        return {'case': new_case.json()}
