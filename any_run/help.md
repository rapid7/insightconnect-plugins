# Description

[Any.Run](https://any.run/) is a cloud-based malware analysis service. Automate analyzing suspicious and malicious activites using this plugin.

This plugin utilizes the [Any.Run API](https://any.run/api-documentation/).

# Key Features

* Submit files for analysis
* Obtain analysis report
* Search task history

# Requirements

* Requires an API Key or username and password combination

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|False|API Key for Any.Run|None|WbTbwa4KFk77eQNffMJynWXm49jLwGjwPMKM9Xc4|
|credentials|credential_username_password|None|False|Username and password|None|{ "username": "user@example.com", "password":"mypassword"}|

## Technical Details

### Actions

#### Get History Tasks

This action is used to get history Tasks.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|limit|integer|25|False|Limits number of records, Size range 1-100|None|25|
|skip|integer|0|False|Skip records|None|25|
|team|boolean|False|False|Leave this field blank to get your history or specify to get team history|None|False|

Example input:

```
{
  "limit": 1
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tasks|[]task|False|History tasks|

Example output:

```
{
  "tasks": [
    {
      "date": "2020-04-18T18:53:06.794Z",
      "file": "https://content.any.run/tasks/5a181e40-bd50-40aa-9e33-077b261b6381/download/files/d0975bad-6e74-40e9-af55-47b2080c2027",
      "hashes": {
        "head_hash": "0145ad575b213b1703cb94c6c3568a2e",
        "md5": "926e6146fdb288e932a1846029ad07db",
        "sha1": "fc73d7c62e324cad4240fbaf7a6d53716ecc4de7",
        "sha256": "f6df99db2023558798d234f9c118497db8ec83da37682f886859f643fc8cc44b",
        "ssdeep": "768:s+QiSf3rhTePO38fXbEmJS2Iro2wFW0kEeu:svXj5ePO3CXbEES2vw0Heu"
      },
      "json": "https://api.any.run/report/5a181e40-bd50-40aa-9e33-077b261b6381/summary/json",
      "misp": "https://api.any.run/report/5a181e40-bd50-40aa-9e33-077b261b6381/summary/misp",
      "name": "http://pastebin.com/raw/xGXyTALF",
      "pcap": "https://content.any.run/tasks/5a181e40-bd50-40aa-9e33-077b261b6381/download/pcap",
      "related": "https://app.any.run/tasks/5a181e40-bd50-40aa-9e33-077b261b6381",
      "tags": [],
      "verdict": "No threats detected"
    }
  ]
}
```

#### Get Report

This action is used to get task report.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|task|string|None|True|Task UUID|None|0cf223f2-530e-4a50-b68f-563045268648|

Example input:

```
{
  "task": "4649c7fc-5780-476a-86b0-b89e424339bc"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reports|object|False|Task reports|

Example output:

```
{
  "reports": {
    "analysis": {
      "content": {
        "mainObject": {
          "filename": "setup.exe",
          "hashes": {
            "md5": "c4ab8765314fc770e3ee8ca0693df8f9",
            "sha1": "0194f8c5364d1dad03a1fe6eaa0fd98a10accd9e",
            "sha256": "9ed4502b2eb64dd0a4394e593cb3666e621e751c26d06f3dbb953808bf83536e",
            "ssdeep": "6144:0mvr9RLcN0BvxoLjGRU4UUU3UUUD9rOAerhj4Dy6ZTab8QCuzkLyS0RliUFh:0mr9RUsJGjqU4UUU3UUUZa7NjP6pbhOp"
          },
          "info": {
            "exif": {
              "EXE": {
                "CharacterSet": "Unicode",
                "CodeSize": 65536,
                "CompanyName": "Mozilla",
                "EntryPoint": "0x34310",
                "FileDescription": "Firefox",
                "FileFlags": "(none)",
                "FileFlagsMask": "0x003f",
                "FileOS": "Windows NT 32-bit",
                "FileSubtype": 0,
                "FileVersion": 18.05,
                "FileVersionNumber": "18.5.0.0",
                "ImageVersion": 0,
                "InitializedDataSize": 65536,
                "InternalName": "7zS.sfx",
                "LanguageCode": "English (U.S.)",
                "LegalCopyright": "Mozilla",
                "LinkerVersion": 6,
                "MachineType": "Intel 386 or later, and compatibles",
                "OSVersion": 4,
                "ObjectFileType": "Executable application",
                "OriginalFileName": "7zS.sfx.exe",
                "PEType": "PE32",
                "ProductName": "Firefox",
                "ProductVersion": 18.05,
                "ProductVersionNumber": "18.5.0.0",
                "Subsystem": "Windows GUI",
                "SubsystemVersion": 4,
                "TimeStamp": "2018:08:31 00:18:33+02:00",
                "UninitializedDataSize": 147456
              }
            },
            "ext": "exe",
            "file": "PE32 executable (GUI) Intel 80386, for MS Windows, UPX compressed",
            "mime": "application/x-dosexec",
            "pe": [
              {
                "key": "Summary",
                "value": [
                  {
                    "key": "Architecture",
                    "value": "IMAGE_FILE_MACHINE_I386"
                  },
                  {
                    "key": "Subsystem",
                    "value": "IMAGE_SUBSYSTEM_WINDOWS_GUI"
                  },
                  {
                    "key": "Compilation Date",
                    "value": "30-Aug-2018 22:18:33"
                  },
                  {
                    "key": "Detected languages",
                    "value": [
                      "English - United States"
                    ]
                  },
                  {
                    "key": "CompanyName",
                    "value": "Mozilla"
                  },
                  {
                    "key": "FileDescription",
                    "value": "Firefox"
                  },
                  {
                    "key": "FileVersion",
                    "value": "18.05"
                  },
                  {
                    "key": "InternalName",
                    "value": "7zS.sfx"
                  },
                  {
                    "key": "LegalCopyright",
                    "value": "Mozilla"
                  },
                  {
                    "key": "OriginalFilename",
                    "value": "7zS.sfx.exe"
                  },
                  {
                    "key": "ProductName",
                    "value": "Firefox"
                  },
                  {
                    "key": "ProductVersion",
                    "value": "18.05"
                  }
                ]
              },
              {
                "key": "DOS Header",
                "value": [
                  {
                    "key": "Magic number",
                    "value": "MZ"
                  },
                  {
                    "key": "Bytes on last page of file",
                    "value": "0x0090"
                  },
                  {
                    "key": "Pages in file",
                    "value": "0x0003"
                  },
                  {
                    "key": "Relocations",
                    "value": "0x0000"
                  },
                  {
                    "key": "Size of header",
                    "value": "0x0004"
                  },
                  {
                    "key": "Min extra paragraphs",
                    "value": "0x0000"
                  },
                  {
                    "key": "Max extra paragraphs",
                    "value": "0xFFFF"
                  },
                  {
                    "key": "Initial SS value",
                    "value": "0x0000"
                  },
                  {
                    "key": "Initial SP value",
                    "value": "0x00B8"
                  },
                  {
                    "key": "Checksum",
                    "value": "0x0000"
                  },
                  {
                    "key": "Initial IP value",
                    "value": "0x0000"
                  },
                  {
                    "key": "Initial CS value",
                    "value": "0x0000"
                  },
                  {
                    "key": "Overlay number",
                    "value": "0x0000"
                  },
                  {
                    "key": "OEM identifier",
                    "value": "0x0000"
                  },
                  {
                    "key": "OEM information",
                    "value": "0x0000"
                  },
                  {
                    "key": "Address of NE header",
                    "value": "0x000000F0"
                  }
                ]
              },
              {
                "key": "PE Header",
                "value": [
                  {
                    "key": "Signature",
                    "value": "PE"
                  },
                  {
                    "key": "Machine",
                    "value": "IMAGE_FILE_MACHINE_I386"
                  },
                  {
                    "key": "Number of sections",
                    "value": "3"
                  },
                  {
                    "key": "Time date stamp",
                    "value": "30-Aug-2018 22:18:33"
                  },
                  {
                    "key": "Pointer to Symbol Table",
                    "value": "0x00000000"
                  },
                  {
                    "key": "Number of symbols",
                    "value": "0"
                  },
                  {
                    "key": "Size of Optional Header",
                    "value": "0x00E0"
                  },
                  {
                    "key": "Characteristics",
                    "value": [
                      "IMAGE_FILE_32BIT_MACHINE",
                      "IMAGE_FILE_EXECUTABLE_IMAGE",
                      "IMAGE_FILE_LINE_NUMS_STRIPPED",
                      "IMAGE_FILE_LOCAL_SYMS_STRIPPED",
                      "IMAGE_FILE_RELOCS_STRIPPED"
                    ]
                  }
                ]
              },
              {
                "key": "Image Optional Header",
                "value": [
                  {
                    "key": "Magic",
                    "value": "PE32"
                  },
                  {
                    "key": "LinkerVersion",
                    "value": "6.0"
                  },
                  {
                    "key": "SizeOfCode",
                    "value": "0x00010000"
                  },
                  {
                    "key": "SizeOfInitializedData",
                    "value": "0x00010000"
                  },
                  {
                    "key": "SizeOfUninitializedData",
                    "value": "0x00024000"
                  },
                  {
                    "key": "AddressOfEntryPoint",
                    "value": "0x00034310 (Section: UPX1)"
                  },
                  {
                    "key": "BaseOfCode",
                    "value": "0x00025000"
                  },
                  {
                    "key": "BaseOfData",
                    "value": "0x00035000"
                  },
                  {
                    "key": "ImageBase",
                    "value": "0x00400000"
                  },
                  {
                    "key": "SectionAlignment",
                    "value": "0x00001000"
                  },
                  {
                    "key": "FileAlignment",
                    "value": "0x00000200"
                  },
                  {
                    "key": "OperatingSystemVersion",
                    "value": "4.0"
                  },
                  {
                    "key": "ImageVersion",
                    "value": "0.0"
                  },
                  {
                    "key": "SubsystemVersion",
                    "value": "4.0"
                  },
                  {
                    "key": "Win32VersionValue",
                    "value": "0"
                  },
                  {
                    "key": "SizeOfImage",
                    "value": "0x00045000"
                  },
                  {
                    "key": "SizeOfHeaders",
                    "value": "0x00001000"
                  },
                  {
                    "key": "Checksum",
                    "value": "0x00058C84"
                  },
                  {
                    "key": "Subsystem",
                    "value": "IMAGE_SUBSYSTEM_WINDOWS_GUI"
                  },
                  {
                    "key": "SizeofStackReserve",
                    "value": "0x00100000"
                  },
                  {
                    "key": "SizeofStackCommit",
                    "value": "0x00001000"
                  },
                  {
                    "key": "SizeofHeapReserve",
                    "value": "0x00100000"
                  },
                  {
                    "key": "SizeofHeapCommit",
                    "value": "0x00001000"
                  },
                  {
                    "key": "LoaderFlags",
                    "value": "0x00000000"
                  },
                  {
                    "key": "NumberOfRvaAndSizes",
                    "value": "16"
                  }
                ]
              },
              {
                "key": "Sections",
                "value": [
                  {
                    "key": "UPX0",
                    "value": {
                      "Characteristics": [
                        "IMAGE_SCN_CNT_UNINITIALIZED_DATA",
                        "IMAGE_SCN_MEM_EXECUTE",
                        "IMAGE_SCN_MEM_READ",
                        "IMAGE_SCN_MEM_WRITE"
                      ],
                      "Entropy": "0",
                      "NumberOfLineNumbers": "0",
                      "NumberOfRelocations": "0",
                      "PointerToLineNumbers": "0x00000000",
                      "PointerToRawData": "0x00000400",
                      "PointerToRelocations": "0x00000000",
                      "SizeOfRawData": "0x00000000",
                      "VirtualAddress": "0x00001000",
                      "VirtualSize": "0x00024000"
                    }
                  },
                  {
                    "key": "UPX1",
                    "value": {
                      "Characteristics": [
                        "IMAGE_SCN_CNT_INITIALIZED_DATA",
                        "IMAGE_SCN_MEM_EXECUTE",
                        "IMAGE_SCN_MEM_READ",
                        "IMAGE_SCN_MEM_WRITE"
                      ],
                      "Entropy": "7.89699",
                      "NumberOfLineNumbers": "0",
                      "NumberOfRelocations": "0",
                      "PointerToLineNumbers": "0x00000000",
                      "PointerToRawData": "0x00000400",
                      "PointerToRelocations": "0x00000000",
                      "SizeOfRawData": "0x0000F600",
                      "VirtualAddress": "0x00025000",
                      "VirtualSize": "0x00010000"
                    }
                  },
                  {
                    "key": ".rsrc",
                    "value": {
                      "Characteristics": [
                        "IMAGE_SCN_CNT_INITIALIZED_DATA",
                        "IMAGE_SCN_MEM_READ",
                        "IMAGE_SCN_MEM_WRITE"
                      ],
                      "Entropy": "7.39743",
                      "NumberOfLineNumbers": "0",
                      "NumberOfRelocations": "0",
                      "PointerToLineNumbers": "0x00000000",
                      "PointerToRawData": "0x0000FA00",
                      "PointerToRelocations": "0x00000000",
                      "SizeOfRawData": "0x0000F200",
                      "VirtualAddress": "0x00035000",
                      "VirtualSize": "0x00010000"
                    }
                  }
                ]
              },
              {
                "key": "Imports",
                "value": [
                  {
                    "key": "KERNEL32.DLL",
                    "value": [
                      "LoadLibraryA",
                      "ExitProcess",
                      "GetProcAddress",
                      "VirtualProtect"
                    ]
                  },
                  {
                    "key": "MSVCRT.dll",
                    "value": [
                      "free"
                    ]
                  }
                ]
              },
              {
                "key": "Resources",
                "value": [
                  {
                    "key": "1",
                    "value": {
                      "Codepage": "UNKNOWN",
                      "Entropy": "5.38843",
                      "Language": "UNKNOWN",
                      "Size": "1365",
                      "Type": "RT_MANIFEST"
                    }
                  },
                  {
                    "key": "2",
                    "value": {
                      "Codepage": "UNKNOWN",
                      "Entropy": "5.28933",
                      "Language": "English - United States",
                      "Size": "5160",
                      "Type": "RT_ICON"
                    }
                  },
                  {
                    "key": "3",
                    "value": {
                      "Codepage": "UNKNOWN",
                      "Entropy": "5.05971",
                      "Language": "English - United States",
                      "Size": "11560",
                      "Type": "RT_ICON"
                    }
                  },
                  {
                    "key": "4",
                    "value": {
                      "Codepage": "UNKNOWN",
                      "Detected Filetype": "PNG graphic file",
                      "Entropy": "7.98148",
                      "Language": "English - United States",
                      "Size": "40620",
                      "Type": "RT_ICON"
                    }
                  },
                  {
                    "key": "5",
                    "value": {
                      "Codepage": "UNKNOWN",
                      "Entropy": "6.59467",
                      "Language": "English - United States",
                      "Size": "136",
                      "Type": "RT_STRING"
                    }
                  },
                  {
                    "key": "97",
                    "value": {
                      "Codepage": "UNKNOWN",
                      "Entropy": "6.89291",
                      "Language": "English - United States",
                      "Size": "184",
                      "Type": "RT_DIALOG"
                    }
                  },
                  {
                    "key": "188",
                    "value": {
                      "Codepage": "UNKNOWN",
                      "Entropy": "6.06482",
                      "Language": "English - United States",
                      "Size": "84",
                      "Type": "RT_STRING"
                    }
                  },
                  {
                    "key": "207",
                    "value": {
                      "Codepage": "UNKNOWN",
                      "Entropy": "5.46967",
                      "Language": "English - United States",
                      "Size": "52",
                      "Type": "RT_STRING"
                    }
                  }
                ]
              },
              {
                "key": "Version Info",
                "value": [
                  {
                    "key": "Resource LangID",
                    "value": "English - United States"
                  },
                  {
                    "key": "VS_VERSION_INFO",
                    "value": {
                      "CompanyName": "Mozilla",
                      "FileDescription": "Firefox",
                      "FileFlags": [],
                      "FileOs": [
                        "VOS_DOS_WINDOWS32",
                        "VOS_NT",
                        "VOS_NT_WINDOWS32",
                        "VOS_WINCE",
                        "VOS__WINDOWS32"
                      ],
                      "FileType": "VFT_APP",
                      "FileVersion": "18.05",
                      "InternalName": "7zS.sfx",
                      "Language": "English - United States",
                      "LegalCopyright": "Mozilla",
                      "OriginalFilename": "7zS.sfx.exe",
                      "ProductName": "Firefox",
                      "ProductVersion": "18.05",
                      "Signature": "0xFEEF04BD",
                      "StructVersion": "0x00010000"
                    }
                  }
                ]
              }
            ],
            "trid": [
              {
                "extension": ".exe",
                "filetype": "UPX compressed Win32 Executable",
                "procent": 64.2
              },
              {
                "extension": ".dll",
                "filetype": "Win32 Dynamic Link Library (generic)",
                "procent": 15.6
              },
              {
                "extension": ".exe",
                "filetype": "Win32 Executable (generic)",
                "procent": 10.6
              },
              {
                "extension": ".exe",
                "filetype": "Generic Win/DOS Executable",
                "procent": 4.7
              },
              {
                "extension": ".exe",
                "filetype": "DOS Executable Generic",
                "procent": 4.7
              }
            ]
          },
          "permanentUrl": "https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/files/39dc46f5-c516-4f1e-966c-b03a56c01caf",
          "type": "file"
        },
        "pcap": {
          "permanentUrl": "https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/pcap",
          "present": true
        },
        "screenshots": [
          {
            "permanentUrl": "https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/screens/2def6256-a961-48b7-ba39-044cf5fefec9/image.jpeg",
            "thumbnailUrl": "https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/thumbnails/2def6256-a961-48b7-ba39-044cf5fefec9/image.jpeg",
            "time": 17633,
            "uuid": "2def6256-a961-48b7-ba39-044cf5fefec9"
          }
        ],
        "video": {
          "permanentUrl": "https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/mp4",
          "present": true
        }
      },
      "creation": 1587156254891,
      "creationText": "2020-04-17T20:44:14.891Z",
      "duration": 60,
      "options": {
        "additionalTime": 0,
        "automatization": {
          "uac": false
        },
        "fakeNet": false,
        "heavyEvasion": false,
        "hideSource": false,
        "mitm": false,
        "network": true,
        "presentation": false,
        "privacy": "bylink",
        "privateSample": false,
        "timeout": 60,
        "tor": {
          "geo": "fastest",
          "used": false
        },
        "video": true
      },
      "permanentUrl": "https://app.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc",
      "reports": {
        "HTML": "https://api.any.run/report/4649c7fc-5780-476a-86b0-b89e424339bc/summary/html",
        "IOC": "https://api.any.run/report/4649c7fc-5780-476a-86b0-b89e424339bc/ioc/json",
        "MISP": "https://api.any.run/report/4649c7fc-5780-476a-86b0-b89e424339bc/summary/misp",
        "graph": "https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/graph"
      },
      "sandbox": {
        "name": "ANY.RUN - Interactive Sandbox",
        "plan": {
          "name": "Tester"
        }
      },
      "scores": {
        "specs": {
          "autostart": false,
          "cpuOverrun": false,
          "crashedApps": false,
          "crashedTask": false,
          "debugOutput": false,
          "executableDropped": true,
          "exploitable": false,
          "injects": false,
          "lowAccess": false,
          "memOverrun": false,
          "multiprocessing": true,
          "networkLoader": false,
          "networkThreats": false,
          "notStarted": false,
          "privEscalation": false,
          "rebooted": false,
          "serviceLauncher": false,
          "spam": false,
          "staticDetections": false,
          "stealing": false,
          "suspStruct": true,
          "torUsed": false
        },
        "verdict": {
          "score": 100,
          "threatLevel": 2,
          "threatLevelText": "Malicious activity"
        }
      },
      "tags": [],
      "uuid": "4649c7fc-5780-476a-86b0-b89e424339bc"
    },
    "counters": {
      "files": {
        "malicious": 3,
        "suspicious": 0,
        "text": 0,
        "unknown": 0
      },
      "network": {
        "connections": 0,
        "dns": 0,
        "http": 0,
        "threats": 0
      },
      "processes": {
        "malicious": 2,
        "monitored": 2,
        "suspicious": 0,
        "total": 38
      },
      "registry": {
        "delete": 0,
        "read": 333,
        "total": 333,
        "write": 0
      }
    },
    "debugStrings": [],
    "environments": {
      "hotfixes": [
        {
          "title": "KB976902"
        },
        {
          "title": "KB4019990"
        },
        {
          "title": "KB2999226"
        },
        {
          "title": "KB2888049"
        },
        {
          "title": "KB2882822"
        },
        {
          "title": "KB2834140"
        },
        {
          "title": "KB2786081"
        },
        {
          "title": "KB2731771"
        },
        {
          "title": "KB2729094"
        },
        {
          "title": "KB2639308"
        },
        {
          "title": "KB2534111"
        },
        {
          "title": "KB2533623"
        },
        {
          "title": "UltimateEdition"
        },
        {
          "title": "ProfessionalEdition"
        },
        {
          "title": "PlatformUpdate Win7 SRV08R2 Package TopLevel"
        },
        {
          "title": "LocalPack ZA Package"
        },
        {
          "title": "LocalPack US Package"
        },
        {
          "title": "LocalPack GB Package"
        },
        {
          "title": "LocalPack CA Package"
        },
        {
          "title": "LocalPack AU Package"
        },
        {
          "title": "InternetExplorer Package TopLevel"
        },
        {
          "title": "InternetExplorer Optional Package"
        },
        {
          "title": "IE Troubleshooters Package"
        },
        {
          "title": "IE Spelling Parent Package English"
        },
        {
          "title": "IE Hyphenation Parent Package English"
        },
        {
          "title": "Foundation Package"
        },
        {
          "title": "CodecPack Basic Package"
        },
        {
          "title": "Client Refresh LanguagePack Package"
        },
        {
          "title": "Client LanguagePack Package"
        }
      ],
      "internetExplorer": {
        "kbnum": "KB3058515",
        "version": "11.0.9600.17843"
      },
      "os": {
        "bitness": 32,
        "build": 7601,
        "major": "7",
        "product": "Windows",
        "productType": "Client",
        "servicePack": "1",
        "softSet": "complete",
        "title": "Windows 7 Professional Service Pack 1 (build: 7601, 32 bit)",
        "variant": "Professional"
      },
      "software": [
        {
          "title": "Microsoft Visual C++ 2013 x86 Additional Runtime - 12.0.21005",
          "version": "12.0.21005"
        },
        {
          "title": "Microsoft Visual C++ 2013 Redistributable (x86) - 12.0.30501",
          "version": "12.0.30501.0"
        },
        {
          "title": "Microsoft Visual C++ 2010  x86 Redistributable - 10.0.40219",
          "version": "10.0.40219"
        },
        {
          "title": "Adobe Acrobat Reader DC MUI",
          "version": "15.023.20070"
        },
        {
          "title": "Adobe Refresh Manager",
          "version": "1.8.0"
        },
        {
          "title": "Microsoft Visual C++ 2008 Redistributable - x86 9.0.30729.6161",
          "version": "9.0.30729.6161"
        },
        {
          "title": "Update for Microsoft .NET Framework 4.7.2 (KB4087364)",
          "version": "1"
        },
        {
          "title": "Microsoft .NET Framework 4.7.2",
          "version": "4.7.03062"
        },
        {
          "title": "Microsoft Office Access Setup Metadata MUI (English) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office Shared Setup Metadata MUI (English) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office X MUI (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office X MUI (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office X MUI (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office X MUI (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office X MUI (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office X MUI (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office X MUI (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office X MUI (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office X MUI (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office O MUI (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office O MUI (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office O MUI (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office O MUI (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office O MUI (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office O MUI (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office O MUI (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office O MUI (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office O MUI (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Groove MUI (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Groove MUI (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office Groove MUI (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Groove MUI (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Groove MUI (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Groove MUI (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Groove MUI (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Groove MUI (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Groove MUI (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office OneNote MUI (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office OneNote MUI (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office OneNote MUI (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office OneNote MUI (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office OneNote MUI (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office OneNote MUI (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office OneNote MUI (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office OneNote MUI (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office OneNote MUI (English) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office OneNote MUI (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Shared MUI (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Shared MUI (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office Shared MUI (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Shared MUI (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Shared MUI (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Shared MUI (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Shared MUI (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Shared MUI (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Shared MUI (English) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office Shared MUI (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office InfoPath MUI (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office InfoPath MUI (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office InfoPath MUI (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office InfoPath MUI (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office InfoPath MUI (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office InfoPath MUI (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office InfoPath MUI (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office InfoPath MUI (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office InfoPath MUI (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Single Image 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office Proofing (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proofing (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office Proofing (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proofing (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proofing (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proofing (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proofing (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proofing (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proofing (English) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office Proofing (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office IME (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office IME (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proof (Spanish) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office Proof (Galician) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proof (Basque) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proof (Ukrainian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proof (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office Proof (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proof (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proof (Dutch) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proof (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proof (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proof (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proof (French) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office Proof (English) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office Proof (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proof (Catalan) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Proof (Arabic) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Word MUI (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Word MUI (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office Word MUI (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Word MUI (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Word MUI (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Word MUI (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Word MUI (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Word MUI (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Word MUI (English) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office Word MUI (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Outlook MUI (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Outlook MUI (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office Outlook MUI (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Outlook MUI (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Outlook MUI (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Outlook MUI (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Outlook MUI (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Outlook MUI (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Outlook MUI (English) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office Outlook MUI (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Publisher MUI (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Publisher MUI (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office Publisher MUI (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Publisher MUI (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Publisher MUI (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Publisher MUI (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Publisher MUI (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Publisher MUI (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Publisher MUI (English) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office Publisher MUI (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office PowerPoint MUI (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office PowerPoint MUI (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office PowerPoint MUI (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office PowerPoint MUI (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office PowerPoint MUI (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office PowerPoint MUI (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office PowerPoint MUI (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office PowerPoint MUI (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office PowerPoint MUI (English) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office PowerPoint MUI (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office SharePoint Designer MUI (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office SharePoint Designer MUI (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office SharePoint Designer MUI (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office SharePoint Designer MUI (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office SharePoint Designer MUI (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office SharePoint Designer MUI (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office SharePoint Designer MUI (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office SharePoint Designer MUI (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office SharePoint Designer MUI (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Excel MUI (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Excel MUI (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office Excel MUI (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Excel MUI (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Excel MUI (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Excel MUI (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Excel MUI (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Excel MUI (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Excel MUI (English) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office Excel MUI (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Access MUI (Spanish) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Access MUI (Turkish) 2010",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office Access MUI (Russian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Access MUI (Portuguese (Brazil)) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Access MUI (Korean) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Access MUI (Japanese) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Access MUI (Italian) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Access MUI (French) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Access MUI (English) 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office Access MUI (German) 2010",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Google Chrome",
          "version": "75.0.3770.100"
        },
        {
          "title": "Google Update Helper",
          "version": "1.3.34.7"
        },
        {
          "title": "Java Auto Updater",
          "version": "2.8.92.14"
        },
        {
          "title": "Microsoft Visual C++ 2015-2019 Redistributable (x86) - 14.21.27702",
          "version": "14.21.27702.2"
        },
        {
          "title": "Java 8 Update 92",
          "version": "8.0.920.14"
        },
        {
          "title": "Microsoft Visual C++ 2019 X86 Additional Runtime - 14.21.27702",
          "version": "14.21.27702"
        },
        {
          "title": "Microsoft Visual C++ 2019 X86 Minimum Runtime - 14.21.27702",
          "version": "14.21.27702"
        },
        {
          "title": "Microsoft Visual C++ 2013 x86 Minimum Runtime - 12.0.21005",
          "version": "12.0.21005"
        },
        {
          "title": "WinRAR 5.60 (32-bit)",
          "version": "5.60.0"
        },
        {
          "title": "VLC media player",
          "version": "2.2.6"
        },
        {
          "title": "Skype version 8.29",
          "version": "8.29"
        },
        {
          "title": "Opera 12.15",
          "version": "12.15.1748"
        },
        {
          "title": "Microsoft Office Professional 2010",
          "version": "14.0.6029.1000"
        },
        {
          "title": "Microsoft Office Language Pack 2010 - Turkish/Türkçe",
          "version": "14.0.4763.1013"
        },
        {
          "title": "Microsoft Office Language Pack 2010 - Russian/русский",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Language Pack 2010 - Portuguese/Português (Brasil)",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Language Pack 2010 - Korean/한국어",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Language Pack 2010 - Japanese/日本語",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Language Pack 2010 - Italian/Italiano",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Language Pack 2010 - French/Français",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Language Pack 2010 - Spanish/Español",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Microsoft Office Language Pack 2010 - German/Deutsch",
          "version": "14.0.4763.1000"
        },
        {
          "title": "Notepad++ (32-bit x86)",
          "version": "7.5.1"
        },
        {
          "title": "Mozilla Firefox 68.0.1 (x86 en-US)",
          "version": "68.0.1"
        },
        {
          "title": "FileZilla Client 3.36.0",
          "version": "3.36.0"
        },
        {
          "title": "CCleaner",
          "version": "5.35"
        },
        {
          "title": "Adobe Flash Player 26 PPAPI",
          "version": "26.0.0.131"
        },
        {
          "title": "Adobe Flash Player 26 NPAPI",
          "version": "26.0.0.131"
        },
        {
          "title": "Adobe Flash Player 26 ActiveX",
          "version": "26.0.0.131"
        }
      ]
    },
    "incidents": [
      {
        "count": 1,
        "desc": "Dropped",
        "events": [],
        "firstSeen": 1587156271952,
        "mitre": [],
        "process": "bc166dfd-6e6d-478a-82fc-8b04f5dd501d",
        "source": "drops",
        "threatLevel": 2,
        "title": "Application was dropped or rewritten from another process"
      },
      {
        "count": 17,
        "desc": "Dropped",
        "events": [],
        "firstSeen": 1587156271930,
        "mitre": [
          "T1129"
        ],
        "process": "bc166dfd-6e6d-478a-82fc-8b04f5dd501d",
        "source": "drops",
        "threatLevel": 2,
        "title": "Loads dropped or rewritten executable"
      },
      {
        "count": 1,
        "desc": "Installation",
        "events": [
          {
            "filename": "C:\\Users\\admin\\AppData\\Local\\Temp\\7zS48B57DC6\\setup-stub.exe",
            "md5": "00e2a6420dc88f8e72de0a5876a22b7e",
            "size": 426488,
            "time": 1587156270839
          }
        ],
        "firstSeen": 1587156270839,
        "mitre": [],
        "process": "0dcddb87-b2f9-43eb-bbd3-0fbeaf78f9a7",
        "source": "drops",
        "threatLevel": 1,
        "title": "Executable content was dropped or overwritten"
      },
      {
        "count": 2,
        "desc": "Installation",
        "events": [
          {
            "filename": "C:\\Users\\admin\\AppData\\Local\\Temp\\nsgE1FD.tmp\\UAC.dll",
            "md5": "113c5f02686d865bc9e8332350274fd1",
            "size": 18432,
            "time": 1587156271183
          },
          {
            "filename": "C:\\Users\\admin\\AppData\\Local\\Temp\\nsgE1FD.tmp\\System.dll",
            "md5": "17ed1c86bd67e78ade4712be48a7d2bd",
            "size": 11776,
            "time": 1587156271167
          }
        ],
        "firstSeen": 1587156271183,
        "mitre": [],
        "process": "bc166dfd-6e6d-478a-82fc-8b04f5dd501d",
        "source": "drops",
        "threatLevel": 1,
        "title": "Executable content was dropped or overwritten"
      }
    ],
    "mitre": [
      {
        "id": "T1129",
        "name": "Execution through Module Load",
        "phases": [
          "execution"
        ]
      }
    ],
    "modified": {
      "files": [
        {
          "filename": "C:\\Users\\admin\\AppData\\Local\\Temp\\nsgE1FD.tmp\\UAC.dll",
          "hashes": {
            "head_hash": "af8e997d1695590cf0c51e860c0ce700",
            "md5": "113c5f02686d865bc9e8332350274fd1",
            "sha1": "4fa4414666f8091e327adb4d81a98a0d6e2e254a",
            "sha256": "0d21041a1b5cd9f9968fc1d457c78a802c9c5a23f375327e833501b65bcd095d",
            "ssdeep": "192:5cdcpry0igQ1Ii1rzn6U4gbfW6irWP+vOg7XRSEi+OPLjte86jugnincl0Nr90Og:WqVibvTh4qnFP+OPEzinclP+"
          },
          "info": {
            "file": "application/x-dosexec"
          },
          "permanentUrl": "https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/files/da5e5597-61bb-434d-8049-2eeceb49c7aa",
          "process": "bc166dfd-6e6d-478a-82fc-8b04f5dd501d",
          "size": 18432,
          "threatLevel": "HIGH",
          "time": 1587156271183,
          "type": "executable"
        },
        {
          "filename": "C:\\Users\\admin\\AppData\\Local\\Temp\\nsgE1FD.tmp\\System.dll",
          "hashes": {
            "head_hash": "17ed1c86bd67e78ade4712be48a7d2bd",
            "md5": "17ed1c86bd67e78ade4712be48a7d2bd",
            "sha1": "1cc9fe86d6d6030b4dae45ecddce5907991c01a0",
            "sha256": "bd046e6497b304e4ea4ab102cab2b1f94ce09bde0eebba4c59942a732679e4eb",
            "ssdeep": "192:eY24sihno00Wfl97nH6T2enXwWobpWBTU4VtHT7dmN35Ol+Sl:E8QIl975eXqlWBrz7YLOl+"
          },
          "info": {
            "file": "application/x-dosexec"
          },
          "permanentUrl": "https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/files/5a26df0a-9f58-4707-9549-83eaad71773c",
          "process": "bc166dfd-6e6d-478a-82fc-8b04f5dd501d",
          "size": 11776,
          "threatLevel": "HIGH",
          "time": 1587156271167,
          "type": "executable"
        },
        {
          "filename": "C:\\Users\\admin\\AppData\\Local\\Temp\\7zS48B57DC6\\setup-stub.exe",
          "hashes": {
            "head_hash": "665f7cd5c6d976951b9296bd1721703c",
            "md5": "00e2a6420dc88f8e72de0a5876a22b7e",
            "sha1": "26dca592dc00c741e404cc86efd740c38862363a",
            "sha256": "a7d0b746d12c58a51986ed8cf1c64d97fa80c106c9004b7bf92e104a89cffda4",
            "ssdeep": "6144:OspNjlsl/dj7qZXBs1P7iqv9AEGRLq9mRX51h134jG4YO6T:Oc6IwP7igCEd98pl4i4Yj"
          },
          "info": {
            "file": "application/x-dosexec"
          },
          "permanentUrl": "https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/files/e33f9a2a-1b69-49bf-9fd1-a01378271a8b",
          "process": "0dcddb87-b2f9-43eb-bbd3-0fbeaf78f9a7",
          "size": 426488,
          "threatLevel": "HIGH",
          "time": 1587156270839,
          "type": "executable"
        },
        {
          "filename": "C:\\Users\\admin\\AppData\\Local\\Temp\\7zS48B57DC6\\postSigningData",
          "process": "0dcddb87-b2f9-43eb-bbd3-0fbeaf78f9a7",
          "size": 0,
          "time": 1587156270855
        }
      ],
      "registry": []
    },
    "network": {
      "connections": [],
      "dnsRequests": [],
      "httpRequests": [],
      "threats": []
    },
    "processes": [
      {
        "commandLine": "\"C:\\Users\\admin\\AppData\\Local\\Temp\\setup.exe\" ",
        "context": {
          "integrityLevel": "MEDIUM",
          "rebootNumber": 0,
          "userName": "admin"
        },
        "fileName": "setup.exe",
        "fileType": "DROPPED",
        "image": "C:\\Users\\admin\\AppData\\Local\\Temp\\setup.exe",
        "mainProcess": true,
        "modules": [
          {
            "image": "c:\\windows\\winsxs\\x86_microsoft.windows.common-controls_6595b64144ccf1df_6.0.7601.17514_none_41e6975e2bd6f2b2\\comctl32.dll",
            "time": 1587156270824
          },
          {
            "image": "c:\\windows\\system32\\oleaut32.dll",
            "time": 1587156270839
          },
          {
            "image": "c:\\windows\\system32\\rpcrt4.dll",
            "time": 1587156270839
          },
          {
            "image": "c:\\windows\\system32\\cryptbase.dll",
            "time": 1587156270839
          },
          {
            "image": "c:\\windows\\system32\\usp10.dll",
            "time": 1587156270808
          },
          {
            "image": "c:\\users\\admin\\appdata\\local\\temp\\setup.exe",
            "time": 1587156270792
          },
          {
            "image": "c:\\windows\\system32\\lpk.dll",
            "time": 1587156270808
          },
          {
            "image": "c:\\systemroot\\system32\\ntdll.dll",
            "time": 1587156270792
          },
          {
            "image": "c:\\windows\\system32\\user32.dll",
            "time": 1587156270792
          },
          {
            "image": "c:\\windows\\system32\\shlwapi.dll",
            "time": 1587156270824
          },
          {
            "image": "c:\\windows\\system32\\sechost.dll",
            "time": 1587156270839
          },
          {
            "image": "c:\\windows\\system32\\msctf.dll",
            "time": 1587156270808
          },
          {
            "image": "c:\\windows\\system32\\apphelp.dll",
            "time": 1587156270855
          },
          {
            "image": "c:\\windows\\system32\\kernel32.dll",
            "time": 1587156270792
          },
          {
            "image": "c:\\windows\\system32\\clbcatq.dll",
            "time": 1587156270839
          },
          {
            "image": "c:\\windows\\system32\\kernelbase.dll",
            "time": 1587156270792
          },
          {
            "image": "c:\\windows\\system32\\imm32.dll",
            "time": 1587156270808
          },
          {
            "image": "c:\\windows\\system32\\advapi32.dll",
            "time": 1587156270839
          },
          {
            "image": "c:\\users\\admin\\appdata\\local\\temp\\7zs48b57dc6\\setup-stub.exe",
            "time": 1587156270855
          },
          {
            "image": "c:\\windows\\system32\\uxtheme.dll",
            "time": 1587156270824
          },
          {
            "image": "c:\\windows\\system32\\ole32.dll",
            "time": 1587156270839
          },
          {
            "image": "c:\\windows\\system32\\msvcrt.dll",
            "time": 1587156270792
          },
          {
            "image": "c:\\windows\\system32\\gdi32.dll",
            "time": 1587156270792
          }
        ],
        "pid": 2948,
        "ppid": 372,
        "scores": {
          "dropped": false,
          "injected": false,
          "loadsSusp": false,
          "monitoringReason": "Main process",
          "specs": {
            "autoStart": false,
            "crashedApps": false,
            "debugOutput": false,
            "executableDropped": true,
            "exploitable": false,
            "injects": false,
            "knownThreat": false,
            "lowAccess": false,
            "network": false,
            "networkLoader": false,
            "privEscalation": false,
            "stealing": false
          },
          "verdict": {
            "score": 100,
            "threatLevel": 2,
            "threatLevelText": "Malicious activity"
          }
        },
        "status": "STILL RUNNING",
        "times": {
          "monitoringSince": 1587156270699,
          "start": 1587156270699
        },
        "uuid": "0dcddb87-b2f9-43eb-bbd3-0fbeaf78f9a7",
        "versionInfo": {
          "company": "Mozilla",
          "description": "Firefox",
          "version": "18.05"
        }
      },
      {
        "commandLine": ".\\setup-stub.exe",
        "context": {
          "integrityLevel": "MEDIUM",
          "rebootNumber": 0,
          "userName": "admin"
        },
        "droppedBy": [
          "0dcddb87-b2f9-43eb-bbd3-0fbeaf78f9a7"
        ],
        "fileName": "setup-stub.exe",
        "fileType": "DROPPED",
        "image": "C:\\Users\\admin\\AppData\\Local\\Temp\\7zS48B57DC6\\setup-stub.exe",
        "mainProcess": false,
        "modules": [
          {
            "image": "c:\\windows\\system32\\imm32.dll",
            "time": 1587156270917
          },
          {
            "image": "c:\\windows\\system32\\userenv.dll",
            "time": 1587156270917
          },
          {
            "image": "c:\\windows\\system32\\user32.dll",
            "time": 1587156270886
          },
          {
            "image": "c:\\windows\\system32\\advapi32.dll",
            "time": 1587156270902
          },
          {
            "image": "c:\\windows\\system32\\dwmapi.dll",
            "time": 1587156270933
          },
          {
            "image": "c:\\windows\\system32\\sspicli.dll",
            "time": 1587156271183
          },
          {
            "image": "c:\\systemroot\\system32\\ntdll.dll",
            "time": 1587156270886
          },
          {
            "image": "c:\\windows\\system32\\gdi32.dll",
            "time": 1587156270886
          },
          {
            "image": "c:\\windows\\system32\\oleaut32.dll",
            "time": 1587156270917
          },
          {
            "image": "c:\\windows\\system32\\apphelp.dll",
            "time": 1587156270933
          },
          {
            "image": "c:\\windows\\system32\\cryptbase.dll",
            "time": 1587156270933
          },
          {
            "image": "c:\\windows\\system32\\kernel32.dll",
            "time": 1587156270886
          },
          {
            "image": "c:\\windows\\system32\\shell32.dll",
            "time": 1587156270902
          },
          {
            "image": "c:\\windows\\system32\\rpcrt4.dll",
            "time": 1587156270902
          },
          {
            "image": "c:\\windows\\system32\\msctf.dll",
            "time": 1587156270917
          },
          {
            "image": "c:\\windows\\system32\\shdocvw.dll",
            "time": 1587156271167
          },
          {
            "image": "c:\\users\\admin\\appdata\\local\\temp\\nsge1fd.tmp\\uac.dll",
            "permanentUrl": "https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/files/da5e5597-61bb-434d-8049-2eeceb49c7aa",
            "time": 1587156271183
          },
          {
            "image": "c:\\users\\admin\\appdata\\local\\temp\\7zs48b57dc6\\setup-stub.exe",
            "time": 1587156271355
          },
          {
            "image": "c:\\windows\\system32\\shfolder.dll",
            "time": 1587156270933
          },
          {
            "image": "c:\\windows\\system32\\wldap32.dll",
            "time": 1587156270949
          },
          {
            "image": "c:\\windows\\system32\\mpr.dll",
            "time": 1587156271214
          },
          {
            "image": "c:\\windows\\system32\\secur32.dll",
            "time": 1587156271183
          },
          {
            "image": "c:\\windows\\system32\\ole32.dll",
            "time": 1587156270902
          },
          {
            "image": "c:\\windows\\system32\\oleacc.dll",
            "time": 1587156270933
          },
          {
            "image": "c:\\windows\\system32\\msvcrt.dll",
            "time": 1587156270902
          },
          {
            "image": "c:\\windows\\system32\\shlwapi.dll",
            "time": 1587156270902
          },
          {
            "image": "c:\\users\\admin\\appdata\\local\\temp\\nsge1fd.tmp\\system.dll",
            "permanentUrl": "https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/files/5a26df0a-9f58-4707-9549-83eaad71773c",
            "time": 1587156271183
          },
          {
            "image": "c:\\windows\\system32\\lpk.dll",
            "time": 1587156270886
          },
          {
            "image": "c:\\windows\\winsxs\\x86_microsoft.windows.common-controls_6595b64144ccf1df_6.0.7601.17514_none_41e6975e2bd6f2b2\\comctl32.dll",
            "time": 1587156270902
          },
          {
            "image": "c:\\windows\\system32\\kernelbase.dll",
            "time": 1587156270886
          },
          {
            "image": "c:\\windows\\system32\\setupapi.dll",
            "time": 1587156270917
          },
          {
            "image": "c:\\windows\\system32\\clbcatq.dll",
            "time": 1587156270933
          },
          {
            "image": "c:\\windows\\system32\\uxtheme.dll",
            "time": 1587156270917
          },
          {
            "image": "c:\\windows\\system32\\cfgmgr32.dll",
            "time": 1587156270917
          },
          {
            "image": "c:\\windows\\system32\\sechost.dll",
            "time": 1587156270902
          },
          {
            "image": "c:\\windows\\system32\\propsys.dll",
            "time": 1587156270933
          },
          {
            "image": "c:\\windows\\system32\\usp10.dll",
            "time": 1587156270886
          },
          {
            "image": "c:\\windows\\system32\\profapi.dll",
            "time": 1587156270917
          },
          {
            "image": "c:\\windows\\system32\\devobj.dll",
            "time": 1587156270917
          },
          {
            "image": "c:\\windows\\system32\\version.dll",
            "time": 1587156270933
          },
          {
            "image": "c:\\windows\\system32\\ntmarta.dll",
            "time": 1587156270949
          }
        ],
        "parentUUID": "0dcddb87-b2f9-43eb-bbd3-0fbeaf78f9a7",
        "pid": 3532,
        "ppid": 2948,
        "scores": {
          "dropped": false,
          "injected": false,
          "loadsSusp": false,
          "monitoringReason": "Child process",
          "specs": {
            "autoStart": false,
            "crashedApps": false,
            "debugOutput": false,
            "executableDropped": true,
            "exploitable": false,
            "injects": false,
            "knownThreat": false,
            "lowAccess": false,
            "network": false,
            "networkLoader": false,
            "privEscalation": false,
            "stealing": false
          },
          "verdict": {
            "score": 100,
            "threatLevel": 2,
            "threatLevelText": "Malicious activity"
          }
        },
        "status": "STILL RUNNING",
        "times": {
          "monitoringSince": 1587156270855,
          "start": 1587156270855
        },
        "uuid": "bc166dfd-6e6d-478a-82fc-8b04f5dd501d",
        "versionInfo": {
          "company": "Mozilla Corporation",
          "description": "Firefox Installer",
          "version": "63.0.3"
        }
      }
    ],
    "status": "done"
  }
}
```

#### Run Analysis

This action is used to run new analysis.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|env_bitness|int|32|False|Bitness of operation system|[32, 64]|32|
|env_os|string|windows|False|Operation system|['windows']|windows|
|env_type|string|complete|False|Environment preset type|['clean', 'office', 'complete']|complete|
|env_version|string|7|False|Version of OS|['vista', '7', '8.1', '10']|7|
|file|file|None|False|Malware file|None|{ "filename": "file.txt", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==" }|
|obj_ext_browser|string|None|False|Browser name, used only for "url" type|None|Google Chrome|
|obj_ext_cmd|string|None|False|Optional command line|None|bash /tmp/run|
|obj_ext_elevateprompt|boolean|True|False|Auto-accept UAC option|None|True|
|obj_ext_extension|boolean|True|False|Change extension to valid|None|True|
|obj_ext_startfolder|string|temp|False|Start object from|['desktop', 'home', 'downloads', 'appdata', 'temp', 'windows', 'root']|temp|
|obj_ext_useragent|string|None|False|User agent, used only for "download" type|None|Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0|
|obj_type|string|file|True|Type of new task|['file', 'url', 'download']|None|
|obj_url|string|None|False|URL, used only if "obj_type" is "url" or "download"|None|http://example.org|
|opt_kernel_heavyevasion|boolean|False|False|Heavy evasion option|None|False|
|opt_network_connect|boolean|True|False|Network connection state|None|True|
|opt_network_fakenet|boolean|False|False|FakeNet feature status|None|False|
|opt_network_geo|string|None|False|Geo location option|['fastest', 'AU', 'BR', 'DE', 'CH', 'FR', 'KR', 'US', 'RU', 'GB', 'IT']|fastest|
|opt_network_mitm|boolean|False|False|HTTPS MITM proxy option|None|False|
|opt_network_tor|boolean|False|False|TOR using|None|False|
|opt_privacy_hidesource|boolean|True|False|Option for hiding of source URL, used only for "download" type|None|True|
|opt_privacy_type|string|bylink|False|Privacy settings|['public', 'bylink', 'owner']|bylink|
|opt_timeout|integer|60|False|Timeout option, size range 10-660|None|60|

Example input:

```
{
      "file": {
        "content": "dGVzdAo=",
        "filename": "test.exe"
      },
      "obj_type": "file"
    }
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|uuid|string|False|Response task UUID|

Example output:

```
{
  "uuid": "0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### hashes

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Head Hash|string|True|Head hash|
|MD5|string|True|MD5 hash|
|SHA1|string|True|SHA1 hash|
|SHA256|string|True|SHA256 hash|
|Ssdeep|string|True|Ssdeep hash|

#### task

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Date|string|True|Task date|
|File|string|True|Task file url|
|Hashe|hashes|True|Task hashes|
|JSON|string|True|Task JSON url|
|MISP|string|True|Task MISP url|
|Name|string|True|Task name|
|PCap|string|True|Task PCAP url|
|Related|string|True|Task related url|
|Tags|[]string|True|Task tags|
|Verdict|string|True|Task verdict|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Any Run](https://any.run/)
* [Any Run documentation](https://any.run/api-documentation/)
