import shlex

import insightconnect_plugin_runtime

from .schema import ReplaceInput, ReplaceOutput
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_tr.util.utils import exec_command

# DoS protection
MAX_TEXT_LENGTH = 10000
MAX_EXPR_LENGTH = 100


class Replace(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="replace",
            description="Runs a tr expression on a string input",
            input=ReplaceInput(),
            output=ReplaceOutput(),
        )

    def run(self, params={}):
        text = params.get("text")
        expression = params.get("expression")

        if len(text) > MAX_TEXT_LENGTH:
            raise PluginException(
                cause="Input text exceeds allowed length.",
                assistance=f"Maximum allowed length is {MAX_TEXT_LENGTH} characters.",
                data={"max_length": MAX_TEXT_LENGTH},
            )

        if len(expression) > MAX_EXPR_LENGTH:
            raise PluginException(
                cause="Expression exceeds allowed length.",
                assistance=f"Maximum allowed length is {MAX_EXPR_LENGTH} characters.",
                data={"max_length": MAX_EXPR_LENGTH},
            )

        try:
            args = shlex.split(expression)
        except ValueError:
            raise PluginException(
                cause="Invalid expression format.",
                assistance="Ensure the expression is properly formatted and quoted.",
                data={"expression": expression},
            )

        forbidden_args = {"--help", "--version"}

        for arg in args:
            if arg in forbidden_args:
                raise PluginException(
                    cause="Unsupported tr option.",
                    assistance="The options --help and --version are not allowed.",
                    data={"argument": arg},
                )

        if not args:
            raise PluginException(
                cause="Missing tr arguments.",
                assistance="Provide at least STRING1 or valid tr options.",
                data={},
            )

        command = ["tr"] + args
        self.logger.info(f"Replace: Executing command: {' '.join(command)}")
        proc = exec_command(command, text)

        if proc["rcode"] == 0:
            result = proc["stdout"].decode("utf-8")
            result = result.rstrip()
            return {"result": result}
        else:
            self.logger.error(
                f"InsightConnectPluginRuntimeHelper: ExecCommand: Failed to execute: "
                f"{command}\n{proc['stderr'].decode('utf-8')}"
            )
            raise PluginException(
                cause=f"Text processing failed:\n{proc['stderr'].decode('utf-8')}",
                assistance="Please see log for details.",
            )

    def test(self):
        return self.run(params={"text": "Long    spaces    here", "expression": "-s [:space:] " ""})
