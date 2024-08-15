import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import CreateAnEventInput, CreateAnEventOutput, Input, Component

# Custom imports below
import json


class CreateAnEvent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_an_event",
            description=Component.DESCRIPTION,
            input=CreateAnEventInput(),
            output=CreateAnEventOutput(),
        )

    def run(self, params={}):
        dist = {
            "This Organization": "0",
            "This Community": "1",
            "Connected Communities": "2",
            "All Communities": "3",
        }

        try:
            event = self.connection.client.add_event(
                event={
                    "distribution": dist[params.get(Input.DISTRIBUTION)] or None,
                    "threat_level_id": params.get(Input.THREAT_LEVEL_ID),
                    "analysis": params.get(Input.ANALYSIS) or None,
                    "info": params.get(Input.INFO),
                    "date": None,
                    "published": params.get(Input.PUBLISHED),
                    "orgc_id": params.get(Input.ORGC_ID) or None,
                    "org_id": params.get(Input.ORG_ID) or None,
                    "sharing_group_id": params.get(Input.SHARING_GROUP_ID) or None,
                }
            )
            output = json.loads(json.dumps(event))
        except Exception as error:
            self.logger.error(error)
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        try:
            return output.get("Event")
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
