import komand
from .schema import DecodeInput, DecodeOutput
import base64


class Decode(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='decode',
                description='Decode Base64 to data',
                input=DecodeInput(),
                output=DecodeOutput())

    def run(self, params={}):
        try:
            data = params.get('base64')
            errors = params.get('errors')
            result = base64.standard_b64decode(data)
            if errors in ["replace", "ignore"]:
                return {'data': result.decode('utf-8', errors=errors)}
            else:
                return {'data': result.decode('utf-8')}
        except Exception as e:
            self.logger.error("An error has occurred while decoding ", e)
            raise

    def test(self):
        b64 = 'YmFzZTY0'
        result = base64.standard_b64decode(b64).decode('utf-8')
        if result == 'base64':
          return {'data': result}
        raise Exception('Base64 decode failed: %s') % result
