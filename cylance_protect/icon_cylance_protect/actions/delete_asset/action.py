import insightconnect_plugin_runtime
from .schema import DeleteAssetInput, DeleteAssetOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below
from icon_cylance_protect.util.find_helpers import find_in_whitelist, find_agent_by_ip
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
        agents = params.get(Input.AGENTS)

        valid_ids = []
        valid_devices = []
        invalid_devices = []
        for agent in agents:
            if validators.ipv4(agent):
                agent = find_agent_by_ip(self.connection, agent)

            device_obj = self.connection.client.get_agent_details(agent)

            if device_obj:
                if whitelist:
                    matches = find_in_whitelist(device_obj, whitelist)
                    if matches:
                        invalid_devices.append(agent)
                    else:
                        valid_devices.append(agent)
                        valid_ids = self.add_to_valid_devices(device_obj, valid_ids)
                else:
                    valid_devices.append(agent)
                    valid_ids = self.add_to_valid_devices(device_obj, valid_ids)
            else:
                self.connection.logger.info("NOT FOUND %s" % agent)
                invalid_devices.append(agent)

        payload = {"device_ids": valid_ids}
        success = self.connection.client.delete_devices(payload)
        if not success:
            raise PluginException(
                cause="One of the devices failed to delete.",
                assistance=f"Example assistance"
            )
            return {Output.SUCCESS: False}

        return {Output.SUCCESS: True, Output.DELETED: valid_devices, Output.NOT_DELETED: invalid_devices}

    def add_to_valid_devices(self, device_obj, valid_ids):
        device_id = device_obj.get('id')
        device_id.replace('-', '').upper()
        valid_ids.append(device_id)
        return valid_ids


