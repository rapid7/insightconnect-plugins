# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "The Put Blob action creates a new block, page, or append blob, or updates the content of an existing block blob"


class Input:
    ACCESS_TIER = "access_tier"
    ADDITIONAL_HEADERS = "additional_headers"
    BLOB_CONTENT = "blob_content"
    BLOB_CONTENT_LENGTH = "blob_content_length"
    BLOB_NAME = "blob_name"
    BLOB_TYPE = "blob_type"
    CONTAINER_NAME = "container_name"
    TIMEOUT = "timeout"


class Output:
    MESSAGE = "message"
    SUCCESS = "success"


class PutBlobInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "access_tier": {
      "type": "string",
      "title": "Access Tier",
      "description": "Indicates the tier to be set on blob. For page blobs on a premium storage account only. Valid values for block blob tiers are Hot/Cool/Archive. For detailed information about block blob tiering see https://docs.microsoft.com/enus/azure/storage/blobs/access -tiers-overview",
      "default": "Hot",
      "enum": [
        "Hot",
        "Cool",
        "Archive",
        "None"
      ],
      "order": 6
    },
    "additional_headers": {
      "type": "object",
      "title": "Additional Headers",
      "description": "Additional headers to pass to the API request",
      "order": 8
    },
    "blob_content": {
      "type": "string",
      "title": "Blob Content",
      "description": "Content of the new blob. This field is allowed only for BlockBlob type",
      "order": 5
    },
    "blob_content_length": {
      "type": "integer",
      "title": "Blob Content Length",
      "description": "Required for page blobs. This header specifies the maximum size for the page blob, up to 8 TiB. The page blob size must be aligned to a 512-byte boundary",
      "order": 7
    },
    "blob_name": {
      "type": "string",
      "title": "Blob Name",
      "description": "Name of the new blob",
      "order": 2
    },
    "blob_type": {
      "type": "string",
      "title": "Blob Type",
      "description": "Specifies the type of blob to create - block blob, page blob, or append blob",
      "enum": [
        "BlockBlob",
        "PageBlob",
        "AppendBlob"
      ],
      "order": 4
    },
    "container_name": {
      "type": "string",
      "title": "Container Name",
      "description": "Container name where the new blob will be put",
      "order": 1
    },
    "timeout": {
      "type": "integer",
      "title": "Timeout",
      "description": "Maximum time to wait for server response in seconds, not larger than 10 minutes per megabyte",
      "order": 3
    }
  },
  "required": [
    "blob_name",
    "container_name"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PutBlobOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Creation message",
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether the action was successful or not",
      "order": 1
    }
  },
  "required": [
    "message",
    "success"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
