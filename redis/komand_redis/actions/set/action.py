import komand
from .schema import SetInput, SetOutput, Input, Output, Component
from komand_redis.util.helper import Helper


class Set(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='set',
            description=Component.DESCRIPTION,
            input=SetInput(),
            output=SetOutput())

    def run(self, params={}):
        reply = 'OK'
        expire = Helper.clear_expire(params.get(Input.EXPIRE))
        if not expire:
            result = self.connection.redis.set(params[Input.KEY], params[Input.VALUE])
        else:
            result = self.connection.redis.setex(params[Input.KEY], expire, params[Input.VALUE])

        if not result:
            reply = 'Failed'

        return {
            Output.REPLY: reply
        }
