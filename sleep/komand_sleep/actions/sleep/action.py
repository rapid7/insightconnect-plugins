import komand
import time
from .schema import SleepInput, SleepOutput, Input, Output, Component
from komand.exceptions import PluginException


class Sleep(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='sleep',
            description=Component.DESCRIPTION,
            input=SleepInput(),
            output=SleepOutput())

    def run(self, params={}):
        time_ = params.get(Input.INTERVAL)
        if int(time_) < 0:
            raise PluginException(cause='Wrong input',
                                  assistance=f"{Input.INTERVAL.capitalize()} should not be less than zero")
        time.sleep(time_)
        return {Output.SLEPT: time_}
