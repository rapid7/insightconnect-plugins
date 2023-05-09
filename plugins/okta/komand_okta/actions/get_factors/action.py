import insightconnect_plugin_runtime
from .schema import GetFactorsInput, GetFactorsOutput, Input, Output, Component

# Custom imports below
from komand_okta.util.helpers import clean


class GetFactors(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_factors",
            description=Component.DESCRIPTION,
            input=GetFactorsInput(),
            output=GetFactorsOutput(),
        )

    def run(self, params={}):
        response = self.connection.api_client.get_factors(user_id=params.get(Input.USERID))
        for factor in response:
            factor["links"] = factor.pop("_links") if factor.get("_links") else {}
            factor["embedded"] = factor.pop("_embedded") if factor.get("_embedded") else {}
            if factor.get("embedded", {}).get("activation", {}).get("_links"):
                factor["embedded"]["activation"]["links"] = factor["embedded"]["activation"].pop("_links")

        return {Output.FACTORS: clean(response)}
