import insightconnect_plugin_runtime
from .schema import BlacklistByIocHashInput, BlacklistByIocHashOutput, Input, Output
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class BlacklistByIocHash(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='blacklist_by_ioc_hash',
                description='Add hashed indicator of compromise to global blacklist',
                input=BlacklistByIocHashInput(),
                output=BlacklistByIocHashOutput())

    def run(self, params={}):
        # ioc_hash = params.get(Input.HASH)
        # agent_id = params.get(Input.AGENT_ID)
        # result = self.connection.blacklist_by_ioc_hash(ioc_hash, agent_id)
        #
        # result_data = result.get('data')
        # new_result = {
        #     'blacklist_data': result_data
        # }
        # return {Output.RESULT: new_result}

        raise PluginException(
            cause="This action is obsolete. The endpoint in the SentinelOne API is no longer supported.",
            assistance="Please use a different Blacklist action."
        )
