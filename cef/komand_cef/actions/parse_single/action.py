import komand
from ..utils import parse_cef
from .schema import ParseSingleInput, ParseSingleOutput


class ParseSingle(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='parse_single',
                description='Parse a single CEF formatted string',
                input=ParseSingleInput(),
                output=ParseSingleOutput())

    def run(self, params={}):
        return {
          'cef': parse_cef(params.get('cef_string'))
        }

    def test(self):
        cef = 'CEF:0|Komand|Komand|1|2|Some Event|Low| _cefVer=0.1'
        result = self.run({ 'cef_string': cef })
        cef_obj = result['cef']
        if ('signature_id' not in cef_obj
            or 'device_version' not in cef_obj 
            or 'severity' not in cef_obj 
            or 'device_product' not in cef_obj 
            or 'version' not in cef_obj 
            or 'name' not in cef_obj
            or 'device_vendor' not in cef_obj):
              raise Exception('Parse Single CEF failed: {}'.format(result))
        return { 'cef': result }
       
