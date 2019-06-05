import komand
from .schema import AttachIncidentInput, AttachIncidentOutput
# Custom imports below


class AttachIncident(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='attach_incident',
                description='Attach a file to an incident',
                input=AttachIncidentInput(),
                output=AttachIncidentOutput())

    def run(self, params={}):
        incident_id = params.get('incident_id')
        attachment_bytes = params.get('attachment_bytes')
        attachment_name = params.get('attachment_name')

        attachment = self.connection.api.attach_file_to_incident(
            incident_id, attachment_bytes, attachment_name
        )

        return {'attachment': attachment}

    def test(self):
        return {
            'attachment': {
                'id': 27211951,
                'content_type': 'text/plain',
                'size': 12,
                'filename': 'Hello.txt',
                'url': 'https://s3.amazonaws.com/Production_CustomerData/attachments/3e696549fd7763d9ca28/Hello.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIABLAHBLAHBLAH%2F20181122%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20181122T192713Z&X-Amz-Expires=600&X-Amz-SignedHeaders=host&X-Amz-Signature=443e9699312d3ce11e8910b0dd2def736b76846e72b9cd8f241481ddfad6536e',
                'shared_attachment': False,
                'attachable_id': 31851783,
                'attachable_type': 'Incident',
                'attachment_type': 'attachment',
                'thumb_url': '/attachments/3e696549fd7763d9ca28/hello-txt.plain?thumb=true',
                'secure_url': '/attachments/3e696549fd7763d9ca28/hello-txt.plain',
                'uuid': '3e696549fd7763d9ca28'
            }
        }
