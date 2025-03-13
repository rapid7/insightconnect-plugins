import insightconnect_plugin_runtime
from .schema import TextInput, TextOutput, Input, Output, Component

# Custom imports below
from bs4 import BeautifulSoup


class Text(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="text",
            description=Component.DESCRIPTION,
            input=TextInput(),
            output=TextOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        document = params.get(Input.DOC, "")
        remove_scripts = params.get(Input.REMOVE_SCRIPTS, False)
        # END INPUT BINDING - DO NOT REMOVE

        if not document:
            return {Output.TEXT: ""}

        soup = BeautifulSoup(document, features="html.parser")
        if remove_scripts:
            for script in soup(
                ["script", "style"]
            ):  # remove all javascript and stylesheet code
                script.extract()
        return {Output.TEXT: soup.get_text()}
