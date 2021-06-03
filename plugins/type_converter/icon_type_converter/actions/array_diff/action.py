import insightconnect_plugin_runtime
from .schema import ArrayDiffInput, ArrayDiffOutput, Input, Output, Component

# Custom imports below


class ArrayDiff(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="array_diff", description=Component.DESCRIPTION, input=ArrayDiffInput(), output=ArrayDiffOutput()
        )

    def run(self, params={}):
        return {Output.DIFFERENCE_ARRAY: list(set(params.get(Input.ARRAY1)).difference(params.get(Input.ARRAY2)))}
