import komand
import pypandoc
import base64
import re
from .schema import MarkdownInput, MarkdownOutput
from komand.exceptions import PluginException


class Markdown(komand.Action):
  def __init__(self):
      super(self.__class__, self).__init__(
              name='markdown',
              description='Convert HTML to Markdown',
              input=MarkdownInput(),
              output=MarkdownOutput())

  def run(self, params={}):
    tag_parser = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"
    tags = re.findall(tag_parser, params.get('doc'))
    try:
        if not len(tags):
            raise PluginException(cause='Run: Input Invalid',
                                  assistance='Input must be of type HTML')
        output = pypandoc.convert_text(params.get('doc'), 'md', format='html')
        f = base64.b64encode(output.encode('ascii')).decode()
        return {'markdown_contents': output, 'markdown_file': f}
    except:
        return {'error': 'Error occured please try again'}

  def test(self):
    return {'test': 'test Success'}
