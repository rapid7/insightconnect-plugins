import insightconnect_plugin_runtime
from .schema import ListMessagesInChatInput, ListMessagesInChatOutput, Input, Output, Component


class ListMessagesInChat(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_messages_in_chat",
            description=Component.DESCRIPTION,
            input=ListMessagesInChatInput(),
            output=ListMessagesInChatOutput(),
        )

    def run(self, params={}):
        chat_id = params.get(Input.CHAT_ID, "")

        messages = self.connection.client.list_chat_messages(chat_id)

        return {Output.MESSAGES: messages}
