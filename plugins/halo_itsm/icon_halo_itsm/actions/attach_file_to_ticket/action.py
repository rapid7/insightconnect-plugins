import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument
from .schema import AttachFileToTicketInput, AttachFileToTicketOutput, Input, Output, Component
from icon_halo_itsm.util.helpers import clean_action


class AttachFileToTicket(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="attach_file_to_ticket",
            description=Component.DESCRIPTION,
            input=AttachFileToTicketInput(),
            output=AttachFileToTicketOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        content = params.get(Input.CONTENT)
        filename = params.get(Input.FILENAME)
        hiddenfromuser = params.get(Input.HIDDENFROMUSER, False)
        note = params.get(Input.NOTE)
        ticket_id = params.get(Input.TICKET_ID)
        # END INPUT BINDING - DO NOT REMOVE

        # Accepted so existing workflows still import; Halo attachments have neither (see plugin.spec.yaml)
        del note, hiddenfromuser

        self.logger.info(f"Attaching file '{filename}' to ticket ID: {ticket_id}")
        result = self.connection.client.attach_file_to_ticket(ticket_id=ticket_id, filename=filename, content=content)

        return {Output.ACTION: clean_action(result)}
