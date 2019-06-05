import komand
import base64

from ..utils import parse_cef

from .schema import ParseMultipleInput, ParseMultipleOutput


class ParseMultiple(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='parse_multiple',
                description='Parse multiple CEF formatted strings from a file',
                input=ParseMultipleInput(),
                output=ParseMultipleOutput())

    def run(self, params={}):
        f = params.get('file')
        decoded = base64.b64decode(f).decode('utf-8')        
        lines = decoded.split('\n')

        return {
          'cefs': [parse_cef(line) for line in lines]
        }

    def test(self):
        return self.run({'file': 'Q0VGOjB8S29tYW5kfEtvbWFuZHwxfDJ8U29tZSBFdmVudHxMb3d8IF9jZWZWZXI9MC4xCkNFRjowfEtvbWFuZHxLb21hbmR8MXwyfFNvbWUgRXZlbnR8TG93fCBfY2VmVmVyPTAuMQpDRUY6MHxLb21hbmR8S29tYW5kfDF8MnxTb21lIEV2ZW50fExvd3wgX2NlZlZlcj0wLjE='})
