import insightconnect_plugin_runtime
from .schema import ReadInput, ReadOutput, Input, Output

# Custom imports below
import base64
import subprocess  # nosec
from uuid import uuid4
from pathlib import Path
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_tcpdump.util.constants import DEFAULT_TIMEOUT
from komand_tcpdump.util.sanitizer import validate_options, validate_filter


class Read(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="read",
            description="Read contents from a PCAP file",
            input=ReadInput(),
            output=ReadOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        pcap = params.get(Input.PCAP)
        options = params.get(Input.OPTIONS, "")
        filter_ = params.get(Input.FILTER, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Generate a secure filename using UUID
        filename = f"/tmp/input-{uuid4()}.pcap"  # nosec
        try:
            # Decode the base64-encoded PCAP data
            try:
                pcap_decoded = base64.b64decode(pcap)
            except Exception as error:
                raise PluginException(
                    cause="Invalid PCAP data provided. ", assistance="Failed to decode PCAP data", data=error
                )

            # Write PCAP data to file
            with open(filename, "wb") as file_:
                file_.write(pcap_decoded)

            # Build command as a list for subprocess to prevent shell injection
            command = ["tcpdump", "-r", filename]

            # Validate and add options if provided
            if options:
                command.extend(validate_options(options))

            # Validate and add filter if provided
            if filter_:
                command.append(validate_filter(filter_))

            # Execute command without shell=True to prevent injection
            self.logger.info(f"Executing tcpdump with command: {' '.join(command)}")
            response = subprocess.run(command, capture_output=True, check=False, timeout=DEFAULT_TIMEOUT)  # nosec
            stderr = response.stderr.decode()

            # If response is not successful, log error and raise exception
            if response.returncode != 0:
                self.logger.error(f"{stderr}")
                raise PluginException(cause="Tcpdump execution failed", assistance=f"Tcpdump returned error: {stderr}")

            # Encode the output as base64 to safely return binary data
            dump_file = base64.b64encode(response.stdout)
            stdout_list = insightconnect_plugin_runtime.helper.clean(response.stdout.decode().split("\n"))
            return {Output.DUMP_CONTENTS: stdout_list, Output.DUMP_FILE: dump_file.decode(), Output.STDERR: stderr}
        finally:
            # Clean up temporary file
            file_path = Path(filename)
            if file_path.is_file():
                file_path.unlink()
