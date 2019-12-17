import komand
from .schema import ParseTapAlertInput, ParseTapAlertOutput, Input, Output
# Custom imports below
from html_table_parser import HTMLTableParser
from komand_proofpoint_tap.util.tap_formatter import TAP
from urlextract import URLExtract


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

        # Get the Threat details URL which is NOT an HTML table element, but instead the <a> link of the
        #    table element
        extractor = URLExtract()
        cleaned_input_for_extractor = params.get(Input.TAP_ALERT)
        cleaned_input_for_extractor.replace('\n', '')
        urls_from_input = extractor.find_urls(cleaned_input_for_extractor)
        threat_details_urls = list(filter(lambda u: r'threat/email' in u and r'threatinsight.proofpoint.com' in u[:40],
                                     urls_from_input))
        if threat_details_urls:
            clean_data['threat']['threat_details_url'] = threat_details_urls[0]

        return {Output.RESULTS: clean_data}
