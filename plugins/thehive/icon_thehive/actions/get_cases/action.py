import insightconnect_plugin_runtime
from .schema import GetCasesInput, GetCasesOutput, Output, Component

# Custom imports below
import requests


class GetCases(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_cases",
            description=Component.DESCRIPTION,
            input=GetCasesInput(),
            output=GetCasesOutput(),
        )

    def run(self, params={}):
        client = self.connection.client

        try:
            cases = client.find_cases()
            cases.raise_for_status()
        except requests.exceptions.HTTPError:
            self.logger.error(cases.json())
            raise
        except:
            self.logger.error("Failed to get cases")
            raise

        return {Output.LIST: cases.json()}
