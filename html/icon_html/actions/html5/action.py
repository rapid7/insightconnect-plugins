import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
import pypandoc
import base64
import re
from .schema import Html5Input, Html5Output


class Html5(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='html5',
            description='Convert HTML to HTML5',
            input=Html5Input(),
            output=Html5Output())

    def run(self, params={}):
        tag_parser = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"  # noqa: W605
        tags = re.findall(tag_parser, params.get('doc'))
        try:
            if not len(tags):
                raise PluginException(cause='Run: Invalid input.',
                                      assistance='Input must be of type HTML.')
            output = pypandoc.convert_text(params.get('doc'), 'html', format='md')
            new_output = pypandoc.convert(output, 'html5', format="md")
            f = base64.b64encode(new_output.encode('ascii')).decode()
            return {'html5_contents': output, 'html5_file': f}
        except Exception:
            return {'error': 'Error occurred please try again'}

    def test(self):
        return {'test': 'test Success'}
