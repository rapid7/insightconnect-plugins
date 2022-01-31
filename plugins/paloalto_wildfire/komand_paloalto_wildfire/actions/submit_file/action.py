# Custom imports below
import base64
import hashlib

import komand

from komand.exceptions import PluginException
from komand_paloalto_wildfire.util.constants import UNKNOWN_VERDICT, SUPPORTED_FILES
from .schema import SubmitFileInput, SubmitFileOutput, Input, Output


class SubmitFile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_file",
            description="Submit a file for analysis",
            input=SubmitFileInput(),
            output=SubmitFileOutput(),
        )

    def run(self, params={}):
        file = base64.b64decode(params.get(Input.FILE))
        filename = params.get(Input.FILENAME)
        if filename.lower().endswith(SUPPORTED_FILES):
            verdict = self.connection.client.get_verdicts(analysed_hash=hashlib.md5(file).hexdigest())
            if verdict == UNKNOWN_VERDICT:
                out = self.connection.client.submit_file(_file=file, filename=filename)
                if "filename" not in out.keys():
                    out["filename"] = "Unknown"

                if "url" not in out.keys():
                    out["url"] = "Unknown"

                return {Output.SUBMISSION: komand.helper.clean(out)}
            else:
                return {Output.VERDICT: verdict.capitalize()}
        else:
            raise PluginException(
                cause="Unsupported file was received by the plugin.",
                assistance=f"Check if your file is one of the supported files and resubmit with an approved file type. Supported files: {SUPPORTED_FILES}",
            )
