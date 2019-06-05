import komand
from .schema import ParseTapAlertInput, ParseTapAlertOutput, Input, Output
# Custom imports below
from html_table_parser import HTMLTableParser
from komand_proofpoint_tap.util.tap_formatter import TAP


class ParseTapAlert(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='parse_tap_alert',
                description='Parses a TAP alert',
                input=ParseTapAlertInput(),
                output=ParseTapAlertOutput())

    def run(self, params={}):
        p = HTMLTableParser()
        p.feed(params.get(Input.TAP_ALERT))
        data = p.tables
        clean_data = TAP(data).data

        return {Output.RESULTS: clean_data}
