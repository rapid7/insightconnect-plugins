import komand
import pdfkit
import tempfile
import shutil
from komand_markdown.util import utils
from .schema import MarkdownToPdfInput, MarkdownToPdfOutput


def makePDF(html,path):
    infile = path+"str.html"
    outfile = path+"tmp.pdf"
    with open(infile,'w') as f:
        f.write(html)
    pdfkit.from_file(infile, outfile)
    outbytes = ""
    with open(outfile, 'r') as f:
        outbytes = f.read()
    return outbytes

class MarkdownToPdf(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='markdown_to_pdf',
                description='Convert Markdown to PDF',
                input=MarkdownToPdfInput(),
                output=MarkdownToPdfOutput())

    def run(self, params={}):
        inbytes = params.get('markdown')
        instr = params.get('markdown_string')
        if  not (((instr == None) ^ (inbytes == None)) or ((instr == "") ^ (inbytes ==  ""))):
            raise Exception("Only one of Markdown or Markdown String can be defined" if instr != inbytes else "You must define one of Markdown or Markdown String.")
        
        
        
        path = tempfile.mkdtemp()+"/"
        if instr:
            html_string = utils.convert(instr,'md', 'html')
            pdf_string = makePDF(html_string,path)
            pdf_b64 = utils.to_bytes(pdf_string)
        else:
            html_string = utils.convert(utils.from_bytes(inbytes),'md', 'html')
            pdf_string = makePDF(html_string,path)
            pdf_b64 = utils.to_bytes(pdf_string)
        shutil.rmtree(path)
        return {'pdf_string': pdf_string, 'pdf': pdf_b64}

    def test(self):
        return {}

