import komand
from .schema import AddAttachmentInput, AddAttachmentOutput
# Custom imports below
import shutil
import tempfile
import base64


class AddAttachment(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_attachment',
                description='Add attachment to event',
                input=AddAttachmentInput(),
                output=AddAttachmentOutput())

    def run(self, params={}):
        
        attachment = params.get('attachment')
        filename = params.get('filename')

        path = tempfile.mkdtemp()+"/"
        fname = 'tmp.txt'
        with open(path+fname, 'w') as f:
            f.write(base64.b64decode(attachment).decode('utf-8'))

        client = self.connection.client
        in_event = client.get_event(params.get('event'))
        out = client.add_attachment(in_event, attachment=path+fname, filename=filename)
        self.logger.info(out)
        shutil.rmtree(path)
        return {'status': True}

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        self.logger.info(output)
        return {"status": True}
