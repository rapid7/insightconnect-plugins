import insightconnect_plugin_runtime
from .schema import SearchThreatsInput, SearchThreatsOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below


class SearchThreats(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_threats',
                description=Component.DESCRIPTION,
                input=SearchThreatsInput(),
                output=SearchThreatsOutput())

    def run(self, params={}):
        matching_threats = self.connection.client.search_threats(params.get(Input.THREAT_IDENTIFIER))
        score = params.get(Input.SCORE, None)
        if score:
            for threat in matching_threats:
                if score != threat.get('cylance_score'):
                    matching_threats.remove(threat)
            if len(matching_threats) == 0:
                raise PluginException(
                    cause="No threats matching the score found.",
                    assistance="Unable to find any threats using identifier and score provided."
                )

        return {
            Output.THREATS: matching_threats
        }
