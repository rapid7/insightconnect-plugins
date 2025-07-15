import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import CreateTicketInput, CreateTicketOutput, Input, Output, Component

# Custom imports below
import requests


class CreateTicket(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ticket",
            description=Component.DESCRIPTION,
            input=CreateTicketInput(),
            output=CreateTicketOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        activity_type = params.get(Input.ACTIVITY_TYPE)
        additional_fields = params.get(Input.ADDITIONAL_FIELDS, {})
        description_html = params.get(Input.DESCRIPTION_HTML)
        subject = params.get(Input.SUBJECT)
        # END INPUT BINDING - DO NOT REMOVE

        # Map activity_type string to number
        activity_type_map = {"Incident": 0, "Service Request": 6}
        activity_type_number = activity_type_map.get(activity_type)

        # Prepare the URL for creating a ticket
        url = f"{self.connection.api_url}ticket/create?activityType={activity_type_number}"

        # Prepare headers
        headers = self.connection.request_header

        # Prepare body
        body = {
            "Subject": subject,
            "DescriptionHTML": description_html,
            **additional_fields,
        }

        # Make the request
        try:
            self.logger.info("Creating ticket ...")
            response = requests.post(url=url, headers=headers, json=body)
            response.raise_for_status()
        except requests.RequestException as e:
            raise PluginException(
                cause="Failed to create ticket in Matrix42.",
                assistance="Please check your Matrix42 connection, credentials, and input parameters.",
                data=str(e),
            )

        # Extract the ticket ID from the response
        try:
            response_json = response.json()
        except ValueError as e:
            raise PluginException(
                cause="Failed to parse JSON response from Matrix42.",
                assistance="The response was not valid JSON.",
                data=response.text,
            )

        ticket_id = response_json.strip('"') if response_json else None
        if not ticket_id:
            raise PluginException(
                cause="Failed to create ticket in Matrix42.",
                assistance="The response did not contain a ticket ID.",
                data=response_json,
            )
        self.logger.info(f"Ticket created successfully with ID: {ticket_id}")

        return {Output.ID: ticket_id}
