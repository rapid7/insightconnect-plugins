import komand
from .schema import DetectEncodingInput, DetectEncodingOutput, Input, Output, Component
# Custom imports below
import chardet
import base64


class DetectEncoding(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='detect_encoding',
                description=Component.DESCRIPTION,
                input=DetectEncodingInput(),
                output=DetectEncodingOutput())

    def run(self, params={}):
        string_to_analyze = params.get(Input.BYTES_TO_ANALYZE)
        bytes_to_analyze = base64.standard_b64decode(string_to_analyze)
        output = chardet.detect(bytes_to_analyze)

        return {Output.RECOMMENDATION: output}
