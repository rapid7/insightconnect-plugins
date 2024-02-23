import insightconnect_plugin_runtime
from .schema import ListKeyboardLayoutsInput, ListKeyboardLayoutsOutput, Output

# Custom imports below


class ListKeyboardLayouts(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_keyboard_layouts",
            description="Retrieve a list of available keyboard layouts for Windows analyzers",
            input=ListKeyboardLayoutsInput(),
            output=ListKeyboardLayoutsOutput(),
        )

    def run(
        self,
    ):
        keyboard_layouts = self.connection.api.server_keyboard_layouts()
        return {Output.KEYBOARD_LAYOUTS: keyboard_layouts}
