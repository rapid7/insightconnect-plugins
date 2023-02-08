import insightconnect_plugin_runtime
from .schema import ListEventsInput, ListEventsOutput, Output, Component

# Custom imports below
from icon_bitwarden.util.helpers import clean_dict


class ListEvents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="listEvents", description=Component.DESCRIPTION, input=ListEventsInput(), output=ListEventsOutput()
        )

    def run(self, params={}):
        self.logger.info("[ACTION] Getting a list of events...")
        return {Output.EVENTS: self.connection.api_client.list_events(clean_dict(params)).get("data", [])}
