import insightconnect_plugin_runtime
from .schema import GetCaseInput, GetCaseOutput, Input, Output, Component

# Custom imports below
import requests


class GetCase(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_case",
            description=Component.DESCRIPTION,
            input=GetCaseInput(),
            output=GetCaseOutput(),
        )

    def run(self, params={}):
        client = self.connection.client

        try:
            case = client.get_case(params.get(Input.ID))
            case.raise_for_status()
        except requests.exceptions.HTTPError:
            self.logger.error(case.json())
            raise
        except:
            self.logger.error("Failed to get case")
            raise

        return {Output.CASE: case.json()}
