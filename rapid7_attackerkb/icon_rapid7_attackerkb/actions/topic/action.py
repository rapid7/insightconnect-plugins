import komand
from .schema import TopicInput, TopicOutput, Input, Component
from komand.exceptions import PluginException


class Topic(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="topic",
            description=Component.DESCRIPTION,
            input=TopicInput(),
            output=TopicOutput())

    def run(self, params={}):
        if not params.get(Input.ID):
            raise PluginException(cause="Input error",
                                  assistance="ID can't be empty")

        return self.connection.attackerKB_api.call_api(f"topics/{params.get(Input.ID)}")
