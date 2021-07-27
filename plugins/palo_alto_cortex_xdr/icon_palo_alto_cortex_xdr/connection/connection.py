import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from ..util.api import CortexXdrAPI
from datetime import datetime, timezone
import secrets
import string
import hashlib
import requests


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.xdr_api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")

        api_key = params.get(Input.API_KEY).get("secretKey")
        api_key_id = params.get(Input.API_KEY_ID)
        fqdn = params.get(Input.URL)
        fqdn = self.clean_up_fqdn(fqdn)

        security_level = params.get(Input.SECURITY_LEVEL)

        self.xdr_api = CortexXdrAPI(api_key_id, api_key, fqdn, security_level, self.logger)

    def clean_up_fqdn(self, fqdn):
        # Add trailing slash if needed
        if not fqdn.endswith("/"):
            fqdn = fqdn + "/"

        if not fqdn.startswith("http://") and not fqdn.startswith("https://"):
            fqdn = f"https://{fqdn}"

        return fqdn

    def test(self):
        self.xdr_api.test_connection()
        return {"status": "pass"}
