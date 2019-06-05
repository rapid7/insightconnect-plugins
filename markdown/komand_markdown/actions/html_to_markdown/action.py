import komand
from komand_markdown.util import utils
from .schema import HtmlToMarkdownInput, HtmlToMarkdownOutput


class HtmlToMarkdown(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='html_to_markdown',
                description='Convert HTML to Markdown',
                input=HtmlToMarkdownInput(),
                output=HtmlToMarkdownOutput())

    def run(self, params={}):
        inbytes = params.get('html')
        instr = params.get('html_string')
        if  not (((instr == None) ^ (inbytes == None)) or ((instr == "") ^ (inbytes == ""))):
            raise Exception("Only one of HTML or HTML String can be defined" if instr != inbytes else "You must define one of HTML or HTML String.")
        if instr:
            markdown_string = utils.convert(instr,'html', 'md')
            markdown_b64 = utils.to_bytes(markdown_string)
        else:
            markdown_string = utils.convert(utils.from_bytes(inbytes),'html', 'md')
            markdown_b64 = utils.to_bytes(markdown_string)
        return {'markdown_string': markdown_string, 'markdown': markdown_b64}

    def test(self):
        return {}
