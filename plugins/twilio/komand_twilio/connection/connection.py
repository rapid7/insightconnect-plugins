import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from typing import Dict, Any
from .schema import ConnectionSchema, Input

# Custom imports below
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from twilio.http.http_client import TwilioHttpClient
from komand_twilio.util.utils import handle_exception_status_code


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.twilio_phone_number = None
        self.client = None

    def connect(self, params={}) -> None:
        self.logger.info("Connect: Connecting...")
        account_sid = params.get(Input.CREDENTIALS, {}).get("username").strip()
        auth_token = params.get(Input.CREDENTIALS, {}).get("password").strip()
        self.twilio_phone_number = params.get(Input.TWILIO_PHONE_NUMBER, "").strip()
        self.client = Client(account_sid, auth_token)

    def test(self) -> Dict[str, Any]:
        try:
            self.logger.info("Running TLS test over twilio...")
            TwilioHttpClient().request("GET", "https://tls-test.twilio.com")
            self.logger.info("TLS test passed.")
            self.client.messages.list(limit=1)
            return {"success": True}
        except TwilioRestException as error:
            handle_exception_status_code(error)
        except Exception as error:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNKNOWN, data=error)
