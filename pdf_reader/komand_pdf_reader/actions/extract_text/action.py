import komand
from .schema import ExtractTextInput, ExtractTextOutput
# Custom imports below
import PyPDF2
import base64

class ExtractText(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='extract_text',
                description='Extract text from PDF file',
                input=ExtractTextInput(),
                output=ExtractTextOutput())

    def run(self, params={}):
        try:
            if params.get('contents'):
                pdfFile = base64.b64decode(params.get('contents'))
            else:
                raise Exception("File contents missing!")
        except Exception as e:
            self.logger.error("File contents missing: ", e)
            raise
        try:
            with open("temp.pdf", 'wb') as temp_pdf:
                temp_pdf.write(pdfFile)
                pdfReader = PyPDF2.PdfFileReader(open('temp.pdf', 'rb'))
                pdftext = ""
                for page in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(page)
                    pdftext += pageObj.extractText().replace('\n','')
        except Exception as e:
            self.logger.info("An error occurred while extracting text: ", e)
            raise
        return {"output": pdftext}

    def test(self):
        return {"output": "successful"}
