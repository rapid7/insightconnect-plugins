import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from .schema import GetCompanyInput, GetCompanyOutput, Input, Output, Component

# Custom imports below


class GetCompany(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_company", description=Component.DESCRIPTION, input=GetCompanyInput(), output=GetCompanyOutput()
        )

    def run(self, params: dict = None) -> dict:
        return clean({Output.COMPANY: self.connection.api_client.get_company(params.get(Input.COMPANY_ID))})
