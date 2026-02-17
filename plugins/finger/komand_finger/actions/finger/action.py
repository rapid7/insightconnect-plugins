import re

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import FingerInput, FingerOutput, Input, Output, Component

# Custom imports below
DEFAULT_ENCODING = "utf-8"


class Finger(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="finger", description=Component.DESCRIPTION, input=FingerInput(), output=FingerOutput()
        )

    def found(self, stdout, stderr, errors):
        """Check for errors in output"""
        for msg in errors:
            self.logger.info(msg)
            if msg in stderr:
                return False, msg
            if msg in stdout:
                return False, msg
        return True, "Success"

    # Validate input to prevent injection. Only allow alphanumeric characters, dots, dashes, and underscores
    def validate_input(self, input_string: str):
        return re.match(r"^[\w\.\-]+$", input_string) is not None

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        host = params.get(Input.HOST, "")
        user = params.get(Input.USER, "")
        # END INPUT BINDING - DO NOT REMOVE

        if not self.validate_input(user) or not self.validate_input(host):
            raise PluginException(
                cause=PluginException.Preset.BAD_REQUEST,
                assistance="Only alphanumeric characters, dots, dashes, and underscores are allowed in user and host values.",
            )

        try:
            output = {}
            # GNU Finger's error messages from binary: $ strings /bin/finger
            errors = [
                "Finger online user list request denied",
                "Finger online user list denied",
                "Finger server disable",
                "Sorry, we do not support empty finger queries",
                "User not found",
                "finger: unknown host: ",
                "finger: connect: Connection timed out",
                "finger: fdopen: ",
                "finger: tcp/finger: unknown service",
                "finger: Out of space.",
                "finger: out of space.",
                "finger: socket: ",
                "usage: finger [-",
                f"finger: {user}: no such user",
                "In real life: ???",
                "finger: connect: Connection refused",
            ]
            binary = "/usr/bin/finger"

            cmd = f"{binary} -l -m {user}@{host}"
            result = insightconnect_plugin_runtime.helper.exec_command(cmd)

            keys = [
                "Shell",
                "Home phone",
                "Work phone",
                "Room",
                "Project",
                "PGP key",
            ]

            # Did finger succeed in finding a user?
            stdout = result.get("stdout", "").decode(DEFAULT_ENCODING)
            output["Found"], output["Plugin Status"] = self.found(
                stdout, result.get("stderr", "").decode(DEFAULT_ENCODING), errors
            )

            for key in keys:
                # Put value in dictionary with index as key.
                output[key] = insightconnect_plugin_runtime.helper.extract_value(r"\s", key, r":\s(.*)\s", stdout)

            # Try to manually match everything that didn't before
            # Grab Login status/Never logged in
            if "\nNever logged in.\n" in stdout:
                output["Login Status"] = "Never logged in"
                output["Login From"] = "Never logged in"
            else:
                output["Login Status"] = insightconnect_plugin_runtime.helper.extract_value(
                    r"\n", "On since", r"\s(.*)\n", stdout
                )
                output["Login From"] = insightconnect_plugin_runtime.helper.extract_value(
                    r"\n", "On since", r"\s.* from (\S+)\n", stdout
                )

            # Grab Last mail read/No mail.
            mail = ["No mail.", "No unread mail"]
            for msg in mail:
                if "\n" + msg + "\n" in stdout:
                    output["Mail Status"] = msg.rstrip(".")
                    break
                output["Mail Status"] = insightconnect_plugin_runtime.helper.extract_value(
                    r"\n", "Mail last read", r"\s(.*)\n", stdout
                )

            # Grab login name
            output["Login"] = insightconnect_plugin_runtime.helper.extract_value(
                r"\n", "(?:Login|Login name)", r": (\S+)\s", stdout
            )
            # Grab full name
            output["Name"] = insightconnect_plugin_runtime.helper.extract_value(
                r"\s", "(?:Name|In real life)", r":\s(.*)\s", stdout
            )
            # Grab home dself.irectory
            output["Directory"] = insightconnect_plugin_runtime.helper.extract_value(
                "\n", "Directory", r":\s(\S+)\s+", stdout
            )
            # Grab forward maself.il address
            output["Mail forwarded to"] = insightconnect_plugin_runtime.helper.extract_value(
                r"\n", "Mail forwarded to", r"\s(\S+)\n", stdout
            )
            # Grab plan
            if "\nNo Plan.\n" in stdout:
                output["Plan"] = "No plan"
            else:
                output["Plan"] = insightconnect_plugin_runtime.helper.extract_value(r"\n", "Plan", r":\n(.*)", stdout)

            output = {
                Output.FOUND: output.get("Found"),
                Output.LOGIN: output.get("Login"),
                Output.LOGINSTATUS: output.get("Login Status"),
                Output.LOGINFROM: output.get("Login From"),
                Output.HOME: output.get("Directory"),
                Output.FULLNAME: output.get("Name"),
                Output.SHELL: output.get("Shell"),
                Output.MAIL: output.get("Mail forwarded to"),
                Output.MAILSTATUS: output.get("Mail Status"),
                Output.PLAN: output.get("Plan"),
                Output.PROJECT: output.get("Project"),
                Output.PUBKEY: output.get("PGP key"),
                Output.WORKPHONE: output.get("Work phone"),
                Output.HOMEPHONE: output.get("Home phone"),
                Output.ROOM: output.get("Room"),
                Output.STATUS: output.get("Plugin Status"),
            }
            return insightconnect_plugin_runtime.helper.clean_dict(output)
        except Exception as exception:
            raise PluginException(
                cause=PluginException.Preset.UNKNOWN,
                assistance="An unexpected error occurred while running the finger command.",
                data=exception,
            )
