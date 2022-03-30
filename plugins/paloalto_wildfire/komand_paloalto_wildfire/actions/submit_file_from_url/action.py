import hashlib

import insightconnect_plugin_runtime

# Custom imports below
import xmltodict
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_paloalto_wildfire.util.constants import SUPPORTED_FILES
from komand_paloalto_wildfire.util.utils import Utils
from .schema import SubmitFileFromUrlInput, SubmitFileFromUrlOutput, Input, Output, Component
from ...util.constants import UNKNOWN_VERDICT


class SubmitFileFromUrl(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_file_from_url",
            description=Component.DESCRIPTION,
            input=SubmitFileFromUrlInput(),
            output=SubmitFileFromUrlOutput(),
        )

    def run(self, params={}):
        # Formatted with None and tuples so requests sends form-data properly
        # => Send data, 299 bytes (0x12b)
        # 0000: --------------------------8557684369749613
        # 002c: Content-Disposition: form-data; name="apikey"
        # 005b:
        # 005d: 740219c8fab2606b9206b2d40626b2d1
        # 007f: --------------------------8557684369749613
        # 00ab: Content-Disposition: form-data; name="format"
        # 00d8:
        # 00da: pdf
        # 00fd: --------------------------8557684369749613--
        # ...
        url = params.get(Input.URL)
        if Utils.check_link_for_supported_file_type(url):
            file_from_url = self.connection.client.get_file_from_url(url=url)
            verdict = self.connection.client.get_verdicts(analysed_hash=hashlib.sha256(file_from_url).hexdigest())
            if verdict == UNKNOWN_VERDICT:
                try:
                    o = xmltodict.parse(self.connection.client.submit_file_from_url(url))
                    out = dict(o["wildfire"]["upload-file-info"])
                except PluginException:
                    self.logger.info("Error occurred")
                    raise

                if not out.get("filename"):
                    out["filename"] = "Unknown"

                return {Output.SUBMISSION: out}
            else:
                return {Output.VERDICT: verdict.capitalize()}
        else:
            raise PluginException(
                cause="Unsupported file was received by the plugin.",
                assistance=f"Check if your file is one of the supported files and resubmit with an approved file type. Supported files: {SUPPORTED_FILES}",
            )
