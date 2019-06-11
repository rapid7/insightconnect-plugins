from komand.action import Action


class LogHelper(Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='loghelper',
            description='Log Helper',
            input=None,
            output=None)

    def run(self, params={}):
        pass

    def test(self, params={}):
        pass