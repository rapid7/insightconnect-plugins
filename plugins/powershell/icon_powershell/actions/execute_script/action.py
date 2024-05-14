import base64

import insightconnect_plugin_runtime

from .schema import Component, ExecuteScriptInput, ExecuteScriptOutput, Input
from icon_powershell.util import util
from insightconnect_plugin_runtime.exceptions import PluginException


class ExecuteScript(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="execute_script",
            description=Component.DESCRIPTION,
            input=ExecuteScriptInput(),
            output=ExecuteScriptOutput(),
        )

    def run(self, params={}):  # noqa: MC0001
        host_ip = params.get(Input.ADDRESS)
        encoded_powershell_script = params.get(Input.SCRIPT)
        host_name = params.get(Input.HOST_NAME)

        powershell_script = self.decode_b64_script(encoded_powershell_script)
        powershell_script = util.add_credentials_to_script(powershell_script, self.connection.script_credentials)

        return util.run_powershell_script(
            auth=self.connection.auth_type,
            action=self,
            host_ip=host_ip,
            kdc=self.connection.kdc,
            domain=self.connection.domain,
            host_name=host_name,
            powershell_script=powershell_script,
            password=self.connection.password,
            username=self.connection.username,
            port=self.connection.port,
        )

    def decode_b64_script(self, encoded_powershell_script):
        try:
            powershell_script = base64.b64decode(encoded_powershell_script)
        except base64.binascii.Error as e:
            self.logger.error("Base64 input" + encoded_powershell_script)
            raise PluginException(cause="While decoding the base64 into bytes the following error occurred", data=e)
        except Exception as e:
            self.logger.error("Base64 input " + encoded_powershell_script)
            raise PluginException(
                cause="Something went wrong decoding the base64 script into bytes",
                assistance="See log for more information",
                data=e,
            )
        try:
            powershell_script = powershell_script.decode("utf-8")
        except UnicodeDecodeError:
            try:
                powershell_script = powershell_script.decode("ISO-8859-1")
            except (UnicodeDecodeError, base64.binascii.Error) as exception:
                # Log the base64 input and decoded bytes
                self.logger.error("Base64 input: " + encoded_powershell_script)
                self.logger.error("Base64 decoded as bytes: " + powershell_script)

                # Raise a PluginException with the error information
                raise PluginException(
                    cause="While decoding the bytes into UTF-8 or ISO-8859-1 the following error occurred",
                    data=exception,
                )
            except Exception as exception:
                self.logger.error("Base64 input " + encoded_powershell_script)
                self.logger.error("Base64 decoded as bytes" + powershell_script)
                raise PluginException(
                    cause="Something went wrong decoding the base64 script bytes into utf-8.",
                    assistance="See log for more information",
                    data=exception,
                )
        except Exception as exception:
            self.logger.error("Base64 input " + encoded_powershell_script)
            self.logger.error("Base64 decoded as bytes" + powershell_script)
            raise PluginException(
                cause="Something went wrong decoding the base64 script bytes into utf-8.",
                assistance="See log for more information",
                data=exception,
            )
        return powershell_script

    @staticmethod
    def safe_encode(in_byte):
        new_string = str(in_byte)
        return str(new_string.encode("ascii", "ignore"), "utf-8")
