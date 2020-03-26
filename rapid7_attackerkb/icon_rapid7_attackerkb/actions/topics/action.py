import komand
from .schema import TopicsInput, TopicsOutput, Component, Output


class Topics(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='topics',
            description=Component.DESCRIPTION,
            input=TopicsInput(),
            output=TopicsOutput())

    def run(self, params={}):
        return {
            Output.DATA: self.connection.attackerKB_api.call_api_pages(f"topics", params=params)
        }
