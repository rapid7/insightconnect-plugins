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
                Output.VALUE: response.get("value"),
                Output.TYPE: response.get("type"),
                Output.SEVERITY: response.get("severity"),
                Output.SCORE: response.get("score", 0),
                Output.WHITELIST: response.get("whitelisted", False),
                Output.FIRST_SEEN: response.get("firstSeen"),
                Output.LAST_SEEN: response.get("lastSeen"),
                Output.LAST_UPDATE: response.get("lastUpdateDate"),
                Output.GEO_LOCATION: response.get("Geolocation"),
                Output.SOURCES: response.get("sources", []),
                Output.TAGS: response.get("tags", []),
                Output.SYSTEM_TAGS: response.get("SystemTags", []),
                Output.RELATED_MALWARE: response.get("relatedMalware", []),
                Output.RELATED_CAMPAIGNS: response.get("relatedCampaigns", []),
                Output.RELATED_THREAT_ACTORS: response.get("relatedThreatActors", []),
                Output.STATUS: response.get("status"),
                Output.REPORTED_FEEDS: response.get("reportedFeeds", []),
            }
        )
