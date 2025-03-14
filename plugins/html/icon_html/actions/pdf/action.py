import insightconnect_plugin_runtime
from .schema import PdfInput, PdfOutput, Input, Output, Component
from icon_html.util.api import HTMLConverter
from icon_html.util.strategies import ConvertToPDF


class Pdf(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="pdf",
            description=Component.DESCRIPTION,
            input=PdfInput(),
            output=PdfOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        document = params.get(Input.DOC, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.PDF: HTMLConverter(ConvertToPDF()).convert(document)}
