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
        data = {
            "asset_name": params.get(Input.ASSET_NAME),
            "assetid": params.get(Input.ASSET_ID),
            "assettag": params.get(Input.ASSET_TAG),
            "ci_asset_tag": params.get(Input.CI_ASSET_TAG),
            "ci_id": params.get(Input.CI_ID),
            "ci_name": params.get(Input.CI_NAME),
            "department_code": params.get(Input.DEPARTMENT_CODE),
            "department_id": params.get(Input.DEPARTMENT_ID),
            "description": params.get(Input.DESCRIPTION),
            "external_reference": params.get(Input.EXTERNAL_REFERENCE),
            "impact_id": params.get(Input.IMPACT_ID),
            "location_code": params.get(Input.LOCATION_CODE),
            "location_id": params.get(Input.LOCATION_ID),
            "origin": params.get(Input.ORIGIN),
            "parentrequest": params.get(Input.PARENTREQUEST),
            "phone": params.get(Input.PHONE),
            "recipient_id": params.get(Input.RECIPIENT_ID),
            "recipient_identification": params.get(Input.RECIPIENT_IDENTIFICATION),
            "recipient_mail": params.get(Input.RECIPIENT_MAIL),
            "recipient_name": params.get(Input.RECIPIENT_NAME),
            "requestor_identification": params.get(Input.REQUESTOR_IDENTIFICATION),
            "requestor_mail": params.get(Input.REQUESTOR_MAIL),
            "requestor_name": params.get(Input.REQUESTOR_NAME),
            "severity_id": params.get(Input.SEVERITY_ID),
            "submit_date": params.get(Input.SUBMIT_DATE),
            "title": params.get(Input.TITLE),
            "urgency_id": params.get(Input.URGENCY_ID),
        }
        catalog = params.get(Input.CATALOG)
        if validators.uuid(catalog):
            data.update({"catalog_guid": catalog})
        else:
            data.update({"catalog_code": catalog})
        return {Output.RESULT: self.connection.client.ticket_action("POST", {"requests": [data]})}
