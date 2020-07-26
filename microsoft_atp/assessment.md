## Assessment
### Run

<details>

```
{
  "body": {
    "log": "Connecting...\nTime Now: 1595778039.448557\nTime Ago: 0\nSeconds elapsed:1595778039\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************50vQw\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: get_machine_information\nRunning...\nTime Now: 1595778039.9974692\nTime Ago: 1595778039.994403\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAttempting to get information for machine ID: a542d20dceff077a189b84f8871747d674fb57a2\nTime Now: 1595778043.340414\nTime Ago: 1595778039.994403\nSeconds elapsed:3\nToken is valid, not refreshing.\nUpdating session headers.\n",
    "meta": {},
    "output": {
      "machine": {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Machines/$entity",
        "agentVersion": "10.5860.17763.1158",
        "computerDnsName": "msedgewin10",
        "deviceValue": "Normal",
        "exposureLevel": "Medium",
        "firstSeen": "2020-07-02T23:52:55.3516047Z",
        "healthStatus": "Inactive",
        "id": "a542d20dceff077a189b84f8871747d674fb57a2",
        "lastExternalIpAddress": "208.118.227.19",
        "lastIpAddress": "10.0.2.15",
        "lastSeen": "2020-07-09T13:58:12.0001411Z",
        "machineTags": [],
        "osBuild": 17763,
        "osPlatform": "Windows10",
        "osProcessor": "x64",
        "rbacGroupId": 0,
        "riskScore": "None",
        "version": "1809"
      }
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/01_get_machine_information_id.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "Connecting...\nTime Now: 1595778048.3811293\nTime Ago: 0\nSeconds elapsed:1595778048\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************j4AsA\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: get_machine_information\nRunning...\nTime Now: 1595778049.1033583\nTime Ago: 1595778049.0988588\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAttempting to get information for machine ID: a542d20dceff077a189b84f8871747d674fb57a2\nTime Now: 1595778049.7651772\nTime Ago: 1595778049.0988588\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\n",
    "meta": {},
    "output": {
      "machine": {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Machines/$entity",
        "agentVersion": "10.5860.17763.1158",
        "computerDnsName": "msedgewin10",
        "deviceValue": "Normal",
        "exposureLevel": "Medium",
        "firstSeen": "2020-07-02T23:52:55.3516047Z",
        "healthStatus": "Inactive",
        "id": "a542d20dceff077a189b84f8871747d674fb57a2",
        "lastExternalIpAddress": "208.118.227.19",
        "lastIpAddress": "10.0.2.15",
        "lastSeen": "2020-07-09T13:58:12.0001411Z",
        "machineTags": [],
        "osBuild": 17763,
        "osPlatform": "Windows10",
        "osProcessor": "x64",
        "rbacGroupId": 0,
        "riskScore": "None",
        "version": "1809"
      }
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/02_get_machine_information_external_IP.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "Connecting...\nTime Now: 1595778055.8682668\nTime Ago: 0\nSeconds elapsed:1595778055\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************TbbRg\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: get_machine_information\nRunning...\nTime Now: 1595778056.5684068\nTime Ago: 1595778056.5647938\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAttempting to get information for machine ID: a542d20dceff077a189b84f8871747d674fb57a2\nTime Now: 1595778057.9167783\nTime Ago: 1595778056.5647938\nSeconds elapsed:1\nToken is valid, not refreshing.\nUpdating session headers.\n",
    "meta": {},
    "output": {
      "machine": {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Machines/$entity",
        "agentVersion": "10.5860.17763.1158",
        "computerDnsName": "msedgewin10",
        "deviceValue": "Normal",
        "exposureLevel": "Medium",
        "firstSeen": "2020-07-02T23:52:55.3516047Z",
        "healthStatus": "Inactive",
        "id": "a542d20dceff077a189b84f8871747d674fb57a2",
        "lastExternalIpAddress": "208.118.227.19",
        "lastIpAddress": "10.0.2.15",
        "lastSeen": "2020-07-09T13:58:12.0001411Z",
        "machineTags": [],
        "osBuild": 17763,
        "osPlatform": "Windows10",
        "osProcessor": "x64",
        "rbacGroupId": 0,
        "riskScore": "None",
        "version": "1809"
      }
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/03_get_machine_information_IP.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "Connecting...\nTime Now: 1595778061.2910986\nTime Ago: 0\nSeconds elapsed:1595778061\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************at6tg\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: get_machine_information\nRunning...\nTime Now: 1595778061.797926\nTime Ago: 1595778061.7945662\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAttempting to get information for machine ID: a542d20dceff077a189b84f8871747d674fb57a2\nTime Now: 1595778062.5049772\nTime Ago: 1595778061.7945662\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\n",
    "meta": {},
    "output": {
      "machine": {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Machines/$entity",
        "agentVersion": "10.5860.17763.1158",
        "computerDnsName": "msedgewin10",
        "deviceValue": "Normal",
        "exposureLevel": "Medium",
        "firstSeen": "2020-07-02T23:52:55.3516047Z",
        "healthStatus": "Inactive",
        "id": "a542d20dceff077a189b84f8871747d674fb57a2",
        "lastExternalIpAddress": "208.118.227.19",
        "lastIpAddress": "10.0.2.15",
        "lastSeen": "2020-07-09T13:58:12.0001411Z",
        "machineTags": [],
        "osBuild": 17763,
        "osPlatform": "Windows10",
        "osProcessor": "x64",
        "rbacGroupId": 0,
        "riskScore": "None",
        "version": "1809"
      }
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/04_get_machine_information_hostname.json
</summary>
</details>

<details>

```
{
  "body": {
    "error": "An error occurred during plugin execution!\n\nInvalid or unreachable endpoint provided. Verify the endpoint/URL/hostname configured in your plugin connection is correct.",
    "log": "Connecting...\nTime Now: 1595778067.5303385\nTime Ago: 0\nSeconds elapsed:1595778067\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************vBYFA\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: get_machine_information\nRunning...\nTime Now: 1595778067.979213\nTime Ago: 1595778067.977733\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nMachine not_exist not found\nAn error occurred during plugin execution!\n\nInvalid or unreachable endpoint provided. Verify the endpoint/URL/hostname configured in your plugin connection is correct.\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.8/site-packages/insightconnect_plugin_runtime-4.0.2-py3.8.egg/insightconnect_plugin_runtime/plugin.py\", line 307, in handle_step\n    output = self.start_step(\n  File \"/usr/local/lib/python3.8/site-packages/insightconnect_plugin_runtime-4.0.2-py3.8.egg/insightconnect_plugin_runtime/plugin.py\", line 428, in start_step\n    output = func(params)\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/actions/get_machine_information/action.py\", line 18, in run\n    machine_id = self.connection.client.find_first_machine(params.get(Input.MACHINE)).get(\"id\")\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/util/api.py\", line 76, in find_first_machine\n    raise PluginException(preset=PluginException.Preset.NOT_FOUND)\ninsightconnect_plugin_runtime.exceptions.PluginException: An error occurred during plugin execution!\n\nInvalid or unreachable endpoint provided. Verify the endpoint/URL/hostname configured in your plugin connection is correct.\n",
    "meta": {},
    "status": "error"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/05_get_machine_information_bad.json
</summary>
</details>

<details>

```
{
  "body": {
    "error": "An error occurred during plugin execution!\n\nInvalid or unreachable endpoint provided. Verify the endpoint/URL/hostname configured in your plugin connection is correct.",
    "log": "Connecting...\nTime Now: 1595778111.6909032\nTime Ago: 0\nSeconds elapsed:1595778111\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************gR5eA\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: isolate_machine\nRunning...\nTime Now: 1595778112.1128569\nTime Ago: 1595778112.10919\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nMachine not_exist not found\nAn error occurred during plugin execution!\n\nInvalid or unreachable endpoint provided. Verify the endpoint/URL/hostname configured in your plugin connection is correct.\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.8/site-packages/insightconnect_plugin_runtime-4.0.2-py3.8.egg/insightconnect_plugin_runtime/plugin.py\", line 307, in handle_step\n    output = self.start_step(\n  File \"/usr/local/lib/python3.8/site-packages/insightconnect_plugin_runtime-4.0.2-py3.8.egg/insightconnect_plugin_runtime/plugin.py\", line 428, in start_step\n    output = func(params)\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/actions/isolate_machine/action.py\", line 18, in run\n    machine_id = self.connection.client.find_first_machine(params.get(Input.MACHINE)).get(\"id\")\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/util/api.py\", line 76, in find_first_machine\n    raise PluginException(preset=PluginException.Preset.NOT_FOUND)\ninsightconnect_plugin_runtime.exceptions.PluginException: An error occurred during plugin execution!\n\nInvalid or unreachable endpoint provided. Verify the endpoint/URL/hostname configured in your plugin connection is correct.\n",
    "meta": {},
    "status": "error"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/06_isolate_machine_bad_name.json
</summary>
</details>

<details>

```
{
  "body": {
    "error": "An error occurred during plugin execution!\n\nInvalid or unreachable endpoint provided. Verify the endpoint/URL/hostname configured in your plugin connection is correct.",
    "log": "Connecting...\nTime Now: 1595778116.0043244\nTime Ago: 0\nSeconds elapsed:1595778116\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************Efsaw\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: unisolate_machine\nRunning...\nTime Now: 1595778116.4258034\nTime Ago: 1595778116.4243479\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nMachine not_exist not found\nAn error occurred during plugin execution!\n\nInvalid or unreachable endpoint provided. Verify the endpoint/URL/hostname configured in your plugin connection is correct.\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.8/site-packages/insightconnect_plugin_runtime-4.0.2-py3.8.egg/insightconnect_plugin_runtime/plugin.py\", line 307, in handle_step\n    output = self.start_step(\n  File \"/usr/local/lib/python3.8/site-packages/insightconnect_plugin_runtime-4.0.2-py3.8.egg/insightconnect_plugin_runtime/plugin.py\", line 428, in start_step\n    output = func(params)\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/actions/unisolate_machine/action.py\", line 18, in run\n    machine_id = self.connection.client.find_first_machine(params.get(Input.MACHINE)).get(\"id\")\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/util/api.py\", line 76, in find_first_machine\n    raise PluginException(preset=PluginException.Preset.NOT_FOUND)\ninsightconnect_plugin_runtime.exceptions.PluginException: An error occurred during plugin execution!\n\nInvalid or unreachable endpoint provided. Verify the endpoint/URL/hostname configured in your plugin connection is correct.\n",
    "meta": {},
    "status": "error"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/07_unisolate_machine_bad_name.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "Connecting...\nTime Now: 1595778120.6259418\nTime Ago: 0\nSeconds elapsed:1595778120\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************TI0Xg\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: isolate_machine\nRunning...\nTime Now: 1595778121.3039231\nTime Ago: 1595778121.3015966\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAttempting to isolate machine id: a542d20dceff077a189b84f8871747d674fb57a2\nTime Now: 1595778121.761878\nTime Ago: 1595778121.3015966\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAction is already in progress\n",
    "meta": {},
    "output": {
      "machine_isolation_response": {
        "status": "Action is already in progress"
      }
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/08_isolate_machine_in_progress.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "Connecting...\nTime Now: 1595778130.6629694\nTime Ago: 0\nSeconds elapsed:1595778130\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************ZYXtA\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: unisolate_machine\nRunning...\nTime Now: 1595778131.3838422\nTime Ago: 1595778131.3824573\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAttempting to unisolate machine id: a542d20dceff077a189b84f8871747d674fb57a2\nTime Now: 1595778131.7877243\nTime Ago: 1595778131.3824573\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAction is already in progress\n",
    "meta": {},
    "output": {
      "machine_isolation_response": {
        "status": "Action is already in progress"
      }
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/09_unisolate_machine_in_progress.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "Connecting...\nTime Now: 1595778144.6548288\nTime Ago: 0\nSeconds elapsed:1595778144\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************vrehQ\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: run_antivirus_scan\nRunning...\nTime Now: 1595778145.3474581\nTime Ago: 1595778145.3425195\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAttempting to run a Quick antivirus scan on machine id: a542d20dceff077a189b84f8871747d674fb57a2\nRun Antivirus Scan with machine id: a542d20dceff077a189b84f8871747d674fb57a2, scan Type: Quick, comment: run antivirus scan\nTime Now: 1595778145.7667353\nTime Ago: 1595778145.3425195\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAction is already in progress\n",
    "meta": {},
    "output": {
      "machine_action_response": {
        "status": "Action is already in progress"
      }
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/10_run_antivirus_scan_bad_in_progress.json
</summary>
</details>

<details>

```
{
  "body": {
    "error": "An error occurred during plugin execution!\n\nSomething unexpected occurred. Check the logs and if the issue persists please contact support. Response was: {\"error\":{\"code\":\"ResourceNotFound\",\"message\":\"Sha1 04ac748e29caab6416d2460217c3ccade8406f39 was not found in machine a542d20dceff077a189b84f8871747d674fb57a2\",\"target\":\"3623eb65-e788-4957-b005-e57df329f176\"}}",
    "log": "Connecting...\nTime Now: 1595778154.3016372\nTime Ago: 0\nSeconds elapsed:1595778154\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************mRjKA\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: stop_and_quarantine_file\nRunning...\nTime Now: 1595778154.728581\nTime Ago: 1595778154.7272258\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAttempting to stop and quarantine file: 04ac748e29caab6416d2460217c3ccade8406f39\nAttempting to stop and quarantine file on machine: a542d20dceff077a189b84f8871747d674fb57a2\nStop and quarantine file with: a542d20dceff077a189b84f8871747d674fb57a2, SHA1_ID: 04ac748e29caab6416d2460217c3ccade8406f39, comment: stop and quarantine file\nTime Now: 1595778155.0172746\nTime Ago: 1595778154.7272258\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAn error occurred during plugin execution!\n\nSomething unexpected occurred. Check the logs and if the issue persists please contact support. Response was: {\"error\":{\"code\":\"ResourceNotFound\",\"message\":\"Sha1 04ac748e29caab6416d2460217c3ccade8406f39 was not found in machine a542d20dceff077a189b84f8871747d674fb57a2\",\"target\":\"3623eb65-e788-4957-b005-e57df329f176\"}}\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.8/site-packages/insightconnect_plugin_runtime-4.0.2-py3.8.egg/insightconnect_plugin_runtime/plugin.py\", line 307, in handle_step\n    output = self.start_step(\n  File \"/usr/local/lib/python3.8/site-packages/insightconnect_plugin_runtime-4.0.2-py3.8.egg/insightconnect_plugin_runtime/plugin.py\", line 428, in start_step\n    output = func(params)\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/actions/stop_and_quarantine_file/action.py\", line 24, in run\n    response = self.connection.stop_and_quarantine_file(machine_id, sha1_id, comment)\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/connection/connection.py\", line 37, in stop_and_quarantine_file\n    return self.client.stop_and_quarantine_file(machine_id, sha1_id, comment)\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/util/api.py\", line 111, in stop_and_quarantine_file\n    return self._make_request(\"POST\", f\"machines/{machine_id}/StopAndQuarantineFile\", json_data={\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/util/api.py\", line 128, in _make_request\n    return self._call_api(\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/util/api.py\", line 165, in _call_api\n    raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)\ninsightconnect_plugin_runtime.exceptions.PluginException: An error occurred during plugin execution!\n\nSomething unexpected occurred. Check the logs and if the issue persists please contact support. Response was: {\"error\":{\"code\":\"ResourceNotFound\",\"message\":\"Sha1 04ac748e29caab6416d2460217c3ccade8406f39 was not found in machine a542d20dceff077a189b84f8871747d674fb57a2\",\"target\":\"3623eb65-e788-4957-b005-e57df329f176\"}}\n",
    "meta": {},
    "status": "error"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/11_stop_and_quarantine_file_id_bad.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "Connecting...\nTime Now: 1595778158.8808384\nTime Ago: 0\nSeconds elapsed:1595778158\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************G5PbQ\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: get_file_id_from_alert_id\nRunning...\nLooking for alerts matching ID: da637293198146839977_2089064327\nTime Now: 1595778159.5619826\nTime Ago: 1595778159.560856\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\n",
    "meta": {},
    "output": {
      "file_list": [
        {
          "determinationType": "Unknown",
          "determinationValue": "HackTool:MSIL/AutoKms",
          "globalFirstObserved": "2015-11-01T02:48:27.1103102Z",
          "globalLastObserved": "2020-07-25T19:59:00.4121214Z",
          "globalPrevalence": 488,
          "isPeFile": true,
          "isValidCertificate": false,
          "md5": "a69acb01b99959efec7c0a2a8caa7545",
          "sha1": "f093e7767bb63ac973b697d3fd1d40a78b87b8bf",
          "sha256": "470a75fe3da2ddf9d27fb3f9c96e6c665506ea7ba26ab89f0c89606f678ae4a2",
          "signerHash": "006276223396f7510653e20f0d10cd1a5d97176e",
          "size": 740544
        },
        {
          "determinationType": "Unknown",
          "determinationValue": "HackTool:Win32/AutoKMS",
          "globalFirstObserved": "2015-11-01T02:48:27.1103102Z",
          "globalLastObserved": "2020-07-25T19:50:43.5748852Z",
          "globalPrevalence": 460,
          "isPeFile": true,
          "isValidCertificate": false,
          "md5": "bd8cb75cd1d80a311d72db68b7bde770",
          "sha1": "ad0c0f2fa80411788e81a4567d1d8758b83cd76e",
          "sha256": "88f11abdd3e82c4ff30c0b67d4af73e10df6f83d6cbe0ce4f94fc2b2ebc013b8",
          "signerHash": "006276223396f7510653e20f0d10cd1a5d97176e",
          "size": 3210792
        },
        {
          "determinationType": "Unknown",
          "determinationValue": "HackTool:Win32/AutoKMS",
          "globalFirstObserved": "2014-09-01T10:04:05.0745759Z",
          "globalLastObserved": "2020-07-26T05:14:09.9641725Z",
          "globalPrevalence": 4500,
          "isPeFile": false,
          "md5": "d228137b7b77d7ef3fcdc06ddabebeef",
          "sha1": "9415587011a75484fce405287a548d488973fd09",
          "sha256": "0552a48861a2c9825d51eeb0197a959dc85e4e960fb00cee89ccc4806eaadba8",
          "size": 146
        },
        {
          "determinationType": "Unknown",
          "determinationValue": "HackTool:MSIL/AutoKMS",
          "globalFirstObserved": "2015-11-01T05:02:30.9429013Z",
          "globalLastObserved": "2020-07-25T19:58:59.6769456Z",
          "globalPrevalence": 494,
          "isPeFile": true,
          "isValidCertificate": false,
          "md5": "ea4137f439c07464c8094c90fce47084",
          "sha1": "d20b2eb35b9ea7978bafd6138d1dbe8d04383dc6",
          "sha256": "91539a89fb6531ad4e52e8b19bfe02ec4cbb22393bc0058cc15f56d926017ac7",
          "signerHash": "006276223396f7510653e20f0d10cd1a5d97176e",
          "size": 925376
        },
        {
          "determinationType": "Unknown",
          "determinationValue": "HackTool:Win32/AutoKMS",
          "globalFirstObserved": "2014-10-12T15:17:19.3829568Z",
          "globalLastObserved": "2020-07-26T05:13:58.7297523Z",
          "globalPrevalence": 1259,
          "isPeFile": false,
          "md5": "3d9673422f0cdd485ade60ac1abb2f62",
          "sha1": "04ac748e29caab6416d2460217c3ccade8406f39",
          "sha256": "7339a4cc48220a161fcc737ed26e99e5678a4d1faa3f7e2686c46b5a5d234828",
          "size": 365
        },
        {
          "determinationType": "Unknown",
          "determinationValue": "HackTool:Win32/AutoKMS",
          "globalFirstObserved": "2013-11-12T18:50:39.0695598Z",
          "globalLastObserved": "2020-07-26T05:12:59.5732481Z",
          "globalPrevalence": 2866,
          "isPeFile": false,
          "md5": "ec0220e538223df10e4ccaedceaa1e3a",
          "sha1": "4bf98d8a88490b911a050a982296a78be890c592",
          "sha256": "784e531d9e132f24f622b3eb74bec791d2843912a28c25b28a1be09e9e771c9b",
          "size": 175
        }
      ]
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/12_get_file_id_from_alert_id.json
</summary>
</details>

<details>

```
{
  "body": {
    "error": "An error occurred during plugin execution!\n\nSomething unexpected occurred. Check the logs and if the issue persists please contact support. Response was: {\"error\":{\"code\":\"ResourceNotFound\",\"message\":\"Alert not_exist not found\",\"target\":\"fa354014-2f27-4a41-bb12-2d3767933945\"}}",
    "log": "Connecting...\nTime Now: 1595778164.767826\nTime Ago: 0\nSeconds elapsed:1595778164\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************4FBdw\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: get_file_id_from_alert_id\nRunning...\nLooking for alerts matching ID: not_exist\nTime Now: 1595778165.4390006\nTime Ago: 1595778165.4374418\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAn error occurred during plugin execution!\n\nSomething unexpected occurred. Check the logs and if the issue persists please contact support. Response was: {\"error\":{\"code\":\"ResourceNotFound\",\"message\":\"Alert not_exist not found\",\"target\":\"fa354014-2f27-4a41-bb12-2d3767933945\"}}\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.8/site-packages/insightconnect_plugin_runtime-4.0.2-py3.8.egg/insightconnect_plugin_runtime/plugin.py\", line 307, in handle_step\n    output = self.start_step(\n  File \"/usr/local/lib/python3.8/site-packages/insightconnect_plugin_runtime-4.0.2-py3.8.egg/insightconnect_plugin_runtime/plugin.py\", line 428, in start_step\n    output = func(params)\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/actions/get_file_id_from_alert_id/action.py\", line 20, in run\n    file_payload = self.connection.get_files_from_id(alert_id)\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/connection/connection.py\", line 46, in get_files_from_id\n    return self.client.get_files_from_id(alert_id)\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/util/api.py\", line 85, in get_files_from_id\n    return self._make_request(\"GET\", f\"alerts/{alert_id}/files\")\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/util/api.py\", line 128, in _make_request\n    return self._call_api(\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/util/api.py\", line 165, in _call_api\n    raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)\ninsightconnect_plugin_runtime.exceptions.PluginException: An error occurred during plugin execution!\n\nSomething unexpected occurred. Check the logs and if the issue persists please contact support. Response was: {\"error\":{\"code\":\"ResourceNotFound\",\"message\":\"Alert not_exist not found\",\"target\":\"fa354014-2f27-4a41-bb12-2d3767933945\"}}\n",
    "meta": {},
    "status": "error"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/13_get_file_id_from_alert_id_bad.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "Connecting...\nTime Now: 1595778168.8661973\nTime Ago: 0\nSeconds elapsed:1595778168\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************VxakA\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: get_machine_action\nRunning...\nAttempting to get action for action ID: f442c95f-2b29-4152-b179-24181d343ec6\nTime Now: 1595778169.2969294\nTime Ago: 1595778169.2948396\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\n",
    "meta": {},
    "output": {
      "machine_action_response": {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
        "commands": [],
        "computerDnsName": "msedgewin10",
        "creationDateTimeUtc": "2020-07-06T19:27:22.973464Z",
        "errorHResult": 0,
        "id": "f442c95f-2b29-4152-b179-24181d343ec6",
        "lastUpdateDateTimeUtc": "2020-07-06T19:27:57.7626631Z",
        "machineId": "a542d20dceff077a189b84f8871747d674fb57a2",
        "requestSource": "Unspecified",
        "requestor": "82f42fca-e931-4f03-b54c-47af94bd394d",
        "requestorComment": "Run virus scan",
        "scope": "Quick",
        "status": "Succeeded",
        "type": "RunAntiVirusScan"
      }
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/14_get_machine_action.json
</summary>
</details>

<details>

```
{
  "body": {
    "error": "An error occurred during plugin execution!\n\nSomething unexpected occurred. Check the logs and if the issue persists please contact support.",
    "log": "Connecting...\nTime Now: 1595778172.7482176\nTime Ago: 0\nSeconds elapsed:1595778172\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************_5gHQ\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: get_machine_action\nRunning...\nAttempting to get action for action ID: not_exist\nTime Now: 1595778173.4145162\nTime Ago: 1595778173.4132667\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\nAn error occurred during plugin execution!\n\nSomething unexpected occurred. Check the logs and if the issue persists please contact support.\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.8/site-packages/insightconnect_plugin_runtime-4.0.2-py3.8.egg/insightconnect_plugin_runtime/plugin.py\", line 307, in handle_step\n    output = self.start_step(\n  File \"/usr/local/lib/python3.8/site-packages/insightconnect_plugin_runtime-4.0.2-py3.8.egg/insightconnect_plugin_runtime/plugin.py\", line 428, in start_step\n    output = func(params)\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/actions/get_machine_action/action.py\", line 21, in run\n    response = self.connection.get_machine_action(action_id)\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/connection/connection.py\", line 43, in get_machine_action\n    return self.client.get_machine_action(action_id)\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/util/api.py\", line 63, in get_machine_action\n    return self._make_request(\"GET\", f\"machineactions/{action_id}\")\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/util/api.py\", line 128, in _make_request\n    return self._call_api(\n  File \"/usr/local/lib/python3.8/site-packages/microsoft_atp_rapid7_plugin-2.0.0-py3.8.egg/komand_microsoft_atp/util/api.py\", line 165, in _call_api\n    raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)\ninsightconnect_plugin_runtime.exceptions.PluginException: An error occurred during plugin execution!\n\nSomething unexpected occurred. Check the logs and if the issue persists please contact support.\n",
    "meta": {},
    "status": "error"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug run < tests/15_get_machine_action_bad.json
</summary>
</details>

### Test

Autogenerate with:
<details>

```
{
  "body": {
    "log": "Connecting...\nTime Now: 1595778176.7717915\nTime Ago: 0\nSeconds elapsed:1595778176\nRefreshing auth token\nUpdating Auth Token...\nGetting token from: https://login.windows.net/5c824599-dc8c-4d31-96fb-3b886d4f8f10/oauth2/token\nAuthentication was successful, token is: ******************Eha3A\nrapid7/Microsoft Windows Defender ATP:2.0.0. Step name: get_machine_information\nTime Now: 1595778177.2135217\nTime Ago: 1595778177.2132194\nSeconds elapsed:0\nToken is valid, not refreshing.\nUpdating session headers.\n",
    "meta": {},
    "output": {
      "status": true
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/microsoft_atp:2.0.0 --debug test < tests/01_get_machine_information_id.json
</summary>
</details>

### Validate

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
[*] Executing validator RuntimeValidator
[*] Executing validator ExceptionValidator
[*] Executing validator CredentialsValidator
[*] Executing validator PasswordValidator
[*] Executing validator PrintValidator
[*] Executing validator ConfidentialValidator
[*] Executing validator DockerValidator
[*] Executing validator URLValidator
WARNING: URLs found that return a 4xx code. Verify they are publicly accessible and if not, update with a working URL.
violation: help.md[173]: https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity
violation: help.md[216]: https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity
violation: help.md[261]: https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity
violation: help.md[309]: https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity
violation: help.md[350]: https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity
[*] Plugin successfully validated!

----
[*] Total time elapsed: 59768.780999999995ms

```

<summary>
icon-validate --all .
</summary>
</details>