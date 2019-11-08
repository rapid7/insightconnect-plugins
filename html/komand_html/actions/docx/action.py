import komand
import base64
import pypandoc
import re

from komand.exceptions import PluginException
from .schema import DocxInput, DocxOutput


class Docx(komand.Action):
  def __init__(self):
      super(self.__class__, self).__init__(
              name='docx',
              description='Convert HTML to DOCX',
              input=DocxInput(),
              output=DocxOutput())

  def run(self, params={}):
    temp_file = 'temp_html_2_docx.docx'
    tag_parser = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"
    tags = re.findall(tag_parser, params.get('doc'))
    try:
        if not len(tags):
            raise PluginException(cause='Run: Input Invalid.',
                                  assistance='Input must be of type HTML.')
        pypandoc.convert(params.get('doc'), 'docx', outputfile=temp_file, format='html')
        with open(temp_file, 'rb') as output:
            #Reading the output and sending it in base64
            return {'docx': base64.b64encode(output.read()).decode('utf-8')}
    except:
        return {'error': 'Error occurred please try again'}

  def test(self):
    return {'test': 'test Success'}
