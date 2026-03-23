import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ExtractArchiveInput, ExtractArchiveOutput, Component, Input, Output
from komand_compression.util import utils, decompressor
from komand_compression.util.utils import sanitize_filename
from komand_compression.util.constants import UTF_8
from base64 import b64encode, b64decode


class ExtractArchive(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="extract_archive",
            description=Component.DESCRIPTION,
            input=ExtractArchiveInput(),
            output=ExtractArchiveOutput(),
        )

    def run(self, params: dict = {}) -> dict:
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        archive = params.get(Input.ARCHIVE, {})
        # END INPUT BINDING - DO NOT REMOVE

        # Extract filename and content from the archive
        archive_content = archive.get("content", "")
        archive_filename = archive.get("filename", "")
        file_bytes = b64decode(archive_content)

        # Determine compression type and extract files
        compression_type = utils.determine_compression_type(file_bytes)
        decompressed_data = decompressor.dispatch_decompress(
            algorithm=compression_type, file_bytes=file_bytes, logger=self.logger
        )

        # Process extracted files
        extracted_files = []
        if isinstance(decompressed_data, dict):
            for file_path, content in decompressed_data.items():
                try:
                    safe_name = sanitize_filename(file_path)
                except PluginException:
                    self.logger.info(f"Invalid filename: {file_path}. Skipping file.")
                    continue

                # Check if content is already base64 encoded, if not encode
                try:
                    # Attempt to decode to check if it's already encoded
                    b64decode(content)

                    # If content is bytes decode to string
                    if isinstance(content, bytes):
                        content = b64encode(content).decode(UTF_8)

                except Exception:
                    content = b64encode(content).decode(UTF_8)
                extracted_files.append({"filename": safe_name, "content": content})
        else:
            # For single file archives, use the original filename
            encoded_content = b64encode(decompressed_data).decode(UTF_8)
            extracted_files.append({"filename": archive_filename, "content": encoded_content})
        return {Output.FILES: extracted_files}
