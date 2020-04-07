import komand
from .schema import CalculateInput, CalculateOutput, Input, Output, Component
from komand.exceptions import PluginException
from simpleeval import simple_eval


class Calculate(komand.Action):
    _result = None

    def __init__(self):
        super(self.__class__, self).__init__(
            name='calculate',
            description=Component.DESCRIPTION,
            input=CalculateInput(),
            output=CalculateOutput())

    def run(self, params={}):
        equation = params.get(Input.EQUATION)
        result = Calculate.execute_equation(equation)

        if result is None:
            raise PluginException(
                cause='Calculation error',
                assistance="Error occurred while calculating the equation. Check to make sure it is valid and try "
                           "again. "
            )

        return {
            Output.RESULT: result
        }

    @staticmethod
    def execute_equation(eq):
        eq = str().join([c for c in eq if (c.isdecimal() or c in ["+", "-", "*", "/", "**", "%", "(", ")", "."])])
        return simple_eval(eq)
