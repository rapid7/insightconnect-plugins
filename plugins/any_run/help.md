# Description

Analyze suspicious and malicious activities using the cloud-based malware analysis service

# Key Features

* Submit files for analysis
* Obtain analysis reports
* Search task history

# Requirements

* Requires an API Key or username and password combination

# Supported Product Versions

* Any.Run API 2025-11-05

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
|tasks|[]task|False|Task history|[{"related":"https://app.any.run/tasks/82ab98a6-b406-4ba5-8deb-...","json":"https://api.any.run/report/82ab98a6-b406-4ba5-8deb...","file":"https://content.any.run/tasks/82ab98a6-b406-4ba5-8...","hashes":{"head_hash":"0145ad575b213b1703cb94c6c3568a2e","md5":"926e6146fdb288e932a1846029ad07db","sha1":"fc73d7c62e324cad4240fbaf7a6d53716ecc4de7","sha256":"f6df99db2023558798d234f9c118497db8ec83da37682f8868...","ssdeep":"768:s+QiSf3rhTePO38fXbEmJS2Iro2wFW0kEeu:svXj5ePO3C..."},"misp":"https://api.any.run/report/82ab98a6-b406-4ba5-8deb...","name":"http://pastebin.com/raw/xGXyTALF","pcap":"https://content.any.run/tasks/82ab98a6-b406-4ba5-8...","tags":[],"verdict":"No threats detected","date":"2020-04-23T21:00:13.890Z"},{"date":"2020-04-20T02:14:11.452Z","file":"https://content.any.run/tasks/923fa62b-2689-4e6a-b...","hashes":{"sha256":"71f34b8bda00b54713e92cb8aee8c04a11ea5dea650b07f4b1...","ssdeep":"3:N1KdJMP2:CO2","head_hash":"780024dc16cb4331cdf98d18eb111bb4","md5":"780024dc16cb4331cdf98d18eb111bb4","sha1":"dfc3414b0e62c18787631322ae7a8c7489e845c9"},"json":"https://api.any.run/report/923fa62b-2689-4e6a-be76...","pcap":"https://content.any.run/tasks/923fa62b-2689-4e6a-b...","tags":[],"misp":"https://api.any.run/report/923fa62b-2689-4e6a-be76...","name":"http://clicnews.com","related":"https://app.any.run/tasks/923fa62b-2689-4e6a-be76-...","verdict":"Malicious activity"}]|
  
Example output:

```
{
  "tasks": [
    {
      "date": "2020-04-23T21:00:13.890Z",
      "file": "https://content.any.run/tasks/82ab98a6-b406-4ba5-8...",
      "hashes": {
        "head_hash": "0145ad575b213b1703cb94c6c3568a2e",
        "md5": "926e6146fdb288e932a1846029ad07db",
        "sha1": "fc73d7c62e324cad4240fbaf7a6d53716ecc4de7",
        "sha256": "f6df99db2023558798d234f9c118497db8ec83da37682f8868...",
        "ssdeep": "768:s+QiSf3rhTePO38fXbEmJS2Iro2wFW0kEeu:svXj5ePO3C..."
      },
      "json": "https://api.any.run/report/82ab98a6-b406-4ba5-8deb...",
      "misp": "https://api.any.run/report/82ab98a6-b406-4ba5-8deb...",
      "name": "http://pastebin.com/raw/xGXyTALF",
      "pcap": "https://content.any.run/tasks/82ab98a6-b406-4ba5-8...",
      "related": "https://app.any.run/tasks/82ab98a6-b406-4ba5-8deb-...",
      "tags": [],
      "verdict": "No threats detected"
    },
    {
      "date": "2020-04-20T02:14:11.452Z",
      "file": "https://content.any.run/tasks/923fa62b-2689-4e6a-b...",
      "hashes": {
        "head_hash": "780024dc16cb4331cdf98d18eb111bb4",
        "md5": "780024dc16cb4331cdf98d18eb111bb4",
        "sha1": "dfc3414b0e62c18787631322ae7a8c7489e845c9",
        "sha256": "71f34b8bda00b54713e92cb8aee8c04a11ea5dea650b07f4b1...",
        "ssdeep": "3:N1KdJMP2:CO2"
      },
      "json": "https://api.any.run/report/923fa62b-2689-4e6a-be76...",
      "misp": "https://api.any.run/report/923fa62b-2689-4e6a-be76...",
      "name": "http://clicnews.com",
      "pcap": "https://content.any.run/tasks/923fa62b-2689-4e6a-b...",
      "related": "https://app.any.run/tasks/923fa62b-2689-4e6a-be76-...",
      "tags": [],
      "verdict": "Malicious activity"
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
|reports|reports|False|Reports|{"analysis":{"content":{"mainObject":{"filename":"setup.exe","hashes":{"md5":"c4ab8765314fc770e3ee8ca0693df8f9","sha1":"0194f8c5364d1dad03a1fe6eaa0fd98a10accd9e","sha256":"9ed4502b2eb64dd0a4394e593cb3666e621e751c26d06f3dbb953808bf83536e","ssdeep":"6144:0mvr9RLcN0BvxoLjGRU4UUU3UUUD9rOAerhj4Dy6ZTab8QCuzkLyS0RliUFh:0mr9RUsJGjqU4UUU3UUUZa7NjP6pbhOp"},"info":{"exif":{"EXE":{"CharacterSet":"Unicode","CodeSize":65536,"CompanyName":"Mozilla","EntryPoint":"0x34310","FileDescription":"Firefox","FileFlags":"(none)","FileFlagsMask":"0x003f","FileOS":"Windows NT 32-bit","FileSubtype":0,"FileVersion":18.05,"FileVersionNumber":"18.5.0.0","ImageVersion":0,"InitializedDataSize":65536,"InternalName":"7zS.sfx","LanguageCode":"English (U.S.)","LegalCopyright":"Mozilla","LinkerVersion":6,"MachineType":"Intel 386 or later, and compatibles","OSVersion":4,"ObjectFileType":"Executable application","OriginalFileName":"7zS.sfx.exe","PEType":"PE32","ProductName":"Firefox","ProductVersion":18.05,"ProductVersionNumber":"18.5.0.0","Subsystem":"Windows GUI","SubsystemVersion":4,"TimeStamp":"2018:08:31 00:18:33+02:00","UninitializedDataSize":147456}},"ext":"exe","file":"PE32 executable (GUI) Intel 80386, for MS Windows, UPX compressed","mime":"application/x-dosexec","pe":[{"key":"Summary","value":[{"key":"Architecture","value":"IMAGE_FILE_MACHINE_I386"},{"key":"Subsystem","value":"IMAGE_SUBSYSTEM_WINDOWS_GUI"}]},{"key":"DOS Header","value":[{"key":"Magic number","value":"MZ"},{"key":"Bytes on last page of file","value":"0x0090"}]},{"key":"PE Header","value":[{"key":"Signature","value":"PE"},{"key":"Machine","value":"IMAGE_FILE_MACHINE_I386"},{"key":"Characteristics","value":["IMAGE_FILE_32BIT_MACHINE","IMAGE_FILE_EXECUTABLE_IMAGE","IMAGE_FILE_LINE_NUMS_STRIPPED","IMAGE_FILE_LOCAL_SYMS_STRIPPED","IMAGE_FILE_RELOCS_STRIPPED"]}]},{"key":"Image Optional Header","value":[{"key":"Magic","value":"PE32"},{"key":"LinkerVersion","value":"6.0"}]},{"key":"Sections","value":[{"key":"UPX0","value":{"Characteristics":["IMAGE_SCN_CNT_UNINITIALIZED_DATA","IMAGE_SCN_MEM_EXECUTE","IMAGE_SCN_MEM_READ","IMAGE_SCN_MEM_WRITE"],"Entropy":"0","NumberOfLineNumbers":"0","NumberOfRelocations":"0","PointerToLineNumbers":"0x00000000","PointerToRawData":"0x00000400","PointerToRelocations":"0x00000000","SizeOfRawData":"0x00000000","VirtualAddress":"0x00001000","VirtualSize":"0x00024000"}},{"key":"UPX1","value":{"Characteristics":["IMAGE_SCN_CNT_INITIALIZED_DATA","IMAGE_SCN_MEM_EXECUTE","IMAGE_SCN_MEM_READ","IMAGE_SCN_MEM_WRITE"],"Entropy":"7.89699","NumberOfLineNumbers":"0","NumberOfRelocations":"0","PointerToLineNumbers":"0x00000000","PointerToRawData":"0x00000400","PointerToRelocations":"0x00000000","SizeOfRawData":"0x0000F600","VirtualAddress":"0x00025000","VirtualSize":"0x00010000"}},{"key":".rsrc","value":{"Characteristics":["IMAGE_SCN_CNT_INITIALIZED_DATA","IMAGE_SCN_MEM_READ","IMAGE_SCN_MEM_WRITE"],"Entropy":"7.39743","NumberOfLineNumbers":"0","NumberOfRelocations":"0","PointerToLineNumbers":"0x00000000","PointerToRawData":"0x0000FA00","PointerToRelocations":"0x00000000","SizeOfRawData":"0x0000F200","VirtualAddress":"0x00035000","VirtualSize":"0x00010000"}}]},{"key":"Imports","value":[{"key":"KERNEL32.DLL","value":["LoadLibraryA","ExitProcess","GetProcAddress","VirtualProtect"]},{"key":"MSVCRT.dll","value":["free"]}]},{"key":"Resources","value":[{"key":"1","value":{"Codepage":"UNKNOWN","Entropy":"5.38843","Language":"UNKNOWN","Size":"1365","Type":"RT_MANIFEST"}},{"key":"2","value":{"Codepage":"UNKNOWN","Entropy":"5.28933","Language":"English - United States","Size":"5160","Type":"RT_ICON"}}]},{"key":"Version Info","value":[{"key":"Resource LangID","value":"English - United States"},{"key":"VS_VERSION_INFO","value":{"CompanyName":"Mozilla","FileDescription":"Firefox","FileFlags":[],"FileOs":["VOS_DOS_WINDOWS32","VOS_NT","VOS_NT_WINDOWS32","VOS_WINCE","VOS__WINDOWS32"],"FileType":"VFT_APP","FileVersion":"18.05","InternalName":"7zS.sfx","Language":"English - United States","LegalCopyright":"Mozilla","OriginalFilename":"7zS.sfx.exe","ProductName":"Firefox","ProductVersion":"18.05","Signature":"0xFEEF04BD","StructVersion":"0x00010000"}}]}],"trid":[{"extension":".exe","filetype":"UPX compressed Win32 Executable","procent":64.2},{"extension":".dll","filetype":"Win32 Dynamic Link Library (generic)","procent":15.6}]},"permanentUrl":"https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/files/39dc46f5-c516-4f1e-966c-b03a56c01caf","type":"file"},"pcap":{"permanentUrl":"https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/pcap","present":true},"screenshots":[{"permanentUrl":"https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/screens/2def6256-a961-48b7-ba39-044cf5fefec9/image.jpeg","thumbnailUrl":"https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/thumbnails/2def6256-a961-48b7-ba39-044cf5fefec9/image.jpeg","time":17633,"uuid":"2def6256-a961-48b7-ba39-044cf5fefec9"}],"video":{"permanentUrl":"https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/mp4","present":true}},"creation":1587156254891,"creationText":"2020-04-17T20:44:14.891Z","duration":60,"options":{"additionalTime":0,"automatization":{"uac":false},"fakeNet":false,"heavyEvasion":false,"hideSource":false,"mitm":false,"network":true,"presentation":false,"privacy":"bylink","privateSample":false,"timeout":60,"tor":{"geo":"fastest","used":false},"video":true},"permanentUrl":"https://app.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc","reports":{"HTML":"https://api.any.run/report/4649c7fc-5780-476a-86b0-b89e424339bc/summary/html","IOC":"https://api.any.run/report/4649c7fc-5780-476a-86b0-b89e424339bc/ioc/json","MISP":"https://api.any.run/report/4649c7fc-5780-476a-86b0-b89e424339bc/summary/misp","graph":"https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/graph"},"sandbox":{"name":"ANY.RUN - Interactive Sandbox","plan":{"name":"Tester"}},"scores":{"specs":{"autostart":false,"cpuOverrun":false,"crashedApps":false,"crashedTask":false,"debugOutput":false,"executableDropped":true,"exploitable":false,"injects":false,"lowAccess":false,"memOverrun":false,"multiprocessing":true,"networkLoader":false,"networkThreats":false,"notStarted":false,"privEscalation":false,"rebooted":false,"serviceLauncher":false,"spam":false,"staticDetections":false,"stealing":false,"suspStruct":true,"torUsed":false},"verdict":{"score":100,"threatLevel":2,"threatLevelText":"Malicious activity"}},"tags":[],"uuid":"4649c7fc-5780-476a-86b0-b89e424339bc"},"counters":{"files":{"malicious":3,"suspicious":0,"text":0,"unknown":0},"network":{"connections":0,"dns":0,"http":0,"threats":0},"processes":{"malicious":2,"monitored":2,"suspicious":0,"total":38},"registry":{"delete":0,"read":333,"total":333,"write":0}},"debugStrings":[],"environments":{"hotfixes":[{"title":"KB976902"},{"title":"KB4019990"}],"internetExplorer":{"kbnum":"KB3058515","version":"11.0.9600.17843"},"os":{"bitness":32,"build":7601,"major":"7","product":"Windows","productType":"Client","servicePack":"1","softSet":"complete","title":"Windows 7 Professional Service Pack 1 (build: 7601, 32 bit)","variant":"Professional"},"software":[{"title":"Microsoft Visual C++ 2013 x86 Additional Runtime - 12.0.21005","version":"12.0.21005"},{"title":"Microsoft Visual C++ 2013 Redistributable (x86) - 12.0.30501","version":"12.0.30501.0"}]},"incidents":[{"count":1,"desc":"Dropped","events":[],"firstSeen":1587156271952,"mitre":[],"process":"bc166dfd-6e6d-478a-82fc-8b04f5dd501d","source":"drops","threatLevel":2,"title":"Application was dropped or rewritten from another process"},{"count":17,"desc":"Dropped","events":[],"firstSeen":1587156271930,"mitre":["T1129"],"process":"bc166dfd-6e6d-478a-82fc-8b04f5dd501d","source":"drops","threatLevel":2,"title":"Loads dropped or rewritten executable"},{"count":1,"desc":"Installation","events":[{"filename":"C:\\Users\\admin\\AppData\\Local\\Temp\\7zS48B57DC6\\setup-stub.exe","md5":"00e2a6420dc88f8e72de0a5876a22b7e","size":426488,"time":1587156270839}],"firstSeen":1587156270839,"mitre":[],"process":"0dcddb87-b2f9-43eb-bbd3-0fbeaf78f9a7","source":"drops","threatLevel":1,"title":"Executable content was dropped or overwritten"},{"count":2,"desc":"Installation","events":[{"filename":"C:\\Users\\admin\\AppData\\Local\\Temp\\nsgE1FD.tmp\\UAC.dll","md5":"113c5f02686d865bc9e8332350274fd1","size":18432,"time":1587156271183},{"filename":"C:\\Users\\admin\\AppData\\Local\\Temp\\nsgE1FD.tmp\\System.dll","md5":"17ed1c86bd67e78ade4712be48a7d2bd","size":11776,"time":1587156271167}],"firstSeen":1587156271183,"mitre":[],"process":"bc166dfd-6e6d-478a-82fc-8b04f5dd501d","source":"drops","threatLevel":1,"title":"Executable content was dropped or overwritten"}],"mitre":[{"id":"T1129","name":"Execution through Module Load","phases":["execution"]}],"modified":{"files":[{"filename":"C:\\Users\\admin\\AppData\\Local\\Temp\\nsgE1FD.tmp\\UAC.dll","hashes":{"head_hash":"af8e997d1695590cf0c51e860c0ce700","md5":"113c5f02686d865bc9e8332350274fd1","sha1":"4fa4414666f8091e327adb4d81a98a0d6e2e254a","sha256":"0d21041a1b5cd9f9968fc1d457c78a802c9c5a23f375327e833501b65bcd095d","ssdeep":"192:5cdcpry0igQ1Ii1rzn6U4gbfW6irWP+vOg7XRSEi+OPLjte86jugnincl0Nr90Og:WqVibvTh4qnFP+OPEzinclP+"},"info":{"file":"application/x-dosexec"},"permanentUrl":"https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/files/da5e5597-61bb-434d-8049-2eeceb49c7aa","process":"bc166dfd-6e6d-478a-82fc-8b04f5dd501d","size":18432,"threatLevel":"HIGH","time":1587156271183,"type":"executable"},{"filename":"C:\\Users\\admin\\AppData\\Local\\Temp\\nsgE1FD.tmp\\System.dll","hashes":{"head_hash":"17ed1c86bd67e78ade4712be48a7d2bd","md5":"17ed1c86bd67e78ade4712be48a7d2bd","sha1":"1cc9fe86d6d6030b4dae45ecddce5907991c01a0","sha256":"bd046e6497b304e4ea4ab102cab2b1f94ce09bde0eebba4c59942a732679e4eb","ssdeep":"192:eY24sihno00Wfl97nH6T2enXwWobpWBTU4VtHT7dmN35Ol+Sl:E8QIl975eXqlWBrz7YLOl+"},"info":{"file":"application/x-dosexec"},"permanentUrl":"https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/files/5a26df0a-9f58-4707-9549-83eaad71773c","process":"bc166dfd-6e6d-478a-82fc-8b04f5dd501d","size":11776,"threatLevel":"HIGH","time":1587156271167,"type":"executable"},{"filename":"C:\\Users\\admin\\AppData\\Local\\Temp\\7zS48B57DC6\\setup-stub.exe","hashes":{"head_hash":"665f7cd5c6d976951b9296bd1721703c","md5":"00e2a6420dc88f8e72de0a5876a22b7e","sha1":"26dca592dc00c741e404cc86efd740c38862363a","sha256":"a7d0b746d12c58a51986ed8cf1c64d97fa80c106c9004b7bf92e104a89cffda4","ssdeep":"6144:OspNjlsl/dj7qZXBs1P7iqv9AEGRLq9mRX51h134jG4YO6T:Oc6IwP7igCEd98pl4i4Yj"},"info":{"file":"application/x-dosexec"},"permanentUrl":"https://content.any.run/tasks/4649c7fc-5780-476a-86b0-b89e424339bc/download/files/e33f9a2a-1b69-49bf-9fd1-a01378271a8b","process":"0dcddb87-b2f9-43eb-bbd3-0fbeaf78f9a7","size":426488,"threatLevel":"HIGH","time":1587156270839,"type":"executable"},{"filename":"C:\\Users\\admin\\AppData\\Local\\Temp\\7zS48B57DC6\\postSigningData","process":"0dcddb87-b2f9-43eb-bbd3-0fbeaf78f9a7","size":0,"time":1587156270855}],"registry":[]},"network":{"connections":[],"dnsRequests":[],"httpRequests":[],"threats":[]},"processes":[{"commandLine":"\"C:\\Users\\admin\\AppData\\Local\\Temp\\setup.exe\" ","context":{"integrityLevel":"MEDIUM","rebootNumber":0,"userName":"admin"},"fileName":"setup.exe","fileType":"DROPPED","image":"C:\\Users\\admin\\AppData\\Local\\Temp\\setup.exe","mainProcess":true,"modules":[{"image":"c:\\windows\\winsxs\\x86_microsoft.windows.common-controls_6595b64144ccf1df_6.0.7601.17514_none_41e6975e2bd6f2b2\\comctl32.dll","time":1587156270824},{"image":"c:\\windows\\system32\\oleaut32.dll","time":1587156270839}],"pid":2948,"ppid":372,"scores":{"dropped":false,"injected":false,"loadsSusp":false,"monitoringReason":"Main process","specs":{"autoStart":false,"crashedApps":false,"debugOutput":false,"executableDropped":true,"exploitable":false,"injects":false,"knownThreat":false,"lowAccess":false,"network":false,"networkLoader":false,"privEscalation":false,"stealing":false},"verdict":{"score":100,"threatLevel":2,"threatLevelText":"Malicious activity"}},"status":"STILL RUNNING","times":{"monitoringSince":1587156270699,"start":1587156270699},"uuid":"0dcddb87-b2f9-43eb-bbd3-0fbeaf78f9a7","versionInfo":{"company":"Mozilla","description":"Firefox","version":"18.05"}},{"commandLine":".\\setup-stub.exe","context":{"integrityLevel":"MEDIUM","rebootNumber":0,"userName":"admin"},"droppedBy":["0dcddb87-b2f9-43eb-bbd3-0fbeaf78f9a7"],"fileName":"setup-stub.exe","fileType":"DROPPED","image":"C:\\Users\\admin\\AppData\\Local\\Temp\\7zS48B57DC6\\setup-stub.exe","mainProcess":false,"modules":[{"image":"c:\\windows\\system32\\imm32.dll","time":1587156270917},{"image":"c:\\windows\\system32\\userenv.dll","time":1587156270917}],"parentUUID":"0dcddb87-b2f9-43eb-bbd3-0fbeaf78f9a7","pid":3532,"ppid":2948,"scores":{"dropped":false,"injected":false,"loadsSusp":false,"monitoringReason":"Child process","specs":{"autoStart":false,"crashedApps":false,"debugOutput":false,"executableDropped":true,"exploitable":false,"injects":false,"knownThreat":false,"lowAccess":false,"network":false,"networkLoader":false,"privEscalation":false,"stealing":false},"verdict":{"score":100,"threatLevel":2,"threatLevelText":"Malicious activity"}},"status":"STILL RUNNING","times":{"monitoringSince":1587156270855,"start":1587156270855},"uuid":"bc166dfd-6e6d-478a-82fc-8b04f5dd501d","versionInfo":{"company":"Mozilla Corporation","description":"Firefox Installer","version":"63.0.3"}}],"status":"done"}|
  
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
|uuid|string|False|Response task UUID|0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15|
  
Example output:

```
{
  "uuid": "0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15"
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
|UUID|string|None|False|Task UUID|None|
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
  
**incidents_mitre**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Sid|string|None|False|The signature ID used in detection|None|
|Tid|string|None|False|The technique ID of the MITRE ATT&CK technique associated with the incident|None|
|V|string|None|False|The version of the technique|None|
  
**incidents**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Count|integer|None|False|Count|None|
|Desc|string|None|False|Desc|None|
|Events|[]object|None|False|Events|None|
|Firstseen|integer|None|False|Firstseen|None|
|Mitre|[]incidents_mitre|None|False|Mitre|None|
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
|Tags|[]string|None|False|Tags|None|
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

* When configuring the connection, only one authentication method can be supplied. Enter an API key or the username and password combination

# Version History

* 2.0.0 - Actions: `Get Report` - Updated output schema types | Updated SDK to the latest version (6.3.10)
* 1.1.2 - Fix issue with file defaulting to Windows 7 32-Bit
* 1.1.1 - Fix issue with invalid inputs in Run Analysis action | Fix issue where Run Analysis action fails if optional inputs are provided as empty strings | Fix issue where Get Report action fails when fields in output contain `None` value | Improve error handling
* 1.1.0 - Allow user agent input when using URL type in Run Analysis action
* 1.0.0 - Initial plugin

# Links

* [Any Run](https://any.run/)

## References

* [Any Run](https://any.run/)
* [Any Run documentation](https://any.run/api-documentation/)