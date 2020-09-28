import komand
import requests
from .schema import ListUrlRiskRulesInput, ListUrlRiskRulesOutput, Output, Component
# Custom imports below


class ListUrlRiskRules(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_url_risk_rules',
                description=Component.DESCRIPTION,
                input=ListUrlRiskRulesInput(),
                output=ListUrlRiskRulesOutput())

    def run(self, params={}):
        try:
            query_headers = {"X-RFToken": self.connection.token}
            results = requests.get(
                "https://api.recordedfuture.com/v2/url/riskrules",
                headers=query_headers
            ).json()
            return {
                Output.RISK_RULES: results["data"]["results"]
            }
        except Exception as e:
            self.logger.error("Error: " + str(e))
