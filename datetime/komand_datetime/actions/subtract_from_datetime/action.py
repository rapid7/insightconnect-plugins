import komand
from .schema import SubtractFromDatetimeInput, SubtractFromDatetimeOutput, Input, Output
import maya


class SubtractFromDatetime(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='subtract_from_datetime',
                description='Subtract datetime units from a datetime',
                input=SubtractFromDatetimeInput(),
                output=SubtractFromDatetimeOutput())

    def run(self, params={}):
        base_time = params.get(Input.BASE_TIME)

        new_date = maya.MayaDT.from_rfc3339(base_time)
        new_date = new_date.subtract(years=params.get(Input.YEARS),
                                     months=params.get(Input.MONTHS),
                                     days=params.get(Input.DAYS),
                                     hours=params.get(Input.HOURS),
                                     minutes=params.get(Input.MINUTES),
                                     seconds=params.get(Input.SECONDS))

        new_date_rfc3339 = new_date.rfc3339()

        return {Output.DATE: new_date_rfc3339}
