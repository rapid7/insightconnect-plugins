import komand

from ..utils import obj_to_cef
from .schema import CreateStringInput, CreateStringOutput


class CreateString(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_string',
                description='Creates a CEF formatted string',
                input=CreateStringInput(),
                output=CreateStringOutput())

    def run(self, params={}):
        return {
          'cef_string': obj_to_cef(params.get('cef'))
        }

    def test(self):
        result = self.run({
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
          raise Exception('Create CEF String failed: {}'.format(result))
        return result
