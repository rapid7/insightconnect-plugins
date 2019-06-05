import komand
from .schema import CreateDocumentInput, CreateDocumentOutput, Input, Output, Component
# Custom imports below


class CreateDocument(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_document',
                description=Component.DESCRIPTION,
                input=CreateDocumentInput(),
                output=CreateDocumentOutput())

    def run(self, params={}):
        doc_title = params.get(Input.TITLE)
        doc_body = params.get(Input.CONTENT)

        body = {
            'title': doc_title
        }

        doc_result = self.connection.doc_service.documents().create(body=body).execute()
        document_id = doc_result.get('documentId')

        self.logger.info(f"Document created with ID: {document_id}")

        doc_request = [
            {
                'insertText': {
                    'location': {
                        'index': 1,
                    },
                    'text': doc_body
                }
            }
        ]

        doc_result_insert_text = self.connection.doc_service.documents().batchUpdate(
            documentId=document_id, body={'requests': doc_request}).execute()

        self.logger.info(f"Text inserted successfully")

        return {Output.RESULT: doc_result_insert_text}
