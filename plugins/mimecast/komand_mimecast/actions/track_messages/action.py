import insightconnect_plugin_runtime
from .schema import TrackMessagesInput, TrackMessagesOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_mimecast.util.constants import (
    DATA_FIELD,
    TRACKED_EMAILS_FIELD,
    TRACKED_EMAILS_ADVANCED_OPTIONS,
    TRACKED_EMAILS_ADVANCED_CAUSE,
    TRACKED_EMAILS_REQUIRED_CAUSE,
    TRACKED_EMAILS_ASSISTANCE,
)
from komand_mimecast.util.util import Utils


class TrackMessages(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="track_messages",
            description=Component.DESCRIPTION,
            input=TrackMessagesInput(),
            output=TrackMessagesOutput(),
        )

    def run(self, params={}):
        search_reason = params.get(Input.SEARCH_REASON)
        start_date = params.get(Input.START_DATE)
        end_date = params.get(Input.END_DATE)
        message_id = params.get(Input.MESSAGE_ID)
        routes = params.get(Input.ROUTES)
        send_from = params.get(Input.SEND_FROM)
        send_to = params.get(Input.SEND_TO)
        subject = params.get(Input.SUBJECT)
        sender_ip = params.get(Input.SENDER_IP)

        data = Utils.return_non_empty(
            {
                "searchReason": search_reason,
                "start": start_date,
                "end": end_date,
                "messageId": message_id,
                TRACKED_EMAILS_ADVANCED_OPTIONS: {
                    "senderIP": sender_ip,
                    "to": send_to,
                    "from": send_from,
                    "subject": subject,
                    "route": routes,
                },
            }
        )

        if TRACKED_EMAILS_ADVANCED_OPTIONS in data and not any((send_from, send_to, subject, sender_ip)):
            raise PluginException(
                cause=TRACKED_EMAILS_ADVANCED_CAUSE,
                assistance=TRACKED_EMAILS_ASSISTANCE,
            )

        if (TRACKED_EMAILS_ADVANCED_OPTIONS in data and message_id) or (
            TRACKED_EMAILS_ADVANCED_OPTIONS not in data and not message_id
        ):
            raise PluginException(
                cause=TRACKED_EMAILS_REQUIRED_CAUSE,
                assistance=TRACKED_EMAILS_ASSISTANCE,
            )

        response = self.connection.client.search_message_finder(data)
        tracked_emails = response.get(DATA_FIELD, [])[0].get(TRACKED_EMAILS_FIELD, [])
        return {Output.TRACKED_EMAILS: tracked_emails}
