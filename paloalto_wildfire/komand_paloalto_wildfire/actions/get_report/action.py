import komand
from .schema import GetReportInput, GetReportOutput
# Custom imports below
import requests
import base64


class GetReport(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_report',
                description='Query for an XML or PDF report for a particular sample',
                input=GetReportInput(),
                output=GetReportOutput())

    def run(self, params={}):
        """TODO: Run action"""
        endpoint =  "/publicapi/get/report"
        client = self.connection.client
        url = 'https://{}/{}'.format(self.connection.host, endpoint)
        # Formatted with None and tuples so requests sends form-data properly
        # => Send data, 299 bytes (0x12b)
        # 0000: --------------------------8557684369749613
        # 002c: Content-Disposition: form-data; name="apikey"
        # 005b:
        # 005d: 740219c8fab2606b9206b2d40626b2d1
        # 007f: --------------------------8557684369749613
        # 00ab: Content-Disposition: form-data; name="format"
        # 00d8:
        # 00da: pdf
        # 00fd: --------------------------8557684369749613--
        # ...

        req = {
            'apikey': (None, self.connection.api_key),
            'hash': (None, params.get('hash')),
            'format': (None, params.get('format'))
        }
        r = requests.post(url, files=req)
        out = base64.b64encode(r.content).decode()
        return { 'report': out }

    def test(self):
        """TODO: Test action"""
        client = self.connection.client
        return { 'report': 'Test' }
