# Description

[Jenkins](https://jenkins.io/) is an open source automation server which enables developers around the world to reliably build, test, and deploy their software.
This plugin utilizes the [Jenkins Python API](http://git.openstack.org/cgit/openstack/python-jenkins).

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|Username and password|None|
|host|string|None|True|Jenkins server URL|None|

## Technical Details

### Actions

#### Build Job

This action is used to start a build job.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|Name of job|None|
|parameters|string|None|False|Dictionary of job parameters|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|job_number|integer|False|queue item|

Example output:

```

{
  "job_number": 4101
}

```

#### Build Info

This action is used to return detailed information on a build.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|Job name|None|
|Build number|integer|None|True|The build number you want detailed information on|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|build_info|build_info|False|Information on the build|

Example output:

```

{
  "build_info": {
    "building": false,
    "full_display_name": "example-komand-plugins-master #529",
    "keep_log": false,
    "number": 529,
    "queue_id": 4423,
    "result": "SUCCESS",
    "timestamp": 1533096110941,
    "url": "https://example.com/job/example-komand-plugins-master/529/",
    "built_on": "jenkins.example.com",
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
        "commitId": "5a1b5315634dfac220b0b9843d02db3f8fead210",
        "timestamp": 1524589889000,
        "author": {
          "absoluteUrl": "https://jenkins.example.com/user/mbroomfield",
          "fullName": "Matt Broomfield"
        },
        "authorEmail": "mbroomfield@example.com",
        "comment": "Update pork_knocker to v2 Python plugin architecture\n",
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
        ]
      },
      {
        "_class": "hudson.plugins.git.GitChangeSet",
        "affectedPaths": [
          "port_knocking/plugin.spec.yaml"
        ],
        "commitId": "6915b6023f84ea17c15c677262f47eb640686248",
        "timestamp": 1525360320000,
        "author": {
          "absoluteUrl": "https://jenkins.example.com/user/mbroomfield",
          "fullName": "Matt Broomfield"
        },
        "authorEmail": "mbroomfield@example.com",
        "comment": "Auto formatting plugin.spec.yaml\n",
        "date": "2018-05-03 11:12:00 -0400",
        "id": "6915b6023f84ea17c15c677262f47eb640686248",
        "msg": "Auto formatting plugin.spec.yaml",
        "paths": [
          {
            "editType": "edit",
            "file": "port_knocking/plugin.spec.yaml"
          }
        ]
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
        "commitId": "aae7faa0389dbc3a461aedf0324913dba34a748a",
        "timestamp": 1533095364000,
        "author": {
          "absoluteUrl": "https://jenkins.example.com/user/mrinehart",
          "fullName": "Mike Rinehart"
        }a
        "authorEmail": "bob_ross@example.com",
        "comment": "Update to v2\n",
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
        ]
      }
    ]
  }
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

For build job parameters boolean values must be lower case and strings must be in quotes.
e.g. `{"mykeyone": false, "mykeytwo": "mystring", "mykeythree": 27}`

# Version History

* 1.1.0 - Add build info action
* 1.0.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [API Documentation](https://python-jenkins.readthedocs.io/en/latest/api.html)

