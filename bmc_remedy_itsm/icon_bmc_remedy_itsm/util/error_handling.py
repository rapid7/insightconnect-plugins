from komand.exceptions import PluginException
from requests.models import Response
import json


class ErrorHelper(object):
    """
    This class finds and raises errors in the returns for the BMC API
    """

    _ERROR_CODES = {
        400: "400, Bad Request",
        401: "401, Unauthorized",
        403: "403, Forbidden",
        404: "404, Not Found",
        500: "500, Internal Server Error",
        503: "503, Service Unavailable",
        000: "Unknown Status Code"
    }

    _ERROR_ASSISTANCE = {400: "This code is used if the request body is not correct. This can be caused by invalid inputs.",
                         401: "This code is used if the user is not authenticated.",
                         403: "This code is used when the call is authenticated, but the user does not have access to the resource.",
                         404: "This code is used when a resource does not exist.",
                         500: "This code is the default response for any error that occurs when an API call is being processed.",
                         503: "This code is used when the server can not be found",
                         000: "Contact support for help"}

    def error_handling(self, result: Response):
        """
        Checks for issues with a return from the BMC API
        :param result: A requests rest request result object
        """

        # Check for non 2xx status code
        if result.status_code not in range(200, 299):
            raw = result.text
            status_code_message = self._ERROR_CODES.get(result.status_code, self._ERROR_CODES[000])
            status_code_assistance = self._ERROR_ASSISTANCE.get(result.status_code, self._ERROR_ASSISTANCE[000])
            raise PluginException(cause=f"A {status_code_message} error code was returned",
                                  assistance=status_code_assistance,
                                  data=raw)

        # BMC error messages e.g. [{"messageType":"ERROR","messageText":"Entry ID parameter length is longer than the maximum allowed length.","messageAppendedText":"INC0000000000212","messageNumber":101}]
        try:
            message = result.json()
            if isinstance(message, list):
                if message[0].get('messageType') == "ERROR":
                    raise PluginException(cause="The BMC server returned an Error",
                                          assistance="Check the error message for additional data",
                                          data=message[0])
        except json.JSONDecodeError:
            pass
        except IndexError:
            pass

