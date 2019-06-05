import komand
from .schema import GetDatetimeInput, GetDatetimeOutput
import time
import maya


class GetDatetime(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_datetime',
                description='Gets the current datetime in a specified format',
                input=GetDatetimeInput(),
                output=GetDatetimeOutput())

    def run(self, params={}):
        format_string = params.get("format_string")
        use_rfc3339_format = params.get("use_rfc3339_format")

        if not use_rfc3339_format:
            current_time = time.strftime(format_string)
        else:
            current_time = maya.now().rfc3339()

        epoch_timestamp = maya.now().epoch

        return {"datetime": current_time, "epoch_timestamp": epoch_timestamp}
