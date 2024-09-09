import insightconnect_plugin_runtime
from .schema import SplitToObjectInput, SplitToObjectOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Dict, Any


class SplitToObject(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="split_to_object",
            description="Converts a string to an object containing key:value strings",
            input=SplitToObjectInput(),
            output=SplitToObjectOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        input_string = params.get(Input.STRING)
        string_delimiter = params.get(Input.STRING_DELIMITER)
        block_delimiter = params.get(Input.BLOCK_DELIMITER)
        # END INPUT BINDING - DO NOT REMOVE

        if not input_string:
            raise PluginException(
                cause="Action failed! Missing required user input.",
                assistance="Please provide the input string.",
            )

        if not string_delimiter:
            self.logger.info("User did not supply a string delimiter. Defaulting to a space character.")
            string_delimiter = " "

        dict_ = {}
        if block_delimiter:
            # Split a block of text before applying user's string split delimiter
            try:
                for line in input_string.split(block_delimiter):
                    pair = line.split(string_delimiter)
                    length_pair = len(pair)
                    if length_pair == 2:
                        # Assign 1st element as key, 2nd as value to dict
                        dict_[pair[0].strip('"')] = pair[1].strip('"')
                    else:
                        self.logger.info(f"Skipping {length_pair} element split: {pair}")
                return {Output.OBJECT: dict_}
            except Exception as error:
                raise PluginException(
                    cause="Action failed! Unable to split string cleanly.",
                    assistance="Please try specifying the block delimiter for more multi-key:value input.",
                    data=error,
                )

        # Single key:value pair split e.g. USER=bob
        try:
            list_ = input_string.split(string_delimiter)
            self.logger.info(f"User input to split: {input_string} -> {list_}")
            dict_[list_[0]] = list_[1]
            return {Output.OBJECT: dict_}
        except Exception as error:
            self.logger.error("It looks like the input contained more than a single key:value split.")
            raise PluginException(
                cause="Action failed! Unable to split string cleanly.",
                assistance="Please try specifying the block delimiter for more multi-key:value input.",
                data=error,
            )
