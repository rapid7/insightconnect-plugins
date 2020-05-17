## Assessment
### Run

<details>

```
{
  "Data": {
    "Code": 0,
    "CodeType": 1,
    "Data": {
      "content": [
        {
          "content": {
            "agentEntity": [
              {
                "agentGuid": "626dcf14-b0c3-4b00-bc76-71cf5713ab2e",
                "ip": "10.0.2.15",
                "isEnable": true,
                "isImportant": false,
                "isOnline": true,
                "isolateStatus": 1,
                "machineGuid": "3E4EC062-A620-4DE6-9DA9-395DD98EC1D8",
                "machineName": "TREND-MICRO-TES",
                "machineOS": "Windows 10",
                "machineType": "Desktop",
                "productType": 15,
                "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
                "userGuid": "6AC1B3DCF-CE52-8279-EE9E-E101FD504E3",
                "userName": "TREND-MICRO-TES\\vagrant"
              }
            ],
            "agentQueryStatus": {
              "hasFullAgents": true,
              "hasFullRbac": true
            },
            "pagination": {
              "limit": 50,
              "offset": 0,
              "total": 1
            }
          },
          "message": "Success",
          "statusCode": 0
        }
      ],
      "hasMore": false
    },
    "Message": "OK",
    "TimeZone": -4
  },
  "FeatureCtrl": {
    "mode": "0"
  },
  "Meta": {
    "errorCode": 0,
    "errorMessgae": "Success",
    "result": 1
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/01_agent_list.json
</summary>
</details>

<details>

```
{
  "Data": {
    "Code": 0,
    "CodeType": 1,
    "Data": {
      "content": [
        {
          "content": {
            "agentEntity": [
              {
                "agentGuid": "626dcf14-b0c3-4b00-bc76-71cf5713ab2e",
                "ip": "10.0.2.15",
                "isEnable": true,
                "isImportant": false,
                "isOnline": true,
                "isolateStatus": 1,
                "machineGuid": "3E4EC062-A620-4DE6-9DA9-395DD98EC1D8",
                "machineName": "TREND-MICRO-TES",
                "machineOS": "Windows 10",
                "machineType": "Desktop",
                "productType": 15,
                "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
                "userGuid": "6AC1B3DCF-CE52-8279-EE9E-E101FD504E3",
                "userName": "TREND-MICRO-TES\\vagrant"
              }
            ],
            "agentQueryStatus": {
              "hasFullAgents": true,
              "hasFullRbac": true
            },
            "pagination": {
              "limit": 50,
              "offset": 0,
              "total": 1
            }
          },
          "message": "Success",
          "statusCode": 0
        }
      ],
      "hasMore": false
    },
    "Message": "OK",
    "TimeZone": -4
  },
  "FeatureCtrl": {
    "mode": "0"
  },
  "Meta": {
    "errorCode": 0,
    "errorMessgae": "Success",
    "result": 1
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/02_agent_list_with_filter.json
</summary>
</details>

<details>

```
{
  "Data": {
    "Code": 0,
    "CodeType": 1,
    "Data": {
      "content": [
        {
          "content": {
            "agentEntity": [
              {
                "agentGuid": "626dcf14-b0c3-4b00-bc76-71cf5713ab2e",
                "ip": "10.0.2.15",
                "isEnable": true,
                "isImportant": false,
                "isOnline": true,
                "isolateStatus": 1,
                "machineGuid": "3E4EC062-A620-4DE6-9DA9-395DD98EC1D8",
                "machineName": "TREND-MICRO-TES",
                "machineOS": "Windows 10",
                "machineType": "Desktop",
                "productType": 15,
                "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
                "userGuid": "6AC1B3DCF-CE52-8279-EE9E-E101FD504E3",
                "userName": "TREND-MICRO-TES\\vagrant"
              }
            ],
            "agentQueryStatus": {
              "hasFullAgents": true,
              "hasFullRbac": true
            },
            "pagination": {
              "limit": 50,
              "offset": 0,
              "total": 1
            }
          },
          "message": "Success",
          "statusCode": 0
        }
      ],
      "hasMore": false
    },
    "Message": "OK",
    "TimeZone": -4
  },
  "FeatureCtrl": {
    "mode": "0"
  },
  "Meta": {
    "errorCode": 0,
    "errorMessgae": "Success",
    "result": 1
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/03_agent_list_with_pagination.json
</summary>
</details>

<details>

```
{
  "FeatureCtrl": {
    "mode": "0"
  },
  "Meta": {
    "ErrorCode": 0,
    "Result": 1
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  },
  "uploaded_info_list": [
    {
      "FileHashID": "cd9b739b7c6e488080412e9a831e9260a468564f",
      "FileName": "file.txt",
      "UploadedStatus": 1
    }
  ],
  "uploaded_message_list": [
    {
      "Message": "Uploaded 1 OpenIOC file(s) successfully.",
      "MessageType": 1
    }
  ]
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/04_upload_openioc_file.json
</summary>
</details>

<details>

```
{
  "Data": {
    "FileContentBase64": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXMtYXNjaWkiPz4NCjxpb2MgeG1sbnM6eHNpPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZSIgeG1sbnM6eHNkPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYSIgaWQ9ImExM2UyODJkLTY1ZTEtNDI2My05YjMxLTVmOTEyNTE1Mjg4YyIgbGFzdC1tb2RpZmllZD0iMjAxMy0xMC0zMFQxOTowNzo0NiIgeG1sbnM9Imh0dHA6Ly9zY2hlbWFzLm1hbmRpYW50LmNvbS8yMDEwL2lvYyI+DQogIDxzaG9ydF9kZXNjcmlwdGlvbj5DcnlwdG9sb2NrZXIgRGV0ZWN0aW9uIChFWFBFUklNRU5UQUwpPC9zaG9ydF9kZXNjcmlwdGlvbj4NCiAgPGRlc2NyaXB0aW9uPlRoaXMgSU9DIGRldGVjdHMgcmVnaXN0cnkgZW50cmllcyBjcmVhdGVkIHdoZW4gdGhlIENyeXB0b2xvY2tlciBjcmltZXdhcmUgcnVucy4gUHJlc2VuY2Ugb2Ygb25lIG9mIHRoZXNlIHJlZ2lzdHJ5IGtleSBzaG93cyB0aGF0IGEgYm94IGhhcyBsaWtlbHkgYmVlbiBpbmZlY3RlZCB3aXRoIHRoZSBDcnlwdG9sb2NrZXIgc29mdHdhcmUuPC9kZXNjcmlwdGlvbj4NCiAgPGF1dGhvcmVkX2J5Pk1hbmRpYW50PC9hdXRob3JlZF9ieT4NCiAgPGF1dGhvcmVkX2RhdGU+MjAxMy0xMC0yOFQxNDoyNzoxMjwvYXV0aG9yZWRfZGF0ZT4NCiAgPGxpbmtzPg0KICAgIDxsaW5rIHJlbD0iZ3JhZGUiPnVudGVzdGVkPC9saW5rPg0KICA8L2xpbmtzPg0KICA8ZGVmaW5pdGlvbj4NCiAgICA8SW5kaWNhdG9yIG9wZXJhdG9yPSJPUiIgaWQ9IjdlYTYwNWI3LThhYjEtNGUxYy05MTI4LTk5OTI2NWNkOWYyMSI+DQogICAgICA8SW5kaWNhdG9ySXRlbSBpZD0iYTcxZWIwZDctYWZlNS00NzA4LThkYmItMzc5YmQ0M2NjOWQ3IiBjb25kaXRpb249ImNvbnRhaW5zIj4NCiAgICAgICAgPENvbnRleHQgZG9jdW1lbnQ9IlJlZ2lzdHJ5SXRlbSIgc2VhcmNoPSJSZWdpc3RyeUl0ZW0vUGF0aCIgdHlwZT0ibWlyIiAvPg0KICAgICAgICA8Q29udGVudCB0eXBlPSJzdHJpbmciPlNvZnR3YXJlXENyeXB0b0xvY2tlclxGaWxlczwvQ29udGVudD4NCiAgICAgIDwvSW5kaWNhdG9ySXRlbT4NCiAgICAgIDxJbmRpY2F0b3Igb3BlcmF0b3I9IkFORCIgaWQ9ImJmYmVmOGEyLTdmMTktNDAwZC04Yjg5LTg3ZjdjNzYwNzhhZSI+DQogICAgICAgIDxJbmRpY2F0b3JJdGVtIGlkPSI0MmU5Njk5OC03MTYxLTRmMjItYmI3Ny03MzY2MGUyNjlhNmIiIGNvbmRpdGlvbj0iY29udGFpbnMiPg0KICAgICAgICAgIDxDb250ZXh0IGRvY3VtZW50PSJSZWdpc3RyeUl0ZW0iIHNlYXJjaD0iUmVnaXN0cnlJdGVtL1BhdGgiIHR5cGU9Im1pciIgLz4NCiAgICAgICAgICA8Q29udGVudCB0eXBlPSJzdHJpbmciPkN1cnJlbnRWZXJzaW9uXFJ1bjwvQ29udGVudD4NCiAgICAgICAgPC9JbmRpY2F0b3JJdGVtPg0KICAgICAgICA8SW5kaWNhdG9ySXRlbSBpZD0iNWQ1YjgyOTYtMDFjOS00MTQ2LTlhNzQtYWJhNTMxYzU3NDc5IiBjb25kaXRpb249ImNvbnRhaW5zIj4NCiAgICAgICAgICA8Q29udGV4dCBkb2N1bWVudD0iUmVnaXN0cnlJdGVtIiBzZWFyY2g9IlJlZ2lzdHJ5SXRlbS9QYXRoIiB0eXBlPSJtaXIiIC8+DQogICAgICAgICAgPENvbnRlbnQgdHlwZT0ic3RyaW5nIj5DcnlwdG9sb2NrZXI8L0NvbnRlbnQ+DQogICAgICAgIDwvSW5kaWNhdG9ySXRlbT4NCiAgICAgIDwvSW5kaWNhdG9yPg0KICAgIDwvSW5kaWNhdG9yPg0KICA8L2RlZmluaXRpb24+DQo8L2lvYz4=",
    "FileName": "file.txt"
  },
  "FeatureCtrl": {
    "mode": "0"
  },
  "Meta": {
    "ErrorCode": 0,
    "Result": 1
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/05_download_openioc_file.json
</summary>
</details>

<details>

```
{
  "Data": {
    "FilingCabinet": [
      {
        "ExtractingStatus": 999,
        "FileAddedDatetime": "05/10/2020 15:58:41",
        "FileHashID": "cd9b739b7c6e488080412e9a831e9260a468564f",
        "FileName": "file.txt",
        "ShortDesc": "Cryptolocker Detection (EXPERIMENTAL)",
        "UploadedBy": "Integration Lab",
        "UploadedFrom": 1
      },
      {
        "ExtractingStatus": 1,
        "FileAddedDatetime": "05/10/2020 12:28:18",
        "FileHashID": "2a99370fd6218b6b8e0c3413f11eb504a4a60225",
        "FileName": "openioc1",
        "ShortDesc": "SHELLDC.DLL (BACKDOOR)",
        "UploadedBy": "Integration Lab",
        "UploadedFrom": 1
      },
      {
        "ExtractingStatus": 1,
        "FileAddedDatetime": "05/10/2020 10:39:17",
        "FileHashID": "fc3f17bd9068c2588c4c475d2d08a0e7f04f434d",
        "FileName": "cryptolocker2.ioc",
        "ShortDesc": "Cryptolocker Detection (EXPERIMENTAL)",
        "UploadedBy": "Integration Lab",
        "UploadedFrom": 1
      },
      {
        "ExtractingStatus": 999,
        "FileAddedDatetime": "05/10/2020 10:39:17",
        "FileHashID": "769fcc7550bf98d96bccb7e22a5557301c403455",
        "FileName": "file.txt",
        "ShortDesc": "Cryptolocker Detection (EXPERIMENTAL)",
        "UploadedBy": "Integration Lab",
        "UploadedFrom": 1
      }
    ],
    "TotalIOCCount": 4
  },
  "FeatureCtrl": {
    "mode": "0"
  },
  "Meta": {
    "ErrorCode": 0,
    "Result": 1
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/06_openioc_files_list.json
</summary>
</details>

<details>

```
{
  "Data": {
    "FilingCabinet": [
      {
        "ExtractingStatus": 999,
        "FileAddedDatetime": "05/10/2020 15:58:41",
        "FileHashID": "cd9b739b7c6e488080412e9a831e9260a468564f",
        "FileName": "file.txt",
        "ShortDesc": "Cryptolocker Detection (EXPERIMENTAL)",
        "UploadedBy": "Integration Lab",
        "UploadedFrom": 1
      },
      {
        "ExtractingStatus": 1,
        "FileAddedDatetime": "05/10/2020 12:28:18",
        "FileHashID": "2a99370fd6218b6b8e0c3413f11eb504a4a60225",
        "FileName": "openioc1",
        "ShortDesc": "SHELLDC.DLL (BACKDOOR)",
        "UploadedBy": "Integration Lab",
        "UploadedFrom": 1
      },
      {
        "ExtractingStatus": 1,
        "FileAddedDatetime": "05/10/2020 10:39:17",
        "FileHashID": "fc3f17bd9068c2588c4c475d2d08a0e7f04f434d",
        "FileName": "cryptolocker2.ioc",
        "ShortDesc": "Cryptolocker Detection (EXPERIMENTAL)",
        "UploadedBy": "Integration Lab",
        "UploadedFrom": 1
      },
      {
        "ExtractingStatus": 999,
        "FileAddedDatetime": "05/10/2020 10:39:17",
        "FileHashID": "769fcc7550bf98d96bccb7e22a5557301c403455",
        "FileName": "file.txt",
        "ShortDesc": "Cryptolocker Detection (EXPERIMENTAL)",
        "UploadedBy": "Integration Lab",
        "UploadedFrom": 1
      }
    ],
    "TotalIOCCount": 4
  },
  "FeatureCtrl": {
    "mode": "0"
  },
  "Meta": {
    "ErrorCode": 0,
    "Result": 1
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/07_openioc_files_list_fuzzy_match_string.json
</summary>
</details>

<details>

```
{
  "Data": {
    "FilingCabinet": [
      {
        "ExtractingStatus": 999,
        "FileAddedDatetime": "05/10/2020 10:39:17",
        "FileHashID": "769fcc7550bf98d96bccb7e22a5557301c403455",
        "FileName": "file.txt",
        "ShortDesc": "Cryptolocker Detection (EXPERIMENTAL)",
        "UploadedBy": "Integration Lab",
        "UploadedFrom": 1
      }
    ],
    "TotalIOCCount": 1
  },
  "FeatureCtrl": {
    "mode": "0"
  },
  "Meta": {
    "ErrorCode": 0,
    "Result": 1
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/08_openioc_files_list_hash_list.json
</summary>
</details>

<details>

```
{
  "Data": {
    "Code": 0,
    "CodeType": 1,
    "Message": "OK",
    "Data": {
      "taskId": "B44BE9AE-80A9-4048-A4CE-064D90CB6D4C",
      "lastContentId": "[\r\n  {\r\n    \"serverGuid\": \"C22E1795-BF95-45BB-BC82-486B0F5161BE\",\r\n    \"lastContentId\": 48,\r\n    \"hasMore\": false,\r\n    \"totalProgress\": 0,\r\n    \"currentProgress\": 0\r\n  }\r\n]",
      "hasMore": false,
      "serverName": "Apex One as a Service",
      "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
      "content": [
        {
          "statusCode": 0,
          "message": "TMSL_S_SUCCESS",
          "content": {
            "agentServerMeta": [
              {
                "agentGuid": "626dcf14-b0c3-4b00-bc76-71cf5713ab2e",
                "minFirstSeen": 1589061887,
                "serverMeta": [
                  {
                    "criteriaNo": 0,
                    "sweepingType": 7,
                    "metaValue": "notepad.exe",
                    "metaHashId": "-1666102285318829169",
                    "firstSeen": 1589061887,
                    "lastSeen": 1589131161
                  }
                ],
                "isCriteriaExceedMaxMetaCount": [
                  false
                ],
                "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
                "serverName": "Apex One as a Service",
                "serverMode": 1,
                "isOnline": true,
                "isEnable": true,
                "isImportant": false,
                "ip": "10.0.2.15",
                "machineGuid": "3E4EC062-A620-4DE6-9DA9-395DD98EC1D8",
                "machineName": "TREND-MICRO-TES",
                "machineType": "Desktop",
                "userName": "TREND-MICRO-TES\\vagrant",
                "userGuid": "6AC1B3DCF-CE52-8279-EE9E-E101FD504E3",
                "isolateStatus": 4,
                "machineOS": "Windows 10",
                "productType": 15
              }
            ]
          }
        }
      ]
    },
    "TimeZone": -4
  },
  "Meta": {
    "result": 1,
    "errorCode": 0,
    "errorMessgae": "Success"
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "FeatureCtrl": {
    "mode": "0"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/09_get_rca_object.json
</summary>
</details>

<details>

```
{
  "api_response": {
    "Data": {
      "Code": 0,
      "CodeType": 1,
      "Message": "OK",
      "Data": {
        "taskId": "21afcb09-05c9-4dfe-9d1e-5751e99e639c",
        "hasMore": false,
        "serverName": "Apex One as a Service",
        "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
        "content": [
          {
            "statusCode": 0,
            "message": "TMSL_S_SUCCESS",
            "content": {
              "csv": "Host Name,TREND-MICRO-TES\nIP Address,10.0.2.15\nChain,Operation Time,Parent,Activity,Object Type,Object Name,Process ID,Command Line,User,Server Name,File Path,SHA1,SHA2,MD5,Signer,Connect To IP,Port,DNS Query,Resolved DNS,Registry Key,Registry Name,Registry Data\n1,05/10/20 1:00:20 -04:00,compattelrunner.exe,creation,process,compattelrunner.exe,11192,C:\\WINDOWS\\system32\\CompatTelRunner.exe -m:appraiser.dll -f:DoScheduledTelemetryRun -cv:lg+7FM07T0yHrx0b.1,SYSTEM,NT AUTHORITY,c:\\windows\\system32\\compattelrunner.exe,9c6a334bac3122876fcfe3e46ce9a08bc60d6c3a,924405fd4df46b0a1d955aa492f441b938f051cc830ab494e88398def701fc1f,1e79615ef9946eb8a28d15584b21db2f,microsoft windows (Invalid),-,-,-,-,-,-,-\n1,05/10/20 1:02:26 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\appxprovider.dll,creation,file,appxprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\appxprovider.dll,caac3efe84f653fbd1e1f27ce6180a5775653f50,b2e72ab88312e701830170ed750becda9d20cd65969f86a1e533ae2074abcb93,302aeac868a4c8045eca8340537a5214,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:25 -04:00,c:\\windows\\system32\\dism\\logprovider.dll,load,file,logprovider.dll,-,-,-,-,c:\\windows\\system32\\dism\\logprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:27 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcoreps.dll,modify,file,dismcoreps.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcoreps.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:40 -04:00,trend-micro-test,query,dns,trend-micro-test,-,-,-,-,-,-,-,-,-,-,-,trend-micro-test,10.0.2.15,-,-,-\n1,05/10/20 1:01:36 -04:00,c:\\windows\\system32\\drivers\\en-us\\kbdhid.sys.mui,access,file,kbdhid.sys.mui,-,-,-,-,c:\\windows\\system32\\drivers\\en-us\\kbdhid.sys.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\folderprovider.dll.mui,delete,file,folderprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\folderprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:17 -04:00,c:\\program files (x86)\\trend micro\\officescan client\\activeupdate\\officescan\\hotfix_pccnt\\common\\pccntmon.exe,access,file,pccntmon.exe,-,-,-,-,c:\\program files (x86)\\trend micro\\officescan client\\activeupdate\\officescan\\hotfix_pccnt\\common\\pccntmon.exe,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:39 -04:00,c:\\windows\\appcompat\\ua\\genericerror.png,creation,file,genericerror.png,-,-,-,-,c:\\windows\\appcompat\\ua\\genericerror.png,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:18 -04:00,c:\\program files (x86)\\trend micro\\officescan client\\activeupdate\\officescan\\hotfix_pccnt\\drv\\x64\\tmwfp.sys,access,file,tmwfp.sys,-,-,-,-,c:\\program files (x86)\\trend micro\\officescan client\\activeupdate\\officescan\\hotfix_pccnt\\drv\\x64\\tmwfp.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:44 -04:00,c:\\windows\\system32\\drivers\\ndfltr.sys,access,file,ndfltr.sys,-,-,-,-,c:\\windows\\system32\\drivers\\ndfltr.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\setupplatformprovider.dll.mui,creation,file,setupplatformprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\setupplatformprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:51 -04:00,c:\\windows\\system32\\drivers\\rasacd.sys,access,file,rasacd.sys,-,-,-,-,c:\\windows\\system32\\drivers\\rasacd.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:25 -04:00,c:\\windows\\system32\\dism\\dismprov.dll,load,file,dismprov.dll,-,-,-,-,c:\\windows\\system32\\dism\\dismprov.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcoreps.dll,delete,file,dismcoreps.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcoreps.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:39 -04:00,c:\\windows\\system32\\en-us\\netshell.dll.mui,access,file,netshell.dll.mui,-,-,-,-,c:\\windows\\system32\\en-us\\netshell.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\genericprovider.dll,delete,file,genericprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\genericprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:30 -04:00,c:\\windows\\system32\\devinv.dll,load,file,devinv.dll,-,-,-,-,c:\\windows\\system32\\devinv.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\wimprovider.dll.mui,copy,file,wimprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\wimprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\dmiprovider.dll.mui,delete,file,dmiprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\dmiprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\unattendprovider.dll.mui,creation,file,unattendprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\unattendprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:06 -04:00,c:\\windows\\system32\\drivers\\urscx01000.sys,access,file,urscx01000.sys,-,-,-,-,c:\\windows\\system32\\drivers\\urscx01000.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:51 -04:00,c:\\windows\\system32\\dismapi.dll,load,file,dismapi.dll,-,-,-,-,c:\\windows\\system32\\dismapi.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\genericprovider.dll.mui,modify,file,genericprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\genericprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:27 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismprov.dll,modify,file,dismprov.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismprov.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:30 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\intlprovider.dll,creation,file,intlprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\intlprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:36 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\transmogprovider.dll,delete,file,transmogprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\transmogprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:40 -04:00,c:\\windows\\system32\\pnrpnsp.dll,load,file,pnrpnsp.dll,-,-,-,-,c:\\windows\\system32\\pnrpnsp.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:36 -04:00,c:\\windows\\logs\\dism\\dism.log,access,file,dism.log,-,-,-,-,c:\\windows\\logs\\dism\\dism.log,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:41 -04:00,c:\\windows\\system32\\newdev.dll,load,file,newdev.dll,-,-,-,-,c:\\windows\\system32\\newdev.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:36 -04:00,c:\\windows\\logs\\dism\\dism.log,creation,file,dism.log,-,-,-,-,c:\\windows\\logs\\dism\\dism.log,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\offlinesetupprovider.dll.mui,creation,file,offlinesetupprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\offlinesetupprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ffuprovider.dll.mui,copy,file,ffuprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ffuprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\smiprovider.dll.mui,creation,file,smiprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\smiprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:25 -04:00,c:\\windows\\system32\\dism\\ffuprovider.dll,load,file,ffuprovider.dll,-,-,-,-,c:\\windows\\system32\\dism\\ffuprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:12 -04:00,c:\\windows\\system32\\drivers\\arcsas.sys,access,file,arcsas.sys,-,-,-,-,c:\\windows\\system32\\drivers\\arcsas.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:27 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\appxprovider.dll.mui,modify,file,appxprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\appxprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\offlinesetupprovider.dll,delete,file,offlinesetupprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\offlinesetupprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\smiprovider.dll,delete,file,smiprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\smiprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:23 -04:00,c:\\program files (x86)\\trend micro\\iservice\\ivp\\infsys\\vistarelease\\tbimdsa.sys,access,file,tbimdsa.sys,-,-,-,-,c:\\program files (x86)\\trend micro\\iservice\\ivp\\infsys\\vistarelease\\tbimdsa.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:20 -04:00,c:\\program files (x86)\\trend micro\\iservice\\ivp\\ivpagent.exe,access,file,ivpagent.exe,-,-,-,-,c:\\program files (x86)\\trend micro\\iservice\\ivp\\ivpagent.exe,ad5c9d9b85f83bc3ad075b61248367c05eb5774d,6928a1a89db5a0aa5b796c064386b9106cbb318c3c5435d7329f577dcd7caf44,db5ddc230e5cd8d8b032c3c80ee21d54,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:44 -04:00,c:\\windows\\system32\\drivers\\en-us\\nwifi.sys.mui,access,file,nwifi.sys.mui,-,-,-,-,c:\\windows\\system32\\drivers\\en-us\\nwifi.sys.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:03 -04:00,c:\\windows\\system32\\drivers\\ucmtcpcicx.sys,access,file,ucmtcpcicx.sys,-,-,-,-,c:\\windows\\system32\\drivers\\ucmtcpcicx.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:40 -04:00,c:\\windows\\system32\\ktmw32.dll,load,file,ktmw32.dll,-,-,-,-,c:\\windows\\system32\\ktmw32.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:21 -04:00,c:\\windows\\system32\\windows.security.authentication.onlineid.dll,load,file,windows.security.authentication.onlineid.dll,-,-,-,-,c:\\windows\\system32\\windows.security.authentication.onlineid.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ibsprovider.dll.mui,delete,file,ibsprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ibsprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:40 -04:00,c:\\windows\\system32\\wshbth.dll,load,file,wshbth.dll,-,-,-,-,c:\\windows\\system32\\wshbth.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:33 -04:00,c:\\windows\\system32\\updatepolicy.dll,load,file,updatepolicy.dll,-,-,-,-,c:\\windows\\system32\\updatepolicy.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:31 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\wimprovider.dll,copy,file,wimprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\wimprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:58 -04:00,c:\\program files (x86)\\trend micro\\officescan client\\amsi\\tmamsiprovider64.dll,load,file,tmamsiprovider64.dll,-,-,-,-,c:\\program files (x86)\\trend micro\\officescan client\\amsi\\tmamsiprovider64.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:21 -04:00,c:\\windows\\system32\\dusmapi.dll,load,file,dusmapi.dll,-,-,-,-,c:\\windows\\system32\\dusmapi.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:24 -04:00,c:\\windows\\system32\\dismapi.dll,access,file,dismapi.dll,-,-,-,-,c:\\windows\\system32\\dismapi.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:27 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcore.dll,copy,file,dismcore.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcore.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:33 -04:00,settings-win.data.microsoft.com,query,dns,settings-win.data.microsoft.com,-,-,-,-,-,-,-,-,-,-,-,settings-win.data.microsoft.com,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ffuprovider.dll.mui,delete,file,ffuprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ffuprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\intlprovider.dll.mui,copy,file,intlprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\intlprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\logprovider.dll.mui,creation,file,logprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\logprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:27 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcoreps.dll,copy,file,dismcoreps.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcoreps.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\folderprovider.dll.mui,copy,file,folderprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\folderprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\smiprovider.dll.mui,copy,file,smiprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\smiprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\dmiprovider.dll.mui,modify,file,dmiprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\dmiprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:57 -04:00,c:\\windows\\system32\\drivers\\smartsamd.sys,access,file,smartsamd.sys,-,-,-,-,c:\\windows\\system32\\drivers\\smartsamd.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\genericprovider.dll,creation,file,genericprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\genericprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:31 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\wimprovider.dll,creation,file,wimprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\wimprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:30 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\intlprovider.dll,copy,file,intlprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\intlprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:27 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\dmiprovider.dll.mui,copy,file,dmiprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\dmiprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:27 -04:00,c:\\windows\\system32\\wuapi.dll,load,file,wuapi.dll,-,-,-,-,c:\\windows\\system32\\wuapi.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:42 -04:00,c:\\windows\\system32\\drivers\\mslldp.sys,access,file,mslldp.sys,-,-,-,-,c:\\windows\\system32\\drivers\\mslldp.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dmiprovider.dll,delete,file,dmiprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dmiprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:17 -04:00,c:\\program files (x86)\\trend micro\\officescan client\\activeupdate\\officescan\\hotfix_admin\\tmuninst.exe,access,file,tmuninst.exe,-,-,-,-,c:\\program files (x86)\\trend micro\\officescan client\\activeupdate\\officescan\\hotfix_admin\\tmuninst.exe,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\ibsprovider.dll,copy,file,ibsprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\ibsprovider.dll,dbbeb426cedb8ee7d402cff66fb859eedde93182,c88ad6c3919519468b3694cbf2d90a40df7eaaa10210854cf546598a104d2526,280d67aa4d95a9f517129db2173ba5cc,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ibsprovider.dll.mui,copy,file,ibsprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ibsprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\unattendprovider.dll.mui,modify,file,unattendprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\unattendprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:21 -04:00,c:\\windows\\winsxs\\amd64_microsoft.windows.gdiplus_6595b64144ccf1df_1.1.18362.778_none_17b1aa466d9fc986\\gdiplus.dll,load,file,gdiplus.dll,-,-,-,-,c:\\windows\\winsxs\\amd64_microsoft.windows.gdiplus_6595b64144ccf1df_1.1.18362.778_none_17b1aa466d9fc986\\gdiplus.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:26 -04:00,c:\\windows\\system32\\generaltel.dll,load,file,generaltel.dll,-,-,-,-,c:\\windows\\system32\\generaltel.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:41 -04:00,c:\\windows\\system32\\drvstore.dll,load,file,drvstore.dll,-,-,-,-,c:\\windows\\system32\\drvstore.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:20 -04:00,c:\\windows\\system32\\appraiser.dll,load,file,appraiser.dll,-,-,-,-,c:\\windows\\system32\\appraiser.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:59 -04:00,c:\\windows\\system32\\drivers\\storufs.sys,access,file,storufs.sys,-,-,-,-,c:\\windows\\system32\\drivers\\storufs.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:22 -04:00,c:\\windows\\system32\\catroot\\{f750e6c3-38ee-11d1-85e5-00c04fc295ee}\\microsoft-windows-client-features-package00~31bf3856ad364e35~amd64~~10.0.18362.1.cat,access,file,microsoft-windows-client-features-package00~31bf3856ad364e35~amd64~~10.0.18362.1.cat,-,-,-,-,c:\\windows\\system32\\catroot\\{f750e6c3-38ee-11d1-85e5-00c04fc295ee}\\microsoft-windows-client-features-package00~31bf3856ad364e35~amd64~~10.0.18362.1.cat,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:41 -04:00,c:\\windows\\system32\\acmigration.dll,load,file,acmigration.dll,-,-,-,-,c:\\windows\\system32\\acmigration.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:18 -04:00,c:\\windows\\system32\\drivers\\bttflt.sys,access,file,bttflt.sys,-,-,-,-,c:\\windows\\system32\\drivers\\bttflt.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:40 -04:00,c:\\windows\\system32\\napinsp.dll,load,file,napinsp.dll,-,-,-,-,c:\\windows\\system32\\napinsp.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:31 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\transmogprovider.dll,modify,file,transmogprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\transmogprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:19 -04:00,svchost.exe,creation,process,compattelrunner.exe,7304,C:\\WINDOWS\\system32\\compattelrunner.exe,SYSTEM,NT AUTHORITY,c:\\windows\\system32\\compattelrunner.exe,9c6a334bac3122876fcfe3e46ce9a08bc60d6c3a,924405fd4df46b0a1d955aa492f441b938f051cc830ab494e88398def701fc1f,1e79615ef9946eb8a28d15584b21db2f,microsoft windows (Invalid),-,-,-,-,-,-,-\n1,05/10/20 1:00:19 -04:00,c:\\windows\\system32\\compattelrunner.exe,load,file,compattelrunner.exe,-,-,-,-,c:\\windows\\system32\\compattelrunner.exe,9c6a334bac3122876fcfe3e46ce9a08bc60d6c3a,924405fd4df46b0a1d955aa492f441b938f051cc830ab494e88398def701fc1f,1e79615ef9946eb8a28d15584b21db2f,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:45 -04:00,c:\\windows\\system32\\compattelrunner.exe,access,file,compattelrunner.exe,-,-,-,-,c:\\windows\\system32\\compattelrunner.exe,9c6a334bac3122876fcfe3e46ce9a08bc60d6c3a,924405fd4df46b0a1d955aa492f441b938f051cc830ab494e88398def701fc1f,1e79615ef9946eb8a28d15584b21db2f,-,-,-,-,-,-,-,-\n1,05/09/20 17:21:32 -04:00,services.exe,creation,process,svchost.exe,1296,C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Schedule,SYSTEM,NT AUTHORITY,c:\\windows\\system32\\svchost.exe,75c5a97f521f760e32a4a9639a653eed862e9c61,dd191a5b23df92e12a8852291f9fb5ed594b76a28a5a464418442584afd1e048,9520a99e77d6196d0d09833146424113,microsoft windows publisher (Invalid),-,-,-,-,-,-,-\n1,05/09/20 20:51:19 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power install,creation,file,ac power install,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power install,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:53:04 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power install,delete,file,ac power install,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power install,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:53:28 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power download,creation,file,ac power download,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power download,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 23:14:36 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\.net framework\\.net framework ngen v4.0.30319 64 critical,creation,file,.net framework ngen v4.0.30319 64 critical,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\.net framework\\.net framework ngen v4.0.30319 64 critical,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 23:13:52 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\.net framework\\.net framework ngen v4.0.30319 critical,creation,file,.net framework ngen v4.0.30319 critical,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\.net framework\\.net framework ngen v4.0.30319 critical,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:53:28 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\backup scan,creation,file,backup scan,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\backup scan,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:59:14 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\universal orchestrator start,delete,file,universal orchestrator start,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\universal orchestrator start,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:51:19 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power install,modify,file,ac power install,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power install,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:53:28 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power download,modify,file,ac power download,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power download,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:53:29 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power download,delete,file,ac power download,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power download,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:17 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\softwareprotectionplatform\\svcrestarttask,creation,file,svcrestarttask,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\softwareprotectionplatform\\svcrestarttask,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 22:41:48 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\flighting\\onesettings\\refreshcache,creation,file,refreshcache,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\flighting\\onesettings\\refreshcache,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:53:06 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\schedule scan,creation,file,schedule scan,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\schedule scan,-,-,-,-,-,-,-,-,-,-,-\n1,01/01/70 0:00:00 -05:00,-,creation,process,services.exe,656,-,-,-,c:\\windows\\system32\\services.exe,86662690d627002d7cab3285f7be3e6d87b35cfb,9090e0e44e14709fb09b23b98572e0e61c810189e2de8f7156021bc81c3b1bb6,bccc12eb2ef644e662a63a023fb83f9b,microsoft windows publisher (Invalid),-,-,-,-,-,-,-\n1,05/10/20 2:22:10 -04:00,c:\\windows\\security\\database\\edb.chk,creation,file,edb.chk,-,-,-,-,c:\\windows\\security\\database\\edb.chk,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:00 -04:00,c:\\windows\\inf\\ucmucsiacpiclient.pnf,creation,file,ucmucsiacpiclient.pnf,-,-,-,-,c:\\windows\\inf\\ucmucsiacpiclient.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:56 -04:00,c:\\windows\\inf\\iai2c.pnf,creation,file,iai2c.pnf,-,-,-,-,c:\\windows\\inf\\iai2c.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:52 -04:00,c:\\windows\\inf\\bcmfn2.pnf,creation,file,bcmfn2.pnf,-,-,-,-,c:\\windows\\inf\\bcmfn2.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:57 -04:00,c:\\windows\\inf\\msgpiowin32.pnf,creation,file,msgpiowin32.pnf,-,-,-,-,c:\\windows\\inf\\msgpiowin32.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:56 -04:00,c:\\windows\\inf\\ialpss2i_i2c_bxt_p.pnf,creation,file,ialpss2i_i2c_bxt_p.pnf,-,-,-,-,c:\\windows\\inf\\ialpss2i_i2c_bxt_p.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:55 -04:00,c:\\windows\\inf\\wgencounter.pnf,creation,file,wgencounter.pnf,-,-,-,-,c:\\windows\\inf\\wgencounter.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:56 -04:00,c:\\windows\\inf\\ialpss2i_gpio2_bxt_p.pnf,creation,file,ialpss2i_gpio2_bxt_p.pnf,-,-,-,-,c:\\windows\\inf\\ialpss2i_gpio2_bxt_p.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:59 -04:00,c:\\windows\\inf\\sbp2.pnf,creation,file,sbp2.pnf,-,-,-,-,c:\\windows\\inf\\sbp2.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:55 -04:00,c:\\windows\\inf\\hidinterrupt.pnf,creation,file,hidinterrupt.pnf,-,-,-,-,c:\\windows\\inf\\hidinterrupt.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:53 -04:00,c:\\windows\\inf\\mdmbtmdm.pnf,creation,file,mdmbtmdm.pnf,-,-,-,-,c:\\windows\\inf\\mdmbtmdm.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:56 -04:00,c:\\windows\\inf\\ialpss2i_gpio2_glk.pnf,creation,file,ialpss2i_gpio2_glk.pnf,-,-,-,-,c:\\windows\\inf\\ialpss2i_gpio2_glk.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:00 -04:00,c:\\windows\\inf\\umpass.pnf,creation,file,umpass.pnf,-,-,-,-,c:\\windows\\inf\\umpass.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:53 -04:00,c:\\windows\\inf\\microsoft_bluetooth_hfp.pnf,creation,file,microsoft_bluetooth_hfp.pnf,-,-,-,-,c:\\windows\\inf\\microsoft_bluetooth_hfp.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:58 -04:00,c:\\windows\\inf\\mtconfig.pnf,creation,file,mtconfig.pnf,-,-,-,-,c:\\windows\\inf\\mtconfig.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:54 -04:00,c:\\windows\\inf\\circlass.pnf,creation,file,circlass.pnf,-,-,-,-,c:\\windows\\inf\\circlass.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:55 -04:00,c:\\windows\\inf\\hidi2c.pnf,creation,file,hidi2c.pnf,-,-,-,-,c:\\windows\\inf\\hidi2c.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 2:22:10 -04:00,\"[\"\"hklm\\\\system\\\\currentcontrolset\\\\services\\\\acdriver\"\", \"\"imagepath\"\", \"\"system32\\\\DRIVERS\\\\AcDriver.sys\"\", true]\",modify,registry,imagepath,-,-,-,-,-,-,-,-,-,-,-,-,-,hklm\\system\\currentcontrolset\\services\\acdriver,imagepath,system32\\DRIVERS\\AcDriver.sys\n1,05/10/20 2:22:11 -04:00,c:\\windows\\security\\database\\edb.log,creation,file,edb.log,-,-,-,-,c:\\windows\\security\\database\\edb.log,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:00 -04:00,c:\\windows\\inf\\wdma_usb.pnf,creation,file,wdma_usb.pnf,-,-,-,-,c:\\windows\\inf\\wdma_usb.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:57 -04:00,c:\\windows\\inf\\intelpmax.pnf,creation,file,intelpmax.pnf,-,-,-,-,c:\\windows\\inf\\intelpmax.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:02 -04:00,c:\\windows\\inf\\wmiacpi.pnf,creation,file,wmiacpi.pnf,-,-,-,-,c:\\windows\\inf\\wmiacpi.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:55 -04:00,c:\\windows\\inf\\hidbth.pnf,creation,file,hidbth.pnf,-,-,-,-,c:\\windows\\inf\\hidbth.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:56 -04:00,c:\\windows\\inf\\ialpss2i_i2c_skl.pnf,creation,file,ialpss2i_i2c_skl.pnf,-,-,-,-,c:\\windows\\inf\\ialpss2i_i2c_skl.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:01 -04:00,c:\\windows\\inf\\usbcir.pnf,creation,file,usbcir.pnf,-,-,-,-,c:\\windows\\inf\\usbcir.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:58 -04:00,c:\\windows\\inf\\ksfilter.pnf,creation,file,ksfilter.pnf,-,-,-,-,c:\\windows\\inf\\ksfilter.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:59 -04:00,c:\\windows\\inf\\tpm.pnf,creation,file,tpm.pnf,-,-,-,-,c:\\windows\\inf\\tpm.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:55 -04:00,c:\\windows\\inf\\hidspi_km.pnf,creation,file,hidspi_km.pnf,-,-,-,-,c:\\windows\\inf\\hidspi_km.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:01 -04:00,c:\\windows\\inf\\hidvhf.pnf,creation,file,hidvhf.pnf,-,-,-,-,c:\\windows\\inf\\hidvhf.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 2:22:11 -04:00,\"[\"\"hklm\\\\system\\\\currentcontrolset\\\\services\\\\tmiacagentsvc\"\", \"\"imagepath\"\", \"\"\\\"\"C:\\\\Program Files (x86)\\\\Trend Micro\\\\iService\\\\iAC\\\\ac_bin\\\\TMiACAgentSvc.exe\\\"\" --mode SVC --sc --l DEBUG\"\", true]\",modify,registry,imagepath,-,-,-,-,-,-,-,-,-,-,-,-,-,hklm\\system\\currentcontrolset\\services\\tmiacagentsvc,imagepath,\"\"C:\\Program Files (x86)\\Trend Micro\\iService\\iAC\\ac_bin\\TMiACAgentSvc.exe\"\" --mode SVC --sc --l DEBUG\n1,05/10/20 1:00:58 -04:00,c:\\windows\\inf\\memory.pnf,creation,file,memory.pnf,-,-,-,-,c:\\windows\\inf\\memory.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:52 -04:00,c:\\windows\\inf\\amdgpio2.pnf,creation,file,amdgpio2.pnf,-,-,-,-,c:\\windows\\inf\\amdgpio2.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:55 -04:00,c:\\windows\\inf\\hidbatt.pnf,creation,file,hidbatt.pnf,-,-,-,-,c:\\windows\\inf\\hidbatt.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:53 -04:00,c:\\windows\\inf\\bth.pnf,creation,file,bth.pnf,-,-,-,-,c:\\windows\\inf\\bth.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:00 -04:00,c:\\windows\\inf\\urssynopsys.pnf,creation,file,urssynopsys.pnf,-,-,-,-,c:\\windows\\inf\\urssynopsys.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:56 -04:00,c:\\windows\\inf\\iastorv.pnf,creation,file,iastorv.pnf,-,-,-,-,c:\\windows\\inf\\iastorv.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:53 -04:00,c:\\windows\\inf\\virtdisk.pnf,creation,file,virtdisk.pnf,-,-,-,-,c:\\windows\\inf\\virtdisk.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:54 -04:00,c:\\windows\\inf\\netevbda.pnf,creation,file,netevbda.pnf,-,-,-,-,c:\\windows\\inf\\netevbda.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:59 -04:00,c:\\windows\\inf\\stornvme.pnf,creation,file,stornvme.pnf,-,-,-,-,c:\\windows\\inf\\stornvme.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:53 -04:00,c:\\windows\\inf\\buttonconverter.pnf,creation,file,buttonconverter.pnf,-,-,-,-,c:\\windows\\inf\\buttonconverter.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 2:22:11 -04:00,c:\\windows\\security\\database\\secedit.sdb,creation,file,secedit.sdb,-,-,-,-,c:\\windows\\security\\database\\secedit.sdb,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:53 -04:00,c:\\windows\\inf\\chargearbitration.pnf,creation,file,chargearbitration.pnf,-,-,-,-,c:\\windows\\inf\\chargearbitration.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 2:22:10 -04:00,c:\\windows\\system32\\esent.dll,load,file,esent.dll,-,-,-,-,c:\\windows\\system32\\esent.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 2:21:47 -04:00,\"[\"\"hklm\\\\system\\\\currentcontrolset\\\\services\\\\dsasvc\"\", \"\"imagepath\"\", \"\"%SystemRoot%\\\\system32\\\\dgagent\\\\DSAGENT.exe\"\", true]\",modify,registry,imagepath,-,-,-,-,-,-,-,-,-,-,-,-,-,hklm\\system\\currentcontrolset\\services\\dsasvc,imagepath,%SystemRoot%\\system32\\dgagent\\DSAGENT.exe\n1,05/10/20 2:21:47 -04:00,\"[\"\"hklm\\\\system\\\\currentcontrolset\\\\services\\\\sakfile\"\", \"\"imagepath\"\", \"\"system32\\\\drivers\\\\sakfile.sys\"\", true]\",modify,registry,imagepath,-,-,-,-,-,-,-,-,-,-,-,-,-,hklm\\system\\currentcontrolset\\services\\sakfile,imagepath,system32\\drivers\\sakfile.sys\n1,05/10/20 2:22:11 -04:00,\"[\"\"hklm\\\\system\\\\currentcontrolset\\\\services\\\\acdriverhelper\"\", \"\"imagepath\"\", \"\"\\\\SystemRoot\\\\system32\\\\DRIVERS\\\\AcDriverHelper.sys\"\", true]\",modify,registry,imagepath,-,-,-,-,-,-,-,-,-,-,-,-,-,hklm\\system\\currentcontrolset\\services\\acdriverhelper,imagepath,\\SystemRoot\\system32\\DRIVERS\\AcDriverHelper.sys"
            }
          }
        ]
      },
      "TimeZone": -4
    },
    "Meta": {
      "result": 1,
      "errorCode": 0,
      "errorMessgae": "Success"
    },
    "PermissionCtrl": {
      "permission": "255"
    },
    "FeatureCtrl": {
      "mode": "0"
    },
    "SystemCtrl": {
      "TmcmSoDist_Role": "none"
    }
  }
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/10_download_rca_csv_file.json
</summary>
</details>

<details>

```
{
  "Data": {
    "Code": 0,
    "CodeType": 1,
    "Data": {
      "content": [
        {
          "content": {
            "agentGuid": [
              "626dcf14-b0c3-4b00-bc76-71cf5713ab2e"
            ],
            "processTerminationSummaryGuid": "5f7bef38-6603-4edc-b285-837feb136da5",
            "status": 3
          },
          "message": "TMSL_S_SUCCESS",
          "statusCode": 0
        }
      ],
      "hasMore": false,
      "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
      "serverName": "Apex One as a Service",
      "taskId": "5f7bef38-6603-4edc-b285-837feb136da5"
    },
    "Message": "OK",
    "TimeZone": -4
  },
  "FeatureCtrl": {
    "mode": "0"
  },
  "Meta": {
    "errorCode": 0,
    "errorMessgae": "Success",
    "result": 1
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/11_terminate_process.json
</summary>
</details>

<details>

```
{
  "Data": [
    {
      "DeletedStatus": 1,
      "FileHashID": "769fcc7550bf98d96bccb7e22a5557301c403455"
    }
  ],
  "FeatureCtrl": {
    "mode": "0"
  },
  "Meta": {
    "ErrorCode": 0,
    "Result": 1
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/12_delete_openioc_file.json
</summary>
</details>

<details>

```
{
  "result_code": 1,
  "result_description": "Operation successful",
  "result_content": [
    {
      "entity_id": "626dcf14-b0c3-4b00-bc76-71cf5713ab2e",
      "product": "SLF_PRODUCT_OFFICESCAN_CE",
      "managing_server_id": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
      "folder_path": "Workgroup",
      "ip_address_list": "10.0.2.15",
      "mac_address_list": "08-00-27-96-86-8E",
      "host_name": "TREND-MICRO-TES",
      "isolation_status": "normal",
      "capabilities": [
        "cmd_restore_isolated_agent",
        "cmd_isolate_agent",
        "cmd_relocate_agent",
        "cmd_uninstall_agent"
      ]
    }
  ]
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/13_performs_action_isolate.json
</summary>
</details>

<details>

```
{
  "result_code": 1,
  "result_description": "Operation successful",
  "result_content": [
    {
      "entity_id": "626dcf14-b0c3-4b00-bc76-71cf5713ab2e",
      "product": "SLF_PRODUCT_OFFICESCAN_CE",
      "managing_server_id": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
      "folder_path": "Workgroup",
      "ip_address_list": "10.0.2.15",
      "mac_address_list": "08-00-27-96-86-8E",
      "host_name": "TREND-MICRO-TES",
      "isolation_status": "isolated",
      "capabilities": [
        "cmd_restore_isolated_agent",
        "cmd_isolate_agent",
        "cmd_relocate_agent",
        "cmd_uninstall_agent"
      ]
    }
  ]
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 --debug run < tests/14_performs_action_restore.json
</summary>
</details>

<details>

```
{
  "body": {
    "error": "An error occurred during plugin execution!\n\nSomething unexpected occurred. Can't isolate for admin endpoint",
    "log": "rapid7/Trend Micro Apex:1.0.0. Step name: performs_action\nAn error occurred during plugin execution!\n\nSomething unexpected occurred. Can't isolate for admin endpoint\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.7/site-packages/komand-1.0.1-py3.7.egg/komand/plugin.py\", line 311, in handle_step\n    output = self.start_step(input_message['body'], 'action', logger, log_stream, is_test, is_debug)\n  File \"/usr/local/lib/python3.7/site-packages/komand-1.0.1-py3.7.egg/komand/plugin.py\", line 419, in start_step\n    output = func(params)\n  File \"/usr/local/lib/python3.7/site-packages/trendmicro_apex_rapid7_plugin-1.0.0-py3.7.egg/icon_trendmicro_apex/actions/performs_action/action.py\", line 26, in run\n    self._get_payload(params)\n  File \"/usr/local/lib/python3.7/site-packages/trendmicro_apex_rapid7_plugin-1.0.0-py3.7.egg/icon_trendmicro_apex/actions/performs_action/action.py\", line 38, in _get_payload\n    self._validate_allow_action(action_id, params.get(Input.ENTITY_ID), self.connection.skip_entity_ids)\n  File \"/usr/local/lib/python3.7/site-packages/trendmicro_apex_rapid7_plugin-1.0.0-py3.7.egg/icon_trendmicro_apex/actions/performs_action/action.py\", line 61, in _validate_allow_action\n    assistance=f\"Can't {action_id.lower()} for admin endpoint\")\nkomand.exceptions.PluginException: An error occurred during plugin execution!\n\nSomething unexpected occurred. Can't isolate for admin endpoint\n",
    "meta": {},
    "status": "error"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 run < tests/15_performs_action_isolate_entity_bad.json
</summary>
</details>

<details>

```
{
  "body": {
    "error": "An error occurred during plugin execution!\n\nSomething unexpected occurred. Can't isolate for admin endpoint",
    "log": "rapid7/Trend Micro Apex:1.0.0. Step name: performs_action\nAn error occurred during plugin execution!\n\nSomething unexpected occurred. Can't isolate for admin endpoint\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.7/site-packages/komand-1.0.1-py3.7.egg/komand/plugin.py\", line 311, in handle_step\n    output = self.start_step(input_message['body'], 'action', logger, log_stream, is_test, is_debug)\n  File \"/usr/local/lib/python3.7/site-packages/komand-1.0.1-py3.7.egg/komand/plugin.py\", line 419, in start_step\n    output = func(params)\n  File \"/usr/local/lib/python3.7/site-packages/trendmicro_apex_rapid7_plugin-1.0.0-py3.7.egg/icon_trendmicro_apex/actions/performs_action/action.py\", line 26, in run\n    self._get_payload(params)\n  File \"/usr/local/lib/python3.7/site-packages/trendmicro_apex_rapid7_plugin-1.0.0-py3.7.egg/icon_trendmicro_apex/actions/performs_action/action.py\", line 44, in _get_payload\n    self._validate_allow_action(action_id, params.get(Input.IP_ADDRESS), self.connection.skip_address_ips)\n  File \"/usr/local/lib/python3.7/site-packages/trendmicro_apex_rapid7_plugin-1.0.0-py3.7.egg/icon_trendmicro_apex/actions/performs_action/action.py\", line 61, in _validate_allow_action\n    assistance=f\"Can't {action_id.lower()} for admin endpoint\")\nkomand.exceptions.PluginException: An error occurred during plugin execution!\n\nSomething unexpected occurred. Can't isolate for admin endpoint\n",
    "meta": {},
    "status": "error"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 run < tests/16_performs_action_isolate_ip_bad.json
</summary>
</details>

<details>

```
{
  "body": {
    "error": "An error occurred during plugin execution!\n\nSomething unexpected occurred. Can't uninstall for admin endpoint",
    "log": "rapid7/Trend Micro Apex:1.0.0. Step name: performs_action\nAn error occurred during plugin execution!\n\nSomething unexpected occurred. Can't uninstall for admin endpoint\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.7/site-packages/komand-1.0.1-py3.7.egg/komand/plugin.py\", line 311, in handle_step\n    output = self.start_step(input_message['body'], 'action', logger, log_stream, is_test, is_debug)\n  File \"/usr/local/lib/python3.7/site-packages/komand-1.0.1-py3.7.egg/komand/plugin.py\", line 419, in start_step\n    output = func(params)\n  File \"/usr/local/lib/python3.7/site-packages/trendmicro_apex_rapid7_plugin-1.0.0-py3.7.egg/icon_trendmicro_apex/actions/performs_action/action.py\", line 26, in run\n    self._get_payload(params)\n  File \"/usr/local/lib/python3.7/site-packages/trendmicro_apex_rapid7_plugin-1.0.0-py3.7.egg/icon_trendmicro_apex/actions/performs_action/action.py\", line 47, in _get_payload\n    self._validate_allow_action(action_id, params.get(Input.MAC_ADDRESS), self.connection.skip_mac_addresses)\n  File \"/usr/local/lib/python3.7/site-packages/trendmicro_apex_rapid7_plugin-1.0.0-py3.7.egg/icon_trendmicro_apex/actions/performs_action/action.py\", line 61, in _validate_allow_action\n    assistance=f\"Can't {action_id.lower()} for admin endpoint\")\nkomand.exceptions.PluginException: An error occurred during plugin execution!\n\nSomething unexpected occurred. Can't uninstall for admin endpoint\n",
    "meta": {},
    "status": "error"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 run < tests/17_performs_action_uninstall_mac_bad.json
</summary>
</details>

<details>

```
{
  "body": {
    "error": "An error occurred during plugin execution!\n\nSomething unexpected occurred. Can't uninstall for admin endpoint",
    "log": "rapid7/Trend Micro Apex:1.0.0. Step name: performs_action\nAn error occurred during plugin execution!\n\nSomething unexpected occurred. Can't uninstall for admin endpoint\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.7/site-packages/komand-1.0.1-py3.7.egg/komand/plugin.py\", line 311, in handle_step\n    output = self.start_step(input_message['body'], 'action', logger, log_stream, is_test, is_debug)\n  File \"/usr/local/lib/python3.7/site-packages/komand-1.0.1-py3.7.egg/komand/plugin.py\", line 419, in start_step\n    output = func(params)\n  File \"/usr/local/lib/python3.7/site-packages/trendmicro_apex_rapid7_plugin-1.0.0-py3.7.egg/icon_trendmicro_apex/actions/performs_action/action.py\", line 26, in run\n    self._get_payload(params)\n  File \"/usr/local/lib/python3.7/site-packages/trendmicro_apex_rapid7_plugin-1.0.0-py3.7.egg/icon_trendmicro_apex/actions/performs_action/action.py\", line 41, in _get_payload\n    self._validate_allow_action(action_id, params.get(Input.HOST_NAME), self.connection.skip_host_names)\n  File \"/usr/local/lib/python3.7/site-packages/trendmicro_apex_rapid7_plugin-1.0.0-py3.7.egg/icon_trendmicro_apex/actions/performs_action/action.py\", line 61, in _validate_allow_action\n    assistance=f\"Can't {action_id.lower()} for admin endpoint\")\nkomand.exceptions.PluginException: An error occurred during plugin execution!\n\nSomething unexpected occurred. Can't uninstall for admin endpoint\n",
    "meta": {},
    "status": "error"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/trendmicro_apex:1.0.0 run < tests/18_performs_action_uninstall_host_bad.json
</summary>
</details>