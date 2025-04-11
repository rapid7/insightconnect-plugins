import insightconnect_plugin_runtime
from .schema import DocxInput, DocxOutput, Output, Input, Component
from icon_html.util.api import HTMLConverter
from icon_html.util.strategies import ConvertToDocx


class Docx(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="docx",
            description=Component.DESCRIPTION,
            input=DocxInput(),
            output=DocxOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        document = params.get(Input.DOC, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.DOCX: HTMLConverter(ConvertToDocx()).convert(document)}
