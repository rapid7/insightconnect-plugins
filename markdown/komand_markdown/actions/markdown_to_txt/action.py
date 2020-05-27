import komand
from .schema import MarkdownToTxtInput, MarkdownToTxtOutput, Input, Output, Component
from komand_markdown.util import utils
# Custom imports below
from bs4 import BeautifulSoup
import binascii


class MarkdownToTxt(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='markdown_to_txt',
            description=Component.DESCRIPTION,
            input=MarkdownToTxtInput(),
            output=MarkdownToTxtOutput())

    def run(self, params={}):
        markdown_bytes = params.get(Input.MARKDOWN)
        markdown_string = params.get(Input.MARKDOWN_STRING)

        if not (((markdown_string is None) ^ (markdown_bytes is None))
                or ((markdown_string == "") ^ (markdown_bytes == ""))):
            raise Exception("You must define one of Markdown or Markdown String")

        if markdown_bytes is not None:
            try:
                markdown = utils.from_bytes(markdown_bytes)
            except binascii.Error as _:
                bytes_len = len(markdown_bytes)
                markdown = utils.from_bytes(markdown_bytes[:bytes_len - (bytes_len % 4)])
        else:
            markdown = markdown_string

        soup = BeautifulSoup(utils.convert(markdown, 'md', 'html'), features='html.parser')
        for script in soup(["script", "style"]):
            script.extract()
        txt_string = soup.get_text()

        return {
            Output.TXT_STRING: txt_string,
            Output.TXT: utils.to_bytes(txt_string)
        }
