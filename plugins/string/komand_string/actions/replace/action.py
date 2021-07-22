import insightconnect_plugin_runtime
from .schema import ReplaceInput, ReplaceOutput, Input, Output, Component

# Custom imports below
import string


class Replace(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="replace", description=Component.DESCRIPTION, input=ReplaceInput(), output=ReplaceOutput()
        )

    def run(self, params={}):
        in_string = params.get(Input.IN_STRING)
        find_string = params.get(Input.STRING_PART_TO_FIND)
        replace_string = params.get(Input.REPLACEMENT_VALUE, "")

        self.logger.info(f"in_string: {in_string}")
        self.logger.info(f"find_string: {find_string}")
        self.logger.info(f"replace_string: {replace_string}")

        out_string = in_string.replace(find_string, replace_string)

        return {Output.RESULT_STRING: out_string}
