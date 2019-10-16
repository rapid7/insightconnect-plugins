import komand
from .schema import UpdateInput, UpdateOutput, Component
# Custom imports below
from pyotrs import Article, Attachment, DynamicField
from komand_otrs.util.utils import PyOTRSUtils
import mimetypes


class Update(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="update",
                description=Component.DESCRIPTION,
                input=UpdateInput(),
                output=UpdateOutput())

    def run(self, params={}):
        no_article = params.pop("NoArticle")
        client = self.connection.client
        attachments = []
        try:
            client.session_create()
        except Exception as e:
            raise Exception("Unable to connect to OTRS Web Service! Please check your connection information and \
            that you have properly configured OTRS web service. Information on configuring the webservice can be found \
            in the Connection help")

        # dynamic fields
        new_dynamic_fields = params.get("DynamicFields")
        del(params["DynamicFields"])

        params = komand.helper.clean(params)

        # cleaning up params
        new_article = params.get("Article", None)
        if params.get("Article"):
            del(params["Article"])
            # helper.clean will not remove empty list. If these are left empty and not removed the plugin will fail
            if "ExcludeMuteNotificationToUserID" in new_article:
                if not new_article["ExcludeMuteNotificationToUserID"]:
                    del(new_article["ExcludeMuteNotificationToUserID"])
            if "ExcludeNotificationToUserID" in new_article:
                if not new_article["ExcludeNotificationToUserID"]:
                    del(new_article["ExcludeNotificationToUserID"])

            if "ForceNotificationToUserID" in new_article:
                if not new_article["ForceNotificationToUserID"]:
                    del(new_article["ForceNotificationToUserID"])


            new_article = Article(new_article)

        # Set attachments
        if params.get("Attachments"):
            new_attachments = params.pop("Attachments")


            for attachment in new_attachments:
                filename = attachment['filename']
                content = attachment['content']
                mimetype = mimetypes.guess_type(filename)
                attachments.append(Attachment.create_basic(Content=content,
                                                           ContentType=
                                                           mimetype[0],
                                                           Filename=filename))

        ticket_id = params.get('TicketID')
        del(params["TicketID"])

        dynamic_fields = []
        for fields in new_dynamic_fields:
            dynamic_fields.append(DynamicField(**fields))

        #  Pending time
        if params.get("PendingTime").startswith("0001-01-01"):
            del(params['PendingTime'])
        else:
            # Format date
            PyOTRSUtils.add_pendingtime(self, client, params.get("PendingTime"), ticket_id)
            del(params['PendingTime'])

        other_options = params

        if no_article:
            # If attachment exists it will add default Article
            if other_options.get("Attachments"):
                del other_options["Attachments"]

            ticket_update_results = client.ticket_update(
                ticket_id=ticket_id,
                dynamic_fields=dynamic_fields,
                **other_options
            )
        else:
            ticket_update_results = client.ticket_update(
                ticket_id=ticket_id,
                article=new_article,
                attachments=attachments,
                dynamic_fields=dynamic_fields,
                **other_options
            )

        return {'ticket_id': int(ticket_update_results["TicketID"]), 'ticket_number': int(ticket_update_results["TicketNumber"])}
