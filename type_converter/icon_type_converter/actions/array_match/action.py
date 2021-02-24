import insightconnect_plugin_runtime
from .schema import ArrayMatchInput, ArrayMatchOutput, Input, Output, Component


class ArrayMatch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="array_match", description=Component.DESCRIPTION, input=ArrayMatchInput(), output=ArrayMatchOutput()
        )

    def run(self, params={}):
        first_array = params.get(Input.ARRAY1)
        second_array = params.get(Input.ARRAY2)

        if params.get(Input.DEDUPLICATES, True):
            array_match = list(set(first_array) & set(second_array))
        else:
            array_match = self.intersection(first_array, second_array)

        return {Output.MATCHES_ARRAY: array_match, Output.COUNT: len(array_match)}

    @staticmethod
    def intersection(first_array: list, second_array: list) -> list:
        array_match = []
        for l1 in first_array:
            if l1 in second_array:
                array_match.append(l1)
                second_array.remove(l1)

        return array_match
