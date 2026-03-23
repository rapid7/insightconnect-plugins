import shutil
import tempfile
from pathlib import Path

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import CreateArchiveInput, CreateArchiveOutput, Component, Input, Output
from komand_compression.util import utils, compressor
from komand_compression.util.utils import sanitize_filename
from komand_compression.util.constants import (
    UTF_8,
    ZIP_EXTENSION,
    DEFAULT_ARCHIVE_FILENAME_ZIP,
    DEFAULT_ARCHIVE_FILENAME_TARBALL,
)
from base64 import b64decode, b64encode


class CreateArchive(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_archive",
            description=Component.DESCRIPTION,
            input=CreateArchiveInput(),
            output=CreateArchiveOutput(),
        )

    def run(self, params: dict = {}) -> dict:
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        algorithm = params.get(Input.ALGORITHM, "")
        filename = params.get(Input.FILENAME, "")
        files = params.get(Input.FILES, [])
        # END INPUT BINDING - DO NOT REMOVE

        # Set default archive filename if none provided
        archive_filename = filename or (
            DEFAULT_ARCHIVE_FILENAME_ZIP if algorithm == ZIP_EXTENSION else DEFAULT_ARCHIVE_FILENAME_TARBALL
        )

        # Create temporary directory to store files
        temp_directory = Path(tempfile.mkdtemp())
        temp_directory_resolved = temp_directory.resolve()
        try:
            for file_entry in files:
                # Sanitize filename and write content to temporary file
                safe_filename = sanitize_filename(file_entry.get("filename", ""))
                output_path = temp_directory / safe_filename

                # Check for path traversal
                if not output_path.resolve().is_relative_to(temp_directory_resolved):
                    raise PluginException(
                        cause="Wrong filename detected. ",
                        assistance="The filename resolved to a path outside the allowed directory.",
                    )
                output_path.write_bytes(b64decode(file_entry.get("content", "")))

            # Compress files into archive
            compressed_file = compressor.dispatch_compress(
                algorithm=algorithm, file_bytes=None, tmpdir=str(temp_directory) + "/"
            )
        finally:
            # Clean up temporary directory
            shutil.rmtree(temp_directory)

        # Encode archive to base64
        compressed_content = b64encode(compressed_file).decode(UTF_8)
        return {Output.ARCHIVE: {"filename": archive_filename, "content": compressed_content}}
