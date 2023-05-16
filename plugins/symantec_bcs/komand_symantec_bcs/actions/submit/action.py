import insightconnect_plugin_runtime
from .schema import SubmitInput, SubmitOutput

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import requests
import base64
import io
import magic


class Submit(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit",
            description="Submit a malicious file or hash",
            input=SubmitInput(),
            output=SubmitOutput(),
        )

    def run(self, params={}):  # noqa: MC0001
        _type = None
        url = "https://submit.symantec.com/websubmit/bcs.cgi"

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

        stype = params.get("stype")
        headers = {
            "Origin": "https://submit.symantec.com",
            "Referer": "https://submit.symantec.com/websubmit/bcs.cgi",
        }
        req = {
            "mode": (None, "2"),
            "fname": (None, params.get("fname")),
            "lname": (None, params.get("lname")),
            "cname": (None, params.get("cname")),
            "email": (None, params.get("email")),
            "email2": (None, params.get("email")),
            "pin": (None, params.get("pin")),
            "stype": (None, stype),
            "comments": (None, params.get("comments")),
        }

        if params.get("critical") is True:
            req["critical"] = (None, "on")

        data = params.get("data", "")

        if stype == "url":
            self.logger.info("URL specified")
            if not data.startswith("http://") and not data.startswith("https://") and not data.startswith("ftp://"):
                raise PluginException(
                    cause="Invalid URL format", assistance="The URLs must start with http:// or https:// or ftp://"
                )
            req["url"] = (None, data)
        else:
            req["url"] = (None, "")

        if stype == "hash":
            self.logger.info("Hash specified")
            if len(data) != 32 and len(data) != 64:
                raise PluginException(
                    cause="Invalid hash format",
                    assistance="The hash provided should be in the MD5 or SHA256 format only",
                )
            req["hash"] = (None, data)
        else:
            req["hash"] = (None, "")

        if stype == "upfile":
            self.logger.info("File specified")
            filename = params.get("filename")
            if not filename:
                filename = "komand-uploaded.file"
            self.logger.info(f"Filename: {filename}")
            try:
                fisle = io.BytesIO(base64.b64decode(data))
            except:
                self.logger.error("Invalid file bytes input")
                raise PluginException(
                    cause="Invalid file bytes input", assistance="Please enter a valid file bytes input"
                )

            try:
                _type = magic.Magic(mime=True).from_buffer(fisle.read(1024))
                self.logger.info(f"MIME Content Type: {_type}")
            except Exception:
                self.logger.info(f"Unable to determine MIME Content Type of file, using {_type}")
                _type = "application/octet-stream"

            # Reset file counter to beginning of file since read 1024 bytes for magic number above
            fisle.seek(0)

            _bytes = fisle.read()
            if len(_bytes) > 0:
                req["upfile"] = (filename, _bytes, _type)
            else:
                req["upfile"] = ("", "", _type)
        else:
            req["upfile"] = (None, "")

        try:
            response = requests.post(url, headers=headers, files=req) # nosec
            response.raise_for_status()
            out = base64.b64encode(response.content)
        except requests.exceptions.HTTPError as error:
            raise PluginException(cause="HTTP error occurred", assistance=f"Error: {str(error)}")
        except requests.exceptions.ConnectionError as error:
            raise PluginException(cause="A network problem occurred", assistance=f"Error: {str(error)}")
        except requests.exceptions.Timeout as error:
            raise PluginException(cause=PluginException.Preset.TIMEOUT, assistance=f"Error: {str(error)}")
        except requests.exceptions.TooManyRedirects as error:
            raise PluginException(cause="Too many redirects!", assistance=f"Error: {str(error)}")
        except Exception as error:
            raise PluginException(cause=PluginException.Preset.UNKNOWN, assistance=f"Error: {str(error)}")

        # Debugging
        # self.logger.info(r.request.headers)
        # self.logger.info(r.request.body)

        return {"response": out.decode()}

    def test(self):
        url = "https://submit.symantec.com/websubmit/bcs.cgi"

        try:
            response = requests.get(url) # nosec
            response.raise_for_status()
            out = base64.b64encode(response.content)
        except requests.exceptions.HTTPError as error:
            raise PluginException(cause="HTTP error occurred", assistance=f"Error: {str(error)}")
        except requests.exceptions.ConnectionError as error:
            raise PluginException(cause="A network problem occurred", assistance=f"Error: {str(error)}")
        except requests.exceptions.Timeout as error:
            raise PluginException(cause=PluginException.Preset.TIMEOUT, assistance=f"Error: {str(error)}")
        except requests.exceptions.TooManyRedirects as error:
            raise PluginException(cause="Too many redirects!", assistance=f"Error: {str(error)}")
        except Exception as error:
            raise PluginException(cause=PluginException.Preset.UNKNOWN, assistance=f"Error: {str(error)}")
        return {"response": out.decode()}
