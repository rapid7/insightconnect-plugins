from komand_redis.util.helper import Helper

import komand
from .schema import HashSetInput, HashSetOutput, Input, Output, Component


class HashSet(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='hash_set',
            description=Component.DESCRIPTION,
            input=HashSetInput(),
            output=HashSetOutput())

    def run(self, params={}):
        reply = 'OK'
        if not self.connection.redis.hmset(params[Input.KEY], params.get(Input.VALUES, {})):
            reply = 'Failed'

        Helper.set_expire(self.logger, self.connection, params.get(Input.KEY), params.get(Input.EXPIRE))

        return {
            Output.REPLY: reply
        }
