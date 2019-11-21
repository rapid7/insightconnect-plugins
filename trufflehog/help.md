# Description

The [TruffleHog](https://github.com/dxa4481/truffleHog) plugin uses regex and entropy checks to go through the entire commit history of each branch, and check each diff for every commit as well as for secrets.

For entropy checks, TruffleHog will evaluate the shannon entropy for both the base64 character set and hexidecimal character set for every blob of text greater than 20 characters comprised of those character sets in each diff.
If at any point a high entropy string is greater than 20 characters is detected, it will collect the hashes and provide them for use once complete.

# Key Features

* Search through github commit histories, and checks if there is any leaked keys

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Search

This action is used to search through github commit histories, and checks if there is any leaked keys.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|git_url|string|All|True|The git repository that is going to be searched|None|
|do_regex|boolean|False|False|Enable high signal regex checks|None|
|do_entropy|boolean|True|False|Evaluates the shannon entropy for both the base64 char set and hexidecimal char set for every blob of text greater than 20 characters comprised of those character sets in each diff|None|
|custom_regexes|object|None|True|Ignores default regexes. Provide your own|None|
|since_commit|string|None|False|Scan from a given commit hash|None|
|max_depth|integer|1000000|False|Max commit depth to go back when searching for secrets|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issues|[]issue|False|Issues found with TruffleHog|

Example output:

```

{
  "issues": {
     "issue0": {
       "date": "2018-07-30 14:21:41",
       "path": "awssec_pkg.egg-info/PKG-INFO",
       "branch": "origin/master",
       "commit": "Clean up\n",
       "diff": "@@ -0,0 +1,16 @@\n+Metadata-Version: 2.1\n+Name: awssec-pkg\n+Version: 1.0.0\n+Summary: AWS security posture\n+Home-page: https://github.com/rephric/awssec\n+Author: Zachary Estrella\n+Author-email: zjestrella1@example.com\n+License: UNKNOWN\n+Description: AKIAIEXK7JLP3GHRLHBA\n+        0SKunBVneoNiRJQAkfd0NumqsQJZ455aAFMrT5mv\n+        \n+Platform: UNKNOWN\n+Classifier: Programming Language :: Python :: 3.6.5\n+Classifier: License :: OSI Approved :: MIT License\n+Classifier: Operating System :: OS Independent\n+Description-Content-Type: text/markdown\n",
       "stringsFound": [
         "0SKunBVneoNiRJQAkfd0NumqsQJZ455aAFMrT5mv"
       ],
       "printDiff": "@@ -0,0 +1,16 @@\n+Metadata-Version: 2.1\n+Name: awssec-pkg\n+Version: 1.0.0\n+Summary: AWS security posture\n+Home-page: https://github.com/rephric/awssec\n+Author: Zachary Estrella\n+Author-email: zjestrella1@example.com\n+License: UNKNOWN\n+Description: AKIAIEXK7JLP3GHRLHBA\n+        \u001b[93m0SKunBVneoNiRJQAkfd0NumqsQJZ455aAFMrT5mv\u001b[0m\n+        \n+Platform: UNKNOWN\n+Classifier: Programming Language :: Python :: 3.6.5\n+Classifier: License :: OSI Approved :: MIT License\n+Classifier: Operating System :: OS Independent\n+Description-Content-Type: text/markdown\n",
       "commitHash": "31f671b298c122ee35855395ef4a137fb261c545",
       "reason": "High Entropy",
       "url": "https://github.com/rephric/awssec/commit/31f671b298c122ee35855395ef4a137fb261c545"
     },
     "issue1": {
       "date": "2018-07-26 19:35:07",
       "path": "README.md",
       "branch": "origin/master",
       "commit": "Merge branch 'master' of https://github.com/rephric/awssec\n",

       "diff": "@@ -1,51 +1,2 @@\n-## AWSSEC\n-\n-AWS S3 Bucket tool to check your buckets for misconfigurations and SSH Key Leaks in your github repos. AWSSEC check your github repositories using trufflehog to see if you included any passwords or ssh keys in your repos.\n-\n-### Getting Started\n-\n-These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.\n-\n-#### Prerequisites\n-TruffleHog\n-Pip3\n-Python3\n-Boto3\n-\n-```\n-Apt-get install python3\n-Apt -get install pip3\n-Pip install boto3\n-Git clone- https://github.com/rephric/awssec.git\n-Git clone- https://github.com/dxa4481/truffleHog.git or Pip install - trufflehog\n-\n-```\n-#### verify that AWSSEC is working\n-\n-Testing AWSSEC\n-\n-```\n-Awssec.py --help\n-```\n-\n-### Built With\n-\n-* [TruffleHog](https://github.com/dxa4481/truffleHog) - Check Git hub repos for keys\n-* [Python](https://www.python.org/) - Powered by Python\n-* [BOTO3](https://github.com/boto/boto3) - Amazon AWS API\n-\n-### Authors\n-\n-* **Zachary Estrella** - *Initial Idea* - [rephric](https://github.com/rephric)\n-* **Trevor Behrens** - *Contributor* - [tbehrens97](https://github.com/tbehrens97)\n-\n-\n-### License\n-\n-This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details\n-\n-### Acknowledgments\n-\n-* dxa4481 for TruffleHog\n-* Amazon for BOTO3\n-* Python\n\\ No newline at end of file\n+AKIAIEXK7JLP3GHRLHBA\n+0SKunBVneoNiRJQAkfd0NumqsQJZ455aAFMrT5mv\n",

       "stringsFound": [
         "+0SKunBVneoNiRJQAkfd0NumqsQJZ455aAFMrT5mv"
       ],

       "printDiff": "@@ -1,51 +1,2 @@\n-## AWSSEC\n-\n-AWS S3 Bucket tool to check your buckets for misconfigurations and SSH Key Leaks in your github repos. AWSSEC check your github repositories using trufflehog to see if you included any passwords or ssh keys in your repos.\n-\n-### Getting Started\n-\n-These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.\n-\n-#### Prerequisites\n-TruffleHog\n-Pip3\n-Python3\n-Boto3\n-\n-```\n-Apt-get install python3\n-Apt -get install pip3\n-Pip install boto3\n-Git clone- https://github.com/rephric/awssec.git\n-Git clone- https://github.com/dxa4481/truffleHog.git or Pip install - trufflehog\n-\n-```\n-#### verify that AWSSEC is working\n-\n-Testing AWSSEC\n-\n-```\n-Awssec.py --help\n-```\n-\n-### Built With\n-\n-* [TruffleHog](https://github.com/dxa4481/truffleHog) - Check Git hub repos for keys\n-* [Python](https://www.python.org/) - Powered by Python\n-* [BOTO3](https://github.com/boto/boto3) - Amazon AWS API\n-\n-### Authors\n-\n-* **Zachary Estrella** - *Initial Idea* - [rephric](https://github.com/rephric)\n-* **Trevor Behrens** - *Contributor* - [tbehrens97](https://github.com/tbehrens97)\n-\n-\n-### License\n-\n-This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details\n-\n-### Acknowledgments\n-\n-* dxa4481 for TruffleHog\n-* Amazon for BOTO3\n-* Python\n\\ No newline at end of file\n+AKIAIEXK7JLP3GHRLHBA\n\u001b[93m+0SKunBVneoNiRJQAkfd0NumqsQJZ455aAFMrT5mv\u001b[0m\n",

       "commitHash": "d63a33368db5a5e5a2619e2cc764f238b5a4174a",
       "reason": "High Entropy",
       "url": "https://github.com/rephric/awssec/commit/d63a33368db5a5e5a2619e2cc764f238b5a4174a"
     },
     ...
  }
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.1.2 - New spec and help.md format for the Hub
* 1.1.1 - Fix issue where custom_regexes input field in Search action was not working
* 1.1.0 - Update to v2 Python plugin architecture | Support web server mode
* 1.0.0 - Initial plugin

# Links

## References

* [truffleHog](https://github.com/dxa4481/truffleHog)

