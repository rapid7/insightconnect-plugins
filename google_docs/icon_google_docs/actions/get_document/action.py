import komand
from .schema import GetDocumentInput, GetDocumentOutput, Input, Output, Component
# Custom imports below


class GetDocument(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_document',
                description=Component.DESCRIPTION,
                input=GetDocumentInput(),
                output=GetDocumentOutput())

    def run(self, params={}):
        document_id = params.get(Input.DOCUMENT_ID)
        self.logger.info(f"Getting document ID: {document_id}")
        document = self.connection.doc_service.documents().get(documentId=document_id).execute()
        return {Output.DOCUMENT: document}
