from komand_redis.util.helper import Helper

import komand
from komand.exceptions import PluginException
from .schema import HmsetInput, HmsetOutput, Input, Output, Component


class Hmset(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='hmset',
            description=Component.DESCRIPTION,
            input=HmsetInput(),
            output=HmsetOutput())

    def run(self, params={}):
        key = params[Input.KEY]
        values = params[Input.VALUES]
        try:
            result = self.connection.redis.hmset(key, values)
        except Exception as e:
            self.logger.error("An error occurred while running HMSET: ", e)
            raise PluginException(cause='Server error',
                                  assistance="An error occurred while running HMSET",
                                  data=e)

        Helper.set_expire(self.logger, self.connection, params.get(Input.KEY), params.get(Input.EXPIRE))

        return {
            Output.REPLY: result
        }
