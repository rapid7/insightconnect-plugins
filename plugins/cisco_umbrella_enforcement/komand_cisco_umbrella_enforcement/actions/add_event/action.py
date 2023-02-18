import insightconnect_plugin_runtime
from .schema import AddEventInput, AddEventOutput, Input, Output

# Custom imports below


class AddEvent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_event",
            description="Posts a malware event for processing and optionally adding to a customers domain lists",
            input=AddEventInput(),
            output=AddEventOutput(),
        )

    def run(self, params={}):
        domains = params.get(Input.EVENTS)
        events = []

        for event in domains:
            dstUrl = event.get("dstURL")
            event["dstUrl"] = dstUrl
            del event["dstURL"]

            ID = event.get("ID")
            event["deviceId"] = ID
            del event["ID"]

            events.append(event)

        dict_ids = self.connection.client.add_event(events)

        ids = []
        for key, value in dict_ids.items():
            ids.append(value)

        return {Output.ID: ids}
