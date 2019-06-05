import komand
from .schema import CalculateInput, CalculateOutput
# Custom imports below
import json


class Calculate(komand.Action):

    _result = None

    def __init__(self):
        super(self.__class__, self).__init__(
                name='calculate',
                description='Run a calculation',
                input=CalculateInput(),
                output=CalculateOutput())

    def run(self, params={}):
        equation = params.get("equation")
        Calculate.execute_equation(equation)

        if self._result is None:
            raise Exception("Error occurred while calculating the equation. Check to make sure it is valid and try again.")

        return {"result": self._result}

    @staticmethod
    def execute_equation(eq):
        eq = str().join([c for c in eq if (c.isdecimal() or c in ["+", "-", "*", "/", "**", "%", "(", ")", "."])])
        eq_source = "Calculate._result = float({equation})".format(equation=eq)
        eq_compiled = compile(source=eq_source, filename="none", mode="exec")

        eval(eq_compiled)

    def test(self):
        return {"result": 0}
