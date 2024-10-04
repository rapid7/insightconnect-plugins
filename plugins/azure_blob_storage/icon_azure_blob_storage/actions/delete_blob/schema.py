# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "The Delete Blob action marks the specified blob or snapshot for deletion. The blob is later deleted during garbage collection. Note that in order to delete a blob, you must delete all of its snapshots. You can delete both at the same time using snapshots = include parameter"


class Input:
    ADDITIONAL_HEADERS = "additional_headers"
    BLOB_NAME = "blob_name"
    CONTAINER_NAME = "container_name"
    SNAPSHOT_ID = "snapshot_id"
    SNAPSHOTS = "snapshots"
    VERSION_ID = "version_id"


class Output:
    DELETE_TYPE = "delete_type"
    MESSAGE = "message"
    SUCCESS = "success"


class DeleteBlobInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "additional_headers": {
      "type": "object",
      "title": "Additional Headers",
      "description": "Additional headers to pass to the API request",
      "default": "{ \"x-ms-client-request-id\":\"some_request_id\", \"x-ms-lease-id\":\"exa12_lease_id\" }",
      "order": 6
    },
    "blob_name": {
      "type": "string",
      "title": "Blob Name",
      "description": "Name of the blob to delete",
      "order": 2
    },
    "container_name": {
      "type": "string",
      "title": "Container Name",
      "description": "Name of the container",
      "order": 1
    },
    "snapshot_id": {
      "type": "string",
      "title": "Snapshot ID",
      "description": "The snapshot parameter is an opaque DateTime value that, when present, specifies the blob snapshot to delete",
      "order": 3
    },
    "snapshots": {
      "type": "string",
      "title": "Snapshots",
      "description": "Required if the blob has associated snapshots. Specify one of the following two options - 'include' - delete the base blob and all of its snapshots, 'only' - delete only the blob's snapshots and not the blob itself. This header should be specified only for a request against the base blob resource",
      "enum": [
        "include",
        "only",
        "None"
      ],
      "order": 5
    },
    "version_id": {
      "type": "string",
      "title": "Version ID",
      "description": "The versionid parameter is an opaque DateTime value that, when present, specifies the Version of the blob to delete",
      "order": 4
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


class DeleteBlobOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "delete_type": {
      "type": "string",
      "title": "Delete Type",
      "description": "Blob's delete type",
      "order": 3
    },
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Deletion message",
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
    "delete_type",
    "message",
    "success"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
