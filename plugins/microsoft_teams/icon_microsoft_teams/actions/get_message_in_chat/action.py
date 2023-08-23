import insightconnect_plugin_runtime
from .schema import GetMessageInChatInput, GetMessageInChatOutput, Input, Output, Component
from icon_microsoft_teams.util.teams_utils import get_message_from_chat


class GetMessageInChat(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_message_in_chat",
            description=Component.DESCRIPTION,
            input=GetMessageInChatInput(),
            output=GetMessageInChatOutput(),
        )

    def run(self, params={}):
        username = params.get(Input.USERNAME, "")
        chat_id = params.get(Input.CHAT_ID, "")
        message_id = params.get(Input.MESSAGE_ID, "")

        message = get_message_from_chat(self.connection, username, chat_id, message_id)
        return {Output.MESSAGE: message}
