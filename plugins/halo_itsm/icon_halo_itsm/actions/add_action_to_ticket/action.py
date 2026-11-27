import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.telemetry import auto_instrument
from .schema import AddActionToTicketInput, AddActionToTicketOutput, Input, Output, Component
from icon_halo_itsm.util.helpers import clean_action


class AddActionToTicket(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_action_to_ticket",
            description=Component.DESCRIPTION,
            input=AddActionToTicketInput(),
            output=AddActionToTicketOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ticket_id = params.get(Input.TICKET_ID)
        note = params.get(Input.NOTE)
        note_html = params.get(Input.NOTE_HTML)
        outcome = params.get(Input.OUTCOME)
        hiddenfromuser = params.get(Input.HIDDENFROMUSER, False)
        # END INPUT BINDING - DO NOT REMOVE

        if not note and not note_html:
            raise PluginException(
                cause="No note content provided.",
                assistance="Provide Note (plain text) or Note HTML.",
            )

        action_data = {"hiddenfromuser": hiddenfromuser}
        if note:
            action_data["note"] = note
        if note_html:
            action_data["note_html"] = note_html

        if outcome:
            action_data["outcome"] = outcome

        self.logger.info(f"Adding action to ticket ID: {ticket_id}")
        result = self.connection.client.add_action_to_ticket(ticket_id, action_data)

        return {Output.ACTION: clean_action(result)}
