import komand
from .schema import RetrieveInput, RetrieveOutput, Component
# Custom imports below


class Retrieve(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve',
                description=Component.DESCRIPTION,
                input=RetrieveInput(),
                output=RetrieveOutput())

    def run(self, params={}):
        client = self.connection.client
        #
        try:
            client.session_create()
        except Exception as e:
            raise Exception("Unable to connect to OTRS webservice! Please check your connection information and \
            that you have properly configured OTRS webservice. Information on configuring the webservice can be found\
            in the Connection help")

        clean_data = {}
        try:
            ticket = client.ticket_get_by_id(params.get("ticket_id"), articles=True, attachments=True, dynamic_fields=True)
            ticket_data = ticket.to_dct()
            clean_data = komand.helper.clean(ticket_data)
        except Exception as e:
            self.logger.error("Ticket may not exist, please check to make sure the ticket exists ", e)
            raise

        # Type formatting for other actions
        try:
            cleaned_articles = []
            articles = clean_data["Ticket"]["Article"]
            for article in articles:
                if "IsVisibleForCustomer" in article:
                    article["IsVisibleForCustomer"] = int(article["IsVisibleForCustomer"])
                if "TicketID" in article:
                    article["TicketID"] = int(article["TicketID"])
                if "NoAgentNotify" in article:
                    article["NoAgentNotify"] = int(article["NoAgentNotify"])
                cleaned_articles.append(article)
                if "Attachment" in article:
                    cleaned_attachment = []
                    for attachment in article["Attachment"]:
                        attachment["FilesizeRaw"] = int(attachment["FilesizeRaw"])
                        cleaned_attachment.append(attachment)
                    article["Attachment"] = cleaned_attachment
            clean_data["Ticket"]["Article"] = cleaned_articles
            self.logger.info(clean_data)
            if clean_data["Ticket"].get("DynamicField"):
                clean_df = []
                dynamicfields = clean_data["Ticket"].pop("DynamicField")
                for dynamicfield in dynamicfields:
                    # check if value is a str or in and convert to a list of strings
                    if "Value" in dynamicfield:
                        if isinstance(dynamicfield["Value"], (str, int)):
                            dynamicfield["Value"] = [str(dynamicfield["Value"])]
                        clean_df.append(dynamicfield)
                clean_data["Ticket"]["DynamicField"] = clean_df

        except Exception as e:
            self.logger.error("Ticket {} missing Article data! Unable to format data".format(str(params.get("ticket_id"))), e)
            raise

        try:
            clean_data["Ticket"]["TicketID"] = int(clean_data["Ticket"]["TicketID"])
        except Exception as e:
            self.logger.error("Ticket {} missing Ticket ID!".format(str(params.get("ticket_id"))), e)
            raise

        return clean_data
