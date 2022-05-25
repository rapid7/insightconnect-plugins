import insightconnect_plugin_runtime
from .schema import CreateCaseObservableInput, CreateCaseObservableOutput, Input, Output, Component

# Custom imports below
from thehive4py.models import Case, CaseObservable
import requests


class CreateCaseObservable(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_case_observable",
            description=Component.DESCRIPTION,
            input=CreateCaseObservableInput(),
            output=CreateCaseObservableOutput(),
        )

    def run(self, params={}):
        client = self.connection.client
        self.logger.info(params)

        observable = CaseObservable(
            dataType=params.get(Input.OBSERVABLE).get("dataType", None),
            data=params.get(Input.OBSERVABLE).get("data", None),
            tlp=params.get(Input.OBSERVABLE).get("tlp", 2),
            ioc=params.get(Input.OBSERVABLE).get("ioc", None),
            tags=params.get(Input.OBSERVABLE).get("tags", []),
            message=params.get(Input.OBSERVABLE).get("message", None),
        )
        try:
            observable = client.create_case_observable(params.get(Input.ID), observable)
            observable.raise_for_status()
        except requests.exceptions.HTTPError:
            self.logger.error(observable.json())
            raise
        except:
            self.logger.error("Failed to create observable")
            raise

        return {Output.CASE: observable.json()}
