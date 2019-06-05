import komand
from .schema import AddEventInput, AddEventOutput
# Custom imports below


class AddEvent(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_event',
                description='Posts a malware event for processing and optionally adding to a customers domain lists',
                input=AddEventInput(),
                output=AddEventOutput())

    def run(self, params={}):
        domains = params.get("events")
        events = []

        for event in domains:
            dstUrl = event.get("dstURL")
            event['dstUrl'] = dstUrl
            del event['dstURL']

            ID = event.get("ID")
            event['deviceId'] = ID
            del event['ID']

            events.append(event)

        try:
            dictIds = self.connection.api.add_event(events)
        except Exception:
            self.logger.error("AddEvent: run: Problem with request")
            raise Exception("AddEvent: run: Problem with request")

        ids = []
        for key, value in dictIds.items():
            ids.append(value)

        return {"ID": ids}

    def test(self):
        return {"ID": []}
