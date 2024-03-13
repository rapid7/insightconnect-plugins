import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import FindEventInput, FindEventOutput

# Custom imports below


class FindEvent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="find_event",
            description="Receive events based on criteria",
            input=FindEventInput(),
            output=FindEventOutput(),
        )

    def run(self, params={}):
        client = self.connection.client
        try:
            event = client.get_event(params.get("event_id"))

            if isinstance(event, dict):
                # Example of when event is not found
                # {
                #    "message": "Invalid event.",
                #    "url": "/events/23423432",
                #    "errors": [ "Invalid event." ],
                #    "name": "Invalid event."
                # }
                if "Event" not in event:
                    if "message" in event:
                        message = event.pop("message")
                        errors = event.pop("errors")
                else:
                    message = "Event found."
                    errors = ["No errors."]
            else:
                raise PluginException(preset=PluginException.Preset.BAD_REQUEST)
        except:
            self.logger.error("Event %s not found or failure occurred", params.get("event_id"))
            raise PluginException(preset=PluginException.Preset.NOT_FOUND)

        return {"event": event.get("Event"), "message": message, "errors": errors}
