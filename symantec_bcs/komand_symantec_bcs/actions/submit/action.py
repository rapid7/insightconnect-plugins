import komand
from .schema import SubmitInput, SubmitOutput
# Custom imports below
import requests
import base64
import io
import magic


class Submit(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit',
                description='Submit a malicious file or hash',
                input=SubmitInput(),
                output=SubmitOutput())

    def run(self, params={}):
        _type = None
        url = 'https://submit.symantec.com/websubmit/bcs.cgi'

        # Formatted with None and tuples so requests sends form-data properly
        # Request Payload
        # ------WebKitFormBoundaryEczE3Txu7oImEgyU
        # Content-Disposition: form-data; name="mode"
        #
        # 2
        # ------WebKitFormBoundaryEczE3Txu7oImEgyU
        # Content-Disposition: form-data; name="fname"
        #
        # Jon
        # ------WebKitFormBoundaryEczE3Txu7oImEgyU
        # Content-Disposition: form-data; name="lname"
        #
        # Schipp
        # ------WebKitFormBoundaryEczE3Txu7oImEgyU
        # Content-Disposition: form-data; name="cname"
        #
        # Rapid7
        # ------WebKitFormBoundaryEczE3Txu7oImEgyU
        # Content-Disposition: form-data; name="email"
        #
        # jschipp@rapid7.com
        # ------WebKitFormBoundaryEczE3Txu7oImEgyU
        # Content-Disposition: form-data; name="email2"
        #
        # jschipp@rapid7.com
        # ------WebKitFormBoundaryEczE3Txu7oImEgyU
        # Content-Disposition: form-data; name="pin"
        #
        # 12345
        # ------WebKitFormBoundaryEczE3Txu7oImEgyU
        # Content-Disposition: form-data; name="stype"
        #
        # upfile
        # ------WebKitFormBoundaryEczE3Txu7oImEgyU
        # Content-Disposition: form-data; name="upfile"; filename="setup.exe"
        # Content-Type: application/x-msdownload

        stype = params.get('stype')
        headers = {'Origin': 'https://submit.symantec.com', 'Referer': 'https://submit.symantec.com/websubmit/bcs.cgi'}
        req = {
            'mode': (None, "2"),
            'fname': (None, params.get('fname')),
            'lname': (None, params.get('lname')),
            'cname': (None, params.get('cname')),
            'email': (None, params.get('email')),
            'email2': (None, params.get('email')),
            'pin': (None, params.get('pin')),
            'stype': (None, stype),
            'comments': (None, params.get('comments')),
        }

        if params.get('critical') == True:
            req['critical'] = (None, "on")

        data = params.get('data', '')

        if stype == "url":
            self.logger.info('URL specified')
            if not data.startswith('http://') and not data.startswith('https://') and not data.startswith('ftp://'):
                self.logger.error('The URLs must start with http:// or https:// or ftp://')
                raise Exception('Invalid URL format')
            req['url'] = (None, data)
        else:
            req['url'] = (None, "")

        if stype == "hash":
            self.logger.info('Hash specified')
            if len(data) != 32 and len(data) != 64:
                self.logger.error('The hash provided should be in the MD5 or SHA256 format only')
                raise Exception('Invalid hash format')
            req['hash'] = (None, data)
        else:
            req['hash'] = (None, "")

        if stype == "upfile":
            self.logger.info('File specified')
            filename = params.get('filename')
            if not filename: filename = 'komand-uploaded.file'
            self.logger.info('Filename: %s', filename)
            try:
                fisle = io.BytesIO(base64.b64decode(data))
            except:
                self.logger.error('Invalid file bytes input')
                raise

            try:
                _type = magic.Magic(mime=True).from_buffer(fisle.read(1024))
                self.logger.info('MIME Content Type: %s', _type)
            except:
                self.logger.info('Unable to determine MIME Content Type of file, using %s:', _type)
                _type = 'application/octet-stream'
                pass

            # Reset file counter to beginning of file since read 1024 bytes for magic number above
            fisle.seek(0)

            f = fisle.read()
            if len(f) > 0:
                req['upfile'] = (filename, f, _type)
            else:
                req['upfile'] = ("", "", _type)
        else:
            req['upfile'] = (None, "")

        try:
            r = requests.post(url, headers=headers, files=req)
            r.raise_for_status()
            out = base64.b64encode(r.content)
        except requests.exceptions.HTTPError as e:
            self.logger.error("HTTP error occurred. Error: " + str(e))
            raise
        except requests.exceptions.ConnectionError as e:
            self.logger.error("A network problem occurred. Error: " + str(e))
            raise
        except requests.exceptions.Timeout as e:
            self.logger.error("Timeout occurred. Error: " + str(e))
            raise
        except requests.exceptions.TooManyRedirects as e:
            self.logger.error("Too many redirects! Error: " + str(e))
            raise
        except Exception as e:
            self.logger.error("Error: " + str(e))
            raise

        # Debugging
        # self.logger.info(r.request.headers)
        # self.logger.info(r.request.body)

        return {'response': out.decode()}

    def test(self):
        url = 'https://submit.symantec.com/websubmit/bcs.cgi'

        try:
            r = requests.get(url)
            r.raise_for_status()
            out = base64.b64encode(r.content)
        except requests.exceptions.HTTPError as e:
            self.logger.error("HTTP error occurred. Error: " + str(e))
            raise
        except requests.exceptions.ConnectionError as e:
            self.logger.error("A network problem occurred. Error: " + str(e))
            raise
        except requests.exceptions.Timeout as e:
            self.logger.error("Timeout occurred. Error: " + str(e))
            raise
        except requests.exceptions.TooManyRedirects as e:
            self.logger.error("Too many redirects! Error: " + str(e))
            raise
        except Exception as e:
            self.logger.error("Error: " + str(e))
            raise

        return {'response': out.decode()}
