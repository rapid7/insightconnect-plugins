import insightconnect_plugin_runtime
from .schema import ToUtcInput, ToUtcOutput, Input, Output, Component
# Custom imports below
from maya.core import parse
import maya


class ToUtc(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='to_utc',
                description=Component.DESCRIPTION,
                input=ToUtcInput(),
                output=ToUtcOutput())

    def run(self, params={}):
        new_date = parse(params.get(Input.BASE_TIME), timezone=params.get(Input.TIMEZONE))

        return {
            Output.CONVERTED_DATE: maya.MayaDT.from_datetime(new_date.datetime()).rfc3339()
        }
