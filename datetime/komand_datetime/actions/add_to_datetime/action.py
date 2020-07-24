import insightconnect_plugin_runtime
from .schema import AddToDatetimeInput, AddToDatetimeOutput, Input, Output
import maya


class AddToDatetime(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_to_datetime',
                description='Add datetime units to a datetime',
                input=AddToDatetimeInput(),
                output=AddToDatetimeOutput())

    def run(self, params={}):
        base_time = params.get(Input.BASE_TIME)

        new_date = maya.MayaDT.from_rfc3339(base_time)
        new_date = new_date.add(years=params.get(Input.YEARS),
                                months=params.get(Input.MONTHS),
                                days=params.get(Input.DAYS),
                                hours=params.get(Input.HOURS),
                                minutes=params.get(Input.MINUTES),
                                seconds=params.get(Input.SECONDS))

        new_date_rfc3339 = new_date.rfc3339()

        return {Output.DATE: new_date_rfc3339}
