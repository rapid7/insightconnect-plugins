import komand
from .schema import HmgetInput, HmgetOutput, Input, Output, Component
from komand.exceptions import PluginException


class Hmget(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='hmget',
                description=Component.DESCRIPTION,
                input=HmgetInput(),
                output=HmgetOutput())

    def run(self, params={}):
        key = params[Input.KEY]
        fields = params[Input.FIELDS]
        get_all = params[Input.GET_ALL]

        try:
            if get_all:
                result = self.connection.redis.hgetall(key)
            else:
                result = self.connection.redis.hmget(key, fields)
        except Exception as e:
            self.logger.error("An error occurred while running HMSET: ", e)
            raise PluginException(cause='Server error',
                                  assistance="An error occurred while running HMSET",
                                  data=e)

        if result:
            v = {}
            for key, val in result.items():
                v[key.decode('utf-8')] = val.decode('utf-8')
            result = v

        return {
            Output.VALUES: result
        }
