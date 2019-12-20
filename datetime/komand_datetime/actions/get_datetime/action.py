import komand
from .schema import GetDatetimeInput, GetDatetimeOutput, Input, Output
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
        format_string = params.get(Input.FORMAT_STRING)
        use_rfc3339_format = params.get(Input.USE_RFC3339_FORMAT)

        if not use_rfc3339_format:
            current_time = time.strftime(format_string)
        else:
            current_time = maya.now().rfc3339()

        epoch_timestamp = maya.now().epoch

        return {Output.DATETIME: current_time, Output.EPOCH_TIMESTAMP: epoch_timestamp}
