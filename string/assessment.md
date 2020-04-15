
## Assessment
### Run

<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: split_to_object\nBlock delimiter received, performing block split first\n",
    "meta": {},
    "output": {
      "object": {
        "Computer_ID": "bef41e8b-47b8-e188-8e43-3a2b662dd55d",
        "Computer_Name": "dgdemo\\RGWin64",
        "Computer_Type": "Windows"
      }
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug run < tests/complex_split_to_object.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: lower\n",
    "meta": {},
    "output": {
      "lower": "hello"
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug run < tests/lower.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: split_to_object\nBlock delimiter received, performing block split first\nSkipping 1 element split: ['-ServerName:App.AppXzst44mncqdg84v7sv6p7yznqwssy6f7f.mca']\n",
    "meta": {},
    "output": {
      "object": {
        "Agent_Begin_Local_Time": "12/11/2018 12:29:52 PM",
        "Agent_Begin_UTC_Time": "12/11/2018 5:29:52 PM",
        "Agent_End_Local_Time": "12/11/2018 12:29:55 PM",
        "Agent_End_UTC_Time": "12/11/2018 5:29:55 PM",
        "Agent_Local_Date": "2018.12.11",
        "Application": "microsoft.phot",
        "Application_Directory": "c:\\program files\\windowsapps\\microsoft.windows.photos_2017.35063.44410.1000_x64__8wekyb3d8bbwe",
        "Application_Full_Name": "microsoft.photos.exe",
        "Command_Line": "C:\\Program Files\\WindowsApps\\Microsoft.Windows.Photos_2017.35063.44410.1000_x64__8wekyb3d8bbwe\\Microsoft.Photos.exe",
        "Computer_ID": "bef41e8b-47b8-e188-8e43-3a2b662dd55d",
        "Computer_Name": "dgdemo\\RGWin64",
        "Computer_Type": "Windows",
        "Day_of_Week": "Tuesday",
        "Domain_Name": "dgdemo",
        "File_Extension": "exe",
        "Hour_of_Day": "12",
        "MAC_Address": "000c291e11e0",
        "MD5_Checksum": "28ecbc7a01aeaeb08cb5b9d81b67b9f6",
        "MD5_Hash": "7abcec28-ae01-b0ae-8cb5-b9d81b67b9f6",
        "Maximum_Number_of_Threads": "18",
        "Month": "2018/12",
        "Product_Version": "2017.35063.4441000000-2017.35063.13610.0",
        "Scan_Value_Status": "Scanned",
        "Scan_Value_Status_Local_Time": "8/25/2018 6:56:08 AM",
        "Scan_Value_Status_Text": "Virus Total: 0 / 68 scans positive.",
        "Signature_Create_UTC_Time": "",
        "Signature_Executable": "",
        "Signature_Issuer": "",
        "Signature_Publisher": "",
        "Signature_Status": "No Signature",
        "Signature_Subject": "",
        "Signature_Verify_Status": ""
      }
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug run < tests/really_complex_split_to_object.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: set_encoding\n",
    "meta": {},
    "output": {
      "encoded": "hello#world"
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug run < tests/set_encoding.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: split_to_object\nUser input to split: User=Bob -\u003e ['User', 'Bob']\n",
    "meta": {},
    "output": {
      "object": {
        "User": "Bob"
      }
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug run < tests/simple_split_to_object.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: split_to_list\n",
    "meta": {},
    "output": {
      "list": [
        "This",
        "is",
        "a",
        "sentence"
      ]
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug run < tests/split_to_list.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: trim\n",
    "meta": {},
    "output": {
      "trimmed": "this is a string"
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug run < tests/trim.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: upper\n",
    "meta": {},
    "output": {
      "upper": "LDAP"
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug run < tests/upper.json
</summary>
</details>

### Test

Autogenerate with:
<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: split_to_object\n",
    "meta": {},
    "output": null,
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug test < tests/complex_split_to_object.json
</summary>
</details>

Autogenerate with:
<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: lower\n",
    "meta": {},
    "output": null,
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug test < tests/lower.json
</summary>
</details>

Autogenerate with:
<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: split_to_object\n",
    "meta": {},
    "output": null,
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug test < tests/really_complex_split_to_object.json
</summary>
</details>

Autogenerate with:
<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: set_encoding\n",
    "meta": {},
    "output": null,
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug test < tests/set_encoding.json
</summary>
</details>

Autogenerate with:
<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: split_to_object\n",
    "meta": {},
    "output": null,
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug test < tests/simple_split_to_object.json
</summary>
</details>

Autogenerate with:
<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: split_to_list\n",
    "meta": {},
    "output": null,
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug test < tests/split_to_list.json
</summary>
</details>

Autogenerate with:
<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: trim\n",
    "meta": {},
    "output": null,
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug test < tests/trim.json
</summary>
</details>

Autogenerate with:
<details>

```
{
  "body": {
    "log": "rapid7/String Operations:1.2.2. Step name: upper\n",
    "meta": {},
    "output": null,
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/string:1.2.2 --debug test < tests/upper.json
</summary>
</details>

Autogenerate with:
<details>

```
[*] Validating plugin with all validators at .

[*] Running Integration Validators...
[*] Executing validator HelpValidator
[*] Executing validator ChangelogValidator
[*] Executing validator RequiredKeysValidator
[*] Executing validator UseCaseValidator
[*] Executing validator SpecPropertiesValidator
[*] Executing validator SpecVersionValidator
[*] Executing validator FilesValidator
[*] Executing validator TagValidator
[*] Executing validator DescriptionValidator
[*] Executing validator TitleValidator
[*] Executing validator VendorValidator
[*] Executing validator DefaultValueValidator
[*] Executing validator IconValidator
[*] Executing validator RequiredValidator
[*] Executing validator VersionValidator
[*] Executing validator DockerfileParentValidator
[*] Executing validator LoggingValidator
[*] Executing validator ProfanityValidator
[*] Executing validator AcronymValidator
[*] Executing validator JSONValidator
[*] Executing validator OutputValidator
[*] Executing validator RegenerationValidator
[*] Executing validator HelpInputOutputValidator
[*] Executing validator SupportValidator
[*] Executing validator ExceptionValidator
[*] Executing validator CredentialsValidator
[*] Executing validator PasswordValidator
[*] Executing validator PrintValidator
[*] Executing validator ConfidentialValidator
[*] Executing validator DockerValidator
[*] Executing validator URLValidator
[*] Plugin successfully validated!

----
[*] Total time elapsed: 13369.913ms

```

<summary>
icon-validate --all .
</summary>
</details>

Autogenerate with:
<details>

```
[*] Use ``make menu`` for available targets
[*] Including available Makefiles: ../tools/Makefiles/Helpers.mk ../tools/Makefiles/Colors.mk
--
[*] Running validators
[*] Validating plugin at .

[*] Running Integration Validators...
[*] Executing validator HelpValidator
[*] Executing validator ChangelogValidator
[*] Executing validator RequiredKeysValidator
[*] Executing validator UseCaseValidator
[*] Executing validator SpecPropertiesValidator
[*] Executing validator SpecVersionValidator
[*] Executing validator FilesValidator
[*] Executing validator TagValidator
[*] Executing validator DescriptionValidator
[*] Executing validator TitleValidator
[*] Executing validator VendorValidator
[*] Executing validator DefaultValueValidator
[*] Executing validator IconValidator
[*] Executing validator RequiredValidator
[*] Executing validator VersionValidator
[*] Executing validator DockerfileParentValidator
[*] Executing validator LoggingValidator
[*] Executing validator ProfanityValidator
[*] Executing validator AcronymValidator
[*] Executing validator JSONValidator
[*] Executing validator OutputValidator
[*] Executing validator RegenerationValidator
[*] Executing validator HelpInputOutputValidator
[*] Executing validator SupportValidator
[*] Plugin successfully validated!

----
[*] Total time elapsed: 364.248ms

[*] Validating spec with js-yaml
[SUCCESS] Passes js-yaml spec check


[*] Validating markdown...
[SUCCESS] Passes markdown linting

[*] Validating python files for style...
[SUCCESS] Passes flake8 linting

[*] Validating python files for security vulnerabilities...
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.7.6
Run started:2020-03-29 22:08:36.509502

Test results:
        No issues identified.

Code scanned:
        Total lines of code: 507
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
        Total issues (by confidence):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
Files skipped (0):
[SUCCESS] Passes bandit security checks

```

<summary>
make validate
</summary>
</details>
