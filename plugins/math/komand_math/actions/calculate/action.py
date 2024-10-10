from typing import Union

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from simpleeval import simple_eval

from .schema import CalculateInput, CalculateOutput, Component, Input, Output


class Calculate(insightconnect_plugin_runtime.Action):
    _result = None

    def __init__(self):
        super(self.__class__, self).__init__(
            name="calculate",
            description=Component.DESCRIPTION,
            input=CalculateInput(),
            output=CalculateOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        equation = params.get(Input.EQUATION, "")
        # END INPUT BINDING - DO NOT REMOVE

        try:
            result = Calculate.execute_equation(equation)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        if result is None:
            raise PluginException(
                cause="Calculation error",
                assistance="Error occurred while calculating the equation. Check to make sure it is valid and try "
                "again.",
            )
        return {Output.RESULT: result}

    @staticmethod
    def execute_equation(equation) -> Union[int, float]:
        equation = str().join(
            [
                character
                for character in equation
                if (character.isdecimal() or character in ["+", "-", "*", "/", "**", "%", "(", ")", "."])
            ]
        )
        return simple_eval(equation)
