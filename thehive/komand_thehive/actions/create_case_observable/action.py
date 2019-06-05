import komand
from .schema import CreateCaseObservableInput, CreateCaseObservableOutput, Component
# Custom imports below
from thehive4py.models import Case, CaseObservable
import requests


class CreateCaseObservable(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_case_observable',
                description=Component.DESCRIPTION,
                input=CreateCaseObservableInput(),
                output=CreateCaseObservableOutput())

    def run(self, params={}):
        client = self.connection.client
        self.logger.info(params)

        observable = CaseObservable(
            dataType=params.get('observable').get('dataType', None),
            data=params.get('observable').get('data', None),
            tlp=params.get('observable').get('tlp', 2),
            ioc=params.get('observable').get('ioc', None),
            tags=params.get('observable').get('tags', []),
            message=params.get('observable').get('message', None)
        )
        try:
            observable = client.create_case_observable(params.get('id'), observable)
            observable.raise_for_status()
        except requests.exceptions.HTTPError:
            self.logger.error(observable.json())
            raise
        except:
            self.logger.error('Failed to create observable')
            raise

        return {'case': observable.json()}
