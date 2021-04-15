import insightconnect_plugin_runtime
from .schema import CreateTicketInput, CreateTicketOutput, Input, Output, Component

# Custom imports below
import validators


class CreateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ticket",
            description=Component.DESCRIPTION,
            input=CreateTicketInput(),
            output=CreateTicketOutput(),
        )

    def run(self, params={}):
        params["assetid"] = params.get(Input.ASSET_ID)
        params["assettag"] = params.get(Input.ASSET_TAG)
        catalog = params.get(Input.CATALOG)
        if validators.uuid(catalog):
            params.update({"catalog_guid": catalog})
        else:
            params.update({"catalog_code": catalog})
        return {Output.RESULT: self.connection.client.ticket_action("POST", {"requests": [params]})}
