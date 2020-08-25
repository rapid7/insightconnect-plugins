import komand
from .schema import AppendLineInput, AppendLineOutput, Input, Output, Component
# Custom imports below


class AppendLine(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='append_line',
                description=Component.DESCRIPTION,
                input=AppendLineInput(),
                output=AppendLineOutput())

    def run(self, params={}):
        document_id = params.get(Input.DOCUMENT_ID)
        doc_body = params.get(Input.CONTENT)

        self.logger.info(f"Append line at the end of document with ID: {document_id}")

        doc_request = [
            {
                'insertText': {
                    "endOfSegmentLocation": {},
                    'text': "\n" + doc_body
                }
            }
        ]

        doc_result_insert_text = self.connection.doc_service.documents().batchUpdate(
            documentId=document_id, body={'requests': doc_request}).execute()

        self.logger.info(f"Text inserted successfully")

        return {Output.RESULT: doc_result_insert_text}
