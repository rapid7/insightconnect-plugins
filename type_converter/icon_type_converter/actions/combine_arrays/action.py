import insightconnect_plugin_runtime
from .schema import CombineArraysInput, CombineArraysOutput, Input, Output, Component
# Custom imports below


class CombineArrays(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='combine_arrays',
            description=Component.DESCRIPTION,
            input=CombineArraysInput(),
            output=CombineArraysOutput())

    def run(self, params={}):
        return {
            Output.COMBINED_ARRAY: list(set(params.get(Input.ARRAY1))
                                        .union(params.get(Input.ARRAY2))
                                        .union(params.get(Input.ARRAY3, set()))
                                        .union(params.get(Input.ARRAY4, set()))
                                        .union(params.get(Input.ARRAY5, set()))
                                        )
        }
