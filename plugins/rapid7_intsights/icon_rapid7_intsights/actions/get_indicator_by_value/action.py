import insightconnect_plugin_runtime
from .schema import GetIndicatorByValueInput, GetIndicatorByValueOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean


class GetIndicatorByValue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_indicator_by_value",
            description=Component.DESCRIPTION,
            input=GetIndicatorByValueInput(),
            output=GetIndicatorByValueOutput(),
        )

    def run(self, params={}):
        response = self.connection.client.get_indicator_by_value(params.get(Input.INDICATOR_VALUE))
        return clean(
            {
                Output.VALUE: response.get("Value"),
                Output.TYPE: response.get("Type"),
                Output.SEVERITY: response.get("Severity"),
                Output.SCORE: response.get("Score", 0),
                Output.WHITELIST: response.get("Whitelist", False),
                Output.FIRST_SEEN: response.get("FirstSeen"),
                Output.LAST_SEEN: response.get("LastSeen"),
                Output.LAST_UPDATE: response.get("LastUpdate"),
                Output.GEO_LOCATION: response.get("Geolocation"),
                Output.SOURCES: response.get("Sources", []),
                Output.TAGS: response.get("Tags", []),
                Output.SYSTEM_TAGS: response.get("SystemTags", []),
                Output.RELATED_MALWARE: response.get("RelatedMalware", []),
                Output.RELATED_CAMPAIGNS: response.get("RelatedCampaigns", []),
                Output.RELATED_THREAT_ACTORS: response.get("RelatedThreatActors", []),
            }
        )
