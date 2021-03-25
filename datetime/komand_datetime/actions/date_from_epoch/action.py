import insightconnect_plugin_runtime
from .schema import DateFromEpochInput, DateFromEpochOutput, Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
import maya
import re


class DateFromEpoch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="date_from_epoch",
            description="Convert an Epoch as a float to a Datetime",
            input=DateFromEpochInput(),
            output=DateFromEpochOutput(),
        )

    def run(self, params={}):
        epoch = params.get(Input.EPOCH)
        if re.search("([0-9]){21,}", epoch):
            raise PluginException(
                cause="The given epoch is out of range.",
                assistance="This action supports seconds, milliseconds, microseconds, and nanoseconds. Please check "
                "that the given epoch is correct.",
            )
        return {Output.DATE: maya.MayaDT(float(epoch) / self.seconds_division_number(epoch)).rfc3339()}

    @staticmethod
    def seconds_division_number(epoch: str) -> int:
        split_epoch = epoch.split(".")
        if len(split_epoch[0]) > 17:
            return 1000000000
        elif 15 <= len(split_epoch[0]) <= 17:
            return 1000000
        elif 12 <= len(split_epoch[0]) <= 14:
            return 1000
        else:
            return 1
