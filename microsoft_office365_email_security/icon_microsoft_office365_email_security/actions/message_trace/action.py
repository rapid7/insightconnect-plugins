import komand
from komand.exceptions import PluginException
from .schema import MessageTraceInput, MessageTraceOutput, Input, Output, Component
# Custom imports below
import subprocess
import os
import json


class MessageTrace(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="message_trace",
                description=Component.DESCRIPTION,
                input=MessageTraceInput(),
                output=MessageTraceOutput())

    def run(self, params={}):
        start_date = params.get(Input.START_DATE).strip()
        end_date = params.get(Input.END_DATE).strip()
        sender = params.get(Input.SENDER_ADDRESS).strip()

        false = False
        true = True
        null = None

        powershell = subprocess.Popen(["pwsh",
                                       "-ExecutionPolicy",
                                       "Unrestricted",
                                       "-File",
                                       "/powershell/Trace.ps1",
                                       "-Username",
                                       self.connection.username,
                                       "-Password",
                                       self.connection.password,
                                       "-EndDate",
                                       end_date,
                                       "-StartDate",
                                       start_date,
                                       "-Sender",
                                       sender],
                                      cwd=os.getcwd(),
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)

        out, err = powershell.communicate()
        out = str(out)
        out = self.extract_data(out)

        try:
            return {Output.MESSAGE_TRACES: json.loads(out)}
        except json.decoder.JSONDecodeError:
            raise PluginException(
                preset=PluginException.Preset.INVALID_JSON,
                data=out
            )

    def _extract_data(self, out: str) -> str:
        if "Script" not in out:
            raise PluginException(
                cause="PowerShell returned an unexpected response.",
                assistance="Please ensure all of your input parameters are correct.",
                data=out
            )
        return (
            ("[{"+out.split("Script")[-1].split("{")[-1]).replace("\\n","").replace("'","")\
        )
        
