# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List Carbon Black binaries with given parameters"


class Input:
    QUERY = "query"
    ROWS = "rows"
    START = "start"


class Output:
    BINARIES = "binaries"


class ListBinariesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query String",
      "description": "Accepts the same data as the search box on the Process Search page",
      "order": 1
    },
    "rows": {
      "type": "integer",
      "title": "Rows",
      "description": "How many rows of data to return. Default is 10",
      "default": 10,
      "order": 2
    },
    "start": {
      "type": "integer",
      "title": "Start",
      "description": "What row of data to start at. Default is 0",
      "default": 0,
      "order": 3
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListBinariesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "binaries": {
      "type": "array",
      "title": "Binaries",
      "description": "The list of binaries",
      "items": {
        "$ref": "#/definitions/binary"
      },
      "order": 1
    }
  },
  "definitions": {
    "binary": {
      "type": "object",
      "title": "binary",
      "properties": {
        "digsig_prog_name": {
          "type": "string",
          "title": "Digital Signature Program Name",
          "description": "If signed and present, the program name",
          "order": 1
        },
        "digsig_issuer": {
          "type": "string",
          "title": "Digital Signature Issuer",
          "description": "If signed and present, the issuer name",
          "order": 2
        },
        "product_name": {
          "type": "string",
          "title": "Product Name",
          "description": "If present, product name from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)",
          "order": 3
        },
        "is_executable_image": {
          "type": "boolean",
          "title": "Is Executable Image",
          "description": "True if an EXE",
          "order": 4
        },
        "digsig_result": {
          "type": "string",
          "title": "Digital Signature Result",
          "description": "Digital signature status; One of Signed, Unsigned, Expired, Bad Signature, Invalid Signature, Invalid Chain, Untrusted Root, Explicit Distrust",
          "order": 5
        },
        "digsig_subject": {
          "type": "string",
          "title": "Digital Signature Subject",
          "description": "If signed and present, the subject",
          "order": 6
        },
        "observed_filename": {
          "type": "array",
          "title": "Observed Filename",
          "description": "The set of unique filenames this binary has been seen as",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "os_type": {
          "type": "string",
          "title": "OS Types",
          "description": "Operating system type of this binary; one of windows, linux, osx",
          "enum": [
            "Windows",
            "OSX",
            "Linux"
          ],
          "order": 8
        },
        "orig_mod_len": {
          "type": "integer",
          "title": "Original Mod Length",
          "description": "Filesize in bytes",
          "order": 9
        },
        "special_build": {
          "type": "string",
          "title": "Special Build",
          "description": "If present, special build from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)",
          "order": 10
        },
        "company_name": {
          "type": "string",
          "title": "Company Name",
          "description": "If present, company name from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)",
          "order": 11
        },
        "alliance_score_virustotal": {
          "type": "string",
          "title": "Alliance Score Virustotal",
          "description": "If enabled and the hit count is greater than one, the number of [VirusTotal](http://virustotal.com) hits for this MD5",
          "order": 12
        },
        "server_added_timestamp": {
          "type": "string",
          "title": "Server Added Timestamp",
          "description": "The first time this binary was received on the server in the server GMT time",
          "order": 13
        },
        "private_build": {
          "type": "string",
          "title": "Private Build",
          "description": "If present, private build from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)",
          "order": 14
        },
        "internal_name": {
          "type": "string",
          "title": "Internal Name",
          "description": "If present, internal name from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)",
          "order": 15
        },
        "copied_mod_len": {
          "type": "integer",
          "title": "Copied Mod Length",
          "description": "Bytes copied from remote host. If file is greater than 25MB this will be less than orig_mod_len",
          "order": 16
        },
        "file_version": {
          "type": "string",
          "title": "File Version",
          "description": "If present, file version from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)",
          "order": 17
        },
        "product_version": {
          "type": "string",
          "title": "Product Version",
          "description": "If present, product version from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)",
          "order": 18
        },
        "signed": {
          "type": "string",
          "title": "Signed",
          "description": "Digital signature status. One of Signed, Unsigned, Expired, Bad Signature, Invalid Signature, Invalid Chain, Untrusted Root, Explicit Distrust",
          "order": 19
        },
        "digsig_sign_time": {
          "type": "string",
          "title": "Digital Signature Times",
          "description": "If signed, the timestamp of the signature in GMT",
          "order": 20
        },
        "file_desc": {
          "type": "string",
          "title": "File Description",
          "description": "If present, file description from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)",
          "order": 21
        },
        "legal_trademark": {
          "type": "string",
          "title": "Legal Trademark",
          "description": "If present, legal trademark from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)",
          "order": 22
        },
        "digsig_result_code": {
          "type": "string",
          "title": "Digital Signature Result Code",
          "description": "HRESULT_FROM_WIN32 for the result of the digital signature operation via [WinVerifyTrust](http://msdn.microsoft.com/en-us/library/windows/desktop/aa388208)",
          "order": 23
        },
        "original_filename": {
          "type": "string",
          "title": "Original Filename",
          "description": "If present, original filename from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)",
          "order": 24
        },
        "legal_copyright": {
          "type": "string",
          "title": "Legal Copyright",
          "description": "If present, legal copyright from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)",
          "order": 25
        },
        "host_count": {
          "type": "integer",
          "title": "Host Count",
          "description": "Count of unique endpoints which have ever reported this binary",
          "order": 26
        },
        "is_64bit": {
          "type": "boolean",
          "title": "Is 64-bit",
          "description": "True if x64",
          "order": 27
        },
        "md5": {
          "type": "string",
          "title": "MD5",
          "description": "The MD5 hash of this binary",
          "order": 28
        },
        "digsig_publisher": {
          "type": "string",
          "title": "Digital Signature Publisher",
          "description": "If signed and present, the publisher name",
          "order": 29
        },
        "endpoint": {
          "type": "array",
          "title": "Endpoint",
          "items": {
            "type": "string"
          },
          "order": 30
        },
        "group": {
          "type": "array",
          "title": "Group",
          "items": {
            "type": "string"
          },
          "order": 31
        },
        "timestamp": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Timestamp",
          "order": 32
        },
        "cb_version": {
          "type": "integer",
          "title": "Carbon Black Version",
          "order": 33
        },
        "last_seen": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Last Seen",
          "order": 34
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
