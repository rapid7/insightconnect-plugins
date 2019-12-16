import komand
from .schema import UploadSslCertificateInput, UploadSslCertificateOutput
# Custom imports below
import json
import base64


class UploadSslCertificate(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='upload_ssl_certificate',
                description='Upload a SSL Certificate to SecureSphere Server',
                input=UploadSslCertificateInput(),
                output=UploadSslCertificateOutput())

    def run(self, params={}):
        format_type = params['format']
        url = self.connection.url
        upload_ssl_cert_url = "/SecureSphere/api/v1/conf/webServices/{}/{}/{}/sslCertificates/{}".format(
                                                                                    params['sitename'],
                                                                                    params['servergroupname'],
                                                                                    params['webservicename'],
                                                                                    params['sslkeyname']
                                                                                    )
        # Logic for checking what format type
        if format_type == 'pem':
            certkey = "certificate"
            cert = base64.b64decode(params['certificate'])
            keypasskey = "private"
            keypass = base64.b64decode(params['private'])
        else:
            certkey = "pkcs12file"
            cert = base64.b64decode(params['pkcs12file'])
            keypasskey = "pkcs12password"
            keypass = base64.b64decode(params['pkcs12password'])

        payload = {"format":"{}".format(params["format"]),
                   "{}".format(certkey):"{}".format(cert.decode('utf-8')),
                   "{}".format(keypasskey):"{}".format(keypass.decode('utf-8')),
                   "hsm":params['hsm']
                   }
        payload_json = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        try:
            response = self.connection.s.post(url + upload_ssl_cert_url, data=payload_json, headers=headers, verify=False)
            self.logger.info(response.text)
            return {"status_code": response.status_code}
        except Exception:
            raise Exception("An error has occurred while uploading the SSL certificate")

    def test(self):
        try:
            url = self.connection.url
            response = self.connection.s.get(url)
            return {"status_code": response.status_code}
        except Exception:
            raise Exception("An error has occurred while running test")
