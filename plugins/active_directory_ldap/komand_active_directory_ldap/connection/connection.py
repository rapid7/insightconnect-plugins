from ldap3.core.exceptions import LDAPExtensionError

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from .schema import ConnectionSchema, Input
from ..util.api import ActiveDirectoryLdapAPI


# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None
        self.use_ssl = None

    def connect(self, params={}):
        self.use_ssl = params.get(Input.USE_SSL)
        self.client = ActiveDirectoryLdapAPI(
            self.logger,
            use_ssl=self.use_ssl,
            host=params.get(Input.HOST),
            port=params.get(Input.PORT),
            referrals=params.get(Input.CHASE_REFERRALS),
            user_name=params.get(Input.USERNAME_PASSWORD).get("username"),
            password=params.get(Input.USERNAME_PASSWORD).get("password"),
            use_channel_binding=params.get(Input.USE_CHANNEL_BINDING),
        )

    def test(self):
        try:
            # pylint: disable=no-value-for-parameter
            self.client.who_am_i()
        except LDAPExtensionError as e:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED, data=e)

        return {"connection": "successful"}
