import insightconnect_plugin_runtime
from .schema import ListLanguagesAndLocalesInput, ListLanguagesAndLocalesOutput, Input, Output, Component

# Custom imports below


class ListLanguagesAndLocales(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_languages_and_locales",
            description=Component.DESCRIPTION,
            input=ListLanguagesAndLocalesInput(),
            output=ListLanguagesAndLocalesOutput(),
        )

    def run(self):
        self.logger.info("Running server languages and locales")
        locales = self.connection.api.server_languages_and_locales()
        return {Output.KEYBOARD_LAYOUTS: locales}
