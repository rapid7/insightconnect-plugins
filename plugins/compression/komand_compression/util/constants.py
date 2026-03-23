# Encoding
UTF_8 = "utf-8"

# File extensions
ZIP_EXTENSION = "zip"
TARBALL_EXTENSION = "tar.gz"

# Default archive filenames
DEFAULT_ARCHIVE_FILENAME_ZIP = "compressed.zip"
DEFAULT_ARCHIVE_FILENAME_TARBALL = "compressed.tar.gz"

# Decompression safety limits
MAX_COMPRESSION_RATIO = 100
MAX_UNCOMPRESSED_SIZE = 1_073_741_824  # 1 GB
MAX_FILE_ENTRIES = 10_000

# Error messages
INVALID_FILENAME_ERROR = "Filename cannot be empty, contain only dots, or include directory traversal sequences."
INVALID_COMPRESSION_ALGORITHM_ERROR = "Dispatch Compress: Invalid enum passed."
INVALID_DECOMPRESSION_ALGORITHM_ERROR = "Dispatch Decompress: Invalid enum passed."
UNKNOWN_COMPRESSION_TYPE_ERROR = "No compression type could be discerned from magic type description."
COMPRESSION_RATIO_EXCEEDED_ERROR = (
    "The compression ratio exceeds the maximum allowed ratio of {ratio}:1. "
    "This may indicate a zip bomb or other malicious archive."
)
MAX_SIZE_EXCEEDED_ERROR = (
    "The total uncompressed size exceeds the maximum allowed size of {size} bytes. "
    "This may indicate a zip bomb or other malicious archive."
)
MAX_ENTRIES_EXCEEDED_ERROR = (
    "The number of entries in the archive exceeds the maximum allowed count of {count}. "
    "This may indicate a zip bomb or other malicious archive."
)
