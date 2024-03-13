import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import CreateAnEventInput, CreateAnEventOutput

# Custom imports below
import json


class CreateAnEvent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_an_event",
            description="Create a MISP event",
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
            event = self.connection.client.new_event(
                distribution=dist[params.get("distribution")] or None,
                threat_level_id=params.get("threat_level_id"),
                analysis=params.get("analysis") or None,
                info=params.get("info"),
                date=None,
                published=params.get("published"),
                orgc_id=params.get("orgc_id") or None,
                org_id=params.get("org_id") or None,
                sharing_group_id=params.get("sharing_group_id") or None,
            )
            output = json.loads(json.dumps(event))
        except Exception as error:
            self.logger.error(error)
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        try:
            return output["Event"]
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
