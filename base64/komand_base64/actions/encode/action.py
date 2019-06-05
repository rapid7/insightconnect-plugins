import komand
from .schema import EncodeInput, EncodeOutput
import base64


class Encode(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='encode',
                description='Encode data to Base64',
                input=EncodeInput(),
                output=EncodeOutput())

    def run(self, params={}):
        string = params['content'].encode('utf-8')
        result = base64.standard_b64encode(string)
        return { 'data': result.decode('utf-8') }

    def test(self):
        string = 'base64'.encode('utf-8')
        result = base64.standard_b64encode(string).decode('utf-8')
        if result == 'YmFzZTY0':
          return { 'data': result }
        raise Exception('Base64 encode failed: %s') % result
