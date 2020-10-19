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
            try:
                # If IPv4, attempt to find its ID
                ip_agent = None
                if validators.ipv4(agent):
                    ip_agent = find_agent_by_ip(self.connection, agent)
                if ip_agent:
                    device_obj = self.connection.client.get_agent_details(ip_agent)
                else:
                    device_obj = self.connection.client.get_agent_details(agent)

                # Device was found in Cylance
                if device_obj:
                    if whitelist:
                        # Any whitelisted devices will not be deleted
                        matches = find_in_whitelist(device_obj, whitelist)
                        if matches:
                            self.connection.logger.info(f"{agent} found in whitelist. Will not delete.")
                            invalid_devices.append(agent)
                        else:
                            valid_devices.append(agent)
                            valid_ids = self.add_to_valid_devices(device_obj, valid_ids)
                    else:
                        valid_devices.append(agent)
                        valid_ids = self.add_to_valid_devices(device_obj, valid_ids)
                # Device was not found, therefore invalid to delete
                else:
                    self.connection.logger.info(f"{agent} device was not found.")
                    invalid_devices.append(agent)
            except PluginException:
                invalid_devices.append(agent)

        if not valid_ids:
            raise PluginException(
                cause="No valid devices to delete.",
                assistance=f"Be sure that the devices exist in Cylance and are not part of the whitelist."
            )

        payload = {"device_ids": valid_ids}
        success = self.connection.client.delete_devices(payload)
        if not success:
            raise PluginException(
                cause="One of the devices failed to delete.",
                assistance=f"A valid agent deletion may have failed, check your Cylance console."
            )

        return {Output.SUCCESS: True, Output.DELETED: valid_devices, Output.NOT_DELETED: invalid_devices}

    @staticmethod
    def add_to_valid_devices(device_obj, valid_ids):
        device_id = device_obj.get('id')
        device_id.replace('-', '').upper()
        valid_ids.append(device_id)
        return valid_ids


