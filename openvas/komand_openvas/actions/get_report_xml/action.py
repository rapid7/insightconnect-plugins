import komand
from .schema import GetReportXmlInput, GetReportXmlOutput
# Custom imports below
import sys
from openvas_lib import VulnscanTaskNotFinishedError
from openvas_lib import VulnscanServerError
from xml.etree.ElementTree import tostring


class GetReportXml(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_report_xml',
                description='Get the XML version of the report for a particular scan',
                input=GetReportXmlInput(),
                output=GetReportXmlOutput())

    def run(self, params={}):
        scanid = str(params.get('scan_id'))
        try:
            openvas_results = self.connection.scanner.get_raw_xml(scanid)
        except VulnscanTaskNotFinishedError as e:
            return {'report': '', 'success': False, 'message': str(e)}
        except VulnscanServerError as e:
            return {'report': '', 'success': False, 'message': str(e)}
        except:
            return {'report': '', 'success': False,
                    'message': ' | '.join([str(sys.exc_info()[0]), str(sys.exc_info()[1])])}

        return {'report': str(tostring(openvas_results, 'utf-8')), 'success': True,
                'message': 'Successfully obtained OpenVAS Results for taskid ' + str(scanid)}

    def test(self):
        # TODO: Implement test function
        return {}
