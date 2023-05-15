import insightconnect_plugin_runtime
from .schema import GetCasesInput, GetCasesOutput, Component, Input, Output

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

    def run(self, params={}): # pylint: disable=unused-argument

        response = self.connection.client.get_cases()

        return {Output.LIST: response}
