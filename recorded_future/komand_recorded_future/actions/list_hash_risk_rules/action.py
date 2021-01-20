import komand
import requests
from .schema import ListHashRiskRulesInput, ListHashRiskRulesOutput


class ListHashRiskRules(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_hash_risk_rules",
            description="This action is used to list available filtration rules for hash risk lists",
            input=ListHashRiskRulesInput(),
            output=ListHashRiskRulesOutput(),
        )

    def run(self, params={}):
        try:
            risklist = params.get("list")
            query_headers = self.connection.headers
            results = requests.get(
                "https://api.recordedfuture.com/v2/hash/riskrules",
                headers=query_headers,
            ).json()
            return {"risk_rules": results["data"]["results"]}
        except Exception as e:
            self.logger.error("Error: " + str(e))
