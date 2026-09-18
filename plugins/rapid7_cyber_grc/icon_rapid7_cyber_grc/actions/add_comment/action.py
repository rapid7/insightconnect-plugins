import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import AddCommentInput, AddCommentOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException

# Comments are not a sub-resource of the record they belong to. They live in one
# tenant-wide collection and are tied back to a record by the two IDs below.
COMMENT_TYPE = "Discussions"
# The field every commentable record carries, identifying its comment thread.
FIELD_ID = "discussionFieldID"


class AddComment(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_comment", description=Component.DESCRIPTION, input=AddCommentInput(), output=AddCommentOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        comment = params.get(Input.COMMENT)
        discussion_field_id = params.get(Input.DISCUSSION_FIELD_ID)
        form_discussion_id = params.get(Input.FORM_DISCUSSION_ID)
        id = params.get(Input.ID)
        record_type = params.get(Input.RECORD_TYPE)
        user_id = params.get(Input.USER_ID)
        # END INPUT BINDING - DO NOT REMOVE

        body = {
            "comment": comment,
            FIELD_ID: discussion_field_id or self._field_id(record_type, id),
            # Cyber GRC does not document how this resolves. The record's own ID is what
            # matches its observed behaviour, and the input exists to override it.
            "formDiscussionID": form_discussion_id or id,
            # Cyber GRC rejects a comment whose author is not named, so this is required
            # rather than left to the API to infer from the key.
            "userID": user_id,
        }

        return {Output.COMMENT: self.connection.client.create_record(COMMENT_TYPE, body)}

    def _field_id(self, record_type, record_id):
        """Read the comment thread ID off the record being commented on."""
        record = self.connection.client.get_record(record_type, record_id, select=FIELD_ID)
        field_id = record.get(FIELD_ID)
        if not field_id:
            raise PluginException(
                cause=f"{record_type} record {record_id} has no comment thread.",
                assistance="A comment is tied to a record by its Discussion Field ID, and Cyber GRC has not set one "
                "on this record. Opening the record once in the Cyber GRC web interface creates the thread; "
                "alternatively, supply the Discussion Field ID directly on this step.",
            )
        return field_id
