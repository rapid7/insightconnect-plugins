import komand
import base64

from komand.exceptions import PluginException
import pypandoc
import re
from .schema import EpubInput, EpubOutput


class Epub(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='epub',
            description='Convert HTML to EPUB',
            input=EpubInput(),
            output=EpubOutput())

    def run(self, params={}):
        temp_file = 'temp_html_2_epub.epub'
        tag_parser = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"  # noqa: W605
        tags = re.findall(tag_parser, params.get('doc'))
        try:
            if not len(tags):
                raise PluginException(cause='Run: Invalid input.',
                                      assistance='Input must be of type HTML.')
            pypandoc.convert(params.get('doc'), 'epub', outputfile=temp_file, format='html')
            with open(temp_file, 'rb') as output:
                # Reading the output and sending it in base64
                return {'epub': base64.b64encode(output.read()).decode('utf-8')}
        except Exception:
            return {'error': 'Error occurred please try again'}

    def test(self):
        return {'test': 'test Success'}
