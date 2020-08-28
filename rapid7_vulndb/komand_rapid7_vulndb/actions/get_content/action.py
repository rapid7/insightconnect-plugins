import insightconnect_plugin_runtime
from .schema import GetContentInput, GetContentOutput, Input, Output, Component
from komand_rapid7_vulndb.util import extract
# Custom imports below


class GetContent(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_content',
                description=Component.DESCRIPTION,
                input=GetContentInput(),
                output=GetContentOutput())

    def run(self, params={}):
        identifier = params.get(Input.IDENTIFIER)
        content_result = extract.Content.get(identifier)

        return {Output.CONTENT_RESULT: content_result}

