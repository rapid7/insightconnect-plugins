import komand
from .schema import GetReportHtmlInput, GetReportHtmlOutput
# Custom imports below
import base64
import sys


class GetReportHtml(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_report_html',
                description='Get the HTML version of the report for a particular scan',
                input=GetReportHtmlInput(),
                output=GetReportHtmlOutput())

    def run(self, params={}):
        scanid = str(params.get('scan_id'))
        try:
            report_id = self.connection.scanner.get_report_id(scanid)
            xmlresponse = self.connection.scanner.get_report_html(report_id)
            xmlresponse = xmlresponse.find('report')
            # workaround for the fact that xmlresponse.text returns None even though the data is in there,
            # this hack gets you the last element in the iterator.
            last = None
            for last in xmlresponse.itertext():
                pass
            if last == None:
                return {'report': '', 'success': False, 'message': 'Error, malformed XML response from OpenVAS server.'}
            html = base64.b64decode(last)
        except:
            return {'report': '', 'success': False,
                    'message': ' | '.join([str(sys.exc_info()[0]), str(sys.exc_info()[1])])}
        return {'report': html, 'success': True,
                'message': 'Successfully obtained OpenVAS Results for taskid ' + str(scanid)}

    def test(self):
        # TODO: Implement test function
        return {}
