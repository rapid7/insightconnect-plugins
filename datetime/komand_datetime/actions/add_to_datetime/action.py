import komand
from .schema import AddToDatetimeInput, AddToDatetimeOutput
import maya


class AddToDatetime(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_to_datetime',
                description='Add datetime units to a datetime',
                input=AddToDatetimeInput(),
                output=AddToDatetimeOutput())

    def run(self, params={}):
        base_time = params["base_time"]

        new_date = maya.MayaDT.from_rfc3339(base_time)
        new_date = new_date.add(years=params["years"],
                                months=params["months"],
                                days=params["days"],
                                hours=params["hours"],
                                minutes=params["minutes"],
                                seconds=params["seconds"])

        new_date_rfc3339 = new_date.rfc3339()

        return {"date": new_date_rfc3339}
