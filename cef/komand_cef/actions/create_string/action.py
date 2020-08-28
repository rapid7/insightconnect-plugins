import komand

from komand_cef.util import utils
from .schema import CreateStringInput, CreateStringOutput, Input, Output, Component


class CreateString(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_string',
            description=Component.DESCRIPTION,
            input=CreateStringInput(),
            output=CreateStringOutput())

    def run(self, params={}):
        return {
            Output.CEF_STRING: utils.obj_to_cef(params.get(Input.CEF))
        }
