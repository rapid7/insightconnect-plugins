import bz2
import gzip
import io
import lzma
import tarfile
import zipfile
from pathlib import Path
from zipfile import ZipFile

from insightconnect_plugin_runtime.exceptions import PluginException

from .algorithm import Algorithm
from .constants import INVALID_COMPRESSION_ALGORITHM_ERROR


def dispatch_compress(algorithm: str, file_bytes: bytes | None, tmpdir: str = "") -> bytes:
    # Check the algorithm and call the appropriate compression function
    if algorithm == Algorithm.GZIP:
        return gzip_compress(file_bytes)
    elif algorithm == Algorithm.BZIP:
        return bzip_compress(file_bytes)
    elif algorithm == Algorithm.LZ:
        return lz_compress(file_bytes)
    elif algorithm == Algorithm.XZ:
        return xz_compress(file_bytes)
    elif algorithm == Algorithm.ZIP:
        return zip_compress(file_bytes, tmpdir)
    elif algorithm == Algorithm.TARBALL:
        return tarball_compress(tmpdir)
    raise PluginException(
        cause="Invalid compression algorithm.",
        assistance=INVALID_COMPRESSION_ALGORITHM_ERROR,
    )


def gzip_compress(file_bytes: bytes) -> bytes:
    return gzip.compress(file_bytes)


def bzip_compress(file_bytes: bytes) -> bytes:
    return bz2.compress(file_bytes)


def xz_compress(file_bytes: bytes) -> bytes:
    return lzma.compress(data=file_bytes)


def lz_compress(file_bytes: bytes) -> bytes:
    return lzma.compress(data=file_bytes, format=lzma.FORMAT_ALONE)


def zip_compress(file_bytes: bytes | None, tmpdir: str = "") -> bytes:
    # Create a zip archive from the input bytes or temporary directory
    if file_bytes is not None:
        buffer = io.BytesIO()
        with ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zip_object:
            zip_object.writestr("compressed", file_bytes)
        return buffer.getvalue()
    else:
        tmpdir_path = Path(tmpdir)
        zipf = tmpdir_path / "compressed.zip"
        with ZipFile(zipf, "w", zipfile.ZIP_DEFLATED) as zippy:
            for filepath in tmpdir_path.glob("*"):
                if filepath != zipf:
                    zippy.write(filepath, filepath.name)
        data = zipf.read_bytes()
        zipf.unlink()
        return data


def tarball_compress(tmpdir: str) -> bytes:
    # Create a tar.gz archive from the temporary directory
    tmpdir_path = Path(tmpdir)
    tar_path = tmpdir_path / "archive.tar.gz"

    # Create the tar.gz archive
    with tarfile.open(tar_path, "w:gz") as tar:
        for filepath in tmpdir_path.glob("*"):
            if filepath != tar_path:
                tar.add(filepath, arcname=filepath.name)

    # Read the tar.gz file and return its bytes
    data = tar_path.read_bytes()
    tar_path.unlink()
    return data
