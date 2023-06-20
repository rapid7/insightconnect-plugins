import insightconnect_plugin_runtime
from .schema import RandomIntegerRangeInput, RandomIntegerRangeOutput, Input, Output, Component
# Custom imports below
import random

class RandomIntegerRange(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="random_integer_range",
                description=Component.DESCRIPTION,
                input=RandomIntegerRangeInput(),
                output=RandomIntegerRangeOutput())

    def run(self, params={}):

        start_range = params.get(Input.START_RANGE)
        stop_range = params.get(Input.STOP_RANGE)
        result = random.randrange(start_range, stop_range)
        return {Output.RESULT: result}
