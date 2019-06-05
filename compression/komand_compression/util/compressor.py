import io
import glob
from zipfile import ZipFile
import zipfile
import os
import tarfile
import lzma
import gzip
import bz2
from .algorithm import Algorithm


def dispatch_compress(algorithm, file_bytes, tmpdir=""):

    if algorithm == Algorithm.GZIP:
        return gzip_compress(file_bytes)

    elif algorithm == Algorithm.BZIP:
        return bzip_compress(file_bytes)

    elif algorithm == Algorithm.LZ:
        return lz_compress(file_bytes)

    elif algorithm == Algorithm.XZ:
        return xz_compress(file_bytes)

    elif algorithm == Algorithm.ZIP:
        return zip_compress(file_bytes,tmpdir)

    elif algorithm == Algorithm.TARBALL:
        return tarball_compress(file_bytes,tmpdir)

    else:
        raise Exception("Dispatch Compress: Invalid enum passed.")

def tarball_compress(file_bytes,tmpdir):
    with tarfile.open(tmpdir+"test.tar.gz","w:gz") as tar:
        tar.add(tmpdir, recursive=True)
    fbytes=[]
    with open(tmpdir+"test.tar.gz","rb") as f:
        fbytes = f.read()
    os.remove(tmpdir+"test.tar.gz")
    return fbytes


def gzip_compress(file_bytes):
    compressed = gzip.compress(file_bytes)
    return compressed


def bzip_compress(file_bytes):
    compressed = bz2.compress(file_bytes)
    return compressed


def xz_compress(file_bytes):
    compressed = lzma.compress(data=file_bytes)  # Use default parameter argument of format=LZMA.FORMAT_XZ
    return compressed


def lz_compress(file_bytes):
    compressed = lzma.compress(data=file_bytes, format=lzma.FORMAT_ALONE)  # lzma.FORMAT_ALONE = LZMA
    return compressed

def zip_compress(file_bytes,tmpdir=""):
    if file_bytes != None:
        algorithm = zipfile.ZIP_DEFLATED  # sets compression type to deflated (standard for .zip)
        zip_object = ZipFile('/tmp/compressed.zip', "w", algorithm)  # zip archive created in temp
        zip_object.writestr('compressed', file_bytes)  # TODO use magic to corectly name files in arcive
        zip_object.close()
        in_file = open("/tmp/compressed.zip", "rb")
        compressed = in_file.read()
        in_file.close()
        os.remove("/tmp/compressed.zip")  # clean up
        return compressed
    else:
        zipf = tmpdir+"compressed.zip"
        with zipfile.ZipFile(zipf, "w", zipfile.ZIP_DEFLATED) as zippy:
            for x in glob.glob(tmpdir+"*"):
                zippy.write(x,os.path.basename(x))
        with open(zipf,"rb") as f:
            fbytes = f.read()
        os.remove(zipf)
        return fbytes


