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

    @auto_instrument
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

        # Prepare URL
        url = f"{self.connection.api_url}ticket/create?activityType={activity_type_number}"

        # Prepare headers
        headers = {
            "Authorization": f"Bearer {self.connection.access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        # Prepare body
        body = {
            "User": "00000000-0000-0000-0000-000000000000",  # Default user ID, can be overridden in additional_fields
            "Category": "00000000-0000-0000-0000-000000000000",  # Default category ID, can be overridden in additional_fields
            "Subject": subject,
            "DescriptionHTML": description_html,
        }

        # Merge in any additional fields
        body.update(additional_fields)

        # Make the request
        try:
            self.logger.info("Creating ticket ...")
            response = requests.post(url, headers=headers, json=body)
            response.raise_for_status()
        except requests.RequestException as e:
            raise PluginException(
                cause="Failed to create ticket in Matrix42.",
                assistance="Please check your Matrix42 connection, credentials, and input parameters.",
                data=str(e),
            )

        # Extract the ticket ID from the response
        ticket_id = response.text.strip('"') if response.text else None
        if not ticket_id:
            raise PluginException(
                cause="Failed to create ticket in Matrix42.",
                assistance="The response did not contain a ticket ID.",
                data=response.json(),
            )
        self.logger.info(f"Ticket created successfully with ID: {ticket_id}")

        return {Output.ID: ticket_id}
