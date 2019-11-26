# Description

The VMRay plugin allows the user to submit files or URLs for malware analysis.

[VMRay](https://www.vmray.com) delivers advanced threat analysis and detection that combines a unique agentless hypervisor-based network sandbox with a real-time reputation engine. The combination provides both fast, high volume file classification and in-depth malware analysis. The VMRay Analyzer is platform independent and highly scalable, the result of a decade of R&D by some of the world's leading experts on dynamic malware analysis. By monitoring at the hypervisor level, it is undetectable by malware running in the target operating system. VMRay serves leading enterprises around the world.

This plugin utilizes the [VMRay API](https://cloud.vmray.com/static_doc/html/api/REST_API_Documentation.html).

# Key Features

* Submit a file or URL for analysis
* Get reports about files or URLs

# Requirements

* An API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API key for VMRay|None|
|url|string|https\://cloud.vmray.com|True|VMRay host e.g https\://cloud.vmray.com|None|

## Technical Details

### Actions

#### Submit File

This action is used to submit a file for analysis.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|file|None|True|File and filename for analysis|None|
|analyzer_mode|string|default|False|Specify what analyzer mode to use|['default', 'reputation', 'reputation_static', 'reputation_static_dynamic', 'static_dynamic', 'static']|
|optional_params|object|None|False|Parameters that allow finer tuning of the Submit File action, e.g {"analysis_id"\: 12345}|None|

Supported File Types:

```
.exe, .scr, .lnk2, .dll, .sys, .ocx, .pdf, .doc,.docx, .docm, .dot, .dotx, .dotm, .xls,.xlsx, .xlsm, .xlt, .xltx, .xltm, .xlb, .xlsb, .iqy, .slk, .ppt,.pptx, .pptm, .pot, .potx, .potm .mpp, .accdb, .adn, .accdr, .accdt, .accda, .mdw, .accde, .ade, .mdb, .mda, .vsd, .vsdx, .vss, .vst, .vsw, .vdx, .vtx, .vsdx, .vsdm, .vssx, .vssm, .vstx, .vstm, .pub, .puz, .rtf, .url, .html, .htm, .hta, .swf, .msi, .bat, .vbs, .vbe, .js, .jse, .wsf, .jar, .class, .ps1
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|submission_details|details|False|Submission details|
|success|boolean|False|File submission success|

Example output:

```
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
        "reputation_job_user_email": "jonathan_schipp@example.com",
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
        "submission_user_email": "jonathan_schipp@example.com",
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
```

#### Get Analysis

This action is used to get all dynamic and static analyses in the system or details about specific ones.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id_type|string|None|True|Get analysis based on ID of a specified type|["analysis_id", "analyzer", "configuration", "static_config", "created", "job", "jobrule", "job_started", "prescript", "result_code", "sample", "size", "snapshot", "submission", "user", "vm", "vmhost", "vti_score", "all"]|
|id|string|None|False|ID based on ID type selected, leave blank if "all" is selected|None|
|optional_params|object|None|False|Parameters that allow finer tuning of get analysis  e.g {"analysis_id"\: 12345}|None|

Optional Parameters can be found in the API documentation, located `http://vmrayhost/static_doc/html/api/User_API_Reference.html`

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]analysis_result|False|Results returned from analysis|

Example output:

```
[
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
    "analysis_user_email": "demo@vmray.com",
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
    "analysis_user_email": "demo@vmray.com",
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
```

#### Get Samples

This action is used to get all samples in the system or details about specific ones. You can also search by hashes.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sample_type|string|None|False|Specified type of sample|['all', 'sample_id', 'created', 'filesize', 'md5', 'sha1', 'sha256', 'type']|
|sample|string|None|True|Sample ID, hash or type,leave blank if 'all' is selected|None|
|optional_params|object|None|False|Parameters that allow finer tuning of get analysis e.g {"analysis_id"\: 12345}|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]sample|False|Results from samples|

Example output:

```
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
```

#### Submit URL

This action is used to submits a URL for analysis.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to be submitted for analysis|None|
|analyzer_mode|string|None|False|Specify what analyzer mode to use|['default','reputation', 'reputation_static', 'reputation_static_dynamic', 'static_dynamic', 'static']|
|optional_params|object|None|False|Parameters that allow finer tuning of the Submit URL action, e.g {"analysis_id"\: 12345}|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|submit_url|False|Results returned from submitting a URL|

Example output:

```
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
      "job_user_email": "jonathan_schipp@example.com",
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
      "job_user_email": "jonathan_schipp@example.com",
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
      "job_user_email": "jonathan_schipp@example.com",
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
      "reputation_job_user_email": "jonathan_schipp@example.com",
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
      "submission_user_email": "jonathan_schipp@example.com",
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
      "whois_job_user_email": "jonathan_schipp@example.com",
      "whois_job_user_id": 1099
    }
  ]
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 4.0.3 - New spec and help.md format for the Hub
* 4.0.2 - New spec and help.md format for the Hub
* 4.0.1 - Update actions Submit File and Submit URL to specify what analyzer to use | Update file type support for the Submit File action
* 4.0.0 - New actions Get Samples and Submit URL | Removed action Get Analysis by Hash | Fixed issue where Submit File results are not available in the workflow builder, and filename would not be included when submitting the file for analysis | Get Samples should replace Get Analysis by Hash
* 3.0.0 - Added action Get Analysis | Ported over to Python from Go
* 2.0.2 - Regenerate with latest Go SDK to solve bug with triggers
* 2.0.1 - Updating to Go SDK 2.6.4
* 2.0.0 - Rename "Get Analysis By Hash" action to "Get Analysis by Hash"
* 1.0.0 - Initial plugin

# Links

## References

* [VMRay API](https://cloud.vmray.com/static_doc/html/api/REST_API_Documentation.html)

