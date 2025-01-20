from urllib.parse import urlencode

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

from .schema import AuthInput, AuthOutput, Component, Input, Output


class Auth(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="auth",
            description=Component.DESCRIPTION,
            input=AuthInput(),
            output=AuthOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        user_id = params.get(Input.USER_ID, "") or None
        username = params.get(Input.USERNAME, "") or None
        device = params.get(Input.DEVICE, "") or None
        factor = params.get(Input.FACTOR, "")
        ip_address = params.get(Input.IPADDR, "")
        async_ = params.get(Input.ASYNC, False)
        opts = params.get(Input.OPTIONS, {}) or {}
        # END INPUT BINDING - DO NOT REMOVE

        if (username and user_id) or (not username and not user_id):
            raise PluginException(cause="Wrong input", assistance="Only user_id or username should be used. Not both.")

        if push_info := opts.get("pushinfo"):
            push_info = urlencode(push_info)

        try:
            response = self.connection.auth_api.auth(
                factor=factor,
                username=username,
                user_id=user_id,
                ipaddr=ip_address,
                async_txn=async_,
                display_username=username,
                pushinfo=push_info,
                device=device,
                type=opts.get("type"),
                passcode=opts.get("passcode"),
            )
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        return clean(
            {
                Output.RESULT: response.get(Output.RESULT),
                Output.STATUS: response.get(Output.STATUS),
                Output.STATUS_MSG: response.get(Output.STATUS_MSG),
                Output.TRUSTED_DEVICE_TOKEN: response.get(Output.TRUSTED_DEVICE_TOKEN),
                Output.TXID: response.get(Output.TXID),
            }
        )
