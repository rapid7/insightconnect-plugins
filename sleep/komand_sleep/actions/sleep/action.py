import komand
import time
from .schema import SleepInput, SleepOutput


class Sleep(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='sleep',
                description='Suspend execution for an interval of time',
                input=SleepInput(),
                output=SleepOutput())

    def run(self, params={}):
        _time = params.get('interval')
        time.sleep(_time)
        return { 'slept': _time }

    def test(self):
        """TODO: Test action"""
        return {}
