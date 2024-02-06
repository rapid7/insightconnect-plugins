# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Submits a file to the sandbox for analysis (Note. For more information about the supported file types, see the Trend Micro Vision One Online Help. Submissions require credits. Does not require credits in regions where Sandbox Analysis has not been officially released.)"


class Input:
    ARCHIVE_PASSWORD = "archive_password"
    ARGUMENTS = "arguments"
    DOCUMENT_PASSWORD = "document_password"
    FILE = "file"


class Output:
    ARGUMENTS = "arguments"
    DIGEST = "digest"
    ID = "id"


class SubmitFileToSandboxInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "archive_password": {
      "type": "string",
      "title": "Archive Password",
      "description": "Password encoded in Base64 used to decrypt the submitted archive. The maximum password length (without encoding) is 128 bytes",
      "order": 3
    },
    "arguments": {
      "type": "string",
      "title": "Arguments",
      "description": "Parameter that allows you to specify Base64-encoded command line arguments to run the submitted file. The maximum argument length before encoding is 1024 bytes. Arguments are only available for Portable Executable (PE) files and script files",
      "order": 4
    },
    "document_password": {
      "type": "string",
      "title": "Document Password",
      "description": "Password encoded in Base64 used to decrypt the submitted file sample. The maximum password length (without encoding) is 128 bytes",
      "order": 2
    },
    "file": {
      "$ref": "#/definitions/file",
      "title": "File",
      "description": "File submitted to the sandbox (dict of {filename(string) & content(base64(bytes))})",
      "order": 1
    }
  },
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        },
        "content": {
          "type": "string",
          "format": "bytes",
          "title": "Content",
          "description": "File contents"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SubmitFileToSandboxOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "arguments": {
      "type": "string",
      "title": "Arguments",
      "description": "Command line arguments encoded in Base64 of the submitted file",
      "order": 3
    },
    "digest": {
      "type": "object",
      "title": "Digest",
      "description": "The hash value of the file",
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Unique alphanumeric string that identifies a submission",
      "order": 1
    }
  },
  "required": [
    "digest",
    "id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
