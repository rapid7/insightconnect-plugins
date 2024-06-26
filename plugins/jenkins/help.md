# Description

[Jenkins](https://jenkins.io/) is an open-source automation tool built for continuous integration purposes. Jenkins allows developers around the world to reliable build, test, and deploy their software. This plugin uses the [Jenkins Python API](https://opendev.org/jjb/python-jenkins) to programmatically start and collect information from Jenkins builds.

# Key Features

* Continuous Integration/Continuous Deployment
* Start a new build job in Jenkins
* Get information about a specific build

# Requirements

* Username and Password
* Jenkins Server

# Supported Product Versions

* 2024-06-24

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Username and password|None|{"username": "ExampleUser", "password": "ExamplePassword"}|None|None|
|host|string|None|True|Jenkins server URL|None|https://example-jenkins.com|None|None|

Example input:

```
{
  "credentials": {
    "password": "ExamplePassword",
    "username": "ExampleUser"
  },
  "host": "https://example-jenkins.com"
}
```

## Technical Details

### Actions


#### Build Info

This action is used to returns detailed information on a build

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|build_number|integer|None|True|The build number you want detailed information on|None|4101|None|None|
|name|string|None|True|Job name|None|moose-build|None|None|
  
Example input:

```
{
  "build_number": 4101,
  "name": "moose-build"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|build_info|build_info|False|Information on the build|{"building":false,"full_display_name":"moose-build #529","keep_log":false,"number":529,"queue_id":4423,"result":"SUCCESS","timestamp":1533096110941,"url":"https://example.com/job/moose-build/529/","built_on":"jenkins.example.com","items":[{"_class":"hudson.plugins.git.GitChangeSet","affectedPaths":["port_knocking/komand_port_knocking/connection/__init__.py","port_knocking/komand_port_knocking/triggers/__init__.py","port_knocking/komand_port_knocking/actions/knock/action.py","port_knocking/komand_port_knocking/actions/__init__.py","port_knocking/komand_port_knocking/connection.py","port_knocking/komand_port_knocking/connection/schema.py","port_knocking/Makefile","port_knocking/komand_port_knocking/actions/knock/__init__.py","port_knocking/Dockerfile","port_knocking/komand_port_knocking/util/__init__.py","port_knocking/plugin.spec.yaml","port_knocking/bin/komand_port_knocking","port_knocking/requirements.txt","port_knocking/komand_port_knocking/connection/connection.py","port_knocking/komand_port_knocking/actions/knock/schema.py","port_knocking/komand_port_knocking/actions/knock.py","port_knocking/setup.py","port_knocking/komand_port_knocking/__init__.py"],"commitId":"5a1b5315634dfac220b0b9843d02db3f8fead210","timestamp":1524589889000,"author":{"absoluteUrl":"https://jenkins.example.com/user/example","fullName":"John Doe"},"authorEmail":"user@example.com","comment":"Update pork_knocker to v2 Python plugin architecture\n","date":"2018-04-24 13:11:29 -0400","id":"5a1b5315634dfac220b0b9843d02db3f8fead210","msg":"Update pork_knocker to v2 Python plugin architecture","paths":[{"editType":"edit","file":"port_knocking/komand_port_knocking/__init__.py"},{"editType":"edit","file":"port_knocking/Dockerfile"},{"editType":"edit","file":"port_knocking/komand_port_knocking/triggers/__init__.py"},{"editType":"add","file":"port_knocking/komand_port_knocking/actions/knock/action.py"},{"editType":"add","file":"port_knocking/komand_port_knocking/util/__init__.py"},{"editType":"add","file":"port_knocking/komand_port_knocking/connection/schema.py"},{"editType":"add","file":"port_knocking/komand_port_knocking/actions/knock/schema.py"},{"editType":"edit","file":"port_knocking/plugin.spec.yaml"},{"editType":"edit","file":"port_knocking/Makefile"},{"editType":"edit","file":"port_knocking/komand_port_knocking/actions/__init__.py"},{"editType":"delete","file":"port_knocking/komand_port_knocking/actions/knock.py"},{"editType":"add","file":"port_knocking/komand_port_knocking/actions/knock/__init__.py"},{"editType":"edit","file":"port_knocking/setup.py"},{"editType":"edit","file":"port_knocking/bin/komand_port_knocking"},{"editType":"add","file":"port_knocking/requirements.txt"},{"editType":"add","file":"port_knocking/komand_port_knocking/connection/__init__.py"},{"editType":"delete","file":"port_knocking/komand_port_knocking/connection.py"},{"editType":"add","file":"port_knocking/komand_port_knocking/connection/connection.py"}]},{"_class":"hudson.plugins.git.GitChangeSet","affectedPaths":["port_knocking/plugin.spec.yaml"],"commitId":"6915b6023f84ea17c15c677262f47eb640686248","timestamp":1525360320000,"author":{"absoluteUrl":"https://jenkins.example.com/user/example","fullName":"John Doe"},"authorEmail":"user@example.com","comment":"Auto formatting plugin.spec.yaml\n","date":"2018-05-03 11:12:00 -0400","id":"6915b6023f84ea17c15c677262f47eb640686248","msg":"Auto formatting plugin.spec.yaml","paths":[{"editType":"edit","file":"port_knocking/plugin.spec.yaml"}]},{"_class":"hudson.plugins.git.GitChangeSet","affectedPaths":["port_knocking/plugin.spec.yaml","port_knocking/Dockerfile","port_knocking/komand_port_knocking/actions/knock/action.py","port_knocking/Makefile","port_knocking/.gitignore"],"commitId":"aae7faa0389dbc3a461aedf0324913dba34a748a","timestamp":1533095364000,"author":{"absoluteUrl":"https://jenkins.example.com/user/example","fullName":"John Doe"},"authorEmail":"user@example.com","comment":"Update to v2\n","date":"2018-07-31 22:49:24 -0500","id":"aae7faa0389dbc3a461aedf0324913dba34a748a","msg":"Update to v2","paths":[{"editType":"edit","file":"port_knocking/.gitignore"},{"editType":"edit","file":"port_knocking/komand_port_knocking/actions/knock/action.py"},{"editType":"edit","file":"port_knocking/plugin.spec.yaml"},{"editType":"edit","file":"port_knocking/Makefile"},{"editType":"edit","file":"port_knocking/Dockerfile"}]}]}|
  
Example output:

```
{
  "build_info": {
    "building": false,
    "built_on": "jenkins.example.com",
    "full_display_name": "moose-build #529",
    "items": [
      {
        "_class": "hudson.plugins.git.GitChangeSet",
        "affectedPaths": [
          "port_knocking/komand_port_knocking/connection/__init__.py",
          "port_knocking/komand_port_knocking/triggers/__init__.py",
          "port_knocking/komand_port_knocking/actions/knock/action.py",
          "port_knocking/komand_port_knocking/actions/__init__.py",
          "port_knocking/komand_port_knocking/connection.py",
          "port_knocking/komand_port_knocking/connection/schema.py",
          "port_knocking/Makefile",
          "port_knocking/komand_port_knocking/actions/knock/__init__.py",
          "port_knocking/Dockerfile",
          "port_knocking/komand_port_knocking/util/__init__.py",
          "port_knocking/plugin.spec.yaml",
          "port_knocking/bin/komand_port_knocking",
          "port_knocking/requirements.txt",
          "port_knocking/komand_port_knocking/connection/connection.py",
          "port_knocking/komand_port_knocking/actions/knock/schema.py",
          "port_knocking/komand_port_knocking/actions/knock.py",
          "port_knocking/setup.py",
          "port_knocking/komand_port_knocking/__init__.py"
        ],
        "author": {
          "absoluteUrl": "https://jenkins.example.com/user/example",
          "fullName": "John Doe"
        },
        "authorEmail": "user@example.com",
        "comment": "Update pork_knocker to v2 Python plugin architecture\n",
        "commitId": "5a1b5315634dfac220b0b9843d02db3f8fead210",
        "date": "2018-04-24 13:11:29 -0400",
        "id": "5a1b5315634dfac220b0b9843d02db3f8fead210",
        "msg": "Update pork_knocker to v2 Python plugin architecture",
        "paths": [
          {
            "editType": "edit",
            "file": "port_knocking/komand_port_knocking/__init__.py"
          },
          {
            "editType": "edit",
            "file": "port_knocking/Dockerfile"
          },
          {
            "editType": "edit",
            "file": "port_knocking/komand_port_knocking/triggers/__init__.py"
          },
          {
            "editType": "add",
            "file": "port_knocking/komand_port_knocking/actions/knock/action.py"
          },
          {
            "editType": "add",
            "file": "port_knocking/komand_port_knocking/util/__init__.py"
          },
          {
            "editType": "add",
            "file": "port_knocking/komand_port_knocking/connection/schema.py"
          },
          {
            "editType": "add",
            "file": "port_knocking/komand_port_knocking/actions/knock/schema.py"
          },
          {
            "editType": "edit",
            "file": "port_knocking/plugin.spec.yaml"
          },
          {
            "editType": "edit",
            "file": "port_knocking/Makefile"
          },
          {
            "editType": "edit",
            "file": "port_knocking/komand_port_knocking/actions/__init__.py"
          },
          {
            "editType": "delete",
            "file": "port_knocking/komand_port_knocking/actions/knock.py"
          },
          {
            "editType": "add",
            "file": "port_knocking/komand_port_knocking/actions/knock/__init__.py"
          },
          {
            "editType": "edit",
            "file": "port_knocking/setup.py"
          },
          {
            "editType": "edit",
            "file": "port_knocking/bin/komand_port_knocking"
          },
          {
            "editType": "add",
            "file": "port_knocking/requirements.txt"
          },
          {
            "editType": "add",
            "file": "port_knocking/komand_port_knocking/connection/__init__.py"
          },
          {
            "editType": "delete",
            "file": "port_knocking/komand_port_knocking/connection.py"
          },
          {
            "editType": "add",
            "file": "port_knocking/komand_port_knocking/connection/connection.py"
          }
        ],
        "timestamp": 1524589889000
      },
      {
        "_class": "hudson.plugins.git.GitChangeSet",
        "affectedPaths": [
          "port_knocking/plugin.spec.yaml"
        ],
        "author": {
          "absoluteUrl": "https://jenkins.example.com/user/example",
          "fullName": "John Doe"
        },
        "authorEmail": "user@example.com",
        "comment": "Auto formatting plugin.spec.yaml\n",
        "commitId": "6915b6023f84ea17c15c677262f47eb640686248",
        "date": "2018-05-03 11:12:00 -0400",
        "id": "6915b6023f84ea17c15c677262f47eb640686248",
        "msg": "Auto formatting plugin.spec.yaml",
        "paths": [
          {
            "editType": "edit",
            "file": "port_knocking/plugin.spec.yaml"
          }
        ],
        "timestamp": 1525360320000
      },
      {
        "_class": "hudson.plugins.git.GitChangeSet",
        "affectedPaths": [
          "port_knocking/plugin.spec.yaml",
          "port_knocking/Dockerfile",
          "port_knocking/komand_port_knocking/actions/knock/action.py",
          "port_knocking/Makefile",
          "port_knocking/.gitignore"
        ],
        "author": {
          "absoluteUrl": "https://jenkins.example.com/user/example",
          "fullName": "John Doe"
        },
        "authorEmail": "user@example.com",
        "comment": "Update to v2\n",
        "commitId": "aae7faa0389dbc3a461aedf0324913dba34a748a",
        "date": "2018-07-31 22:49:24 -0500",
        "id": "aae7faa0389dbc3a461aedf0324913dba34a748a",
        "msg": "Update to v2",
        "paths": [
          {
            "editType": "edit",
            "file": "port_knocking/.gitignore"
          },
          {
            "editType": "edit",
            "file": "port_knocking/komand_port_knocking/actions/knock/action.py"
          },
          {
            "editType": "edit",
            "file": "port_knocking/plugin.spec.yaml"
          },
          {
            "editType": "edit",
            "file": "port_knocking/Makefile"
          },
          {
            "editType": "edit",
            "file": "port_knocking/Dockerfile"
          }
        ],
        "timestamp": 1533095364000
      }
    ],
    "keep_log": false,
    "number": 529,
    "queue_id": 4423,
    "result": "SUCCESS",
    "timestamp": 1533096110941,
    "url": "https://example.com/job/moose-build/529/"
  }
}
```

#### Build Job

This action is used to start a build job

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Job name|None|515|None|None|
|parameters|object|None|False|Dictionary of job parameters|None|{"simulate_build": false}|None|None|
  
Example input:

```
{
  "name": 515,
  "parameters": {
    "simulate_build": false
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|build_number|integer|False|Build number|4101|
|job_number|integer|False|Item queue ID|101|
  
Example output:

```
{
  "build_number": 4101,
  "job_number": 101
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**build_info**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Building|boolean|None|None|If true the build is in progress|None|
|Built On|string|None|None|The server the build occurred on|None|
|Full Display Name|string|None|None|The full name of the build|None|
|Items|[]object|None|None|More information on the build|None|
|Keep Log|boolean|None|None|flag for whether to keep the log|None|
|Number|integer|None|None|The build Number|None|
|Queue ID|integer|None|None|The queue ID|None|
|Result|string|None|None|The result of the build|None|
|Timestamp|integer|None|None|A timestamp for the build start|None|
|URL|string|None|None|URL for more information on the build|None|


## Troubleshooting

For build job parameters boolean values must be lower case and strings must be in quotes e.g. `{"mykeyone": false, "mykeytwo": "mystring", "mykeythree": 27}`

# Version History

* 1.1.3 - Updated SDK to the latest version | `Build Job`: Fixed problem where actions would fail on jobs with long parameters
* 1.1.2 - Update connection test
* 1.1.1 - New spec and help.md format for the Extension Library
* 1.1.0 - Add build info action
* 1.0.0 - Initial plugin 

# Links

* [Jenkins](https://www.jenkins.io/)

## References

* [API Documentation](https://python-jenkins.readthedocs.io/en/latest/api.html)