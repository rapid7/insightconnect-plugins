import insightconnect_plugin_runtime
from .schema import RandomChoiceInput, RandomChoiceOutput, Input, Output, Component
# Custom imports below
import random

class RandomChoice(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="random_choice",
                description="Chooses a random item from a list",
                input=RandomChoiceInput(),
                output=RandomChoiceOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        user_input = params.get(Input.LIST)
        result = random.choice(user_input)
        return {Output.RESULT: result}
