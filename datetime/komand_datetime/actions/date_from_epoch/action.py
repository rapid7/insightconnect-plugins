import komand
from .schema import DateFromEpochInput, DateFromEpochOutput, Input, Output
import maya


class DateFromEpoch(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='date_from_epoch',
                description='Convert an Epoch as a float to a Datetime',
                input=DateFromEpochInput(),
                output=DateFromEpochOutput())

    def run(self, params={}):
        new_datetime = maya.MayaDT(params.get(Input.EPOCH)).rfc3339()
        return {Output.DATE: new_datetime}
