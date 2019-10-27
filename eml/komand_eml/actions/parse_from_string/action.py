import komand
from .schema import ParseFromStringInput, ParseFromStringOutput, Input, Output, Component
# Custom imports below
import email
from komand_eml.util import format_output


class ParseFromString(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='parse_from_string',
                description=Component.DESCRIPTION,
                input=ParseFromStringInput(),
                output=ParseFromStringOutput())

    def run(self, params={}):
        msg = email.message_from_string(params.get(Input.EMAIL_STRING))
        result = format_output.format_result(self.logger, msg)
        return {Output.RESULT: result}
