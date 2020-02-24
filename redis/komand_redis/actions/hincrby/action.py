import komand
from komand.exceptions import PluginException
from .schema import HincrbyInput, HincrbyOutput, Input, Output, Component


class Hincrby(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='hincrby',
            description=Component.DESCRIPTION,
            input=HincrbyInput(),
            output=HincrbyOutput())

    def run(self, params={}):
        key = params.get(Input.KEY)
        field = params.get(Input.FIELD)
        value = params.get(Input.VALUE)
        try:
            result = self.connection.redis.hincrby(key, field, value)
        except Exception as e:
            self.logger.error("An error occurred while running HINCRBY: ", e)
            raise PluginException(cause='Server error',
                                  assistance="An error occurred while running HINCRBY",
                                  data=e)

        return {
            Output.RESULT: result
        }
