import bz2
import gzip
import io
import lzma
import tarfile
from logging import Logger
from zipfile import ZipFile

from insightconnect_plugin_runtime.exceptions import PluginException

from .algorithm import Algorithm
from .constants import (
    COMPRESSION_RATIO_EXCEEDED_ERROR,
    INVALID_DECOMPRESSION_ALGORITHM_ERROR,
    MAX_COMPRESSION_RATIO,
    MAX_ENTRIES_EXCEEDED_ERROR,
    MAX_FILE_ENTRIES,
    MAX_SIZE_EXCEEDED_ERROR,
    MAX_UNCOMPRESSED_SIZE,
)
from .utils import sanitize_filename


def _validate_compression_ratio(compressed_size: int, uncompressed_size: int) -> None:
    if compressed_size > 0 and uncompressed_size / compressed_size > MAX_COMPRESSION_RATIO:
        raise PluginException(
            cause="Compression ratio exceeded.",
            assistance=COMPRESSION_RATIO_EXCEEDED_ERROR.format(ratio=MAX_COMPRESSION_RATIO),
        )


def _validate_total_size(total_size: int) -> None:
    if total_size > MAX_UNCOMPRESSED_SIZE:
        raise PluginException(
            cause="Maximum uncompressed size exceeded.",
            assistance=MAX_SIZE_EXCEEDED_ERROR.format(size=MAX_UNCOMPRESSED_SIZE),
        )


def _validate_entry_count(count: int) -> None:
    if count > MAX_FILE_ENTRIES:
        raise PluginException(
            cause="Maximum archive entry count exceeded.",
            assistance=MAX_ENTRIES_EXCEEDED_ERROR.format(count=MAX_FILE_ENTRIES),
        )


def dispatch_decompress(algorithm: str, file_bytes: bytes, logger: Logger) -> dict[str, bytes] | bytes:
    # Check the algorithm and call the appropriate function
    if algorithm == Algorithm.GZIP:
        return gzip_decompress(file_bytes)
    elif algorithm == Algorithm.BZIP:
        return bzip_decompress(file_bytes)
    elif algorithm == Algorithm.LZ:
        return lz_decompress(file_bytes)
    elif algorithm == Algorithm.XZ:
        return xz_decompress(file_bytes)
    elif algorithm == Algorithm.ZIP:
        return zip_decompress(file_bytes, logger)
    raise PluginException(
        cause="Invalid decompression algorithm.",
        assistance=INVALID_DECOMPRESSION_ALGORITHM_ERROR,
    )


def gzip_decompress(file_bytes: bytes) -> dict[str, bytes] | bytes:
    decompressed = gzip.decompress(file_bytes)
    _validate_compression_ratio(len(file_bytes), len(decompressed))
    _validate_total_size(len(decompressed))
    if tarfile.is_tarfile(io.BytesIO(decompressed)):
        return tarball_decompress(decompressed)
    return decompressed


def bzip_decompress(file_bytes: bytes) -> bytes:
    decompressed = bz2.decompress(file_bytes)
    _validate_compression_ratio(len(file_bytes), len(decompressed))
    _validate_total_size(len(decompressed))
    return decompressed


def xz_decompress(file_bytes: bytes) -> bytes:
    decompressed = lzma.decompress(file_bytes)
    _validate_compression_ratio(len(file_bytes), len(decompressed))
    _validate_total_size(len(decompressed))
    return decompressed


def lz_decompress(file_bytes: bytes) -> bytes:
    decompressed = lzma.decompress(file_bytes, format=lzma.FORMAT_ALONE)
    _validate_compression_ratio(len(file_bytes), len(decompressed))
    _validate_total_size(len(decompressed))
    return decompressed


def zip_decompress(file_bytes: bytes, logger: Logger) -> dict[str, bytes] | bytes:
    # Initialize variables to track total size and entry count
    files = {}
    total_uncompressed_size = 0
    compressed_size = len(file_bytes)

    #  Process each entry in the zip file
    with ZipFile(io.BytesIO(file_bytes), "r") as zip_object:
        entries = zip_object.infolist()
        _validate_entry_count(len(entries))

        for entry in entries:
            # Skip directories
            if entry.is_dir():
                continue

            # Validate uncompressed size before reading
            total_uncompressed_size += entry.file_size
            _validate_total_size(total_uncompressed_size)
            _validate_compression_ratio(compressed_size, total_uncompressed_size)

            # Sanitize the filename
            try:
                safe_name = sanitize_filename(entry.filename)
            except PluginException as exception:
                logger.info("Skipping archive entry with invalid filename '%s': %s", entry.filename, exception)
                continue

            # Skip hidden files
            if safe_name.startswith("."):
                continue

            # If ".gz" in filename, decompress file
            if safe_name.endswith(".gz"):
                files[safe_name] = gzip_decompress(zip_object.read(entry.filename))
                continue

            # Add the file to the dictionary
            files[safe_name] = zip_object.read(entry.filename)

    # If there is only one file, return it directly
    # Otherwise return the dictionary of files
    return files if len(files) != 1 else files[list(files.keys())[0]]


def tarball_decompress(file_bytes: bytes) -> dict[str, bytes] | bytes:
    #  Initialize variables to track total size, entry count
    files = {}
    total_uncompressed_size = 0
    compressed_size = len(file_bytes)
    entry_count = 0

    # Process each entry in the tar file
    with tarfile.open(fileobj=io.BytesIO(file_bytes), mode="r:*") as tar:
        for member in tar.getmembers():
            # If not a regular file, skip it
            if not member.isfile():
                continue

            entry_count += 1
            _validate_entry_count(entry_count)

            # Validate cumulative uncompressed size before reading
            total_uncompressed_size += member.size
            _validate_total_size(total_uncompressed_size)
            _validate_compression_ratio(compressed_size, total_uncompressed_size)

            # Sanitize the filename
            try:
                safe_name = sanitize_filename(member.name)
            except PluginException:
                continue

            # Skip hidden files
            if safe_name.startswith("."):
                continue

            # If ".gz" in filename, decompress file
            if safe_name.endswith(".gz"):
                files[safe_name] = gzip_decompress(tar.extractfile(member).read())
                continue

            # Add the file to the dictionary
            if extracted := tar.extractfile(member):
                files[safe_name] = extracted.read()

    return files if len(files) != 1 else files[list(files.keys())[0]]
