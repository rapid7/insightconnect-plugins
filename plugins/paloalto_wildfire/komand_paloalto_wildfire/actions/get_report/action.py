# Custom imports below
import base64

import insightconnect_plugin_runtime

from .schema import GetReportInput, GetReportOutput, Output, Input, Component


class GetReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_report",
            description=Component.DESCRIPTION,
            input=GetReportInput(),
            output=GetReportOutput(),
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
        return {
            Output.REPORT: base64.b64encode(
                self.connection.client.get_report(params.get(Input.HASH), params.get(Input.FORMAT))
            ).decode()
        }
