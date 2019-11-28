import komand
from .schema import SplitInput, SplitOutput, Component, Input, Output
# Custom imports below
import re
from icon_advanced_regex.util import shared


class Split(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='split',
                description=Component.DESCRIPTION,
                input=SplitInput(),
                output=SplitOutput())

    def run(self, params={}):
        flags = shared.constructFlags(params)
        regex = params.get(Input.IN_REGEX)
        split = re.split(regex, params.get(Input.IN_STRING), maxsplit=params.get(Input.MAX_SPLIT), flags=flags)

        return {Output.RESULT: split}
