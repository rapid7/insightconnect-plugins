import insightconnect_plugin_runtime
from .schema import EpubInput, EpubOutput, Input, Output, Component
from icon_html.util.api import HTMLConverter
from icon_html.util.strategies import ConvertToEpub


class Epub(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="epub",
            description=Component.DESCRIPTION,
            input=EpubInput(),
            output=EpubOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        document = params.get(Input.DOC, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.EPUB: HTMLConverter(ConvertToEpub()).convert(document)}
