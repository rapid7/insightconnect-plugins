import insightconnect_plugin_runtime
from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import requests

class Quarantine(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='quarantine',
                description=Component.DESCRIPTION,
                input=QuarantineInput(),
                output=QuarantineOutput())

    def run(self, params={}):
        agent_id = params.get(Input.AGENT_ID)
        advertisement_period = params.get(Input.INTERVAL)
        quarantine_state = params.get(Input.QUARANTINE_STATE)

        if quarantine_state:
            quarantine_payload = {
                "query": "mutation( $orgID:String! $agentID:String! $advPeriod:Long! ) { quarantineAssets( orgId:$orgID assetIds: [$agentID] input: {advertisementPeriod: $advPeriod} ) { results { assetId failed } } }",
                "variables": {
                    "orgID": self.connection.org_key,
                    "agentID": agent_id,
                    "advPeriod": advertisement_period
                }
            }
        else:
            quarantine_payload = {
                "query": "mutation( $orgID:String! $agentID:String!) { unquarantineAssets( orgId:$orgID assetIds: [$agentID] ) { results { assetId failed } } }",
                "variables": {
                    "orgID": self.connection.org_key,
                    "agentID": agent_id
                }
            }

        headers = self.connection.get_headers()
        result = requests.post(self.connection.endpoint, headers=headers, json=quarantine_payload)

        try:
            result.raise_for_status()
        except:
            raise PluginException(cause="Error connecting to the Insight Agent API.",
                                  assistance="Please check your Org ID, and API key.\n",
                                  data=result.text)

        results_object = result.json()
        if results_object.get("errors"):
            raise PluginException(cause="Insight Agent API returned errors",
                                  assistance=results_object.get("errors"))

        if quarantine_state:
            failed = results_object.get("data").get("quarantineAssets").get("results")[0].get("failed")
        else:
            failed = results_object.get("data").get("unquarantineAssets").get("results")[0].get("failed")
        return {Output.SUCCESS: not failed}
