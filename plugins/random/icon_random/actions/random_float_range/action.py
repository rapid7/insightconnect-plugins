import insightconnect_plugin_runtime
from .schema import RandomFloatRangeInput, RandomFloatRangeOutput, Input, Output, Component
# Custom imports below
import random


class RandomFloatRange(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="random_float_range",
                description=Component.DESCRIPTION,
                input=RandomFloatRangeInput(),
                output=RandomFloatRangeOutput())

    def run(self, params={}):
        start_range = params.get(Input.START_RANGE)
        stop_range = params.get(Input.STOP_RANGE)
        result = random.triangular(start_range, stop_range)
        return {Output.RESULT: result}
