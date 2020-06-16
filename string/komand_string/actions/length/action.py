import komand
from .schema import LengthInput, LengthOutput, Input, Output, Component
# Custom imports below


class Length(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='length',
                description=Component.DESCRIPTION,
                input=LengthInput(),
                output=LengthOutput())

    def run(self, params={}):
        _str = params.get('string')
        length = len(_str)
        return { "length": length}
