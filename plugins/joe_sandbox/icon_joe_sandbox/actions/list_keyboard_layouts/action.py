import insightconnect_plugin_runtime
from .schema import ListKeyboardLayoutsInput, ListKeyboardLayoutsOutput, Input, Output, Component

# Custom imports below


class ListKeyboardLayouts(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_keyboard_layouts",
            description=Component.DESCRIPTION,
            input=ListKeyboardLayoutsInput(),
            output=ListKeyboardLayoutsOutput(),
        )

    def run(self):
        self.logger.info("Running server_lia_countries")
        locales = self.connection.api.server_languages_and_locales()
        return {Output.KEYBOARD_LAYOUTS: locales}
