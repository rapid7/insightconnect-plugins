# Description

The VMRay plugin allows the user to submit files or URLs for malware analysis with VMRay on-premise or VMRay Cloud.

[VMRay](https://www.vmray.com) delivers advanced threat analysis and detection that combines a unique agent-less hypervisor-based network sandbox with a real-time reputation engine.
The combination provides both fast, high volume file classification and in-depth malware analysis.
The VMRay Analyzer is platform independent and can be scaled, the result of a decade of R&D by some of the world's leading experts on dynamic malware analysis.
By monitoring at the hypervisor level, it is undetectable by malware running in the target operating system.
VMRay serves leading enterprises around the world.

This plugin utilizes the VMRay API. The API is gated and can be found on-premise at `http://vmrayhost/static_doc/html/api/User_API_Reference.html` or in the [VMRay Cloud API documentation](https://cloud.vmray.com/static_doc/html/api/User_API_Reference.html).

# Key Features

* Submit a file or URL for analysis
* Get reports about files or URLs

# Requirements

* VMRay API key

# Supported Product Versions

* 2025-12-18

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|API key for VMRay|None|4SauhjkF9aANClXnIaLfAeE9RVBJnZZ8|None|None|
|url|string|https://cloud.vmray.com|True|The VMRay host URL, both on-premise and cloud is supported|None|https://cloud.vmray.com|None|None|

Example input:

```
{
  "api_key": "4SauhjkF9aANClXnIaLfAeE9RVBJnZZ8",
  "url": "https://cloud.vmray.com"
}
```

## Technical Details

### Actions


#### Get Analysis

This action is used to get all dynamic and static analyses in the system or details about specific ones

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|False|ID based on ID type selected, leave blank if 'all' is selected|None|1490045|None|None|
|id_type|string|None|True|Get analysis based on ID of a specified type|["analysis_id", "analyzer", "configuration", "static_config", "created", "job", "jobrule", "job_started", "prescript", "result_code", "sample", "size", "snapshot", "submission", "user", "vm", "vmhost", "vti_score", "all"]|all|None|None|
|optional_params|object|None|False|Parameters that allow finer tuning of the Get Analysis action, e.g {"analysis_id": 12345}|None|{"analysis_id": 12345}|None|None|
  
Example input:

```
{
  "id": 1490045,
  "id_type": "all",
  "optional_params": {
    "analysis_id": 12345
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]analysis_result|False|Results returned from analysis|[{"analysis_analyzer_id": 1, "analysis_analyzer_name": "vmray", "analysis_analyzer_version": "2.1.0", "analysis_configuration_id": 48, "analysis_configuration_name": "exe", "analysis_created": "2018-02-20T13:00:50", "analysis_id": 1274140, "analysis_ioc_aggregation_state": "ok", "analysis_job_id": 1275657, "analysis_job_started": "2018-02-20T13:00:50", "analysis_job_type": "full_analysis", "analysis_prescript_force_admin": false, "analysis_priority": 5, "analysis_report_version": 1, "analysis_result_code": 1, "analysis_result_str": "Operation completed successfully", "analysis_sample_id": 1358016, "analysis_sample_md5": "9159edb64c4a21d8888d088bf2db23f3", "analysis_sample_sha1": "124f46228d1e220d88ae5e9a24d6e713039a64f9", "analysis_sample_sha256": "2180f4a13add5e346e8cf6994876a9d2f5eac3fcb695db8569537010d24cd6d5", "analysis_sample_ssdeep": "1536:tI05L48IVDAQVzZpJyrOM1GhFNkYL2BxNRj:tI05LBIDAuztyrOMGTkrNRj", "analysis_serialized_result": { "code": 1, "extra_args": {}, "fmt_args": [] }, "analysis_severity": "suspicious", "analysis_size": 3442135, "analysis_snapshot_id": 1, "analysis_snapshot_name": "def", "analysis_submission_id": 1490045, "analysis_tags": [], "analysis_user_email": "user@example.com", "analysis_user_id": 88, "analysis_vm_id": 9, "analysis_vm_name": "win7_64_sp1", "analysis_vmhost_id": 4, "analysis_vmhost_name": "cloud-worker-02", "analysis_vti_aggregation_state": "ok", "analysis_vti_built_in_rules_version": 2.7, "analysis_vti_custom_rules_hash": "d41d8cd98f00b204e9800998ecf8427e", "analysis_vti_score": 70, "analysis_webif_url": "https://cloud.vmray.com/user/analysis/view?id=1274140&sub=%2Freport%2Foverview.html", "analysis_yara_latest_ruleset_date": "2018-02-20T09:55:45", "analysis_yara_match_count": 0 }, { "analysis_analyzer_id": 1, "analysis_analyzer_name": "vmray", "analysis_analyzer_version": "2.2.0", "analysis_configuration_id": 48, "analysis_configuration_name": "exe", "analysis_created": "2017-11-29T12:06:39", "analysis_id": 1153556, "analysis_ioc_aggregation_state": "ok", "analysis_job_id": 1153785, "analysis_job_started": "2017-11-29T12:06:39", "analysis_job_type": "full_analysis", "analysis_prescript_force_admin": false, "analysis_priority": 1, "analysis_result_code": 1, "analysis_result_str": "Operation completed successfully", "analysis_sample_id": 1358016, "analysis_sample_md5": "9159edb64c4a21d8888d088bf2db23f3", "analysis_sample_sha1": "124f46228d1e220d88ae5e9a24d6e713039a64f9", "analysis_sample_sha256": "2180f4a13add5e346e8cf6994876a9d2f5eac3fcb695db8569537010d24cd6d5", "analysis_sample_ssdeep": "1536:tI05L48IVDAQVzZpJyrOM1GhFNkYL2BxNRj:tI05LBIDAuztyrOMGTkrNRj", "analysis_serialized_result": { "code": 1, "extra_args": {}, "fmt_args": [] }, "analysis_severity": "suspicious", "analysis_size": 3317008, "analysis_snapshot_id": 1, "analysis_snapshot_name": "def", "analysis_submission_id": 1490045, "analysis_tags": [], "analysis_user_email": "user@example.com", "analysis_user_id": 88, "analysis_vm_id": 9, "analysis_vm_name": "win7_64_sp1", "analysis_vmhost_id": 3, "analysis_vmhost_name": "cloud-worker-01", "analysis_vti_aggregation_state": "ok", "analysis_vti_built_in_rules_version": 2.6, "analysis_vti_custom_rules_hash": "d41d8cd98f00b204e9800998ecf8427e", "analysis_vti_score": 70, "analysis_webif_url": "https://cloud.vmray.com/user/analysis/view?id=1153556&sub=%2Freport%2Foverview.html", "analysis_yara_latest_ruleset_date": "2017-08-01T13:06:11", "analysis_yara_match_count": 0}]|
  
Example output:

```
{
  "results": [
    {
      "analysis_analyzer_id": 1,
      "analysis_analyzer_name": "vmray",
      "analysis_analyzer_version": "2.1.0",
      "analysis_configuration_id": 48,
      "analysis_configuration_name": "exe",
      "analysis_created": "2018-02-20T13:00:50",
      "analysis_id": 1274140,
      "analysis_ioc_aggregation_state": "ok",
      "analysis_job_id": 1275657,
      "analysis_job_started": "2018-02-20T13:00:50",
      "analysis_job_type": "full_analysis",
      "analysis_prescript_force_admin": false,
      "analysis_priority": 5,
      "analysis_report_version": 1,
      "analysis_result_code": 1,
      "analysis_result_str": "Operation completed successfully",
      "analysis_sample_id": 1358016,
      "analysis_sample_md5": "9159edb64c4a21d8888d088bf2db23f3",
      "analysis_sample_sha1": "124f46228d1e220d88ae5e9a24d6e713039a64f9",
      "analysis_sample_sha256": "2180f4a13add5e346e8cf6994876a9d2f5eac3fcb695db8569537010d24cd6d5",
      "analysis_sample_ssdeep": "1536:tI05L48IVDAQVzZpJyrOM1GhFNkYL2BxNRj:tI05LBIDAuztyrOMGTkrNRj",
      "analysis_serialized_result": {
        "code": 1,
        "extra_args": {},
        "fmt_args": []
      },
      "analysis_severity": "suspicious",
      "analysis_size": 3442135,
      "analysis_snapshot_id": 1,
      "analysis_snapshot_name": "def",
      "analysis_submission_id": 1490045,
      "analysis_tags": [],
      "analysis_user_email": "user@example.com",
      "analysis_user_id": 88,
      "analysis_vm_id": 9,
      "analysis_vm_name": "win7_64_sp1",
      "analysis_vmhost_id": 4,
      "analysis_vmhost_name": "cloud-worker-02",
      "analysis_vti_aggregation_state": "ok",
      "analysis_vti_built_in_rules_version": 2.7,
      "analysis_vti_custom_rules_hash": "d41d8cd98f00b204e9800998ecf8427e",
      "analysis_vti_score": 70,
      "analysis_webif_url": "https://cloud.vmray.com/user/analysis/view?id=1274140&sub=%2Freport%2Foverview.html",
      "analysis_yara_latest_ruleset_date": "2018-02-20T09:55:45",
      "analysis_yara_match_count": 0
    },
    {
      "analysis_analyzer_id": 1,
      "analysis_analyzer_name": "vmray",
      "analysis_analyzer_version": "2.2.0",
      "analysis_configuration_id": 48,
      "analysis_configuration_name": "exe",
      "analysis_created": "2017-11-29T12:06:39",
      "analysis_id": 1153556,
      "analysis_ioc_aggregation_state": "ok",
      "analysis_job_id": 1153785,
      "analysis_job_started": "2017-11-29T12:06:39",
      "analysis_job_type": "full_analysis",
      "analysis_prescript_force_admin": false,
      "analysis_priority": 1,
      "analysis_result_code": 1,
      "analysis_result_str": "Operation completed successfully",
      "analysis_sample_id": 1358016,
      "analysis_sample_md5": "9159edb64c4a21d8888d088bf2db23f3",
      "analysis_sample_sha1": "124f46228d1e220d88ae5e9a24d6e713039a64f9",
      "analysis_sample_sha256": "2180f4a13add5e346e8cf6994876a9d2f5eac3fcb695db8569537010d24cd6d5",
      "analysis_sample_ssdeep": "1536:tI05L48IVDAQVzZpJyrOM1GhFNkYL2BxNRj:tI05LBIDAuztyrOMGTkrNRj",
      "analysis_serialized_result": {
        "code": 1,
        "extra_args": {},
        "fmt_args": []
      },
      "analysis_severity": "suspicious",
      "analysis_size": 3317008,
      "analysis_snapshot_id": 1,
      "analysis_snapshot_name": "def",
      "analysis_submission_id": 1490045,
      "analysis_tags": [],
      "analysis_user_email": "user@example.com",
      "analysis_user_id": 88,
      "analysis_vm_id": 9,
      "analysis_vm_name": "win7_64_sp1",
      "analysis_vmhost_id": 3,
      "analysis_vmhost_name": "cloud-worker-01",
      "analysis_vti_aggregation_state": "ok",
      "analysis_vti_built_in_rules_version": 2.6,
      "analysis_vti_custom_rules_hash": "d41d8cd98f00b204e9800998ecf8427e",
      "analysis_vti_score": 70,
      "analysis_webif_url": "https://cloud.vmray.com/user/analysis/view?id=1153556&sub=%2Freport%2Foverview.html",
      "analysis_yara_latest_ruleset_date": "2017-08-01T13:06:11",
      "analysis_yara_match_count": 0
    }
  ]
}
```

#### Get Samples

This action is used to get all samples in the system or details about specific ones. You can also search by hashes

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|optional_params|object|None|False|Parameters that allow finer tuning of the Get Samples action, e.g {"analysis_id": 12345}|None|{"analysis_id": 12345}|None|None|
|sample|string|None|False|Sample ID, hash or type, leave blank if 'all' is selected|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|sample_type|string|None|True|Specified type of sample|["all", "sample_id", "created", "filesize", "md5", "sha1", "sha256", "type"]|md5|None|None|
  
Example input:

```
{
  "optional_params": {
    "analysis_id": 12345
  },
  "sample": "9de5069c5afe602b2ea0a04b66beb2c0",
  "sample_type": "md5"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]sample|False|Results from samples|[{"sample_classifications": [], "sample_created": "2018-12-03T14:41:09", "sample_filename": "lawl.jpg", "sample_filesize": 69847, "sample_id": 2117136, "sample_is_multipart": false, "sample_last_reputation_severity": "unknown", "sample_md5hash": "064caa4a102c0ace9d6ee06e45b68b1a", "sample_priority": 1, "sample_severity": "unknown", "sample_sha1hash": "fbfc0b783770e68ec5791702fde021cbd6a40480", "sample_sha256hash": "8843ef15c1915d0cfc270676c0df842577eac4ef54ccaa1ae78211dac1bbfc42", "sample_ssdeephash": "1536:3om6XPDy2/Spe0QixPTJmI0rKDJ80f1iPdDbUK4V+:33g/SU0Qi2trK1lClZB", "sample_type": "JPEG image data", "sample_webif_url": "https://cloud.vmray.com/user/sample/view?id=2117136"}]|
  
Example output:

```
{
  "results": [
    {
      "sample_classifications": [],
      "sample_created": "2018-12-03T14:41:09",
      "sample_filename": "lawl.jpg",
      "sample_filesize": 69847,
      "sample_id": 2117136,
      "sample_is_multipart": false,
      "sample_last_reputation_severity": "unknown",
      "sample_md5hash": "064caa4a102c0ace9d6ee06e45b68b1a",
      "sample_priority": 1,
      "sample_severity": "unknown",
      "sample_sha1hash": "fbfc0b783770e68ec5791702fde021cbd6a40480",
      "sample_sha256hash": "8843ef15c1915d0cfc270676c0df842577eac4ef54ccaa1ae78211dac1bbfc42",
      "sample_ssdeephash": "1536:3om6XPDy2/Spe0QixPTJmI0rKDJ80f1iPdDbUK4V+:33g/SU0Qi2trK1lClZB",
      "sample_type": "JPEG image data",
      "sample_webif_url": "https://cloud.vmray.com/user/sample/view?id=2117136"
    }
  ]
}
```

#### Submit File

This action is used to submit file for analysis

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|analyzer_mode|string|default|False|Specify what analyzer mode to use|["default", "reputation", "reputation_static", "reputation_static_dynamic", "static_dynamic", "static"]|default|None|None|
|file|file|None|True|File and filename for analysis|None|{"filename": "setup.exe", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="}|None|None|
|optional_params|object|None|False|Parameters that allow finer tuning of the Submit File action, e.g {"analysis_id": 12345}|None|{"analysis_id": 12345}|None|None|
  
Example input:

```
{
  "analyzer_mode": "default",
  "file": {
    "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
    "filename": "setup.exe"
  },
  "optional_params": {
    "analysis_id": 12345
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|submit_file|False|Results returned from submitting a URL|{ "data": { "errors": [], "jobs": [], "md_jobs": [], "reputation_jobs": [ { "reputation_job_created": "2018-12-03T16:22:32", "reputation_job_id": 154563, "reputation_job_priority": 1, "reputation_job_sample_id": 2101187, "reputation_job_sample_md5": "8c2d61c6a08d569afa1eb68b0ef2fb84", "reputation_job_sample_sha1": "5334037acc20b40923f2f458eeb61e776433536e", "reputation_job_sample_sha256": "fe13606bf1e79124bf6dac32edd5b4655eafd4d024cd36ffc93ceb05502bdd57", "reputation_job_sample_ssdeep": "24:xRc+/8Z8e68874Oa5HaKFL3hgjl8IuKlryRYtxuyshs8vtn:xRqYe/F3ayIuCruyshNn", "reputation_job_status": "queued", "reputation_job_statuschanged": "2018-12-03T16:22:32", "reputation_job_submission_id": 2361855, "reputation_job_user_email": "user@example.com", "reputation_job_user_id": 1099 } ], "samples": [ { "sample_created": "2018-11-29T19:37:09", "sample_filename": "fe13606bf1e79124bf6dac32edd5b4655eafd4d024cd36ffc93ceb05502bdd57", "sample_filesize": 8432, "sample_id": 2101187, "sample_is_multipart": false, "sample_md5hash": "8c2d61c6a08d569afa1eb68b0ef2fb84", "sample_priority": 1, "sample_sha1hash": "5334037acc20b40923f2f458eeb61e776433536e", "sample_sha256hash": "fe13606bf1e79124bf6dac32edd5b4655eafd4d024cd36ffc93ceb05502bdd57", "sample_ssdeephash": "24:xRc+/8Z8e68874Oa5HaKFL3hgjl8IuKlryRYtxuyshs8vtn:xRqYe/F3ayIuCruyshNn", "sample_type": "Mach-O 64-bit x86_64 executable", "sample_webif_url": "https://cloud.vmray.com/user/sample/view?id=2101187", "submission_filename": "a.out" } ], "static_jobs": [], "submissions": [ { "submission_analyzer_mode_analyzer_mode": "reputation_static_dynamic", "submission_analyzer_mode_enable_reputation": true, "submission_analyzer_mode_enable_triage": false, "submission_analyzer_mode_enable_whois": true, "submission_analyzer_mode_id": 971, "submission_created": "2018-12-03T16:22:32", "submission_filename": "a.out", "submission_finished": false, "submission_id": 2361855, "submission_ip_id": 1264, "submission_ip_ip": "64.125.235.6", "submission_known_configuration": false, "submission_original_filename": "a.out", "submission_prescript_force_admin": false, "submission_priority": 1, "submission_reputation_mode": "disabled", "submission_sample_id": 2101187, "submission_sample_md5": "8c2d61c6a08d569afa1eb68b0ef2fb84", "submission_sample_sha1": "5334037acc20b40923f2f458eeb61e776433536e", "submission_sample_sha256": "fe13606bf1e79124bf6dac32edd5b4655eafd4d024cd36ffc93ceb05502bdd57", "submission_sample_ssdeep": "24:xRc+/8Z8e68874Oa5HaKFL3hgjl8IuKlryRYtxuyshs8vtn:xRqYe/F3ayIuCruyshNn", "submission_shareable": false, "submission_tags": [], "submission_type": "api", "submission_user_account_id": 320, "submission_user_account_name": "Rapid7/Komand", "submission_user_account_subscription_mode": "free_account", "submission_user_email": "user@example.com", "submission_user_id": 1099, "submission_webif_url": "https://cloud.vmray.com/user/sample/view?id=2101187", "submission_whois_mode": "disabled" } ], "vt_jobs": [], "whois_jobs": [] }, "result": "ok" }|
  
Example output:

```
{
  "results": {
    "data": {
      "errors": [],
      "jobs": [],
      "md_jobs": [],
      "reputation_jobs": [
        {
          "reputation_job_created": "2018-12-03T16:22:32",
          "reputation_job_id": 154563,
          "reputation_job_priority": 1,
          "reputation_job_sample_id": 2101187,
          "reputation_job_sample_md5": "8c2d61c6a08d569afa1eb68b0ef2fb84",
          "reputation_job_sample_sha1": "5334037acc20b40923f2f458eeb61e776433536e",
          "reputation_job_sample_sha256": "fe13606bf1e79124bf6dac32edd5b4655eafd4d024cd36ffc93ceb05502bdd57",
          "reputation_job_sample_ssdeep": "24:xRc+/8Z8e68874Oa5HaKFL3hgjl8IuKlryRYtxuyshs8vtn:xRqYe/F3ayIuCruyshNn",
          "reputation_job_status": "queued",
          "reputation_job_statuschanged": "2018-12-03T16:22:32",
          "reputation_job_submission_id": 2361855,
          "reputation_job_user_email": "user@example.com",
          "reputation_job_user_id": 1099
        }
      ],
      "samples": [
        {
          "sample_created": "2018-11-29T19:37:09",
          "sample_filename": "fe13606bf1e79124bf6dac32edd5b4655eafd4d024cd36ffc93ceb05502bdd57",
          "sample_filesize": 8432,
          "sample_id": 2101187,
          "sample_is_multipart": false,
          "sample_md5hash": "8c2d61c6a08d569afa1eb68b0ef2fb84",
          "sample_priority": 1,
          "sample_sha1hash": "5334037acc20b40923f2f458eeb61e776433536e",
          "sample_sha256hash": "fe13606bf1e79124bf6dac32edd5b4655eafd4d024cd36ffc93ceb05502bdd57",
          "sample_ssdeephash": "24:xRc+/8Z8e68874Oa5HaKFL3hgjl8IuKlryRYtxuyshs8vtn:xRqYe/F3ayIuCruyshNn",
          "sample_type": "Mach-O 64-bit x86_64 executable",
          "sample_webif_url": "https://cloud.vmray.com/user/sample/view?id=2101187",
          "submission_filename": "a.out"
        }
      ],
      "static_jobs": [],
      "submissions": [
        {
          "submission_analyzer_mode_analyzer_mode": "reputation_static_dynamic",
          "submission_analyzer_mode_enable_reputation": true,
          "submission_analyzer_mode_enable_triage": false,
          "submission_analyzer_mode_enable_whois": true,
          "submission_analyzer_mode_id": 971,
          "submission_created": "2018-12-03T16:22:32",
          "submission_filename": "a.out",
          "submission_finished": false,
          "submission_id": 2361855,
          "submission_ip_id": 1264,
          "submission_ip_ip": "64.125.235.6",
          "submission_known_configuration": false,
          "submission_original_filename": "a.out",
          "submission_prescript_force_admin": false,
          "submission_priority": 1,
          "submission_reputation_mode": "disabled",
          "submission_sample_id": 2101187,
          "submission_sample_md5": "8c2d61c6a08d569afa1eb68b0ef2fb84",
          "submission_sample_sha1": "5334037acc20b40923f2f458eeb61e776433536e",
          "submission_sample_sha256": "fe13606bf1e79124bf6dac32edd5b4655eafd4d024cd36ffc93ceb05502bdd57",
          "submission_sample_ssdeep": "24:xRc+/8Z8e68874Oa5HaKFL3hgjl8IuKlryRYtxuyshs8vtn:xRqYe/F3ayIuCruyshNn",
          "submission_shareable": false,
          "submission_tags": [],
          "submission_type": "api",
          "submission_user_account_id": 320,
          "submission_user_account_name": "Rapid7/Komand",
          "submission_user_account_subscription_mode": "free_account",
          "submission_user_email": "user@example.com",
          "submission_user_id": 1099,
          "submission_webif_url": "https://cloud.vmray.com/user/sample/view?id=2101187",
          "submission_whois_mode": "disabled"
        }
      ],
      "vt_jobs": [],
      "whois_jobs": []
    },
    "result": "ok"
  }
}
```

#### Submit URL

This action is used to submits a URL for analysis

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|analyzer_mode|string|default|False|Specify what analyzer mode to use|["default", "reputation", "reputation_static", "reputation_static_dynamic", "static_dynamic", "static"]|default|None|None|
|optional_params|object|None|False|Parameters that allow finer tuning of the Submit URL action, e.g {"analysis_id": 12345}|None|{"analysis_id": 12345}|None|None|
|url|string|None|True|URL to be submitted for analysis|None|https://example.com|None|None|
  
Example input:

```
{
  "analyzer_mode": "default",
  "optional_params": {
    "analysis_id": 12345
  },
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|submit_url|False|Results returned from submitting a URL|{ "errors": [], "jobs": [ { "job_analyzer_id": 1, "job_analyzer_name": "vmray", "job_configuration_id": 54, "job_configuration_name": "ie", "job_created": "2018-12-03T16:37:00", "job_id": 2365712, "job_jobrule_id": 5, "job_jobrule_sampletype": "URL", "job_prescript_force_admin": false, "job_priority": 1, "job_reputation_job_id": 154567, "job_sample_id": 2118603, "job_sample_md5": "e3c04a783dae53fae0422e3a955bc02a", "job_sample_sha1": "f420470addba27b8577bb40e02229e90af568d69", "job_sample_sha256": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40", "job_sample_ssdeep": "3:EPK:YK", "job_snapshot_id": 1, "job_snapshot_name": "def", "job_status": "queued", "job_statuschanged": "2018-12-03T16:37:00", "job_submission_id": 2361900, "job_tracking_state": "//waiting", "job_type": "full_analysis", "job_user_email": "user@example.com", "job_user_id": 1099, "job_vm_id": 9, "job_vm_name": "win7_64_sp1", "job_vnc_token": "ZUq2Xg2KnGEK9CFAcU2PuU67dieYMtpm" }, { "job_analyzer_id": 1, "job_analyzer_name": "vmray", "job_configuration_id": 54, "job_configuration_name": "ie", "job_created": "2018-12-03T16:37:00", "job_id": 2365713, "job_jobrule_id": 5, "job_jobrule_sampletype": "URL", "job_prescript_force_admin": false, "job_priority": 1, "job_reputation_job_id": 154567, "job_sample_id": 2118603, "job_sample_md5": "e3c04a783dae53fae0422e3a955bc02a", "job_sample_sha1": "f420470addba27b8577bb40e02229e90af568d69", "job_sample_sha256": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40", "job_sample_ssdeep": "3:EPK:YK", "job_snapshot_id": 1, "job_snapshot_name": "def", "job_status": "queued", "job_statuschanged": "2018-12-03T16:37:00", "job_submission_id": 2361900, "job_tracking_state": "//waiting", "job_type": "full_analysis", "job_user_email": "user@example.com", "job_user_id": 1099, "job_vm_id": 17, "job_vm_name": "win7_32_sp1", "job_vnc_token": "nSnAmqNnXm6FX57Dqc0wqwZOISA9FXWq" }, { "job_analyzer_id": 1, "job_analyzer_name": "vmray", "job_configuration_id": 54, "job_configuration_name": "ie", "job_created": "2018-12-03T16:37:00", "job_id": 2365714, "job_jobrule_id": 5, "job_jobrule_sampletype": "URL", "job_prescript_force_admin": false, "job_priority": 1, "job_reputation_job_id": 154567, "job_sample_id": 2118603, "job_sample_md5": "e3c04a783dae53fae0422e3a955bc02a", "job_sample_sha1": "f420470addba27b8577bb40e02229e90af568d69", "job_sample_sha256": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40", "job_sample_ssdeep": "3:EPK:YK", "job_snapshot_id": 1, "job_snapshot_name": "def", "job_status": "queued", "job_statuschanged": "2018-12-03T16:37:00", "job_submission_id": 2361900, "job_tracking_state": "//waiting", "job_type": "full_analysis", "job_user_email": "user@example.com", "job_user_id": 1099, "job_vm_id": 20, "job_vm_name": "win10_64", "job_vnc_token": "Ui1tZG6tKFS14jIJR5894CL7mJJXkNxg" } ], "md_jobs": [], "reputation_jobs": [ { "reputation_job_created": "2018-12-03T16:37:00", "reputation_job_id": 154567, "reputation_job_priority": 1, "reputation_job_sample_id": 2118603, "reputation_job_sample_md5": "e3c04a783dae53fae0422e3a955bc02a", "reputation_job_sample_sha1": "f420470addba27b8577bb40e02229e90af568d69", "reputation_job_sample_sha256": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40", "reputation_job_sample_ssdeep": "3:EPK:YK", "reputation_job_status": "queued", "reputation_job_statuschanged": "2018-12-03T16:37:00", "reputation_job_submission_id": 2361900, "reputation_job_user_email": "user@example.com", "reputation_job_user_id": 1099 } ], "samples": [ { "sample_created": "2018-12-03T16:37:00", "sample_filename": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40.url", "sample_filesize": 14, "sample_id": 2118603, "sample_is_multipart": false, "sample_md5hash": "e3c04a783dae53fae0422e3a955bc02a", "sample_priority": 1, "sample_sha1hash": "f420470addba27b8577bb40e02229e90af568d69", "sample_sha256hash": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40", "sample_ssdeephash": "3:EPK:YK", "sample_type": "URL", "sample_url": "www.reddit.com", "sample_webif_url": "https://cloud.vmray.com/user/sample/view?id=2118603", "submission_filename": "www.reddit.com" } ], "static_jobs": [], "submissions": [ { "submission_analyzer_mode_analyzer_mode": "reputation_static_dynamic", "submission_analyzer_mode_enable_reputation": true, "submission_analyzer_mode_enable_triage": false, "submission_analyzer_mode_enable_whois": true, "submission_analyzer_mode_id": 971, "submission_created": "2018-12-03T16:37:00", "submission_filename": "www.reddit.com", "submission_finished": false, "submission_id": 2361900, "submission_ip_id": 1264, "submission_ip_ip": "64.125.235.6", "submission_known_configuration": false, "submission_prescript_force_admin": false, "submission_priority": 1, "submission_reputation_mode": "disabled", "submission_sample_id": 2118603, "submission_sample_md5": "e3c04a783dae53fae0422e3a955bc02a", "submission_sample_sha1": "f420470addba27b8577bb40e02229e90af568d69", "submission_sample_sha256": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40", "submission_sample_ssdeep": "3:EPK:YK", "submission_shareable": false, "submission_tags": [], "submission_type": "api", "submission_user_account_id": 320, "submission_user_account_name": "Rapid7/Komand", "submission_user_account_subscription_mode": "free_account", "submission_user_email": "user@example.com", "submission_user_id": 1099, "submission_webif_url": "https://cloud.vmray.com/user/sample/view?id=2118603", "submission_whois_mode": "disabled" } ], "vt_jobs": [], "whois_jobs": [ { "whois_job_created": "2018-12-03T16:37:00", "whois_job_id": 2880, "whois_job_priority": 1, "whois_job_reputation_job_id": 154567, "whois_job_sample_id": 2118603, "whois_job_sample_md5": "e3c04a783dae53fae0422e3a955bc02a", "whois_job_sample_sha1": "f420470addba27b8577bb40e02229e90af568d69", "whois_job_sample_sha256": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40", "whois_job_sample_ssdeep": "3:EPK:YK", "whois_job_status": "queued", "whois_job_statuschanged": "2018-12-03T16:37:00", "whois_job_submission_id": 2361900, "whois_job_user_email": "user@example.com", "whois_job_user_id": 1099 } ] }|
  
Example output:

```
{
  "results": {
    "errors": [],
    "jobs": [
      {
        "job_analyzer_id": 1,
        "job_analyzer_name": "vmray",
        "job_configuration_id": 54,
        "job_configuration_name": "ie",
        "job_created": "2018-12-03T16:37:00",
        "job_id": 2365712,
        "job_jobrule_id": 5,
        "job_jobrule_sampletype": "URL",
        "job_prescript_force_admin": false,
        "job_priority": 1,
        "job_reputation_job_id": 154567,
        "job_sample_id": 2118603,
        "job_sample_md5": "e3c04a783dae53fae0422e3a955bc02a",
        "job_sample_sha1": "f420470addba27b8577bb40e02229e90af568d69",
        "job_sample_sha256": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40",
        "job_sample_ssdeep": "3:EPK:YK",
        "job_snapshot_id": 1,
        "job_snapshot_name": "def",
        "job_status": "queued",
        "job_statuschanged": "2018-12-03T16:37:00",
        "job_submission_id": 2361900,
        "job_tracking_state": "//waiting",
        "job_type": "full_analysis",
        "job_user_email": "user@example.com",
        "job_user_id": 1099,
        "job_vm_id": 9,
        "job_vm_name": "win7_64_sp1",
        "job_vnc_token": "ZUq2Xg2KnGEK9CFAcU2PuU67dieYMtpm"
      },
      {
        "job_analyzer_id": 1,
        "job_analyzer_name": "vmray",
        "job_configuration_id": 54,
        "job_configuration_name": "ie",
        "job_created": "2018-12-03T16:37:00",
        "job_id": 2365713,
        "job_jobrule_id": 5,
        "job_jobrule_sampletype": "URL",
        "job_prescript_force_admin": false,
        "job_priority": 1,
        "job_reputation_job_id": 154567,
        "job_sample_id": 2118603,
        "job_sample_md5": "e3c04a783dae53fae0422e3a955bc02a",
        "job_sample_sha1": "f420470addba27b8577bb40e02229e90af568d69",
        "job_sample_sha256": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40",
        "job_sample_ssdeep": "3:EPK:YK",
        "job_snapshot_id": 1,
        "job_snapshot_name": "def",
        "job_status": "queued",
        "job_statuschanged": "2018-12-03T16:37:00",
        "job_submission_id": 2361900,
        "job_tracking_state": "//waiting",
        "job_type": "full_analysis",
        "job_user_email": "user@example.com",
        "job_user_id": 1099,
        "job_vm_id": 17,
        "job_vm_name": "win7_32_sp1",
        "job_vnc_token": "nSnAmqNnXm6FX57Dqc0wqwZOISA9FXWq"
      },
      {
        "job_analyzer_id": 1,
        "job_analyzer_name": "vmray",
        "job_configuration_id": 54,
        "job_configuration_name": "ie",
        "job_created": "2018-12-03T16:37:00",
        "job_id": 2365714,
        "job_jobrule_id": 5,
        "job_jobrule_sampletype": "URL",
        "job_prescript_force_admin": false,
        "job_priority": 1,
        "job_reputation_job_id": 154567,
        "job_sample_id": 2118603,
        "job_sample_md5": "e3c04a783dae53fae0422e3a955bc02a",
        "job_sample_sha1": "f420470addba27b8577bb40e02229e90af568d69",
        "job_sample_sha256": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40",
        "job_sample_ssdeep": "3:EPK:YK",
        "job_snapshot_id": 1,
        "job_snapshot_name": "def",
        "job_status": "queued",
        "job_statuschanged": "2018-12-03T16:37:00",
        "job_submission_id": 2361900,
        "job_tracking_state": "//waiting",
        "job_type": "full_analysis",
        "job_user_email": "user@example.com",
        "job_user_id": 1099,
        "job_vm_id": 20,
        "job_vm_name": "win10_64",
        "job_vnc_token": "Ui1tZG6tKFS14jIJR5894CL7mJJXkNxg"
      }
    ],
    "md_jobs": [],
    "reputation_jobs": [
      {
        "reputation_job_created": "2018-12-03T16:37:00",
        "reputation_job_id": 154567,
        "reputation_job_priority": 1,
        "reputation_job_sample_id": 2118603,
        "reputation_job_sample_md5": "e3c04a783dae53fae0422e3a955bc02a",
        "reputation_job_sample_sha1": "f420470addba27b8577bb40e02229e90af568d69",
        "reputation_job_sample_sha256": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40",
        "reputation_job_sample_ssdeep": "3:EPK:YK",
        "reputation_job_status": "queued",
        "reputation_job_statuschanged": "2018-12-03T16:37:00",
        "reputation_job_submission_id": 2361900,
        "reputation_job_user_email": "user@example.com",
        "reputation_job_user_id": 1099
      }
    ],
    "samples": [
      {
        "sample_created": "2018-12-03T16:37:00",
        "sample_filename": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40.url",
        "sample_filesize": 14,
        "sample_id": 2118603,
        "sample_is_multipart": false,
        "sample_md5hash": "e3c04a783dae53fae0422e3a955bc02a",
        "sample_priority": 1,
        "sample_sha1hash": "f420470addba27b8577bb40e02229e90af568d69",
        "sample_sha256hash": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40",
        "sample_ssdeephash": "3:EPK:YK",
        "sample_type": "URL",
        "sample_url": "www.reddit.com",
        "sample_webif_url": "https://cloud.vmray.com/user/sample/view?id=2118603",
        "submission_filename": "www.reddit.com"
      }
    ],
    "static_jobs": [],
    "submissions": [
      {
        "submission_analyzer_mode_analyzer_mode": "reputation_static_dynamic",
        "submission_analyzer_mode_enable_reputation": true,
        "submission_analyzer_mode_enable_triage": false,
        "submission_analyzer_mode_enable_whois": true,
        "submission_analyzer_mode_id": 971,
        "submission_created": "2018-12-03T16:37:00",
        "submission_filename": "www.reddit.com",
        "submission_finished": false,
        "submission_id": 2361900,
        "submission_ip_id": 1264,
        "submission_ip_ip": "64.125.235.6",
        "submission_known_configuration": false,
        "submission_prescript_force_admin": false,
        "submission_priority": 1,
        "submission_reputation_mode": "disabled",
        "submission_sample_id": 2118603,
        "submission_sample_md5": "e3c04a783dae53fae0422e3a955bc02a",
        "submission_sample_sha1": "f420470addba27b8577bb40e02229e90af568d69",
        "submission_sample_sha256": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40",
        "submission_sample_ssdeep": "3:EPK:YK",
        "submission_shareable": false,
        "submission_tags": [],
        "submission_type": "api",
        "submission_user_account_id": 320,
        "submission_user_account_name": "Rapid7/Komand",
        "submission_user_account_subscription_mode": "free_account",
        "submission_user_email": "user@example.com",
        "submission_user_id": 1099,
        "submission_webif_url": "https://cloud.vmray.com/user/sample/view?id=2118603",
        "submission_whois_mode": "disabled"
      }
    ],
    "vt_jobs": [],
    "whois_jobs": [
      {
        "whois_job_created": "2018-12-03T16:37:00",
        "whois_job_id": 2880,
        "whois_job_priority": 1,
        "whois_job_reputation_job_id": 154567,
        "whois_job_sample_id": 2118603,
        "whois_job_sample_md5": "e3c04a783dae53fae0422e3a955bc02a",
        "whois_job_sample_sha1": "f420470addba27b8577bb40e02229e90af568d69",
        "whois_job_sample_sha256": "582cff1d9cd20ceb2c0ce9f5585406104fbf87bc6598643842862f781f181e40",
        "whois_job_sample_ssdeep": "3:EPK:YK",
        "whois_job_status": "queued",
        "whois_job_statuschanged": "2018-12-03T16:37:00",
        "whois_job_submission_id": 2361900,
        "whois_job_user_email": "user@example.com",
        "whois_job_user_id": 1099
      }
    ]
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**analysis_serialized_result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Code|integer|None|None|Code|None|
|Extra Arguments|object|None|None|Extra args|None|
|Formatted Arguments|[]object|None|None|Formatted arguments|None|
  
**analysis_result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Analysis Analyzer ID|integer|None|None|Analysis analyzer ID|None|
|Analysis Analyzer Name|string|None|None|Analysis analyzer name e.g vmray|None|
|Analysis Analyzer Version|string|None|None|Analysis analyzer version|None|
|Analysis Configuration ID|integer|None|None|Analysis configuration ID|None|
|Analysis Configuration Name|string|None|None|Analysis configuration name|None|
|Analysis Created|string|None|None|Analysis Created|None|
|Analysis Document Password|string|None|None|Analysis document password|None|
|Analysis ID|integer|None|None|Analysis ID|None|
|Analysis IOC Aggregation State|string|None|None|Analysis IOC aggregation state|None|
|Analysis Job ID|integer|None|None|Analysis job ID|None|
|Analysis Job Started|string|None|None|Analysis job started date e.g 2017-11-29T12:06:39|None|
|Analysis Job Type|string|None|None|Analysis job type|None|
|Analysis Job Rule ID|integer|None|None|Analysis job rule ID|None|
|Analysis Prescript Force Admin|boolean|None|None|Analysis prescript force admin|None|
|Analysis Prescript ID|integer|None|None|Analysis prescript ID|None|
|Analysis Priority|integer|None|None|Analysis priority e.g 5|None|
|Analysis Report Version|integer|None|None|Analysis report version|None|
|Analysis Result Code|integer|None|None|Analysis result code|None|
|Analysis Result String|string|None|None|Analysis result string|None|
|Analysis Sample ID|integer|None|None|Analysis sample ID|None|
|Analysis Sample MD5|string|None|None|Analysis sample MD5|None|
|Analysis Sample SHA1|string|None|None|Analysis sample SHA1 e.g 124f46228d1e220d88ae5e9a24d6e713039a64f9|None|
|Analysis Sample SHA-256|string|None|None|Analysis sample SHA-256|None|
|Analysis Sample ssdeep|string|None|None|Analysis sample ssdeep|None|
|Analysis Serialized Results|analysis_serialized_result|None|None|Analysis serialized results|None|
|Analysis Severity|string|None|None|Analysis severity e.g suspicious|None|
|Analysis Size|integer|None|None|Analysis size|None|
|Analysis Snapshot ID|integer|None|None|Analysis snapshot ID|None|
|Analysis Snapshot Name|string|None|None|Analysis snapshot name|None|
|Analysis Static Config ID|integer|None|None|Analysis static config ID|None|
|Analysis submission ID|integer|None|None|Analysis submission ID|None|
|Analysis System Time|string|None|None|Analysis system time|None|
|Analysis tags|[]string|None|None|Analysis tags|None|
|Analysis User Email|string|None|None|Analysis user email e.g demo@vmray.com|None|
|Analysis User ID|integer|None|None|Analysis user ID|None|
|Analysis VM ID|integer|None|None|Analysis VM ID|None|
|Analysis VM Name|string|None|None|Analysis VM name|None|
|Analysis VMhost ID|integer|None|None|Analysis vmhost ID|None|
|Analysis VMhost Name|string|None|None|Analysis vmhost name|None|
|Analysis VTI Aggregation State|string|None|None|Analysis VTI aggregation state|None|
|Analysis VTI Built in Rules Version|string|None|None|Analysis VTI built in rules version|None|
|Analysis VTI Custom Rules Hash|string|None|None|Analysis VTI custom rules hash|None|
|Analysis VIT Score|integer|None|None|Analysis VTI score|None|
|Analysis Webif URL|string|None|None|Analysis webif URL|None|
|Analysis Yara Latest Ruleset Data|string|None|None|Analysis Yara latest ruleset data|None|
|Analysis Yara Match Count|integer|None|None|Analysis Yara match count|None|
  
**job_info**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|slot|integer|None|None|None|None|
|status|string|None|None|None|None|
  
**analysis**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|analysis_analyzer_id|integer|None|None|None|None|
|analysis_analyzer_name|string|None|None|None|None|
|analysis_analyzer_version|string|None|None|None|None|
|analysis_configuration_id|integer|None|None|None|None|
|analysis_configuration_name|string|None|None|None|None|
|analysis_created|string|None|None|None|None|
|analysis_id|integer|None|None|None|None|
|analysis_job_id|integer|None|None|None|None|
|analysis_job_started|string|None|None|None|None|
|analysis_jobrule_sampletype|string|None|None|None|None|
|analysis_priority|integer|None|None|None|None|
|analysis_result_code|integer|None|None|None|None|
|analysis_result_str|string|None|None|None|None|
|analysis_sample_id|integer|None|None|None|None|
|analysis_severity|integer|None|None|None|None|
|analysis_size|integer|None|None|None|None|
|analysis_snapshot_id|integer|None|None|None|None|
|analysis_snapshot_name|string|None|None|None|None|
|analysis_user_email|string|None|None|None|None|
|analysis_user_id|integer|None|None|None|None|
|analysis_vm_id|integer|None|None|None|None|
|analysis_vm_name|string|None|None|None|None|
|analysis_vmhost_id|integer|None|None|None|None|
|analysis_vmhost_name|string|None|None|None|None|
  
**details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|sample_filename|string|None|None|None|None|
|sample_id|int|None|None|None|None|
|sample_md5hash|string|None|None|None|None|
|sample_webif_url|string|None|None|None|None|
  
**analysis_by_hash**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|analysis_results|[]analysis|None|None|None|None|
|job_info|job_info|None|None|None|None|
  
**data**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|sample_filename|string|None|None|None|None|
|sample_id|int|None|None|None|None|
|sample_md5hash|string|None|None|None|None|
|sample_sha256hash|string|None|None|None|None|
|sample_webif_url|string|None|None|None|None|
  
**results**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|data|[]data|None|None|None|None|
|results|string|None|None|None|None|
  
**sample**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Sample Classifications|[]string|None|None|Classifications|None|
|Sample Created|string|None|None|Date sample was created|None|
|Sample Filename|string|None|None|Filename|None|
|Sample Filesize|integer|None|None|Filesize|None|
|Sample Highest VTI Score|integer|None|None|Highest VTI score for sample|None|
|Sample Highest VTI Severity|string|None|None|Highest VTI severity|None|
|Sample ID|integer|None|None|Sample ID|None|
|Sample Import Hash|string|None|None|Import hash|None|
|Sample Is Multipart|boolean|None|None|Is multipart|None|
|Sample Last MD Score|integer|None|None|MD score|None|
|Sample Last Reputation Severity|string|None|None|Last reputation severity|None|
|Sample Last VT Score|integer|None|None|VT score|None|
|Sample MD5 Hash|string|None|None|MD5 Hash|None|
|Sample Priority|integer|None|None|Priority|None|
|Sample Score|integer|None|None|Score|None|
|Sample Severity|string|None|None|Severity|None|
|Sample SHA1 Hash|string|None|None|SHA1 hash|None|
|Sample SHA256 Hash|string|None|None|SHA256 Hash|None|
|Sample ssdeep Hash|string|None|None|Ssdeep hash|None|
|Sample Type|string|None|None|Type|None|
|Sample URL|string|None|None|URL|None|
|Sample VTI Score|integer|None|None|Automated threat score of the sample|None|
|Sample Webif URL|string|None|None|Webif URL|None|
  
**jobs**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Job Analyzer ID|integer|None|None|Job analyzer ID|None|
|Job Analyzer Name|string|None|None|Job analyzer name|None|
|Job Configuration ID|integer|None|None|Job configuration ID|None|
|Job Configuration Name|string|None|None|Job configuration name|None|
|Job Created|string|None|None|Job created|None|
|Job ID|integer|None|None|Job ID|None|
|Job Rule ID|integer|None|None|Job rule ID|None|
|Job Rule Sample Type|string|None|None|Job rule sample type|None|
|Job Prescript Force Admin|boolean|None|None|Job prescript force admin|None|
|Job Priority|integer|None|None|Job priority|None|
|Job Reputation Job ID|integer|None|None|Job reputation job ID|None|
|Job Sample ID|integer|None|None|Job sample ID|None|
|Job Sample MD5|string|None|None|Job sample MD5|None|
|Job Sample SHA1|string|None|None|Job sample SHA1|None|
|Job Sample SHA256|string|None|None|Job sample SHA256|None|
|Job Sample ssdeep|string|None|None|Job sample ssdeep|None|
|Job Snapshot ID|integer|None|None|Job Snapshot ID|None|
|Job Snapshot Name|string|None|None|Job snapshot name|None|
|Job Status|string|None|None|Job status|None|
|Job Status Changed|string|None|None|Job status changed|None|
|Job Submission ID|integer|None|None|Job submission ID|None|
|Job Tracking State|string|None|None|Job tracking state|None|
|Job Type|string|None|None|Job type|None|
|Job User Email|string|None|None|Job user email|None|
|Job User ID|integer|None|None|Job user ID|None|
|Job VM ID|integer|None|None|Job VM ID|None|
|Job VM Name|string|None|None|Job VM name|None|
|Job VNC Token|string|None|None|Job VNC token|None|
  
**whois_jobs**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|WHOIS Job Created|string|None|None|Date the WHOIS job was created|None|
|WHOIS Job ID|integer|None|None|WHOIS job ID|None|
|WHOIS Job Priority|integer|None|None|WHOIS job priority|None|
|WHOIS Job Reputation Job ID|integer|None|None|WHOIS job reputation job ID|None|
|WHOIS Job Sample ID|integer|None|None|WHOIS job sample ID|None|
|WHOIS Job Sample MD5|string|None|None|WHOIS job sample MD5|None|
|WHOIS Job Sample SHA1|string|None|None|WHOIS job sample SHA1|None|
|WHOIS Job Sample SHA256|string|None|None|WHOIS job sample SHA256|None|
|WHOIS Job Sample ssdeep|string|None|None|WHOIS job sample ssdeep|None|
|WHOIS Job Status|string|None|None|WHOIS job status|None|
|WHOIS Job Status Change|string|None|None|WHOIS job status change|None|
|WHOIS Job Submission ID|integer|None|None|WHOIS job submission ID|None|
|WHOIS Job User Email|string|None|None|WHOIS job user email|None|
|WHOIS Job User ID|integer|None|None|WHOIS job user ID|None|
  
**reputation_jobs**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Reputation Job Created|string|None|None|Reputation job created|None|
|Reputation Job ID|integer|None|None|Reputation job ID|None|
|Reputation Job Priority|integer|None|None|Reputation job priority|None|
|Reputation Job Sample ID|integer|None|None|Reputation job sample ID|None|
|Reputaion Job Sample MD5|string|None|None|Reputation job sample MD5|None|
|Reputation Job Sample SHA1|string|None|None|Reputation job sample SHA1|None|
|Reputation Job Sample SHA256|string|None|None|Reputation job sample SHA256|None|
|Reputation Job Sample ssdeep|string|None|None|Reputation job sample ssdeep|None|
|Reputation Job Status|string|None|None|Reputation job status|None|
|Reputation Job Status Changed|string|None|None|Reputation job status changed|None|
|Reputation Job Submission ID|integer|None|None|Reputation job submission ID|None|
|Reputation Job User Email|string|None|None|Reputation job user email|None|
|Reputation Job User ID|integer|None|None|Reputation job user ID|None|
  
**samples_url**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Sample Created|string|None|None|Sample created|None|
|Sample Filename|string|None|None|Sample filename|None|
|Sample Filesize|integer|None|None|Sample filesize|None|
|Sample ID|integer|None|None|Sample ID|None|
|Sample Is Multipart|boolean|None|None|Sample is multipart|None|
|Sample MD5 Hash|string|None|None|Sample MD5 hash|None|
|Sample Priority|integer|None|None|Sample priority|None|
|Sample SHA1 Hash|string|None|None|Sample SHA1 hash|None|
|Sample SHA256|string|None|None|Sample SHA256 hash|None|
|Sample ssdeep Hash|string|None|None|Sample ssdeep hash|None|
|Sample Type|string|None|None|Sample type|None|
|Sample URL|string|None|None|Sample URL|None|
|Sample Webif URL|string|None|None|Sample webif URL|None|
|Submission Filename|string|None|None|Submission filename|None|
  
**submissions_url**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Submission Analyzer Mode|string|None|None|Submission analyzer mode|None|
|Submission Analyzer Mode: Enable Reputation|boolean|None|None|Is reputation mode enabled|None|
|Submission Analyzer Mode: Enable Triage|boolean|None|None|Is triage mode enabled|None|
|Submission Analyzer Mode: Enable WHOIS|boolean|None|None|Is WHOIS mode enabled|None|
|Submission Analyzer Mode: ID|integer|None|None|Submission analyzer mode ID|None|
|Submission Created|string|None|None|Submission created|None|
|Submission Filename|string|None|None|Submission filename|None|
|Submission Finished|boolean|None|None|Submission finished|None|
|Submission ID|integer|None|None|Submission ID|None|
|Submission IP: ID|integer|None|None|Submission IP ID|None|
|Submission IP: IP|string|None|None|Submission IP IP|None|
|Submission Known Configuration|boolean|None|None|Submission known configuration|None|
|Submission Prescript Force Admin|boolean|None|None|Submission prescript force admin|None|
|Submission Priority|integer|None|None|Submission priority|None|
|Submission Reputation Mode|string|None|None|Submission reputation mode|None|
|Submission Sample ID|integer|None|None|Submission sample ID|None|
|Submission Sample MD5|string|None|None|Submission sample MD5|None|
|Submission Sample SHA1|string|None|None|Submission sample SHA1|None|
|Submission Sample SHA256|string|None|None|Submission sample SHA256|None|
|Submission Sample ssdeep|string|None|None|Submission sample ssdeep|None|
|Submission Shareable|boolean|None|None|Submission shareable|None|
|Submission Tags|[]object|None|None|Submission tags|None|
|Submission Type|string|None|None|Submission type|None|
|Submission User Account ID|integer|None|None|Submission user account ID|None|
|Submission User Account Name|string|None|None|Submission user account name|None|
|Submission User account Subscription Mode|string|None|None|Submission user account subscription mode|None|
|Submission User Email|string|None|None|Submission user email|None|
|Submission User ID|integer|None|None|Submission user ID|None|
|Submission Webif URL|string|None|None|Submission webif URL|None|
|Submission WHOIS Mode|string|None|None|Submission WHOIS mode|None|
  
**submit_url**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Errors|[]object|None|None|Errors|None|
|Jobs|[]jobs|None|None|Jobs|None|
|MD Jobs|[]object|None|None|MD jobs|None|
|Reputation Jobs|[]reputation_jobs|None|None|Reputation jobs|None|
|Samples|[]samples_url|None|None|Samples|None|
|Static Jobs|[]object|None|None|Static jobs|None|
|Submissions|[]submissions_url|None|None|Submissions|None|
|VT Jobs|[]object|None|None|VT jobs|None|
|WHOIS Jobs|[]whois_jobs|None|None|WHOIS jobs|None|
  
**submissions_file**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Submission Analyzer Mode Analyzer Mode|string|None|None|Submission analyzer mode analyzer mode|None|
|Submission Analyzer Mode Enable Reputation|boolean|None|None|Submission analyzer mode enable reputation|None|
|Submission Analyzer Mode Enable Triage|boolean|None|None|Submission analyzer mode enable triage|None|
|Submission Analyzer Mode Enable WHOIS|boolean|None|None|Submission analyzer mode enable WHOIS|None|
|Submission Analyzer Mode ID|integer|None|None|Submission analyzer mode ID|None|
|Submission Created|string|None|None|Submission created|None|
|Submission Filename|string|None|None|Submission filename|None|
|Submission Finished|boolean|None|None|Submission finished|None|
|Submission ID|integer|None|None|Submission ID|None|
|Submission IP: ID|integer|None|None|Submission IP ID|None|
|Submission IP: IP|string|None|None|Submission IP: IP|None|
|Submission Known Configuration|boolean|None|None|Submission known configuration|None|
|Submission Original Filename|string|None|None|Submission original filename|None|
|Submission Prescript Force Admin|boolean|None|None|Submission prescript force admin|None|
|Submission Priority|integer|None|None|Submission priority|None|
|Submission Reputation Mode|string|None|None|Submission reputation mode|None|
|Submission Sample: ID|integer|None|None|Submission sample ID|None|
|Submission Sample: MD5|string|None|None|Submission sample MD5|None|
|Submission Sample: SHA1|string|None|None|Submission sample SHA1|None|
|Submission Sample: SHA256|string|None|None|Submission sample SHA256|None|
|Submission Sample: ssdeep|string|None|None|Submission sample ssdeep|None|
|Submission Shareable|boolean|None|None|Submission shareable|None|
|Submission Tags|[]object|None|None|Submission tags|None|
|Submission Type|string|None|None|Submission type|None|
|Submission User Account ID|integer|None|None|Submission user account ID|None|
|Submission User Account Name|string|None|None|Submission user account name|None|
|Submission User Account Subscription Mode|string|None|None|Submission user account subscription mode|None|
|Submission User Email|string|None|None|Submission user email|None|
|Submission User ID|integer|None|None|Submission user ID|None|
|Submission Webif URL|string|None|None|Submission webif URL|None|
|Submission WHOIS Mode|string|None|None|Submission WHOIS mode|None|
  
**samples_files**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Sample Created|string|None|None|Sample created|None|
|Sample Filename|string|None|None|Sample filename|None|
|Sample Filesize|integer|None|None|Sample filesize|None|
|Sample ID|integer|None|None|Sample ID|None|
|Sample Is Multipart|boolean|None|None|Sample is multipart|None|
|Sample MD5 Hash|string|None|None|Sample MD5 hash|None|
|Sample Priority|integer|None|None|Sample priority|None|
|Sample SHA1 Hash|string|None|None|Sample SHA1 hash|None|
|Sample SHA256 Hash|string|None|None|Sample SHA256 hash|None|
|Sample ssdeep hash|string|None|None|Sample ssdeep hash|None|
|Sample Type|string|None|None|Sample type|None|
|Sample Webif URL|string|None|None|Sample webif URL|None|
|Submission Filename|string|None|None|Submission filename|None|
  
**submit_file**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Errors|[]object|None|None|Errors|None|
|Jobs|[]object|None|None|Jobs|None|
|MD Jobs|[]object|None|None|MD jobs|None|
|Reputation Jobs|[]reputation_jobs|None|None|Reputation jobs|None|
|Samples|[]samples_files|None|None|Samples|None|
|Static Jobs|[]object|None|None|Static jobs|None|
|Submissions|[]submissions_file|None|None|Submissions|None|
|VT Jobs|[]object|None|None|VT jobs|None|
|WHOIS Jobs|[]object|None|None|WHOIS jobs|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 6.0.1 - Fixed issue with connection test | Updated SDK to the latest version (6.4.1)
* 6.0.0 - Change type of Analysis VTI Built in Rules Version from `number` to `string`
* 5.0.1 - Add example inputs
* 5.0.0 - New Titles for output data (spelling corrections)
* 4.0.2 - New spec and help.md format for the Extension Library
* 4.0.1 - Update actions and Submit URL to specify what analyzer to use | Update file type support for the Submit File action
* 4.0.0 - New actions Get Samples and Submit URL | Removed action Get Analysis by Hash | Fixed issue where Submit File results are not available in the workflow builder, and filename would not be included when submitting the file for analysis | Get Samples should replace Get Analysis by Hash
* 3.0.0 - Added action Get Analysis | Ported over to Python from Go
* 2.0.2 - Regenerate with latest Go SDK to solve bug with triggers
* 2.0.1 - Updating to Go SDK 2.6.4
* 2.0.0 - Rename "Get Analysis By Hash" action to "Get Analysis by Hash"
* 1.0.0 - Initial plugin

# Links

* [VMRay](https://www.vmray.com)

## References

* [VMRay API](https://cloud.vmray.com/static_doc/html/api/REST_API_Documentation.html)