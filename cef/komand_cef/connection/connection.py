import komand
from .schema import ConnectionSchema
# Custom imports below
from komand.exceptions import ConnectionTestException
from komand_cef.util import utils


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        pass

    def test(self):
        result = utils.obj_to_cef({
            'cef': {
                'severity': "Low",
                'device_version': "1",
                'signature_id': "2",
                'name': "Some Event",
                'device_product': "Komand",
                'device_vendor': "Komand",
                'version': "1"
            }})
        self.logger.info(result)

        if result['cef_string'] != "CEF:0|Komand|Komand|1|2|Some Event|Low| _cefVer=0.1\n":
            raise ConnectionTestException(cause='Test failed!', assistance=f'Create CEF String failed: {result}')

        return result
