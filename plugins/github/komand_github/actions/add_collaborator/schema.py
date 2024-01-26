# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Adds a user as a collaborator to a GitHub repository"


class Input:
    ORGANIZATION = "organization"
    PERMISSION = "permission"
    REPOSITORY = "repository"
    USERNAME = "username"


class Output:
    RESULTS = "results"


class AddCollaboratorInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "organization": {
      "type": "string",
      "title": "Organization",
      "description": "Organization the repository is under",
      "order": 2
    },
    "permission": {
      "type": "string",
      "title": "Permission",
      "description": "The permission to grant the collaborator. Only valid on organization-owned repositories",
      "default": "push",
      "enum": [
        "pull",
        "push",
        "admin"
      ],
      "order": 4
    },
    "repository": {
      "type": "string",
      "title": "Repository",
      "description": "Repository to add user as a collaborator",
      "order": 3
    },
    "username": {
      "type": "string",
      "title": "Username",
      "description": "Username to add as a collaborator",
      "order": 1
    }
  },
  "required": [
    "username"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddCollaboratorOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "$ref": "#/definitions/add_collaborator",
      "title": "Results",
      "description": "Response from adding a new collaborator",
      "order": 1
    }
  },
  "definitions": {
    "add_collaborator": {
      "type": "object",
      "title": "add_collaborator",
      "properties": {
        "id": {
          "type": "integer",
          "order": 1
        },
        "repository": {
          "$ref": "#/definitions/collaborator_repository",
          "order": 2
        },
        "invitee": {
          "$ref": "#/definitions/collaborator_invite",
          "order": 3
        },
        "inviter": {
          "$ref": "#/definitions/collaborator_invite",
          "order": 4
        },
        "permission": {
          "type": "string",
          "order": 5
        },
        "created_at": {
          "type": "string",
          "order": 6
        },
        "url": {
          "type": "string",
          "order": 7
        },
        "html_url": {
          "type": "string",
          "order": 8
        }
      }
    },
    "collaborator_repository": {
      "type": "object",
      "title": "collaborator_repository",
      "properties": {
        "id": {
          "type": "integer",
          "order": 1
        },
        "node_id": {
          "type": "string",
          "order": 2
        },
        "name": {
          "type": "string",
          "order": 3
        },
        "full_name": {
          "type": "string",
          "order": 4
        },
        "owner": {
          "order": 5
        },
        "private": {
          "type": "boolean",
          "order": 6
        },
        "html_url": {
          "type": "string",
          "order": 7
        },
        "description": {
          "type": "string",
          "order": 8
        },
        "fork": {
          "type": "boolean",
          "order": 9
        },
        "url": {
          "type": "string",
          "order": 10
        },
        "archive_url": {
          "type": "string",
          "order": 11
        },
        "assignees_url": {
          "type": "string",
          "order": 12
        },
        "blobs_url": {
          "type": "string",
          "order": 13
        },
        "branches_url": {
          "type": "string",
          "order": 14
        },
        "collaborators_url": {
          "type": "string",
          "order": 15
        },
        "comments_url": {
          "type": "string",
          "order": 16
        },
        "commits_url": {
          "type": "string",
          "order": 17
        },
        "compare_url": {
          "type": "string",
          "order": 18
        },
        "contents_url": {
          "type": "string",
          "order": 19
        },
        "contributors_url": {
          "type": "string",
          "order": 20
        },
        "deployments_url": {
          "type": "string",
          "order": 21
        },
        "downloads_url": {
          "type": "string",
          "order": 22
        },
        "events_url": {
          "type": "string",
          "order": 23
        },
        "forks_url": {
          "type": "string",
          "order": 24
        },
        "git_commits_url": {
          "type": "string",
          "order": 25
        },
        "git_refs_url": {
          "type": "string",
          "order": 26
        },
        "git_tags_url": {
          "type": "string",
          "order": 27
        },
        "git_url": {
          "type": "string",
          "order": 28
        },
        "issue_comment_url": {
          "type": "string",
          "order": 29
        },
        "issue_events_url": {
          "type": "string",
          "order": 30
        },
        "issues_url": {
          "type": "string",
          "order": 31
        },
        "keys_url": {
          "type": "string",
          "order": 32
        },
        "labels_url": {
          "type": "string",
          "order": 33
        },
        "languages_url": {
          "type": "string",
          "order": 34
        },
        "merges_url": {
          "type": "string",
          "order": 35
        },
        "milestones_url": {
          "type": "string",
          "order": 36
        },
        "notifications_url": {
          "type": "string",
          "order": 37
        },
        "pulls_url": {
          "type": "string",
          "order": 38
        },
        "releases_url": {
          "type": "string",
          "order": 39
        },
        "ssh_url": {
          "type": "string",
          "order": 40
        },
        "stargazers_url": {
          "type": "string",
          "order": 41
        },
        "statuses_url": {
          "type": "string",
          "order": 42
        },
        "subscribers_url": {
          "type": "string",
          "order": 43
        },
        "subscription_url": {
          "type": "string",
          "order": 44
        },
        "tags_url": {
          "type": "string",
          "order": 45
        },
        "teams_url": {
          "type": "string",
          "order": 46
        },
        "trees_url": {
          "type": "string",
          "order": 47
        }
      }
    },
    "collaborator_invite": {
      "type": "object",
      "title": "collaborator_invite",
      "properties": {
        "login": {
          "type": "string",
          "order": 1
        },
        "id": {
          "type": "integer",
          "order": 2
        },
        "node_id": {
          "type": "string",
          "order": 3
        },
        "avatar_url": {
          "type": "string",
          "order": 4
        },
        "gravatar_id": {
          "type": "string",
          "order": 5
        },
        "url": {
          "type": "string",
          "order": 6
        },
        "html_url": {
          "type": "string",
          "order": 7
        },
        "followers_url": {
          "type": "string",
          "order": 8
        },
        "following_url": {
          "type": "string",
          "order": 9
        },
        "gists_url": {
          "type": "string",
          "order": 10
        },
        "starred_url": {
          "type": "string",
          "order": 11
        },
        "subscriptions_url": {
          "type": "string",
          "order": 12
        },
        "organizations_url": {
          "type": "string",
          "order": 13
        },
        "repos_url": {
          "type": "string",
          "order": 14
        },
        "events_url": {
          "type": "string",
          "order": 15
        },
        "received_events_url": {
          "type": "string",
          "order": 16
        },
        "type": {
          "type": "string",
          "order": 17
        },
        "site_admin": {
          "type": "boolean",
          "order": 18
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
