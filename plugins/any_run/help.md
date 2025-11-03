# Description

Analyze suspicious and malicious activities using the cloud-based malware analysis service

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* Any.Run API 2022-05-17

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|False|API key for Any.Run|None|WbTbwa4KFk77eQNffMJynWXm49jLwGjwPMKM9Xc4|None|None|
|credentials|credential_username_password|None|False|Username and password|None|{"username": "user@example.com", "password": "mypassword"}|None|None|

Example input:

```
{
  "api_key": "WbTbwa4KFk77eQNffMJynWXm49jLwGjwPMKM9Xc4",
  "credentials": {
    "password": "mypassword",
    "username": "user@example.com"
  }
}
```

## Technical Details

### Actions


#### Get Task History

This action is used to get task history

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|limit|integer|25|False|Limits number of records, Size range 1-100|None|25|None|None|
|skip|integer|0|False|Skip records|None|25|None|None|
|team|boolean|False|False|Leave this field blank to get your history or specify to get team history|None|False|None|None|
  
Example input:

```
{
  "limit": 25,
  "skip": 0,
  "team": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|tasks|[]task|False|Task history|None|
  
Example output:

```
{
  "tasks": [
    {
      "Date": {},
      "File": {},
      "Hashe": {
        "Head Hash": {},
        "MD5": {},
        "SHA1": {},
        "SHA256": {},
        "Ssdeep": {}
      },
      "JSON": {},
      "MISP": {},
      "Name": {},
      "PCAP": {},
      "Related": {},
      "Tags": "[\"suspicious\"]",
      "Verdict": "Malicious activity"
    }
  ]
}
```

#### Get Report

This action is used to get task report

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|task|string|None|True|Task UUID|None|0cf223f2-530e-4a50-b68f-563045268648|None|None|
  
Example input:

```
{
  "task": "0cf223f2-530e-4a50-b68f-563045268648"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reports|reports|False|Reports|None|
  
Example output:

```
{
  "reports": {
    "Analysis": {
      "Content": {
        "Mainobject": {
          "Filename": "",
          "Hashes": {
            "Head Hash": {},
            "MD5": {},
            "SHA1": {},
            "SHA256": {},
            "Ssdeep": {}
          },
          "Info": {
            "Exif": {
              "Exe": {
                "Characterset": {},
                "Codesize": 0,
                "Companyname": {},
                "Entrypoint": {},
                "Filedescription": {},
                "Fileflags": {},
                "Fileflagsmask": {},
                "Fileos": {},
                "Filesubtype": {},
                "Fileversion": 0.0,
                "Fileversionnumber": {},
                "Imageversion": {},
                "Initializeddatasize": {},
                "Internalname": {},
                "Languagecode": {},
                "Legalcopyright": {},
                "Linkerversion": {},
                "Machinetype": {},
                "Objectfiletype": {},
                "Originalfilename": {},
                "Osversion": {},
                "Petype": {},
                "Productname": {},
                "Productversion": {},
                "Productversionnumber": {},
                "Subsystem": {},
                "Subsystemversion": {},
                "Timestamp": {},
                "Uninitializeddatasize": {}
              }
            },
            "Ext": {},
            "File": {},
            "MIME": {},
            "Pe": [
              {
                "Key": {},
                "Value": [
                  {}
                ]
              }
            ],
            "Trid": [
              {
                "Extension": {},
                "Filetype": {},
                "Procent": {}
              }
            ]
          },
          "Permanenturl": {},
          "Type": {}
        },
        "PCAP": {
          "Permanenturl": {},
          "Present": "true"
        },
        "Screenshots": [
          {
            "Permanenturl": {},
            "Thumbnailurl": {},
            "Time": {},
            "UUID": {}
          }
        ],
        "Video": {}
      },
      "Creation": {},
      "Creationtext": {},
      "Duration": {},
      "Options": {
        "Additionaltime": {},
        "Automatization": {
          "Uac": {}
        },
        "Fakenet": {},
        "Heavyevasion": {},
        "Hidesource": {},
        "Mitm": {},
        "Network": {},
        "Presentation": {},
        "Privacy": {},
        "Privatesample": {},
        "Timeout": {},
        "Tor": {
          "Geo": {},
          "Used": {}
        },
        "Video": {}
      },
      "Permanenturl": {},
      "Reports": {},
      "Sandbox": {
        "Name": {},
        "Plan": {
          "Name": {}
        }
      },
      "Scores": {
        "Specs": {
          "Autostart": {},
          "Cpuoverrun": {},
          "Crashedapps": {},
          "Crashedtask": {},
          "Debugoutput": {},
          "Executabledropped": {},
          "Exploitable": {},
          "Injects": {},
          "Lowaccess": {},
          "Memoverrun": {},
          "Multiprocessing": {},
          "Networkloader": {},
          "Networkthreats": {},
          "Notstarted": {},
          "Privescalation": {},
          "Rebooted": {},
          "Servicelauncher": {},
          "Spam": {},
          "Staticdetections": {},
          "Stealing": {},
          "Suspstruct": {},
          "Torused": {}
        },
        "Verdict": {
          "Score": {},
          "Threatlevel": {},
          "Threatleveltext": {}
        }
      },
      "Tags": {},
      "UUID": {}
    },
    "Counters": {
      "Files": {
        "Malicious": {},
        "Suspicious": {},
        "Text": {},
        "Unknown": {}
      },
      "Network": {
        "Connections": {},
        "DNS": {},
        "HTTP": {},
        "Threats": {}
      },
      "Processes": {
        "Malicious": {},
        "Monitored": {},
        "Suspicious": {},
        "Total": {}
      },
      "Registry": {
        "Delete": {},
        "Read": {},
        "Total": {},
        "Write": {}
      }
    },
    "Debugstrings": {},
    "Environments": {
      "Hotfixes": [
        {
          "Title": {}
        }
      ],
      "Internetexplorer": {
        "Kbnum": {},
        "Version": {}
      },
      "Os": {
        "Bitness": {},
        "Build": {},
        "Major": {},
        "Product": {},
        "Producttype": {},
        "Servicepack": {},
        "Softset": {},
        "Title": {},
        "Variant": {}
      },
      "Software": [
        {
          "Title": {},
          "Version": {}
        }
      ]
    },
    "Incidents": [
      {
        "Count": {},
        "Desc": {},
        "Events": {},
        "Firstseen": {},
        "Mitre": [
          {}
        ],
        "Process": {},
        "Source": {},
        "Threatlevel": {},
        "Title": {}
      }
    ],
    "Mitre": [
      {
        "Id": {},
        "Name": {},
        "Phases": {}
      }
    ],
    "Modified": {
      "Files": [
        {
          "Filename": {},
          "Hashes": {
            "Head Hash": {},
            "MD5": {},
            "SHA1": {},
            "SHA256": {},
            "Ssdeep": {}
          },
          "Info": {
            "File": {}
          },
          "Permanenturl": {},
          "Process": {},
          "Size": {},
          "Threatlevel": {},
          "Time": {},
          "Type": {}
        }
      ],
      "Registry": {}
    },
    "Network": {
      "Connections": {},
      "DNS Requests": {},
      "HTTP Requests": {},
      "Threats": {}
    },
    "Processes": [
      {
        "Commandline": {},
        "Context": {
          "Integritylevel": {},
          "Rebootnumber": {},
          "Username": {}
        },
        "Filename": {},
        "Filetype": {},
        "Image": {},
        "Mainprocess": {},
        "Modules": [
          {
            "Image": {},
            "Time": {}
          }
        ],
        "PID": {},
        "Ppid": {},
        "Scores": {
          "Dropped": {},
          "Injected": {},
          "Loadssusp": {},
          "Monitoringreason": {},
          "Specs": {
            "Autostart": {},
            "Crashedapps": {},
            "Debugoutput": {},
            "Executabledropped": {},
            "Exploitable": {},
            "Injects": {},
            "Knownthreat": {},
            "Lowaccess": {},
            "Network": {},
            "Networkloader": {},
            "Privescalation": {},
            "Stealing": {}
          },
          "Verdict": {}
        },
        "Status": {},
        "Times": {
          "Monitoringsince": {},
          "Start": {}
        },
        "UUID": {},
        "Versioninfo": {
          "Company": {},
          "Description": {},
          "Version": {}
        }
      }
    ],
    "Status": {}
  }
}
```

#### Run Analysis

This action is used to run new analysis

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|env_bitness|int|32|False|Bitness of operating system|[32, 64]|32|None|None|
|env_os|string|windows|False|Operation system|["windows"]|windows|None|None|
|env_type|string|complete|False|Environment preset type|["clean", "office", "complete"]|complete|None|None|
|env_version|string|7|False|Version of OS|["vista", "7", "8.1", "10"]|7|None|None|
|file|file|None|False|Malware file|None|{"filename": "file.txt", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==" }|None|None|
|obj_ext_browser|string|None|False|Browser name, used only for "url" type. E.g. Internet Explorer, Google Chrome, Mozilla Firefox, Opera|None|Google Chrome|None|None|
|obj_ext_cmd|string|None|False|Optional command line that the VM will run. E.g. you can use 'RunDll32.EXE %FILENAME%,<func> <param>' to call a function by its name with a parameter in the uploaded sample. '%FILENAME%' is a built-in that will be automatically replaced with the file location in the environment|None|RunDll32.EXE %FILENAME%, func32 -r|None|None|
|obj_ext_elevateprompt|boolean|True|False|Auto-accept UAC option|None|True|None|None|
|obj_ext_extension|boolean|True|False|Change extension to valid|None|True|None|None|
|obj_ext_startfolder|string|temp|False|Start object from|["desktop", "home", "downloads", "appdata", "temp", "windows", "root"]|temp|None|None|
|obj_ext_useragent|string|None|False|User agent, used only for "download" and "url" types|None|Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0|None|None|
|obj_type|string|file|True|Type of new task|["file", "url", "download"]|file|None|None|
|obj_url|string|None|False|URL, used only if "obj_type" is "url" or "download"|None|http://example.org|None|None|
|opt_kernel_heavyevasion|boolean|False|False|Heavy evasion option|None|False|None|None|
|opt_network_connect|boolean|True|False|Network connection state|None|True|None|None|
|opt_network_fakenet|boolean|False|False|FakeNet feature status|None|False|None|None|
|opt_network_geo|string|None|False|Geo location option|["fastest", "AU", "BR", "DE", "CH", "FR", "KR", "US", "RU", "GB", "IT"]|fastest|None|None|
|opt_network_mitm|boolean|False|False|HTTPS MITM proxy option|None|False|None|None|
|opt_network_tor|boolean|False|False|TOR using|None|False|None|None|
|opt_privacy_hidesource|boolean|False|False|Option for hiding of source URL, used only for "download" type|None|False|None|None|
|opt_privacy_type|string|bylink|False|Privacy settings|["public", "bylink", "owner"]|bylink|None|None|
|opt_timeout|integer|60|False|Timeout option, size range 10-660|None|60|None|None|
  
Example input:

```
{
  "env_bitness": 32,
  "env_os": "windows",
  "env_type": "complete",
  "env_version": 7,
  "file": {
    "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
    "filename": "file.txt"
  },
  "obj_ext_browser": "Google Chrome",
  "obj_ext_cmd": "RunDll32.EXE %FILENAME%, func32 -r",
  "obj_ext_elevateprompt": true,
  "obj_ext_extension": true,
  "obj_ext_startfolder": "temp",
  "obj_ext_useragent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
  "obj_type": "file",
  "obj_url": "http://example.org",
  "opt_kernel_heavyevasion": false,
  "opt_network_connect": true,
  "opt_network_fakenet": false,
  "opt_network_geo": "fastest",
  "opt_network_mitm": false,
  "opt_network_tor": false,
  "opt_privacy_hidesource": false,
  "opt_privacy_type": "bylink",
  "opt_timeout": 60
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|uuid|string|False|Response task UUID|None|
  
Example output:

```
{
  "uuid": ""
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**hashes**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Head Hash|string|None|False|Head hash|None|
|MD5|string|None|False|MD5 hash|None|
|SHA1|string|None|False|SHA1 hash|None|
|SHA256|string|None|False|SHA256 hash|None|
|Ssdeep|string|None|False|Ssdeep hash|None|
  
**task**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Date|string|None|True|Task date|2020-04-17 18:44:37.483000+00:00|
|File|string|None|True|Task file URL|https://content.any.run/tasks/0cb5990e-7858-4455-a5f8-8d704051901b/download/files/005d7277-b4c1-4b96-bcd9-ac02b799eec9|
|Hashe|hashes|None|True|Task hashes|None|
|JSON|string|None|True|Task JSON URL|https://api.any.run/report/0cb5990e-7858-4455-a5f8-8d704051901b/summary/json|
|MISP|string|None|True|Task MISP URL|https://api.any.run/report/0cb5990e-7858-4455-a5f8-8d704051901b/summary/misp|
|Name|string|None|True|Task name|setup.exe|
|PCAP|string|None|True|Task PCAP URL|https://content.any.run/tasks/0cb5990e-7858-4455-a5f8-8d704051901b/download/pcap|
|Related|string|None|True|Task related URL|https://app.any.run/tasks/0cb5990e-7858-4455-a5f8-8d704051901b|
|Tags|[]string|None|True|Task tags|["suspicious"]|
|Verdict|string|None|True|Task verdict|Malicious activity|
  
**EXE**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Characterset|string|None|False|Characterset|None|
|Codesize|integer|None|False|Codesize|None|
|Companyname|string|None|False|Companyname|None|
|Entrypoint|string|None|False|Entrypoint|None|
|Filedescription|string|None|False|Filedescription|None|
|Fileflags|string|None|False|Fileflags|None|
|Fileflagsmask|string|None|False|Fileflagsmask|None|
|Fileos|string|None|False|Fileos|None|
|Filesubtype|integer|None|False|Filesubtype|None|
|Fileversion|float|None|False|Fileversion|None|
|Fileversionnumber|string|None|False|Fileversionnumber|None|
|Imageversion|integer|None|False|Imageversion|None|
|Initializeddatasize|integer|None|False|Initializeddatasize|None|
|Internalname|string|None|False|Internalname|None|
|Languagecode|string|None|False|Languagecode|None|
|Legalcopyright|string|None|False|Legalcopyright|None|
|Linkerversion|integer|None|False|Linkerversion|None|
|Machinetype|string|None|False|Machinetype|None|
|Osversion|integer|None|False|Osversion|None|
|Objectfiletype|string|None|False|Objectfiletype|None|
|Originalfilename|string|None|False|Originalfilename|None|
|Petype|string|None|False|Petype|None|
|Productname|string|None|False|Productname|None|
|Productversion|float|None|False|Productversion|None|
|Productversionnumber|string|None|False|Productversionnumber|None|
|Subsystem|string|None|False|Subsystem|None|
|Subsystemversion|integer|None|False|Subsystemversion|None|
|Timestamp|string|None|False|Timestamp|None|
|Uninitializeddatasize|integer|None|False|Uninitializeddatasize|None|
  
**exif**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Exe|EXE|None|False|Exe|None|
  
**pe**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Key|string|None|False|Key|None|
|Value|[]object|None|False|Value|None|
  
**trid**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Extension|string|None|False|Extension|None|
|Filetype|string|None|False|Filetype|None|
|Procent|float|None|False|Procent|None|
  
**info**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Exif|exif|None|False|Exif|None|
|Ext|string|None|False|Ext|None|
|File|string|None|False|File|None|
|MIME|string|None|False|MIME|None|
|Pe|[]pe|None|False|Pe|None|
|Trid|[]trid|None|False|Trid|None|
  
**mainObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Filename|string|None|False|Filename|None|
|Hashes|hashes|None|False|Hashes|None|
|Info|info|None|False|Info|None|
|Permanenturl|string|None|False|Permanenturl|None|
|Type|string|None|False|Type|None|
  
**pcap**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Permanenturl|string|None|False|Permanenturl|None|
|Present|boolean|None|False|Present|None|
  
**screenshots**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Permanenturl|string|None|False|Permanenturl|None|
|Thumbnailurl|string|None|False|Thumbnailurl|None|
|Time|integer|None|False|Time|None|
|UUID|string|None|False|UUID|None|
  
**automatization**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Uac|boolean|None|False|Uac|None|
  
**tor**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Geo|string|None|False|Geo|None|
|Used|boolean|None|False|Used|None|
  
**options**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Additionaltime|integer|None|False|Additionaltime|None|
|Automatization|automatization|None|False|Automatization|None|
|Fakenet|boolean|None|False|Fakenet|None|
|Heavyevasion|boolean|None|False|Heavyevasion|None|
|Hidesource|boolean|None|False|Hidesource|None|
|Mitm|boolean|None|False|Mitm|None|
|Network|boolean|None|False|Network|None|
|Presentation|boolean|None|False|Presentation|None|
|Privacy|string|None|False|Privacy|None|
|Privatesample|boolean|None|False|Privatesample|None|
|Timeout|integer|None|False|Timeout|None|
|Tor|tor|None|False|Tor|None|
|Video|boolean|None|False|Video|None|
  
**content**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Mainobject|mainObject|None|False|Mainobject|None|
|PCAP|pcap|None|False|PCAP|None|
|Screenshots|[]screenshots|None|False|Screenshots|None|
|Video|pcap|None|False|Video|None|
  
**plan**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name|None|
  
**sandbox**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name|None|
|Plan|plan|None|False|Plan|None|
  
**specs**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Autostart|boolean|None|False|Autostart|None|
|Cpuoverrun|boolean|None|False|Cpuoverrun|None|
|Crashedapps|boolean|None|False|Crashedapps|None|
|Crashedtask|boolean|None|False|Crashedtask|None|
|Debugoutput|boolean|None|False|Debugoutput|None|
|Executabledropped|boolean|None|False|Executabledropped|None|
|Exploitable|boolean|None|False|Exploitable|None|
|Injects|boolean|None|False|Injects|None|
|Lowaccess|boolean|None|False|Lowaccess|None|
|Memoverrun|boolean|None|False|Memoverrun|None|
|Multiprocessing|boolean|None|False|Multiprocessing|None|
|Networkloader|boolean|None|False|Networkloader|None|
|Networkthreats|boolean|None|False|Networkthreats|None|
|Notstarted|boolean|None|False|Notstarted|None|
|Privescalation|boolean|None|False|Privescalation|None|
|Rebooted|boolean|None|False|Rebooted|None|
|Servicelauncher|boolean|None|False|Servicelauncher|None|
|Spam|boolean|None|False|Spam|None|
|Staticdetections|boolean|None|False|Staticdetections|None|
|Stealing|boolean|None|False|Stealing|None|
|Suspstruct|boolean|None|False|Suspstruct|None|
|Torused|boolean|None|False|Torused|None|
  
**verdict**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Score|integer|None|False|Score|None|
|Threatlevel|integer|None|False|Threatlevel|None|
|Threatleveltext|string|None|False|Threatleveltext|None|
  
**scores**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Specs|specs|None|False|Specs|None|
|Verdict|verdict|None|False|Verdict|None|
  
**files**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Malicious|integer|None|False|Malicious|None|
|Suspicious|integer|None|False|Suspicious|None|
|Text|integer|None|False|Text|None|
|Unknown|integer|None|False|Unknown|None|
  
**network**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Connections|integer|None|False|Connections|None|
|DNS|integer|None|False|DNS|None|
|HTTP|integer|None|False|HTTP|None|
|Threats|integer|None|False|Threats|None|
  
**processes**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Malicious|integer|None|False|Malicious|None|
|Monitored|integer|None|False|Monitored|None|
|Suspicious|integer|None|False|Suspicious|None|
|Total|integer|None|False|Total|None|
  
**registry**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Delete|integer|None|False|Delete|None|
|Read|integer|None|False|Read|None|
|Total|integer|None|False|Total|None|
|Write|integer|None|False|Write|None|
  
**counters**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Files|files|None|False|Files|None|
|Network|network|None|False|Network|None|
|Processes|processes|None|False|Processes|None|
|Registry|registry|None|False|Registry|None|
  
**hotfixes**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Title|string|None|False|Title|None|
  
**internetExplorer**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Kbnum|string|None|False|Kbnum|None|
|Version|string|None|False|Version|None|
  
**os**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Bitness|integer|None|False|Bitness|None|
|Build|integer|None|False|Build|None|
|Major|string|None|False|Major|None|
|Product|string|None|False|Product|None|
|Producttype|string|None|False|Producttype|None|
|Servicepack|string|None|False|Servicepack|None|
|Softset|string|None|False|Softset|None|
|Title|string|None|False|Title|None|
|Variant|string|None|False|Variant|None|
  
**software**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Title|string|None|False|Title|None|
|Version|string|None|False|Version|None|
  
**environments**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Hotfixes|[]hotfixes|None|False|Hotfixes|None|
|Internetexplorer|internetExplorer|None|False|Internetexplorer|None|
|Os|os|None|False|Os|None|
|Software|[]software|None|False|Software|None|
  
**incidents**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Count|integer|None|False|Count|None|
|Desc|string|None|False|Desc|None|
|Events|[]object|None|False|Events|None|
|Firstseen|integer|None|False|Firstseen|None|
|Mitre|[]string|None|False|Mitre|None|
|Process|string|None|False|Process|None|
|Source|string|None|False|Source|None|
|Threatlevel|integer|None|False|Threatlevel|None|
|Title|string|None|False|Title|None|
  
**mitre**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Id|string|None|False|Id|None|
|Name|string|None|False|Name|None|
|Phases|[]string|None|False|Phases|None|
  
**hashes_0**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Head Hash|string|None|False|Head hash|None|
|MD5|string|None|False|MD5|None|
|SHA1|string|None|False|SHA1|None|
|SHA256|string|None|False|SHA256|None|
|Ssdeep|string|None|False|Ssdeep|None|
  
**info_0**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|File|string|None|False|File|None|
  
**files_0**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Filename|string|None|False|Filename|None|
|Hashes|hashes_0|None|False|Hashes|None|
|Info|info_0|None|False|Info|None|
|Permanenturl|string|None|False|Permanenturl|None|
|Process|string|None|False|Process|None|
|Size|integer|None|False|Size|None|
|Threatlevel|string|None|False|Threatlevel|None|
|Time|integer|None|False|Time|None|
|Type|string|None|False|Type|None|
  
**modified**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Files|[]files_0|None|False|Files|None|
|Registry|[]object|None|False|Registry|None|
  
**network_0**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Connections|[]object|None|False|Connections|None|
|DNS Requests|[]object|None|False|DNS requests|None|
|HTTP Requests|[]object|None|False|HTTP requests|None|
|Threats|[]object|None|False|Threats|None|
  
**context**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Integritylevel|string|None|False|Integritylevel|None|
|Rebootnumber|integer|None|False|Rebootnumber|None|
|Username|string|None|False|Username|None|
  
**modules**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Image|string|None|False|Image|None|
|Time|integer|None|False|Time|None|
  
**specs_0**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Autostart|boolean|None|False|Autostart|None|
|Crashedapps|boolean|None|False|Crashedapps|None|
|Debugoutput|boolean|None|False|Debugoutput|None|
|Executabledropped|boolean|None|False|Executabledropped|None|
|Exploitable|boolean|None|False|Exploitable|None|
|Injects|boolean|None|False|Injects|None|
|Knownthreat|boolean|None|False|Knownthreat|None|
|Lowaccess|boolean|None|False|Lowaccess|None|
|Network|boolean|None|False|Network|None|
|Networkloader|boolean|None|False|Networkloader|None|
|Privescalation|boolean|None|False|Privescalation|None|
|Stealing|boolean|None|False|Stealing|None|
  
**scores_0**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Dropped|boolean|None|False|Dropped|None|
|Injected|boolean|None|False|Injected|None|
|Loadssusp|boolean|None|False|Loadssusp|None|
|Monitoringreason|string|None|False|Monitoringreason|None|
|Specs|specs_0|None|False|Specs|None|
|Verdict|verdict|None|False|Verdict|None|
  
**times**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Monitoringsince|integer|None|False|Monitoringsince|None|
|Start|integer|None|False|Start|None|
  
**versionInfo**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Company|string|None|False|Company|None|
|Description|string|None|False|Description|None|
|Version|string|None|False|Version|None|
  
**processes_0**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Commandline|string|None|False|Commandline|None|
|Context|context|None|False|Context|None|
|Filename|string|None|False|Filename|None|
|Filetype|string|None|False|Filetype|None|
|Image|string|None|False|Image|None|
|Mainprocess|boolean|None|False|Mainprocess|None|
|Modules|[]modules|None|False|Modules|None|
|PID|integer|None|False|PID|None|
|Ppid|integer|None|False|Ppid|None|
|Scores|scores_0|None|False|Scores|None|
|Status|string|None|False|Status|None|
|Times|times|None|False|Times|None|
|UUID|string|None|False|UUID|None|
|Versioninfo|versionInfo|None|False|Versioninfo|None|
  
**analysis**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Content|content|None|False|Content|None|
|Creation|integer|None|False|Creation|None|
|Creationtext|string|None|False|Creationtext|None|
|Duration|integer|None|False|Duration|None|
|Options|options|None|False|Options|None|
|Permanenturl|string|None|False|Permanenturl|None|
|Reports|object|None|False|Reports|None|
|Sandbox|sandbox|None|False|Sandbox|None|
|Scores|scores|None|False|Scores|None|
|Tags|[]object|None|False|Tags|None|
|UUID|string|None|False|UUID|None|
  
**reports**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Analysis|analysis|None|False|Analysis|None|
|Counters|counters|None|False|Counters|None|
|Debugstrings|[]object|None|False|Debugstrings|None|
|Environments|environments|None|False|Environments|None|
|Incidents|[]incidents|None|False|Incidents|None|
|Mitre|[]mitre|None|False|Mitre|None|
|Modified|modified|None|False|Modified|None|
|Network|network_0|None|False|Network|None|
|Processes|[]processes_0|None|False|Processes|None|
|Status|string|None|False|Status|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History
  
*This plugin does not contain a version history.*

# Links
  
*This plugin does not contain any links.*

## References
  
*This plugin does not contain any references.*