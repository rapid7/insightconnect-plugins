import komand
from .schema import UploadInput, UploadOutput
# Custom imports below
import requests
import json
import magic
import hashlib
from requests_toolbelt.multipart.encoder import MultipartEncoder


class Upload(komand.Action):

    _UPLOAD = 'upload'
    _HTTPERROR = {301: 'moved permanently',
                  400: 'bad request',
                  401: 'unauthorized',
                  403: 'forbidden',
                  404: 'not found',
                  500: 'internal server error',
                  503: 'service unavailable',
                  000: 'Unknown Status Code'
                  }

    def __init__(self):
        super(self.__class__, self).__init__(
                name='upload',
                description='Upload a file for analysis',
                input=UploadInput(),
                output=UploadOutput())

    def run(self, params={}):
        file_name = params.get('file_name')
        file_type = params.get('file_type')
        file_bytes = params.get('file_bytes').encode()

        # Build URL
        url = self.connection.url + self._UPLOAD

        # Find mime/type
        mime = magic.Magic(mime=True)
        mime_type = mime.from_buffer(file_bytes)

        # Hash file_bytes
        hashed = hashlib.sha1(file_bytes)
        file_hash = hashed.hexdigest()

        # Build Request JSON
        request = {"request": {'sha1': file_hash,
                               'file_name': file_name,
                               'file_type': file_type
                               }
                   }
        request = json.dumps(request)

        # Build body
        body = MultipartEncoder(
            fields={"request": request,
                    'file': (file_name, file_bytes, mime_type)
                    }
        )
        try:
            response = self.connection.session.post(
                url, headers={'Content-Type': body.content_type}, data=body)
        except requests.RequestException as e:
            raise Exception(e)
        if response.status_code == 200:
            response_json = response.json()
            code = response_json['response']['status']['code']
            if code == 1001 or 1002:
                return {'results': response_json['response']}
            else:
                label = response_json['response']['status']['label']
                message = response_json['response']['status']['message']
                self.logger.error('There was a issue with the return from Checkpoint: {}'
                                  .format(message))
                raise Exception('Checkpoint error {code} {label}'.format(code=code, label=label))
        else:
            status_code_message = self._HTTPERROR.get(response.status_code, self._HTTPERROR[000])
            self.logger.error("{status} ({code})".format(status=status_code_message,
                                                         code=response.status_code))
            raise Exception('HTTP Error code{}'.format(response.status_code))

    def test(self):
        # TODO: Implement test function
        return {}
