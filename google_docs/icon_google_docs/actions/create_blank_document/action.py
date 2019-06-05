import komand
from .schema import CreateBlankDocumentInput, CreateBlankDocumentOutput, Input, Output, Component
# Custom imports below


class CreateBlankDocument(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_blank_document',
                description=Component.DESCRIPTION,
                input=CreateBlankDocumentInput(),
                output=CreateBlankDocumentOutput())

    def run(self, params={}):
        doc_title = params.get(Input.TITLE)

        body = {
            'title': doc_title
        }

        doc_result = self.connection.doc_service.documents().create(body=body).execute()
        document_id = doc_result.get('documentId')

        self.logger.info(f"Document created with ID: {document_id}")

        return {Output.DOCUMENT: doc_result}
