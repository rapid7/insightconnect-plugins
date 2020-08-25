import insightconnect_plugin_runtime
from .schema import ToLocaltimeInput, ToLocaltimeOutput, Input, Output, Component
# Custom imports below
import maya
from maya.core import parse


class ToLocaltime(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='to_localtime',
            description=Component.DESCRIPTION,
            input=ToLocaltimeInput(),
            output=ToLocaltimeOutput())

    def run(self, params={}):
        new_date = parse(params.get(Input.BASE_TIME), timezone='UTC')

        return {
            Output.CONVERTED_DATE: maya.MayaDT.from_datetime(
                new_date.datetime(to_timezone=params.get(Input.TIMEZONE), naive=True)
            ).rfc3339()
        }
