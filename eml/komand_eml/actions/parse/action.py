import komand
from .schema import ParseInput, ParseOutput, Input, Output
# Custom imports below
import base64
import email
from komand_eml.util import format_output
from bs4 import UnicodeDammit


class Parse(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='parse',
            description='Extract headers and file attachments',
            input=ParseInput(),
            output=ParseOutput())

    def run(self, params={}):
        try:
            eml_file = base64.b64decode(params.get(Input.EML_FILE)).decode('utf-8')
        except Exception as ex:
            self.logger.debug(ex)
            self.logger.debug("Failed to parse message as UTF-8, attempting to detwingle first before retrying parse")
            eml_file = UnicodeDammit.detwingle(base64.b64decode(params.get(Input.EML_FILE))).decode('utf-8', errors='ignore')

        msg = email.message_from_string(eml_file)

        result = format_output.format_result(self.logger, msg)
        return {Output.RESULT: result}
