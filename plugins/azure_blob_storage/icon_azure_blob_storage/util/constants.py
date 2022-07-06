DEFAULT_MAX_RESULTS = 20
DEFAULT_TIMEOUT = 30


class BlobType:
    PAGE_BLOB = "PageBlob"
    BLOCK_BLOB = "BlockBlob"
    APPEND_BLOB = "AppendBlob"


class UrlParam:
    TIMEOUT = "timeout"
    DELIMITER = "delimiter"
    INCLUDE = "include"
    MAX_RESULTS = "maxresults"
    PREFIX = "prefix"
    SNAPSHOT_ID = "snapshot"
    VERSION_ID = "versionid"


class HeaderParam:
    BlobType = "x-ms-blob-type"
    ACCESS_TIER = "x-ms-access-tier"
    BLOB_CONTENT_LENGTH = "x-ms-blob-content-length"
    CONTENT_LENGTH = "Content-Length"
    DELETE_SNAPSHOTS = "x-ms-delete-snapshots"
    DELETE_TYPE_PERMANENT = "x-ms-delete-type-permanent"


class Item:
    NAME = "name"
    DELETED = "deleted"
    METADATA = "metadata"
    PROPERTIES = "properties"


class Properties:
    LAST_MODIFIED = "last_modified"
    ETAG = "etag"


class Container(Item):
    pass


class Blob(Item):
    VERSION_ID = "version_id"
    SNAPSHOT_ID = "snapshot_id"
    IS_CURRENT_VERSION = "is_current_version"
    TAGS = "tags"


class ContainerProperties(Properties):
    PUBLIC_ACCESS = "public_access"


class BlobProperties(Properties):
    CREATION_TIME = "creation_time"
    REMAINING_RETENTION_DAYS = "remaining_retention_days"
    TAG_COUNT = "tag_count"
    SERVER_ENCRYPTED = "server_encrypted"
    CONTENT_TYPE = "content_type"
    BLOB_TYPE = "blob_type"
    ACCESS_TIER = "access_tier"
