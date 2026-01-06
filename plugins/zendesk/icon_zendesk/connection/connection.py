import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
import zenpy


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        creds = {}
        missing_fields = []

        for input_key in [Input.EMAIL, Input.SUBDOMAIN, Input.TOKEN]:
            value = params.get(input_key, "")

            if input_key == Input.TOKEN:
                value = value.get("secretKey") if isinstance(value, dict) else ""

            if not value:
                missing_fields.append(input_key)
            else:
                creds[input_key] = value.strip()

        if missing_fields:
            fields_str = ", ".join(missing_fields)
            assistance_message = f"Please provide the following required field(s): {fields_str}."
            raise PluginException(cause="Could not authenticate to Zendesk.", assistance=assistance_message)

        self.client = zenpy.Zenpy(**creds)
        self.logger.info("Connect: Connecting...")

    def test(self):
        try:
            self.client.users()
            return {"success": True}
        except zenpy.lib.exception.APIException as error:
            self.logger.debug(error)
            raise ConnectionTestException(
                cause="Zendesk API connection test failed.",
                assistance="Make sure your credentials are correct.",
                data=error,
            )
        except Exception as error:
            self.logger.debug(error)
            raise ConnectionTestException(
                cause="An unexpected error occurred.",
                assistance="Please ensure that you have entered your details correctly and that your internet connection is active.",
                data=error,
            )
