# Custom imports below
import base64
import hashlib

import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_paloalto_wildfire.util.constants import UNKNOWN_VERDICT, SUPPORTED_FILES
from .schema import SubmitFileInput, SubmitFileOutput, Input, Output, Component


class SubmitFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_file",
            description=Component.DESCRIPTION,
            input=SubmitFileInput(),
            output=SubmitFileOutput(),
        )

    def run(self, params={}):
        file = base64.b64decode(params.get(Input.FILE))
        filename = params.get(Input.FILENAME)
        if filename.lower().endswith(SUPPORTED_FILES):
            verdict = self.connection.client.get_verdicts(analysed_hash=hashlib.sha256(file).hexdigest())
            if verdict == UNKNOWN_VERDICT:
                out = self.connection.client.submit_file(_file=file, filename=filename)
                if "filename" not in out.keys():
                    out["filename"] = "Unknown"

                if "url" not in out.keys():
                    out["url"] = "Unknown"

                return {Output.SUBMISSION: insightconnect_plugin_runtime.helper.clean(out)}
            else:
                return {Output.VERDICT: verdict.capitalize()}
        else:
            raise PluginException(
                cause="Unsupported file was received by the plugin.",
                assistance=f"Check if your file is one of the supported files and resubmit with an approved file type. Supported files: {SUPPORTED_FILES}",
            )
