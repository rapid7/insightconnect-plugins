import insightconnect_plugin_runtime
from .schema import ReplaceInput, ReplaceOutput, Component, Input, Output
# Custom imports below
import re
from icon_advanced_regex.util import shared


class Replace(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='replace',
                description=Component.DESCRIPTION,
                input=ReplaceInput(),
                output=ReplaceOutput())

    def run(self, params={}):
        flags = shared.constructFlags(params)
        regex = params.get(Input.IN_REGEX)
        new = params.get(Input.REPLACE_STRING, '')
        replace_num = params.get(Input.MAX_REPLACE)
        replaced = re.sub(regex, new, params.get(Input.IN_STRING), count=replace_num, flags=flags)
        return {Output.RESULT: replaced}
