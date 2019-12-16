import komand
from .schema import CreateInput, CreateOutput, Component
# Custom imports below
from pyotrs import Article, Ticket, Attachment, DynamicField
import mimetypes
from komand_otrs.util.utils import PyOTRSUtils


class Create(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="create",
                description=Component.DESCRIPTION,
                input=CreateInput(),
                output=CreateOutput())

    def run(self, params={}):

        client = self.connection.client
        try:
            client.session_create()
        except Exception as e:
            raise Exception("Unable to connect to OTRS webservice! Please check your connection information and "
                            "that you have properly configured OTRS webservice. Information on configuring the "
                            "webservice can be found in the Connection help")

        # dynamic fields
        new_dynamic_fields = params.get("dynamic_fields")
        del (params["dynamic_fields"])

        params = komand.helper.clean(params)
        # cleaning up params
        new_article = params.get("article")
        del(params["article"])
        # helper.clean will not remove empty list. If these are left empty and not removed the plugin will fail
        if not new_article["ExcludeMuteNotificationToUserID"]:
            del(new_article["ExcludeMuteNotificationToUserID"])

        if not new_article["ExcludeNotificationToUserID"]:
            del(new_article["ExcludeNotificationToUserID"])

        if not new_article["ForceNotificationToUserID"]:
            del(new_article["ForceNotificationToUserID"])

        # Set attachments
        new_attachments = params.get("attachments")
        del(params["attachments"])

        # basics
        basics = {}
        for basic_param in ["Title", "Queue", "Type", "State", "Priority", "CustomerUser"]:
            if basic_param in params:
                basics[basic_param] = params.get(basic_param)
                del(params[basic_param])
            else:
                raise Exception("Parameter {} was not found. This is required to create a ticket".format(basic_param))
        # left over params added to other_basics
        other_basics = {}
        for k, v in params.items():
            if v:
                other_basics[k] = v
        # build attachments
        attachments = []
        for attachment in new_attachments:
            a = Attachment.create_basic(Content=attachment["content"], ContentType=mimetypes.guess_type(attachment["filename"])[0], Filename=attachment["filename"])
            attachments.append(a)
        # build dynamic fields
        dynamic_fields = list(map(lambda f: DynamicField(**f), new_dynamic_fields))
        # create ticket from basics and all other params
        new_ticket = Ticket.create_basic(**basics)
        new_article = Article(new_article)
        new_attachments = attachments
        new_dynamic_fields = dynamic_fields

        # Create Ticket
        ticket_results = client.ticket_create(
            ticket=new_ticket,
            article=new_article,
            attachments=new_attachments,
            dynamic_fields=new_dynamic_fields,
            **other_basics
        )

        ticket_id = ticket_results.get("TicketID")
        # check if pendingtime is left unmodified
        if params.get("PendingTime").startswith("0001-01-01"):
            del(params["PendingTime"])
        else:
            PyOTRSUtils.add_pendingtime(self, client, params.get("PendingTime"), ticket_id)

        # update SLA
        if params.get("SLA"):
            PyOTRSUtils.add_sla(self, client=client, ticket_id=ticket_id, sla=params.get("SLA"), sla_service=params.get("Service"))
            ticket_details = client.ticket_get_by_id(ticket_id, articles=False,
                                                     attachments=False,
                                                     dynamic_fields=False,
                                                     html_body_as_attachment=False)
            ticket_details = ticket_details.to_dct()
            if ticket_details["Ticket"]["SLAID"] == "":
                raise Exception("SLA and Service was not set. Please check the SLA and Service parameters as they maybe set incorrectly!\n"
                                f"SLA Parameter: {params.get('SLA')}\n"
                                f"SLA Service parameter: {params.get('Service')}\n"
                                f"Please note ticket ID:{ticket_id} was created but the SLA and Service parameters were not updated.")

        # format TicketNumber as its required as an INT in other actions and returned here as a string
        return {"ticket_id": int(ticket_results["TicketID"]), "ticket_number": int(ticket_results["TicketNumber"])}
