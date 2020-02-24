from komand_redis.util.helper import Helper

import komand
from .schema import ListPushInput, ListPushOutput, Input, Output, Component


class ListPush(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='list_push',
            description=Component.DESCRIPTION,
            input=ListPushInput(),
            output=ListPushOutput())

    def run(self, params={}):
        reply = 'OK'
        if not self.connection.redis.rpush(params[Input.KEY], params[Input.VALUE]):
            reply = 'Failed'

        Helper.set_expire(self.logger, self.connection, params.get(Input.KEY), params.get(Input.EXPIRE))

        return {
            Output.REPLY: reply
        }
