import komand
import xmltodict

# Custom imports below
from komand.exceptions import PluginException

from .schema import SubmitUrlInput, SubmitUrlOutput, Output, Input


class SubmitUrl(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_url",
            description="Submit a URL for analysis",
            input=SubmitUrlInput(),
            output=SubmitUrlOutput(),
        )

    def run(self, params={}):
        # Formatted with None and tuples so requests sends form-data properly
        # => Send data, 299 bytes (0x12b)
        # 0000: --------------------------8557684369749613
        # 002c: Content-Disposition: form-data; name="apikey"
        # 005b:
        # 005d: 740219c8fab2606b9206b2d40626b2d1
        # 007f: --------------------------8557684369749613
        # 00ab: Content-Disposition: form-data; name="format"
        # 00d8:
        # 00da: pdf
        # 00fd: --------------------------8557684369749613--
        # ...
        try:
            o = xmltodict.parse(self.connection.client.submit_url(params.get(Input.URL)))
            out = dict(o)

            # {
            #   "submission": {
            #     "error": {
            #       "error-message": "'Invalid webpage type url, url should start with http or https'"
            #     }
            #   }
            # }
            if "submission" in out:
                if "error" in out["submission"]:
                    if "error-message" in out["submission"]["error"]:
                        error = out["submission"]["error"]["error-message"]
                        raise PluginException(
                            cause="Received an error response from Wildfire.",
                            assistance=f"{error}.",
                        )

            # A different response occurs sometimes
            # {'error': OrderedDict([('error-message', "'Invalid webpage type url, url should start with http or https'")])}
            if "error" in out:
                if "error-message" in out["error"]:
                    error = out["error"]["error-message"]
                    raise PluginException(cause="Received an error response from Wildfire.", assistance=f"{error}.")
                else:
                    self.logger.info(out)
                    raise PluginException(
                        cause="Received an error response from Wildfire.",
                        assistance="Check the log output for more details.",
                    )

            out = dict(o["wildfire"]["submit-link-info"])
        except Exception as error:
            raise PluginException(
                cause="Some unexpected error appear.",
                assistance="Please contact support with the status code and error information.",
                data=error,
            )

        return {Output.SUBMISSION: out}
