import komand
from komand_markdown.util import utils 
from .schema import MarkdownToHtmlInput, MarkdownToHtmlOutput


class MarkdownToHtml(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='markdown_to_html',
                description='Convert Markdown to HTML',
                input=MarkdownToHtmlInput(),
                output=MarkdownToHtmlOutput())

    def run(self, params={}):
        inbytes = params.get('markdown')
        instr = params.get('markdown_string')
        if  not (((instr == None) ^ (inbytes == None)) or ((instr == "") ^ (inbytes ==  ""))):
            raise Exception("Only one of Markdown or Markdown String can be defined" if instr != inbytes else "You must define one of Markdown or Markdown String.")
        if instr:
            html_string = utils.convert(instr,'md', 'html')
            html_b64 = utils.to_bytes(html_string)
        else:
            html_string = utils.convert(utils.from_bytes(inbytes),'md', 'html')
            html_b64 = utils.to_bytes(html_string)
        return {'html_string': html_string, 'html': html_b64}

    def test(self):
        return {}