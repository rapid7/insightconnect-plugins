import komand
from .schema import DownloadAttachmentInput, DownloadAttachmentOutput
# Custom imports below
import requests
import base64


class DownloadAttachment(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='download_attachment',
                description='Download attachment',
                input=DownloadAttachmentInput(),
                output=DownloadAttachmentOutput())

    def run(self, params={}):
        key = self.connection.key
        attribute_id = params.get('attribute_id')

        headers = {'content-type': 'application/json', 'Authorization': key}

        path = '/attributes/downloadAttachment/download/%s' % attribute_id
        url = self.connection.url + path

        try:
            # Generate request
            response = requests.get(url, headers=headers, verify=False)
            message = str(response.json()['message'])
            response.raise_for_status()
        except ValueError:
            self.logger.error('Attribute ID did not contain an attachment')
            raise Exception('No attachment found for ID')
        except requests.exceptions.HTTPError as e:
            self.logger.error(e)
            raise

        # Encode data as b64
        attachment = base64.b64encode(response.content).decode("utf-8")

        return {'attachment': attachment}

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        self.logger.info(output)
        return {"status": True}
