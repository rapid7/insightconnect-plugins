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
                if "Event" in event:
                    message = "Event found."
                    errors = ["No errors."]
                else:
                    errors = event.get("errors")
                    for field in errors:
                        if isinstance(field, dict):
                            if "Invalid event" in field.get("message"):
                                message = field.pop("message")
                                self.logger.info(f"Invalid event message: {message}")
                                errors = [event.pop("errors")]
                    raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=errors)

            else:
                raise PluginException(preset=PluginException.Preset.BAD_REQUEST)
        except Exception as error:
            self.logger.error(f"Event %s not found or failure occurred {error}")
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=error)

        return {"event": event.get("Event"), "message": message, "errors": errors}
