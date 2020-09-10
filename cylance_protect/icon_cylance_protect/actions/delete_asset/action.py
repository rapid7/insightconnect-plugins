import insightconnect_plugin_runtime
from .schema import DeleteAssetInput, DeleteAssetOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below
from icon_cylance_protect.util.find_functions import find_in_whitelist, find_agent_by_ip
import validators


class DeleteAsset(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_asset',
            description=Component.DESCRIPTION,
            input=DeleteAssetInput(),
            output=DeleteAssetOutput())

    def run(self, params={}):
        whitelist = params.get(Input.WHITELIST, None)
        agents = params.get(Input.AGENT)

        for agent in agents:
            if validators.ipv4(agent):
                agent = find_agent_by_ip(agent)

            device_obj = self.connection.client.get_agent_details(agent)

            if whitelist:
                matches = find_in_whitelist(device_obj, whitelist)
                if matches:
                    raise PluginException(
                        cause="Agent found in the whitelist.",
                        assistance=f"If you would like to block this host, remove {str(matches)[1:-1]} from the whitelist."
                    )
            success = self.connection.client.delete_device(device_obj.get('id'))
            if not success:
                return {Output.OUTPUT: False}

        return {Output.OUTPUT: True}
