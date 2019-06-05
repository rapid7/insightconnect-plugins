import komand
from .schema import TimeElapsedInput, TimeElapsedOutput
import maya


class TimeElapsed(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='time_elapsed',
                description='Determine the elapsed time between two dates',
                input=TimeElapsedInput(),
                output=TimeElapsedOutput())

    def run(self, params={}):
        time1 = maya.MayaDT.from_rfc3339(params.get("first_time"))
        time2 = maya.MayaDT.from_rfc3339(params.get("second_time"))
        unit = params.get("result_unit")
        diff = int(maya.MayaInterval(start=time1, end=time2).timedelta.total_seconds())
        if unit == "Minutes":
            diff = int(round(diff / 60))
        elif unit == "Hours":
            diff = int(round(diff / 3600))
        elif unit == "Days":
            diff = int(round(diff / 86400))
        elif unit == "Months":
            diff = int(round(diff / 2628000))
        elif unit == "Years":
            diff = int(round(diff / 31540000))
        else:
            diff = diff
        return {"difference": diff, "time_unit": unit}
