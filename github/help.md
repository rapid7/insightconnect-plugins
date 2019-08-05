
# GitHub

## About

[GitHub](https://github.com/) is a popular web-based Git or version control repository and Internet hosting service.
This plugin supports authentication from both personal and organization member accounts.

## Actions

### Add Collaborator

This action is used to add a user as a collaborator to a GitHub repository.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Username to remove|None|
|organization|string|None|False|Remove from organization|None|
|repository|string|None|False|Remove from repository|None|
|permission|string|push|False|The permission to grant the collaborator. Only valid on organization-owned repositories|['pull', 'push', 'admin']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|add_collaborator|False|Response from adding a new collaborator|

Example output:

```

{
  "results": {
    "id": 10231927,
    "node_id": "MDIwOlJlcG9zaXRvcnlJbnZpdGF0aW9uMTAyMzE5Mjc=",
    "repository": {
      "id": 142084604,
      "node_id": "MDEwOlJlcG9zaXRvcnkxNDIwODQ2MDQ=",
      "name": "TestRepo",
      "full_name": "TestUser/TestRepo",
      "owner": {
        "login": "TestUser",
        "id": 966940,
        "node_id": "MDQ6VXNlcjk2Njk0MA==",
        "avatar_url": "https://avatars1.githubusercontent.com/u/966940?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/TestUser",
        "html_url": "https://github.com/TestUser",
        "followers_url": "https://api.github.com/users/TestUser/followers",
        "following_url": "https://api.github.com/users/TestUser/following{/other_user}",
        "gists_url": "https://api.github.com/users/TestUser/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/TestUser/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/TestUser/subscriptions",
        "organizations_url": "https://api.github.com/users/TestUser/orgs",
        "repos_url": "https://api.github.com/users/TestUser/repos",
        "events_url": "https://api.github.com/users/TestUser/events{/privacy}",
        "received_events_url": "https://api.github.com/users/TestUser/received_events",
        "type": "User",
        "site_admin": false
      },
      "private": false,
      "html_url": "https://github.com/TestUser/TestRepo",
      "description": "Test",
      "fork": false,
      "url": "https://api.github.com/repos/TestUser/TestRepo",
      "forks_url": "https://api.github.com/repos/TestUser/TestRepo/forks",
      "keys_url": "https://api.github.com/repos/TestUser/TestRepo/keys{/key_id}",
      "collaborators_url": "https://api.github.com/repos/TestUser/TestRepo/collaborators{/collaborator}",
      "teams_url": "https://api.github.com/repos/TestUser/TestRepo/teams",
      "hooks_url": "https://api.github.com/repos/TestUser/TestRepo/hooks",
      "issue_events_url": "https://api.github.com/repos/TestUser/TestRepo/issues/events{/number}",
      "events_url": "https://api.github.com/repos/TestUser/TestRepo/events",
      "assignees_url": "https://api.github.com/repos/TestUser/TestRepo/assignees{/user}",
      "branches_url": "https://api.github.com/repos/TestUser/TestRepo/branches{/branch}",
      "tags_url": "https://api.github.com/repos/TestUser/TestRepo/tags",
      "blobs_url": "https://api.github.com/repos/TestUser/TestRepo/git/blobs{/sha}",
      "git_tags_url": "https://api.github.com/repos/TestUser/TestRepo/git/tags{/sha}",
      "git_refs_url": "https://api.github.com/repos/TestUser/TestRepo/git/refs{/sha}",
      "trees_url": "https://api.github.com/repos/TestUser/TestRepo/git/trees{/sha}",
      "statuses_url": "https://api.github.com/repos/TestUser/TestRepo/statuses/{sha}",
      "languages_url": "https://api.github.com/repos/TestUser/TestRepo/languages",
      "stargazers_url": "https://api.github.com/repos/TestUser/TestRepo/stargazers",
      "contributors_url": "https://api.github.com/repos/TestUser/TestRepo/contributors",
      "subscribers_url": "https://api.github.com/repos/TestUser/TestRepo/subscribers",
      "subscription_url": "https://api.github.com/repos/TestUser/TestRepo/subscription",
      "commits_url": "https://api.github.com/repos/TestUser/TestRepo/commits{/sha}",
      "git_commits_url": "https://api.github.com/repos/TestUser/TestRepo/git/commits{/sha}",
      "comments_url": "https://api.github.com/repos/TestUser/TestRepo/comments{/number}",
      "issue_comment_url": "https://api.github.com/repos/TestUser/TestRepo/issues/comments{/number}",
      "contents_url": "https://api.github.com/repos/TestUser/TestRepo/contents/{+path}",
      "compare_url": "https://api.github.com/repos/TestUser/TestRepo/compare/{base}...{head}",
      "merges_url": "https://api.github.com/repos/TestUser/TestRepo/merges",
      "archive_url": "https://api.github.com/repos/TestUser/TestRepo/{archive_format}{/ref}",
      "downloads_url": "https://api.github.com/repos/TestUser/TestRepo/downloads",
      "issues_url": "https://api.github.com/repos/TestUser/TestRepo/issues{/number}",
      "pulls_url": "https://api.github.com/repos/TestUser/TestRepo/pulls{/number}",
      "milestones_url": "https://api.github.com/repos/TestUser/TestRepo/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/TestUser/TestRepo/notifications{?since,all,participating}",
      "labels_url": "https://api.github.com/repos/TestUser/TestRepo/labels{/name}",
      "releases_url": "https://api.github.com/repos/TestUser/TestRepo/releases{/id}",
      "deployments_url": "https://api.github.com/repos/TestUser/TestRepo/deployments"
    },
    "invitee": {
      "login": "lmilby-r7",
      "id": 32271028,
      "node_id": "MDQ6VXNlcjMyMjcxMDI4",
      "avatar_url": "https://avatars1.githubusercontent.com/u/32271028?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/lmilby-r7",
      "html_url": "https://github.com/lmilby-r7",
      "followers_url": "https://api.github.com/users/lmilby-r7/followers",
      "following_url": "https://api.github.com/users/lmilby-r7/following{/other_user}",
      "gists_url": "https://api.github.com/users/lmilby-r7/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/lmilby-r7/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/lmilby-r7/subscriptions",
      "organizations_url": "https://api.github.com/users/lmilby-r7/orgs",
      "repos_url": "https://api.github.com/users/lmilby-r7/repos",
      "events_url": "https://api.github.com/users/lmilby-r7/events{/privacy}",
      "received_events_url": "https://api.github.com/users/lmilby-r7/received_events",
      "type": "User",
      "site_admin": false
    },
    "inviter": {
      "login": "TestUser",
      "id": 966940,
      "node_id": "MDQ6VXNlcjk2Njk0MA==",
      "avatar_url": "https://avatars1.githubusercontent.com/u/966940?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/TestUser",
      "html_url": "https://github.com/TestUser",
      "followers_url": "https://api.github.com/users/TestUser/followers",
      "following_url": "https://api.github.com/users/TestUser/following{/other_user}",
      "gists_url": "https://api.github.com/users/TestUser/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/TestUser/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/TestUser/subscriptions",
      "organizations_url": "https://api.github.com/users/TestUser/orgs",
      "repos_url": "https://api.github.com/users/TestUser/repos",
      "events_url": "https://api.github.com/users/TestUser/events{/privacy}",
      "received_events_url": "https://api.github.com/users/TestUser/received_events",
      "type": "User",
      "site_admin": false
    },
    "permissions": "write",
    "created_at": "2018-07-24T15:37:24Z",
    "url": "https://api.github.com/user/repository_invitations/10231927",
    "html_url": "https://github.com/TestUser/TestRepo/invitations"
  }
}

```

### Add Membership

This action is used to add or update user's membership in an organization.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization|string|None|False|The organization that user will be added or updated to|None|
|username|string|None|False|The user that will be added or updated|None|
|role|string|member|False|The role to give the user in the organization|['admin', 'member']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|URL|
|state|string|False|State of users membership|
|role|string|False|Role of users membership|
|user|membership_user|False|User|
|organization|membership_organization|False|Organization|
|organization_url|string|False|Organization URL|
|found|boolean|True|Whether user was successfully added|

Example output:

```

{
  "results": {
    "url": "https://api.github.com/orgs/KomandDev/memberships/jschipp-r7",
    "state": "active",
    "role": "member",
    "organization_url": "https://api.github.com/orgs/KomandDev",
    "user": {
      "login": "jschipp-r7",
      "id": 30870727,
      "node_id": "MDQ6VXNlcjMwODcwNzI3",
      "avatar_url": "https://avatars0.githubusercontent.com/u/30870727?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/jschipp-r7",
      "html_url": "https://github.com/jschipp-r7",
      "followers_url": "https://api.github.com/users/jschipp-r7/followers",
      "following_url": "https://api.github.com/users/jschipp-r7/following{/other_user}",
      "gists_url": "https://api.github.com/users/jschipp-r7/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/jschipp-r7/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/jschipp-r7/subscriptions",
      "organizations_url": "https://api.github.com/users/jschipp-r7/orgs",
      "repos_url": "https://api.github.com/users/jschipp-r7/repos",
      "events_url": "https://api.github.com/users/jschipp-r7/events{/privacy}",
      "received_events_url": "https://api.github.com/users/jschipp-r7/received_events",
      "type": "User",
      "site_admin": false
    },
    "organization": {
      "login": "KomandDev",
      "id": 41839740,
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjQxODM5NzQw",
      "url": "https://api.github.com/orgs/KomandDev",
      "repos_url": "https://api.github.com/orgs/KomandDev/repos",
      "events_url": "https://api.github.com/orgs/KomandDev/events",
      "hooks_url": "https://api.github.com/orgs/KomandDev/hooks",
      "issues_url": "https://api.github.com/orgs/KomandDev/issues",
      "members_url": "https://api.github.com/orgs/KomandDev/members{/member}",
      "public_members_url": "https://api.github.com/orgs/KomandDev/public_members{/member}",
      "avatar_url": "https://avatars1.githubusercontent.com/u/41839740?v=4",
      "description": null
    }
  }
}

```

### Create Issue

This action is used to create an issue ticket.

GitHub users to assign to the ticket must be specified by their GitHub username. They must have the privileges necessary to access the repository.
Milestones must be specified by their relative ID, which is their location in the list of active milestones. Milestone IDs are reused after milestone deletion.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|body|string|None|True|Body text of issue|None|
|assignee|string|None|False|User to assign this issue to|None|
|repository|string|None|True|Repository to post issue|None|
|title|string|None|True|Title of issue|None|
|organization|string|None|False|Organizational owner of repository|None|
|milestone|number|None|False|ID of the milestone to associate this issue with|None|
|labels|string|None|False|GitHub search tags delimited by commas|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|None|

Example output:

```

{
  "url": "https://github.com/jonschipp/ISLET/issues/94"
}

```

### Create Issue Comment

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|body|string|None|True|Body text of issue|None|
|issue_number|number|None|True|Issue number|None|
|repository|string|None|True|Repository to post issue|None|
|organization|string|None|False|Organizational owner of repository|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|None|

### Close Issue

This action is used to close an issue.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|issue_number|number|None|True|Issue number|None|
|repository|string|None|True|Repository to post issue|None|
|organization|string|None|False|Organizational owner of repository|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|None|

### Add Issue Label

This action is used to add a label to an issue.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|issue_number|number|None|True|Issue number|None|
|repository|string|None|True|Repository to post issue|None|
|organization|string|None|False|Organizational owner of repository|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|None|

### Get User

This action is used to retrieve information about a GitHub user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|GitHub username|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|None|
|bio|string|False|None|
|email|string|False|None|
|name|string|False|None|
|avatar|string|False|None|

Example output:

```

{
  "avatar": "https://avatars0.githubusercontent.com/u/30870727?v=4",
  "bio": "Director of Security Engineering at Rapid7. I work on making Komand awesome.",
  "email": "",
  "name": "Jon Schipp",
  "url": "https://github.com/jschipp-r7"
}

```

### Remove User

This action is used to remove a user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Username to remove|None|
|organization|string|None|False|Remove from organization|None|
|repository|string|None|False|Remove from repository|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|

Example output:

```

{
  "status": "Successfully removed John Doe from the repo komand/plugins in komand"
}

```

### Search

This action is used to search GitHub for data. The search by commits endpoint is currently in developer preview and is not supported at this time.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|search_type|string|None|False|The type of search to perform|['Repositories', 'Commits', 'Code', 'Issues']|
|query|string|None|False|Query to match against|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|object|False|None|

Example output:

```

{
  "results": {
    "total_count": 21,
    "incomplete_results": true,
    "items": [
      {
        "name": "plugin.spec.yaml",
        "path": "sample/plugin.spec.yaml",
        "sha": "8e02c9193c142cee15400d09f20bcd6579e3cc8f",
        "url": "https://api.github.com/repositories/63081355/contents/sample/plugin.spec.yaml?ref=943039b180a6c948638fae9d3766a2a373143c22",
        "git_url": "https://api.github.com/repositories/63081355/git/blobs/8e02c9193c142cee15400d09f20bcd6579e3cc8f",
        "html_url": "https://github.com/komand/plugin-sdk-python/blob/943039b180a6c948638fae9d3766a2a373143c22/sample/plugin.spec.yaml",
        "repository": {
          "id": 63081355,
          "node_id": "MDEwOlJlcG9zaXRvcnk2MzA4MTM1NQ==",
          "name": "plugin-sdk-python",
          "full_name": "komand/plugin-sdk-python",
          "owner": {
            "login": "komand",
            "id": 14822860,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0ODIyODYw",
            "avatar_url": "https://avatars0.githubusercontent.com/u/14822860?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/komand",
            "html_url": "https://github.com/komand",
            "followers_url": "https://api.github.com/users/komand/followers",
            "following_url": "https://api.github.com/users/komand/following{/other_user}",
            "gists_url": "https://api.github.com/users/komand/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/komand/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/komand/subscriptions",
            "organizations_url": "https://api.github.com/users/komand/orgs",
            "repos_url": "https://api.github.com/users/komand/repos",
            "events_url": "https://api.github.com/users/komand/events{/privacy}",
            "received_events_url": "https://api.github.com/users/komand/received_events",
            "type": "Organization",
            "site_admin": false
          },
          "private": false,
          "html_url": "https://github.com/komand/plugin-sdk-python",
          "description": null,
          "fork": false,
          "url": "https://api.github.com/repos/komand/plugin-sdk-python",
          "forks_url": "https://api.github.com/repos/komand/plugin-sdk-python/forks",
          "keys_url": "https://api.github.com/repos/komand/plugin-sdk-python/keys{/key_id}",
          "collaborators_url": "https://api.github.com/repos/komand/plugin-sdk-python/collaborators{/collaborator}",
          "teams_url": "https://api.github.com/repos/komand/plugin-sdk-python/teams",
          "hooks_url": "https://api.github.com/repos/komand/plugin-sdk-python/hooks",
          "issue_events_url": "https://api.github.com/repos/komand/plugin-sdk-python/issues/events{/number}",
          "events_url": "https://api.github.com/repos/komand/plugin-sdk-python/events",
          "assignees_url": "https://api.github.com/repos/komand/plugin-sdk-python/assignees{/user}",
          "branches_url": "https://api.github.com/repos/komand/plugin-sdk-python/branches{/branch}",
          "tags_url": "https://api.github.com/repos/komand/plugin-sdk-python/tags",
          "blobs_url": "https://api.github.com/repos/komand/plugin-sdk-python/git/blobs{/sha}",
          "git_tags_url": "https://api.github.com/repos/komand/plugin-sdk-python/git/tags{/sha}",
          "git_refs_url": "https://api.github.com/repos/komand/plugin-sdk-python/git/refs{/sha}",
          "trees_url": "https://api.github.com/repos/komand/plugin-sdk-python/git/trees{/sha}",
          "statuses_url": "https://api.github.com/repos/komand/plugin-sdk-python/statuses/{sha}",
          "languages_url": "https://api.github.com/repos/komand/plugin-sdk-python/languages",
          "stargazers_url": "https://api.github.com/repos/komand/plugin-sdk-python/stargazers",
          "contributors_url": "https://api.github.com/repos/komand/plugin-sdk-python/contributors",
          "subscribers_url": "https://api.github.com/repos/komand/plugin-sdk-python/subscribers",
          "subscription_url": "https://api.github.com/repos/komand/plugin-sdk-python/subscription",
          "commits_url": "https://api.github.com/repos/komand/plugin-sdk-python/commits{/sha}",
          "git_commits_url": "https://api.github.com/repos/komand/plugin-sdk-python/git/commits{/sha}",
          "comments_url": "https://api.github.com/repos/komand/plugin-sdk-python/comments{/number}",
          "issue_comment_url": "https://api.github.com/repos/komand/plugin-sdk-python/issues/comments{/number}",
          "contents_url": "https://api.github.com/repos/komand/plugin-sdk-python/contents/{+path}",
          "compare_url": "https://api.github.com/repos/komand/plugin-sdk-python/compare/{base}...{head}",
          "merges_url": "https://api.github.com/repos/komand/plugin-sdk-python/merges",
          "archive_url": "https://api.github.com/repos/komand/plugin-sdk-python/{archive_format}{/ref}",
          "downloads_url": "https://api.github.com/repos/komand/plugin-sdk-python/downloads",
          "issues_url": "https://api.github.com/repos/komand/plugin-sdk-python/issues{/number}",
          "pulls_url": "https://api.github.com/repos/komand/plugin-sdk-python/pulls{/number}",
          "milestones_url": "https://api.github.com/repos/komand/plugin-sdk-python/milestones{/number}",
          "notifications_url": "https://api.github.com/repos/komand/plugin-sdk-python/notifications{?since,all,participating}",
          "labels_url": "https://api.github.com/repos/komand/plugin-sdk-python/labels{/name}",
          "releases_url": "https://api.github.com/repos/komand/plugin-sdk-python/releases{/id}",
          "deployments_url": "https://api.github.com/repos/komand/plugin-sdk-python/deployments"
        },
        "score": 21.036484
      },
      ...
    ]
  }
}

```

### Get Repo

This action is used to retrieve details, including id, about a specific repo.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|owner|string|None|True|Owner of the repository|None|
|title|string|None|True|Name of the repository|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|repo|True|Repository details and data|

Example output:

```

{
  "data": {
    "id": 24237263,
    "node_id": "MDEwOlJlcG9zaXRvcnkyNDIzNzI2Mw==",
    "name": "ISLET",
    "full_name": "jonschipp/ISLET",
    "owner": {
      "login": "jonschipp",
      "id": 2321183,
      "node_id": "MDQ6VXNlcjIzMjExODM=",
      "avatar_url": "https://avatars0.githubusercontent.com/u/2321183?v=4",
      "url": "https://api.github.com/users/jonschipp",
      "html_url": "https://github.com/jonschipp",
      "followers_url": "https://api.github.com/users/jonschipp/followers",
      "following_url": "https://api.github.com/users/jonschipp/following{/other_user}",
      "gists_url": "https://api.github.com/users/jonschipp/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/jonschipp/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/jonschipp/subscriptions",
      "organizations_url": "https://api.github.com/users/jonschipp/orgs",
      "repos_url": "https://api.github.com/users/jonschipp/repos",
      "events_url": "https://api.github.com/users/jonschipp/events{/privacy}",
      "received_events_url": "https://api.github.com/users/jonschipp/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/jonschipp/ISLET",
    "description": "Isolated, Scalable, & Lightweight Environment for Training",
    "fork": false,
    "url": "https://api.github.com/repos/jonschipp/ISLET",
    "forks_url": "https://api.github.com/repos/jonschipp/ISLET/forks",
    "keys_url": "https://api.github.com/repos/jonschipp/ISLET/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/jonschipp/ISLET/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/jonschipp/ISLET/teams",
    "hooks_url": "https://api.github.com/repos/jonschipp/ISLET/hooks",
    "issue_events_url": "https://api.github.com/repos/jonschipp/ISLET/issues/events{/number}",
    "events_url": "https://api.github.com/repos/jonschipp/ISLET/events",
    "assignees_url": "https://api.github.com/repos/jonschipp/ISLET/assignees{/user}",
    "branches_url": "https://api.github.com/repos/jonschipp/ISLET/branches{/branch}",
    "tags_url": "https://api.github.com/repos/jonschipp/ISLET/tags",
    "blobs_url": "https://api.github.com/repos/jonschipp/ISLET/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/jonschipp/ISLET/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/jonschipp/ISLET/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/jonschipp/ISLET/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/jonschipp/ISLET/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/jonschipp/ISLET/languages",
    "stargazers_url": "https://api.github.com/repos/jonschipp/ISLET/stargazers",
    "contributors_url": "https://api.github.com/repos/jonschipp/ISLET/contributors",
    "subscribers_url": "https://api.github.com/repos/jonschipp/ISLET/subscribers",
    "subscription_url": "https://api.github.com/repos/jonschipp/ISLET/subscription",
    "commits_url": "https://api.github.com/repos/jonschipp/ISLET/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/jonschipp/ISLET/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/jonschipp/ISLET/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/jonschipp/ISLET/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/jonschipp/ISLET/contents/{+path}",
    "compare_url": "https://api.github.com/repos/jonschipp/ISLET/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/jonschipp/ISLET/merges",
    "archive_url": "https://api.github.com/repos/jonschipp/ISLET/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/jonschipp/ISLET/downloads",
    "issues_url": "https://api.github.com/repos/jonschipp/ISLET/issues{/number}",
    "pulls_url": "https://api.github.com/repos/jonschipp/ISLET/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/jonschipp/ISLET/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/jonschipp/ISLET/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/jonschipp/ISLET/labels{/name}",
    "releases_url": "https://api.github.com/repos/jonschipp/ISLET/releases{/id}",
    "deployments_url": "https://api.github.com/repos/jonschipp/ISLET/deployments",
    "created_at": "2014-09-19T16:36:48Z",
    "updated_at": "2018-08-19T04:28:21Z",
    "pushed_at": "2018-01-11T00:24:34Z",
    "git_url": "git://github.com/jonschipp/ISLET.git",
    "ssh_url": "git@github.com:jonschipp/ISLET.git",
    "clone_url": "https://github.com/jonschipp/ISLET.git",
    "svn_url": "https://github.com/jonschipp/ISLET",
    "size": 479,
    "stargazers_count": 91,
    "watchers_count": 91,
    "language": "Shell",
    "has_issues": true,
    "has_projects": true,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": false,
    "forks_count": 13,
    "archived": false,
    "open_issues_count": 27,
    "license": {
      "key": "other",
      "name": "Other",
      "node_id": "MDc6TGljZW5zZTA="
    },
    "forks": 13,
    "open_issues": 27,
    "watchers": 91,
    "default_branch": "master",
    "permissions": {
      "admin": true,
      "push": true,
      "pull": true
    },
    "allow_squash_merge": true,
    "allow_merge_commit": true,
    "allow_rebase_merge": true,
    "network_count": 13,
    "subscribers_count": 20
    }
  }
}

```

### Get My Issues

This action is used to retrieve all issues assigned to the currently authenticated user.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issues|[]issue|False|An array of the issues assigned to the current user|

Example output:

```

{
  "issues": [
    {
      "url": "https://api.github.com/repos/open-nsm/ContainNSM/issues/49",
      "repository_url": "https://api.github.com/repos/open-nsm/ContainNSM",
      "labels_url": "https://api.github.com/repos/open-nsm/ContainNSM/issues/49/labels{/name}",
      "comments_url": "https://api.github.com/repos/open-nsm/ContainNSM/issues/49/comments",
      "events_url": "https://api.github.com/repos/open-nsm/ContainNSM/issues/49/events",
      "html_url": "https://github.com/open-nsm/ContainNSM/pull/49",
      "id": 221813330,
      "node_id": "MDExOlB1bGxSZXF1ZXN0MTE1OTMzOTUy",
      "number": 49,
      "title": "Attempt at fixing27",
      "user": {
        "login": "mrc0der",
        "id": 1816381,
        "node_id": "MDQ6VXNlcjE4MTYzODE=",
        "avatar_url": "https://avatars3.githubusercontent.com/u/1816381?v=4",
        "url": "https://api.github.com/users/mrc0der",
        "html_url": "https://github.com/mrc0der",
        "followers_url": "https://api.github.com/users/mrc0der/followers",
        "following_url": "https://api.github.com/users/mrc0der/following{/other_user}",
        "gists_url": "https://api.github.com/users/mrc0der/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/mrc0der/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/mrc0der/subscriptions",
        "organizations_url": "https://api.github.com/users/mrc0der/orgs",
        "repos_url": "https://api.github.com/users/mrc0der/repos",
        "events_url": "https://api.github.com/users/mrc0der/events{/privacy}",
        "received_events_url": "https://api.github.com/users/mrc0der/received_events",
        "type": "User",
        "site_admin": false
      },
      "labels": [
        {
          "id": 235177181,
          "node_id": "MDU6TGFiZWwyMzUxNzcxODE=",
          "url": "https://api.github.com/repos/open-nsm/ContainNSM/labels/enhancement",
          "name": "enhancement",
          "color": "84b6eb",
          "default": true
        }
      ],
      "state": "open",
      "locked": false,
      "assignee": {
        "login": "jonschipp",
        "id": 2321183,
        "node_id": "MDQ6VXNlcjIzMjExODM=",
        "avatar_url": "https://avatars0.githubusercontent.com/u/2321183?v=4",
        "url": "https://api.github.com/users/jonschipp",
        "html_url": "https://github.com/jonschipp",
        "followers_url": "https://api.github.com/users/jonschipp/followers",
        "following_url": "https://api.github.com/users/jonschipp/following{/other_user}",
        "gists_url": "https://api.github.com/users/jonschipp/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/jonschipp/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/jonschipp/subscriptions",
        "organizations_url": "https://api.github.com/users/jonschipp/orgs",
        "repos_url": "https://api.github.com/users/jonschipp/repos",
        "events_url": "https://api.github.com/users/jonschipp/events{/privacy}",
        "received_events_url": "https://api.github.com/users/jonschipp/received_events",
        "type": "User",
        "site_admin": false
      },
      "assignees": [
        {
          "login": "jonschipp",
          "id": 2321183,
          "node_id": "MDQ6VXNlcjIzMjExODM=",
          "avatar_url": "https://avatars0.githubusercontent.com/u/2321183?v=4",
          "url": "https://api.github.com/users/jonschipp",
          "html_url": "https://github.com/jonschipp",
          "followers_url": "https://api.github.com/users/jonschipp/followers",
          "following_url": "https://api.github.com/users/jonschipp/following{/other_user}",
          "gists_url": "https://api.github.com/users/jonschipp/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/jonschipp/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/jonschipp/subscriptions",
          "organizations_url": "https://api.github.com/users/jonschipp/orgs",
          "repos_url": "https://api.github.com/users/jonschipp/repos",
          "events_url": "https://api.github.com/users/jonschipp/events{/privacy}",
          "received_events_url": "https://api.github.com/users/jonschipp/received_events",
          "type": "User",
          "site_admin": false
        }
      ],
      "comments": 0,
      "created_at": "2017-04-14T13:53:49Z",
      "updated_at": "2017-04-27T16:44:17Z",
      "author_association": "CONTRIBUTOR",
      "repository": {
        "id": 38940415,
        "node_id": "MDEwOlJlcG9zaXRvcnkzODk0MDQxNQ==",
        "name": "ContainNSM",
        "full_name": "open-nsm/ContainNSM",
        "owner": {
          "login": "open-nsm",
          "id": 8526997,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjg1MjY5OTc=",
          "avatar_url": "https://avatars0.githubusercontent.com/u/8526997?v=4",
          "url": "https://api.github.com/users/open-nsm",
          "html_url": "https://github.com/open-nsm",
          "followers_url": "https://api.github.com/users/open-nsm/followers",
          "following_url": "https://api.github.com/users/open-nsm/following{/other_user}",
          "gists_url": "https://api.github.com/users/open-nsm/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/open-nsm/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/open-nsm/subscriptions",
          "organizations_url": "https://api.github.com/users/open-nsm/orgs",
          "repos_url": "https://api.github.com/users/open-nsm/repos",
          "events_url": "https://api.github.com/users/open-nsm/events{/privacy}",
          "received_events_url": "https://api.github.com/users/open-nsm/received_events",
          "type": "Organization",
          "site_admin": false
        },
        "private": false,
        "html_url": "https://github.com/open-nsm/ContainNSM",
        "description": "Dockerfiles for NSM tools",
        "fork": false,
        "url": "https://api.github.com/repos/open-nsm/ContainNSM",
        "forks_url": "https://api.github.com/repos/open-nsm/ContainNSM/forks",
        "keys_url": "https://api.github.com/repos/open-nsm/ContainNSM/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/open-nsm/ContainNSM/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/open-nsm/ContainNSM/teams",
        "hooks_url": "https://api.github.com/repos/open-nsm/ContainNSM/hooks",
        "issue_events_url": "https://api.github.com/repos/open-nsm/ContainNSM/issues/events{/number}",
        "events_url": "https://api.github.com/repos/open-nsm/ContainNSM/events",
        "assignees_url": "https://api.github.com/repos/open-nsm/ContainNSM/assignees{/user}",
        "branches_url": "https://api.github.com/repos/open-nsm/ContainNSM/branches{/branch}",
        "tags_url": "https://api.github.com/repos/open-nsm/ContainNSM/tags",
        "blobs_url": "https://api.github.com/repos/open-nsm/ContainNSM/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/open-nsm/ContainNSM/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/open-nsm/ContainNSM/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/open-nsm/ContainNSM/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/open-nsm/ContainNSM/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/open-nsm/ContainNSM/languages",
        "stargazers_url": "https://api.github.com/repos/open-nsm/ContainNSM/stargazers",
        "contributors_url": "https://api.github.com/repos/open-nsm/ContainNSM/contributors",
        "subscribers_url": "https://api.github.com/repos/open-nsm/ContainNSM/subscribers",
        "subscription_url": "https://api.github.com/repos/open-nsm/ContainNSM/subscription",
        "commits_url": "https://api.github.com/repos/open-nsm/ContainNSM/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/open-nsm/ContainNSM/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/open-nsm/ContainNSM/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/open-nsm/ContainNSM/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/open-nsm/ContainNSM/contents/{+path}",
        "compare_url": "https://api.github.com/repos/open-nsm/ContainNSM/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/open-nsm/ContainNSM/merges",
        "archive_url": "https://api.github.com/repos/open-nsm/ContainNSM/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/open-nsm/ContainNSM/downloads",
        "issues_url": "https://api.github.com/repos/open-nsm/ContainNSM/issues{/number}",
        "pulls_url": "https://api.github.com/repos/open-nsm/ContainNSM/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/open-nsm/ContainNSM/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/open-nsm/ContainNSM/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/open-nsm/ContainNSM/labels{/name}",
        "releases_url": "https://api.github.com/repos/open-nsm/ContainNSM/releases{/id}",
        "deployments_url": "https://api.github.com/repos/open-nsm/ContainNSM/deployments",
        "created_at": "2015-07-11T21:05:06Z",
        "updated_at": "2018-05-18T15:28:38Z",
        "pushed_at": "2017-04-14T15:28:17Z",
        "git_url": "git://github.com/open-nsm/ContainNSM.git",
        "ssh_url": "git@github.com:open-nsm/ContainNSM.git",
        "clone_url": "https://github.com/open-nsm/ContainNSM.git",
        "svn_url": "https://github.com/open-nsm/ContainNSM",
        "size": 195,
        "stargazers_count": 75,
        "watchers_count": 75,
        "language": "Shell",
        "has_issues": true,
        "has_projects": true,
        "has_downloads": true,
        "has_wiki": true,
        "has_pages": false,
        "forks_count": 10,
        "archived": false,
        "open_issues_count": 14,
        "forks": 10,
        "open_issues": 14,
        "watchers": 75,
        "default_branch": "master"
      },
      "pull_request": {
        "url": "https://api.github.com/repos/open-nsm/ContainNSM/pulls/49",
        "html_url": "https://github.com/open-nsm/ContainNSM/pull/49",
        "diff_url": "https://github.com/open-nsm/ContainNSM/pull/49.diff",
        "patch_url": "https://github.com/open-nsm/ContainNSM/pull/49.patch"
      },
      "body": "This should fix #27 but also allow for other group builds to still work. \r\n\r\nThis checks for the existence of tag rather then testing its character classes. \r\n\r\nLet me know what you think. "
    },
    ...
  ]
}

```

### Get Issues by Repo

This action is used to retrieve all issues currently open on the specified repo.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|owner|string|None|True|Owner of the repository|None|
|title|string|None|True|Name of the repository|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issues|[]issue|False|An array of the issues open on the specified repo|

Example output:

```

{
  "issues": [
    {
      "url": "https://api.github.com/repos/jonschipp/ISLET/issues/93",
      "repository_url": "https://api.github.com/repos/jonschipp/ISLET",
      "labels_url": "https://api.github.com/repos/jonschipp/ISLET/issues/93/labels{/name}",
      "comments_url": "https://api.github.com/repos/jonschipp/ISLET/issues/93/comments",
      "events_url": "https://api.github.com/repos/jonschipp/ISLET/issues/93/events",
      "html_url": "https://github.com/jonschipp/ISLET/issues/93",
      "id": 298387293,
      "node_id": "MDU6SXNzdWUyOTgzODcyOTM=",
      "number": 93,
      "title": "make package needs installation folder",
      "user": {
        "login": "javabeanz",
        "id": 3225772,
        "node_id": "MDQ6VXNlcjMyMjU3NzI=",
        "avatar_url": "https://avatars3.githubusercontent.com/u/3225772?v=4",
        "url": "https://api.github.com/users/javabeanz",
        "html_url": "https://github.com/javabeanz",
        "followers_url": "https://api.github.com/users/javabeanz/followers",
        "following_url": "https://api.github.com/users/javabeanz/following{/other_user}",
        "gists_url": "https://api.github.com/users/javabeanz/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/javabeanz/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/javabeanz/subscriptions",
        "organizations_url": "https://api.github.com/users/javabeanz/orgs",
        "repos_url": "https://api.github.com/users/javabeanz/repos",
        "events_url": "https://api.github.com/users/javabeanz/events{/privacy}",
        "received_events_url": "https://api.github.com/users/javabeanz/received_events",
        "type": "User",
        "site_admin": false
      },
      "labels": [],
      "state": "open",
      "locked": false,
      "assignees": [],
      "comments": 0,
      "created_at": "2018-02-19T20:01:25Z",
      "updated_at": "2018-02-19T20:01:25Z",
      "author_association": "NONE",
      "body": "executing \"make package\" requires folder /etc/islet which goes against the function of making a package."
    },
    ...
  ]
}

```

### Block User

This action is used to block a user.

The User Blocking API on GitHub is currently available for developers to preview.
Warning: The API may change without advance notice during the preview period. Preview features are not supported for production use.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Username to block|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether the user was unblocked|

Example output:

```

{
  "success": true
}

```

### Unblock User

This action is used to unblock a user.

The User Blocking API on GitHub is currently available for developers to preview.
Warning: The API may change without advance notice during the preview period. Preview features are not supported for production use.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Username to unblock|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether the user was unblocked|

Example output:

```

{
  "success": true
}

```

## Triggers

### Issue

This trigger is used to monitor a repository for new issues and returns any new issues found.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization|string|None|False|Return issues of a specific organization|None|
|frequency|integer|300|False|Poll frequency in seconds|None|
|repository|string|None|True|Return issues of a specific repository|None|
|assignee|string|None|False|Username of assignee|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issue|object|False|None|

Example output:

```

{
  "issues": {
    "url": "https://github.com/jonschipp/ISLET/issues/95",
    "title": "New ticket",
    "body": "Test body",
    "creation_date": "2018-09-04 15:34:49",
    "author": "jonschipp"
  }
}

```

## Connection

This plugin requires a GitHub username and password (or token).

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|GitHub credentials|None|

## Troubleshooting

If two-factor authentication is enabled on the GitHub account you will need to [generate an access token](https://github.com/settings/tokens) to use instead of your regular password.

### Permissions

By default, a newly created token will be unprivileged. Removing users, creating issues, and viewing any data associated with private repositories will require a token with the appropriate permissions.

All actions can use the "repo" permission scope except "Remove User" which requires the "admin:org" permission scope.

## Workflows

Examples:

* [ChatOps: GitHub Commands](https://market.komand.com/workflows/ross/chatops-github-commands/1.0.0)
* Ticket creation
* User deprovisioning

## Versions

* 0.1.0 - Initial plugin
* 0.2.0 - New actions: Get Repo, Get My Issues, Get Issues by Repo, and Search
* 0.2.1 - New optional Assignee input to Create Issue action
* 0.2.2 - New optional Milestone input to Create Issue action
* 0.2.3 - SSL bug fix in SDK
* 1.0.0 - Add Collaborator action | Update to v2 Python plugin architecture | Support web server mode
* 1.1.0 - Add Membership action
* 1.2.0 - Add Block User and Unblock User action
* 1.2.1 - Update connection documentation and add example outputs to remaining actions and triggers
* 2.0.0 - Rename "User" action to "Get User"
* 2.0.1 - Fix missing Search action | Pin pygithub and python-dateutil libraries | Update to use the `komand/python-3-37-slim-plugin` Docker image to reduce plugin size | Enable verification of SSL/TLS certificates for github.com
* 2.0.2 - New actions: Create Issue Comment, Close Issue, Add Issue Label

## References

* [GitHub](https://github.com)
* [GitHub REST API](https://developer.github.com/v3/)
