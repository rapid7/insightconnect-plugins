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

        data = [
            {
                "alertTime": params.get(Input.ALERTTIME),
                "deviceId": params.get(Input.DEVICEID),
                "deviceVersion": params.get(Input.DEVICEVERSION),
                "dstDomain": params.get(Input.DSTDOMAIN),
                "dstIP": params.get(Input.DSTIP),
                "dstUrl": params.get(Input.DSTURL),
                "eventDescription": params.get(Input.EVENTDESCRIPTION),
                "eventHash": params.get(Input.EVENTHASH),
                "eventSeverity": params.get(Input.EVENTSEVERITY),
                "eventTime": params.get(Input.EVENTTIME),
                "eventType": params.get(Input.EVENTTYPE),
                "externalURL": params.get(Input.EXTERNALURL),
                "fileHash": params.get(Input.FILEHASH),
                "fileName": params.get(Input.FILENAME),
                "protocolVersion": params.get(Input.PROTOCOLVERSION),
                "providerName": params.get(Input.PROVIDERNAME),
                "src": params.get(Input.SRC),
                "disableDstSafeguards": params.get(Input.DISABLEDSTSAFEGUARDS)
             }
        ]

        response = self.connection.client.add_event(data)

        return {Output.ID: response}
