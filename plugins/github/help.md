# Description

[GitHub](https://github.com/) is a popular web-based Git or version control repository and Internet hosting service GitHub. InsightConnect plugin allows users and issues management. This plugin supports authentication from both personal and organization member accounts

# Key Features
  
* Issue management  
* User management

# Requirements
  
* GitHub username and client secret

# Supported Product Versions
  
* GitHub API version 2022-11-28

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|git_hub_credentials|None|True|GitHub credentials|None|{'username': 'test_username', 'personal_token': {'secretKey': 'ghp_123456789abcdefghABCDEFGH'}}|
  
Example input:

```
{
  "credentials": {
    "personal_token": {
      "secretKey": "ghp_123456789abcdefghABCDEFGH"
    },
    "username": "test_username"
  }
}
```

## Technical Details

### Actions


#### Add Collaborator
  
This action is used to adds a user as a collaborator to a GitHub repository

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|organization|string|None|False|Organization the repository is under|None|test_organization|
|permission|string|push|False|The permission to grant the collaborator. Only valid on organization-owned repositories|["pull", "push", "admin"]|admin|
|repository|string|None|False|Repository to add user as a collaborator|None|test_repository|
|username|string|None|True|Username to add as a collaborator|None|test_username|
  
Example input:

```
{
  "organization": "test_organization",
  "permission": "push",
  "repository": "test_repository",
  "username": "test_username"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|add_collaborator|False|Response from adding a new collaborator|{'id': 244304010, 'node_id': 'RI_kwDOLIAEx84Oj8iK', 'repository': {'id': 746587335, 'node_id': 'R_kgDOLIAExw', 'name': 'test_repository', 'full_name': 'test_organization/test_repository', 'private': True, 'owner': {'login': 'test_organization', 'id': 157362711, 'node_id': 'O_kgDOCWEqFw', 'avatar_url': 'https://avatars.githubusercontent.com/u/157362711?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/test_organization', 'html_url': 'https://github.com/test_organization', 'followers_url': 'https://api.github.com/users/test_organization/followers', 'following_url': 'https://api.github.com/users/test_organization/following{/other_user}', 'gists_url': 'https://api.github.com/users/test_organization/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/test_organization/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/test_organization/subscriptions', 'organizations_url': 'https://api.github.com/users/test_organization/orgs', 'repos_url': 'https://api.github.com/users/test_organization/repos', 'events_url': 'https://api.github.com/users/test_organization/events{/privacy}', 'received_events_url': 'https://api.github.com/users/test_organization/received_events', 'type': 'Organization', 'site_admin': False}, 'html_url': 'https://github.com/test_organization/test_repository', 'description': 'test for insight connect plugins', 'fork': False, 'url': 'https://api.github.com/repos/test_organization/test_repository', 'forks_url': 'https://api.github.com/repos/test_organization/test_repository/forks', 'keys_url': 'https://api.github.com/repos/test_organization/test_repository/keys{/key_id}', 'collaborators_url': 'https://api.github.com/repos/test_organization/test_repository/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/test_organization/test_repository/teams', 'hooks_url': 'https://api.github.com/repos/test_organization/test_repository/hooks', 'issue_events_url': 'https://api.github.com/repos/test_organization/test_repository/issues/events{/number}', 'events_url': 'https://api.github.com/repos/test_organization/test_repository/events', 'assignees_url': 'https://api.github.com/repos/test_organization/test_repository/assignees{/user}', 'branches_url': 'https://api.github.com/repos/test_organization/test_repository/branches{/branch}', 'tags_url': 'https://api.github.com/repos/test_organization/test_repository/tags', 'blobs_url': 'https://api.github.com/repos/test_organization/test_repository/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/test_organization/test_repository/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/test_organization/test_repository/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/test_organization/test_repository/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/test_organization/test_repository/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/test_organization/test_repository/languages', 'stargazers_url': 'https://api.github.com/repos/test_organization/test_repository/stargazers', 'contributors_url': 'https://api.github.com/repos/test_organization/test_repository/contributors', 'subscribers_url': 'https://api.github.com/repos/test_organization/test_repository/subscribers', 'subscription_url': 'https://api.github.com/repos/test_organization/test_repository/subscription', 'commits_url': 'https://api.github.com/repos/test_organization/test_repository/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/test_organization/test_repository/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/test_organization/test_repository/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/test_organization/test_repository/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/test_organization/test_repository/contents/{+path}', 'compare_url': 'https://api.github.com/repos/test_organization/test_repository/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/test_organization/test_repository/merges', 'archive_url': 'https://api.github.com/repos/test_organization/test_repository/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/test_organization/test_repository/downloads', 'issues_url': 'https://api.github.com/repos/test_organization/test_repository/issues{/number}', 'pulls_url': 'https://api.github.com/repos/test_organization/test_repository/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/test_organization/test_repository/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/test_organization/test_repository/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/test_organization/test_repository/labels{/name}', 'releases_url': 'https://api.github.com/repos/test_organization/test_repository/releases{/id}', 'deployments_url': 'https://api.github.com/repos/test_organization/test_repository/deployments'}, 'invitee': {'login': 'test_username', 'id': 144030336, 'node_id': 'U_kgDOCJW6gA', 'avatar_url': 'https://avatars.githubusercontent.com/u/144030336?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/test_username', 'html_url': 'https://github.com/test_username', 'followers_url': 'https://api.github.com/users/test_username/followers', 'following_url': 'https://api.github.com/users/test_username/following{/other_user}', 'gists_url': 'https://api.github.com/users/test_username/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/test_username/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/test_username/subscriptions', 'organizations_url': 'https://api.github.com/users/test_username/orgs', 'repos_url': 'https://api.github.com/users/test_username/repos', 'events_url': 'https://api.github.com/users/test_username/events{/privacy}', 'received_events_url': 'https://api.github.com/users/test_username/received_events', 'type': 'User', 'site_admin': False}, 'inviter': {'login': 'test_invite_user', 'id': 157107299, 'node_id': 'U_kgDOCV1EYw', 'avatar_url': 'https://avatars.githubusercontent.com/u/157107299?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/test_invite_user', 'html_url': 'https://github.com/test_invite_user', 'followers_url': 'https://api.github.com/users/test_invite_user/followers', 'following_url': 'https://api.github.com/users/test_invite_user/following{/other_user}', 'gists_url': 'https://api.github.com/users/test_invite_user/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/test_invite_user/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/test_invite_user/subscriptions', 'organizations_url': 'https://api.github.com/users/test_invite_user/orgs', 'repos_url': 'https://api.github.com/users/test_invite_user/repos', 'events_url': 'https://api.github.com/users/test_invite_user/events{/privacy}', 'received_events_url': 'https://api.github.com/users/test_invite_user/received_events', 'type': 'User', 'site_admin': False}, 'permissions': 'write', 'created_at': '2024-01-24T12:02:16Z', 'url': 'https://api.github.com/user/repository_invitations/244304010', 'html_url': 'https://github.com/test_organization/test_repository/invitations'}|
  
Example output:

```
{
  "results": {
    "created_at": "2024-01-24T12:02:16Z",
    "html_url": "https://github.com/test_organization/test_repository/invitations",
    "id": 244304010,
    "invitee": {
      "avatar_url": "https://avatars.githubusercontent.com/u/144030336?v=4",
      "events_url": "https://api.github.com/users/test_username/events{/privacy}",
      "followers_url": "https://api.github.com/users/test_username/followers",
      "following_url": "https://api.github.com/users/test_username/following{/other_user}",
      "gists_url": "https://api.github.com/users/test_username/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/test_username",
      "id": 144030336,
      "login": "test_username",
      "node_id": "U_kgDOCJW6gA",
      "organizations_url": "https://api.github.com/users/test_username/orgs",
      "received_events_url": "https://api.github.com/users/test_username/received_events",
      "repos_url": "https://api.github.com/users/test_username/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/test_username/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/test_username/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/test_username"
    },
    "inviter": {
      "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
      "events_url": "https://api.github.com/users/test_invite_user/events{/privacy}",
      "followers_url": "https://api.github.com/users/test_invite_user/followers",
      "following_url": "https://api.github.com/users/test_invite_user/following{/other_user}",
      "gists_url": "https://api.github.com/users/test_invite_user/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/test_invite_user",
      "id": 157107299,
      "login": "test_invite_user",
      "node_id": "U_kgDOCV1EYw",
      "organizations_url": "https://api.github.com/users/test_invite_user/orgs",
      "received_events_url": "https://api.github.com/users/test_invite_user/received_events",
      "repos_url": "https://api.github.com/users/test_invite_user/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/test_invite_user/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/test_invite_user/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/test_invite_user"
    },
    "node_id": "RI_kwDOLIAEx84Oj8iK",
    "permissions": "write",
    "repository": {
      "archive_url": "https://api.github.com/repos/test_organization/test_repository/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/test_organization/test_repository/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/test_organization/test_repository/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/test_organization/test_repository/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/test_organization/test_repository/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/test_organization/test_repository/comments{/number}",
      "commits_url": "https://api.github.com/repos/test_organization/test_repository/commits{/sha}",
      "compare_url": "https://api.github.com/repos/test_organization/test_repository/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/test_organization/test_repository/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/test_organization/test_repository/contributors",
      "deployments_url": "https://api.github.com/repos/test_organization/test_repository/deployments",
      "description": "test for insight connect plugins",
      "downloads_url": "https://api.github.com/repos/test_organization/test_repository/downloads",
      "events_url": "https://api.github.com/repos/test_organization/test_repository/events",
      "fork": false,
      "forks_url": "https://api.github.com/repos/test_organization/test_repository/forks",
      "full_name": "test_organization/test_repository",
      "git_commits_url": "https://api.github.com/repos/test_organization/test_repository/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/test_organization/test_repository/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/test_organization/test_repository/git/tags{/sha}",
      "hooks_url": "https://api.github.com/repos/test_organization/test_repository/hooks",
      "html_url": "https://github.com/test_organization/test_repository",
      "id": 746587335,
      "issue_comment_url": "https://api.github.com/repos/test_organization/test_repository/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/test_organization/test_repository/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/test_organization/test_repository/issues{/number}",
      "keys_url": "https://api.github.com/repos/test_organization/test_repository/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/test_organization/test_repository/labels{/name}",
      "languages_url": "https://api.github.com/repos/test_organization/test_repository/languages",
      "merges_url": "https://api.github.com/repos/test_organization/test_repository/merges",
      "milestones_url": "https://api.github.com/repos/test_organization/test_repository/milestones{/number}",
      "name": "test_repository",
      "node_id": "R_kgDOLIAExw",
      "notifications_url": "https://api.github.com/repos/test_organization/test_repository/notifications{?since,all,participating}",
      "owner": {
        "avatar_url": "https://avatars.githubusercontent.com/u/157362711?v=4",
        "events_url": "https://api.github.com/users/test_organization/events{/privacy}",
        "followers_url": "https://api.github.com/users/test_organization/followers",
        "following_url": "https://api.github.com/users/test_organization/following{/other_user}",
        "gists_url": "https://api.github.com/users/test_organization/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/test_organization",
        "id": 157362711,
        "login": "test_organization",
        "node_id": "O_kgDOCWEqFw",
        "organizations_url": "https://api.github.com/users/test_organization/orgs",
        "received_events_url": "https://api.github.com/users/test_organization/received_events",
        "repos_url": "https://api.github.com/users/test_organization/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/test_organization/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/test_organization/subscriptions",
        "type": "Organization",
        "url": "https://api.github.com/users/test_organization"
      },
      "private": true,
      "pulls_url": "https://api.github.com/repos/test_organization/test_repository/pulls{/number}",
      "releases_url": "https://api.github.com/repos/test_organization/test_repository/releases{/id}",
      "stargazers_url": "https://api.github.com/repos/test_organization/test_repository/stargazers",
      "statuses_url": "https://api.github.com/repos/test_organization/test_repository/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/test_organization/test_repository/subscribers",
      "subscription_url": "https://api.github.com/repos/test_organization/test_repository/subscription",
      "tags_url": "https://api.github.com/repos/test_organization/test_repository/tags",
      "teams_url": "https://api.github.com/repos/test_organization/test_repository/teams",
      "trees_url": "https://api.github.com/repos/test_organization/test_repository/git/trees{/sha}",
      "url": "https://api.github.com/repos/test_organization/test_repository"
    },
    "url": "https://api.github.com/user/repository_invitations/244304010"
  }
}
```

#### Add Issue Label
  
This action is used to adds a label to an issue

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|issue_number|number|None|True|Issue number|None|1|
|label|string|None|True|Issue label|None|test_label|
|organization|string|None|False|Organizational owner of repository|None|test_organization|
|repository|string|None|True|Repository to post issue|None|test_repository|
  
Example input:

```
{
  "issue_number": 1,
  "label": "test_label",
  "organization": "test_organization",
  "repository": "test_repository"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Returns true if the label was added|True|
  
Example output:

```
{
  "success": true
}
```

#### Add Membership
  
This action is used to add or update user's membership in an organization

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|organization|string|None|False|The organization that user will be added or updated to|None|test_organization|
|role|string|member|False|The role to give the user in the organization|["admin", "member"]|admin|
|username|string|None|False|The user that will be added or updated|None|test_username|
  
Example input:

```
{
  "organization": "test_organization",
  "role": "member",
  "username": "test_username"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|organization|membership_organization|False|Organization|{'avatar_url': 'https://avatars.githubusercontent.com/u/157362711?v=4', 'events_url': 'https://api.github.com/orgs/test_organization/events', 'hooks_url': 'https://api.github.com/orgs/test_organization/hooks', 'id': 157362711, 'issues_url': 'https://api.github.com/orgs/test_organization/issues', 'login': 'test_organization', 'members_url': 'https://api.github.com/orgs/test_organization/members{/member}', 'node_id': 'O_kgDOCWEqFw', 'public_members_url': 'https://api.github.com/orgs/test_organization/public_members{/member}', 'repos_url': 'https://api.github.com/orgs/test_organization/repos', 'url': 'https://api.github.com/orgs/test_organization'}|
|organization_url|string|False|Organization URL|https://api.github.com/orgs/test_organization|
|role|string|False|Role of users membership|member|
|state|string|False|State of users membership|pending|
|url|string|False|URL|https://api.github.com/orgs/test_organization/memberships/test_user|
|user|membership_user|False|User|{'avatar_url': 'https://avatars.githubusercontent.com/u/144030336?v=4', 'events_url': 'https://api.github.com/users/test_user/events{/privacy}', 'followers_url': 'https://api.github.com/users/test_user/followers', 'following_url': 'https://api.github.com/users/test_user/following{/other_user}', 'gists_url': 'https://api.github.com/users/test_user/gists{/gist_id}', 'html_url': 'https://github.com/test_user', 'id': 144030336, 'login': 'test_user', 'node_id': 'U_kgDOCJW6gA', 'organizations_url': 'https://api.github.com/users/test_user/orgs', 'received_events_url': 'https://api.github.com/users/test_user/received_events', 'repos_url': 'https://api.github.com/users/test_user/repos', 'site_admin': False, 'starred_url': 'https://api.github.com/users/test_user/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/test_user/subscriptions', 'type': 'User', 'url': 'https://api.github.com/users/test_user'}|
  
Example output:

```
{
  "organization": {
    "avatar_url": "https://avatars.githubusercontent.com/u/157362711?v=4",
    "events_url": "https://api.github.com/orgs/test_organization/events",
    "hooks_url": "https://api.github.com/orgs/test_organization/hooks",
    "id": 157362711,
    "issues_url": "https://api.github.com/orgs/test_organization/issues",
    "login": "test_organization",
    "members_url": "https://api.github.com/orgs/test_organization/members{/member}",
    "node_id": "O_kgDOCWEqFw",
    "public_members_url": "https://api.github.com/orgs/test_organization/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/test_organization/repos",
    "url": "https://api.github.com/orgs/test_organization"
  },
  "organization_url": "https://api.github.com/orgs/test_organization",
  "role": "member",
  "state": "pending",
  "url": "https://api.github.com/orgs/test_organization/memberships/test_user",
  "user": {
    "avatar_url": "https://avatars.githubusercontent.com/u/144030336?v=4",
    "events_url": "https://api.github.com/users/test_user/events{/privacy}",
    "followers_url": "https://api.github.com/users/test_user/followers",
    "following_url": "https://api.github.com/users/test_user/following{/other_user}",
    "gists_url": "https://api.github.com/users/test_user/gists{/gist_id}",
    "html_url": "https://github.com/test_user",
    "id": 144030336,
    "login": "test_user",
    "node_id": "U_kgDOCJW6gA",
    "organizations_url": "https://api.github.com/users/test_user/orgs",
    "received_events_url": "https://api.github.com/users/test_user/received_events",
    "repos_url": "https://api.github.com/users/test_user/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/test_user/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/test_user"
  }
}
```

#### Block User
  
This action is used to block a user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|username|string|None|True|Username to block|None|test_username|
  
Example input:

```
{
  "username": "test_username"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the user was unblocked|True|
  
Example output:

```
{
  "success": true
}
```

#### Close Issue
  
This action is used to close issue

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|issue_number|number|None|True|Issue number|None|1|
|organization|string|None|False|Organizational owner of repository|None|test_organization|
|repository|string|None|True|Repository to post issue|None|test_repository|
  
Example input:

```
{
  "issue_number": 1,
  "organization": "test_organization",
  "repository": "test_repository"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Returns true if the issue was closed|True|
  
Example output:

```
{
  "success": true
}
```

#### Create Issue
  
This action is used to create an issue ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assignee|string|None|False|User to assign this issue to|None|test_username|
|body|string|None|True|Body text of issue|None|test_body|
|labels|string|None|False|GitHub search tags delimited by commas|None|test_label_2, test_label_2|
|milestone|number|None|False|ID of the milestone to associate this issue with|None|1|
|organization|string|None|False|Organizational owner of repository|None|test_organization|
|repository|string|None|True|Repository to post issue|None|test_repository|
|title|string|None|True|Title of issue|None|test_title|
  
Example input:

```
{
  "assignee": "test_username",
  "body": "test_body",
  "labels": "test_label_2, test_label_2",
  "milestone": 1,
  "organization": "test_organization",
  "repository": "test_repository",
  "title": "test_title"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|url|string|False|URL|https://github.com/test_organization/test_repository/issues/8|
  
Example output:

```
{
  "url": "https://github.com/test_organization/test_repository/issues/8"
}
```

#### Create Issue Comment
  
This action is used to create an issue comment

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|body|string|None|True|Body text of issue|None|test_body|
|issue_number|number|None|True|Issue number|None|1|
|organization|string|None|False|Organizational owner of repository|None|test_organization|
|repository|string|None|True|Repository to post issue|None|test_repository|
  
Example input:

```
{
  "body": "test_body",
  "issue_number": 1,
  "organization": "test_organization",
  "repository": "test_repository"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|url|string|False|URL|https://github.com/test_organization/test_repository/issues/1#issuecomment-123456789|
  
Example output:

```
{
  "url": "https://github.com/test_organization/test_repository/issues/1#issuecomment-123456789"
}
```

#### Get Issues by Repo
  
This action is used to retrieve all issues currently open on the specified repo

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|owner|string|None|True|Owner of the repository|None|test_owner|
|title|string|None|True|Name of the repository|None|test_title|
  
Example input:

```
{
  "owner": "test_owner",
  "title": "test_title"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|issues|[]issue|False|An array of the issues open on the specified repo|[{"assignee": {"avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4","events_url": "https://api.github.com/users/test_user/events{/privacy}","followers_url": "https://api.github.com/users/test_user/followers","following_url": "https://api.github.com/users/test_user/following{/other_user}","gists_url": "https://api.github.com/users/test_user/gists{/gist_id}","html_url": "https://github.com/test_user","id": 157107299,"login": "test_user","node_id": "U_kgDOCV1EYw","organizations_url": "https://api.github.com/users/test_user/orgs","received_events_url": "https://api.github.com/users/test_user/received_events","repos_url": "https://api.github.com/users/test_user/repos","site_admin": false,"starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}","subscriptions_url": "https://api.github.com/users/test_user/subscriptions","type": "User","url": "https://api.github.com/users/test_user"},"assignees": [{"avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4","events_url": "https://api.github.com/users/test_user/events{/privacy}","followers_url": "https://api.github.com/users/test_user/followers","following_url": "https://api.github.com/users/test_user/following{/other_user}","gists_url": "https://api.github.com/users/test_user/gists{/gist_id}","html_url": "https://github.com/test_user","id": 157107299,"login": "test_user","node_id": "U_kgDOCV1EYw","organizations_url": "https://api.github.com/users/test_user/orgs","received_events_url": "https://api.github.com/users/test_user/received_events","repos_url": "https://api.github.com/users/test_user/repos","site_admin": false,"starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}","subscriptions_url": "https://api.github.com/users/test_user/subscriptions","type": "User","url": "https://api.github.com/users/test_user"}],"author_association": "OWNER","body": "This was created so we can see if issues are pulled in correctly","comments": 0,"comments_url": "https://api.github.com/repos/test_user/test_repo/issues/1/comments","created_at": "2024-01-22T09:42:18Z","events_url": "https://api.github.com/repos/test_user/test_repo/issues/1/events","html_url": "https://github.com/test_user/test_repo/issues/1","id": 2093498528,"labels": [{"color": "d73a4a","default": true,"description": "Something isnt working","id": 6460729259,"name": "bug","node_id": "LA_kwDOLH_fnc8AAAABgRbnqw","url": "https://api.github.com/repos/test_user/test_repo/labels/bug"},{"color": "0075ca","default": true,"description": "Improvements or additions to documentation","id": 6460729262,"name": "documentation","node_id": "LA_kwDOLH_fnc8AAAABgRbnrg","url": "https://api.github.com/repos/test_user/test_repo/labels/documentation"},{"color": "cfd3d7","default": true,"description": "This issue or pull request already exists","id": 6460729265,"name": "duplicate","node_id": "LA_kwDOLH_fnc8AAAABgRbnsQ","url": "https://api.github.com/repos/test_user/test_repo/labels/duplicate"}],"labels_url": "https://api.github.com/repos/test_user/test_repo/issues/1/labels{/name}","locked": false,"node_id": "I_kwDOLH_fnc58yECg","number": 1,"reactions": {"+1": 0,"-1": 0,"confused": 0,"eyes": 0,"heart": 0,"hooray": 0,"laugh": 0,"rocket": 0,"total_count": 0,"url": "https://api.github.com/repos/test_user/test_repo/issues/1/reactions"},"repository_url": "https://api.github.com/repos/test_user/test_repo","state": "open","timeline_url": "https://api.github.com/repos/test_user/test_repo/issues/1/timeline","title": "This is a test issue","updated_at": "2024-01-22T09:42:19Z","url": "https://api.github.com/repos/test_user/test_repo/issues/1","user": {"avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4","events_url": "https://api.github.com/users/test_user/events{/privacy}","followers_url": "https://api.github.com/users/test_user/followers","following_url": "https://api.github.com/users/test_user/following{/other_user}","gists_url": "https://api.github.com/users/test_user/gists{/gist_id}","html_url": "https://github.com/test_user","id": 157107299,"login": "test_user","node_id": "U_kgDOCV1EYw","organizations_url": "https://api.github.com/users/test_user/orgs","received_events_url": "https://api.github.com/users/test_user/received_events","repos_url": "https://api.github.com/users/test_user/repos","site_admin": false,"starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}","subscriptions_url": "https://api.github.com/users/test_user/subscriptions","type": "User","url": "https://api.github.com/users/test_user"}}]|
  
Example output:

```
{
  "issues": [
    {
      "assignee": {
        "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
        "events_url": "https://api.github.com/users/test_user/events{/privacy}",
        "followers_url": "https://api.github.com/users/test_user/followers",
        "following_url": "https://api.github.com/users/test_user/following{/other_user}",
        "gists_url": "https://api.github.com/users/test_user/gists{/gist_id}",
        "html_url": "https://github.com/test_user",
        "id": 157107299,
        "login": "test_user",
        "node_id": "U_kgDOCV1EYw",
        "organizations_url": "https://api.github.com/users/test_user/orgs",
        "received_events_url": "https://api.github.com/users/test_user/received_events",
        "repos_url": "https://api.github.com/users/test_user/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/test_user/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/test_user"
      },
      "assignees": [
        {
          "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
          "events_url": "https://api.github.com/users/test_user/events{/privacy}",
          "followers_url": "https://api.github.com/users/test_user/followers",
          "following_url": "https://api.github.com/users/test_user/following{/other_user}",
          "gists_url": "https://api.github.com/users/test_user/gists{/gist_id}",
          "html_url": "https://github.com/test_user",
          "id": 157107299,
          "login": "test_user",
          "node_id": "U_kgDOCV1EYw",
          "organizations_url": "https://api.github.com/users/test_user/orgs",
          "received_events_url": "https://api.github.com/users/test_user/received_events",
          "repos_url": "https://api.github.com/users/test_user/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/test_user/subscriptions",
          "type": "User",
          "url": "https://api.github.com/users/test_user"
        }
      ],
      "author_association": "OWNER",
      "body": "This was created so we can see if issues are pulled in correctly",
      "comments": 0,
      "comments_url": "https://api.github.com/repos/test_user/test_repo/issues/1/comments",
      "created_at": "2024-01-22T09:42:18Z",
      "events_url": "https://api.github.com/repos/test_user/test_repo/issues/1/events",
      "html_url": "https://github.com/test_user/test_repo/issues/1",
      "id": 2093498528,
      "labels": [
        {
          "color": "d73a4a",
          "default": true,
          "description": "Something isnt working",
          "id": 6460729259,
          "name": "bug",
          "node_id": "LA_kwDOLH_fnc8AAAABgRbnqw",
          "url": "https://api.github.com/repos/test_user/test_repo/labels/bug"
        },
        {
          "color": "0075ca",
          "default": true,
          "description": "Improvements or additions to documentation",
          "id": 6460729262,
          "name": "documentation",
          "node_id": "LA_kwDOLH_fnc8AAAABgRbnrg",
          "url": "https://api.github.com/repos/test_user/test_repo/labels/documentation"
        },
        {
          "color": "cfd3d7",
          "default": true,
          "description": "This issue or pull request already exists",
          "id": 6460729265,
          "name": "duplicate",
          "node_id": "LA_kwDOLH_fnc8AAAABgRbnsQ",
          "url": "https://api.github.com/repos/test_user/test_repo/labels/duplicate"
        }
      ],
      "labels_url": "https://api.github.com/repos/test_user/test_repo/issues/1/labels{/name}",
      "locked": false,
      "node_id": "I_kwDOLH_fnc58yECg",
      "number": 1,
      "reactions": {
        "+1": 0,
        "-1": 0,
        "confused": 0,
        "eyes": 0,
        "heart": 0,
        "hooray": 0,
        "laugh": 0,
        "rocket": 0,
        "total_count": 0,
        "url": "https://api.github.com/repos/test_user/test_repo/issues/1/reactions"
      },
      "repository_url": "https://api.github.com/repos/test_user/test_repo",
      "state": "open",
      "timeline_url": "https://api.github.com/repos/test_user/test_repo/issues/1/timeline",
      "title": "This is a test issue",
      "updated_at": "2024-01-22T09:42:19Z",
      "url": "https://api.github.com/repos/test_user/test_repo/issues/1",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
        "events_url": "https://api.github.com/users/test_user/events{/privacy}",
        "followers_url": "https://api.github.com/users/test_user/followers",
        "following_url": "https://api.github.com/users/test_user/following{/other_user}",
        "gists_url": "https://api.github.com/users/test_user/gists{/gist_id}",
        "html_url": "https://github.com/test_user",
        "id": 157107299,
        "login": "test_user",
        "node_id": "U_kgDOCV1EYw",
        "organizations_url": "https://api.github.com/users/test_user/orgs",
        "received_events_url": "https://api.github.com/users/test_user/received_events",
        "repos_url": "https://api.github.com/users/test_user/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/test_user/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/test_user"
      }
    }
  ]
}
```

#### Get My Issues
  
This action is used to retrieve all issues assigned to the currently authenticated user

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|issues|[]issue|False|An array of the issues assigned to the current user|[{"assignee": {"avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4","events_url": "https://api.github.com/users/test_user/events{/privacy}","followers_url": "https://api.github.com/users/test_user/followers","following_url": "https://api.github.com/users/test_user/following{/other_user}","gists_url": "https://api.github.com/users/test_user/gists{/gist_id}","html_url": "https://github.com/test_user","id": 157107299,"login": "test_user","node_id": "U_kgDOCV1EYw","organizations_url": "https://api.github.com/users/test_user/orgs","received_events_url": "https://api.github.com/users/test_user/received_events","repos_url": "https://api.github.com/users/test_user/repos","site_admin": false,"starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}","subscriptions_url": "https://api.github.com/users/test_user/subscriptions","type": "User","url": "https://api.github.com/users/test_user"},"assignees": [{"avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4","events_url": "https://api.github.com/users/test_user/events{/privacy}","followers_url": "https://api.github.com/users/test_user/followers","following_url": "https://api.github.com/users/test_user/following{/other_user}","gists_url": "https://api.github.com/users/test_user/gists{/gist_id}","html_url": "https://github.com/test_user","id": 157107299,"login": "test_user","node_id": "U_kgDOCV1EYw","organizations_url": "https://api.github.com/users/test_user/orgs","received_events_url": "https://api.github.com/users/test_user/received_events","repos_url": "https://api.github.com/users/test_user/repos","site_admin": false,"starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}","subscriptions_url": "https://api.github.com/users/test_user/subscriptions","type": "User","url": "https://api.github.com/users/test_user"}],"author_association": "COLLABORATOR","body": "eehqweiueqiyeq","comments": 0,"comments_url": "https://api.github.com/repos/test_organization/test_repo/issues/6/comments","created_at": "2024-01-23T14:10:18Z","events_url": "https://api.github.com/repos/test_organization/test_repo/issues/6/events","html_url": "https://github.com/test_organization/test_repo/issues/6","id": 2096177224,"labels": [],"labels_url": "https://api.github.com/repos/test_organization/test_repo/issues/6/labels{/name}","locked": false,"node_id": "I_kwDOLIAEx8588SBI","number": 6,"reactions": {"+1": 0,"-1": 0,"confused": 0,"eyes": 0,"heart": 0,"hooray": 0,"laugh": 0,"rocket": 0,"total_count": 0,"url": "https://api.github.com/repos/test_organization/test_repo/issues/6/reactions"},"repository": {"allow_forking": false,"archive_url": "https://api.github.com/repos/test_organization/test_repo/{archive_format}{/ref}","archived": false,"assignees_url": "https://api.github.com/repos/test_organization/test_repo/assignees{/user}","blobs_url": "https://api.github.com/repos/test_organization/test_repo/git/blobs{/sha}","branches_url": "https://api.github.com/repos/test_organization/test_repo/branches{/branch}","clone_url": "https://github.com/test_organization/test_repo.git","collaborators_url": "https://api.github.com/repos/test_organization/test_repo/collaborators{/collaborator}","comments_url": "https://api.github.com/repos/test_organization/test_repo/comments{/number}","commits_url": "https://api.github.com/repos/test_organization/test_repo/commits{/sha}","compare_url": "https://api.github.com/repos/test_organization/test_repo/compare/{base}...{head}","contents_url": "https://api.github.com/repos/test_organization/test_repo/contents/{+path}","contributors_url": "https://api.github.com/repos/test_organization/test_repo/contributors","created_at": "2024-01-22T10:02:32Z","default_branch": "main","deployments_url": "https://api.github.com/repos/test_organization/test_repo/deployments","description": "test for insight connect plugins","disabled": false,"downloads_url": "https://api.github.com/repos/test_organization/test_repo/downloads","events_url": "https://api.github.com/repos/test_organization/test_repo/events","fork": false,"forks": 0,"forks_count": 0,"forks_url": "https://api.github.com/repos/test_organization/test_repo/forks","full_name": "test_organization/test_repo","git_commits_url": "https://api.github.com/repos/test_organization/test_repo/git/commits{/sha}","git_refs_url": "https://api.github.com/repos/test_organization/test_repo/git/refs{/sha}","git_tags_url": "https://api.github.com/repos/test_organization/test_repo/git/tags{/sha}","git_url": "git://github.com/test_organization/test_repo.git","has_discussions": false,"has_downloads": true,"has_issues": true,"has_pages": false,"has_projects": true,"has_wiki": false,"hooks_url": "https://api.github.com/repos/test_organization/test_repo/hooks","html_url": "https://github.com/test_organization/test_repo","id": 746587335,"is_template": false,"issue_comment_url": "https://api.github.com/repos/test_organization/test_repo/issues/comments{/number}","issue_events_url": "https://api.github.com/repos/test_organization/test_repo/issues/events{/number}","issues_url": "https://api.github.com/repos/test_organization/test_repo/issues{/number}","keys_url": "https://api.github.com/repos/test_organization/test_repo/keys{/key_id}","labels_url": "https://api.github.com/repos/test_organization/test_repo/labels{/name}","languages_url": "https://api.github.com/repos/test_organization/test_repo/languages","merges_url": "https://api.github.com/repos/test_organization/test_repo/merges","milestones_url": "https://api.github.com/repos/test_organization/test_repo/milestones{/number}","name": "test_repo","node_id": "R_kgDOLIAExw","notifications_url": "https://api.github.com/repos/test_organization/test_repo/notifications{?since,all,participating}","open_issues": 6,"open_issues_count": 6,"owner": {"avatar_url": "https://avatars.githubusercontent.com/u/157362711?v=4","events_url": "https://api.github.com/users/test_organization/events{/privacy}","followers_url": "https://api.github.com/users/test_organization/followers","following_url": "https://api.github.com/users/test_organization/following{/other_user}","gists_url": "https://api.github.com/users/test_organization/gists{/gist_id}","html_url": "https://github.com/test_organization","id": 157362711,"login": "test_organization","node_id": "O_kgDOCWEqFw","organizations_url": "https://api.github.com/users/test_organization/orgs","received_events_url": "https://api.github.com/users/test_organization/received_events","repos_url": "https://api.github.com/users/test_organization/repos","site_admin": false,"starred_url": "https://api.github.com/users/test_organization/starred{/owner}{/repo}","subscriptions_url": "https://api.github.com/users/test_organization/subscriptions","type": "Organization","url": "https://api.github.com/users/test_organization"},"permissions": {"admin": true,"maintain": true,"pull": true,"push": true,"triage": true},"private": true,"pulls_url": "https://api.github.com/repos/test_organization/test_repo/pulls{/number}","pushed_at": "2024-01-22T10:02:32Z","releases_url": "https://api.github.com/repos/test_organization/test_repo/releases{/id}","size": 0,"ssh_url": "github.com:test_organization/test_repo.git","stargazers_count": 0,"stargazers_url": "https://api.github.com/repos/test_organization/test_repo/stargazers","statuses_url": "https://api.github.com/repos/test_organization/test_repo/statuses/{sha}","subscribers_url": "https://api.github.com/repos/test_organization/test_repo/subscribers","subscription_url": "https://api.github.com/repos/test_organization/test_repo/subscription","svn_url": "https://github.com/test_organization/test_repo","tags_url": "https://api.github.com/repos/test_organization/test_repo/tags","teams_url": "https://api.github.com/repos/test_organization/test_repo/teams","topics": [],"trees_url": "https://api.github.com/repos/test_organization/test_repo/git/trees{/sha}","updated_at": "2024-01-22T13:28:12Z","url": "https://api.github.com/repos/test_organization/test_repo","visibility": "private","watchers": 0,"watchers_count": 0,"web_commit_signoff_required": false},"repository_url": "https://api.github.com/repos/test_organization/test_repo","state": "open","timeline_url": "https://api.github.com/repos/test_organization/test_repo/issues/6/timeline","title": "fshksdhkfsh","updated_at": "2024-01-23T14:10:18Z","url": "https://api.github.com/repos/test_organization/test_repo/issues/6","user": {"avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4","events_url": "https://api.github.com/users/test_user/events{/privacy}","followers_url": "https://api.github.com/users/test_user/followers","following_url": "https://api.github.com/users/test_user/following{/other_user}","gists_url": "https://api.github.com/users/test_user/gists{/gist_id}","html_url": "https://github.com/test_user","id": 157107299,"login": "test_user","node_id": "U_kgDOCV1EYw","organizations_url": "https://api.github.com/users/test_user/orgs","received_events_url": "https://api.github.com/users/test_user/received_events","repos_url": "https://api.github.com/users/test_user/repos","site_admin": false,"starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}","subscriptions_url": "https://api.github.com/users/test_user/subscriptions","type": "User","url": "https://api.github.com/users/test_user"}}]|
  
Example output:

```
{
  "issues": [
    {
      "assignee": {
        "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
        "events_url": "https://api.github.com/users/test_user/events{/privacy}",
        "followers_url": "https://api.github.com/users/test_user/followers",
        "following_url": "https://api.github.com/users/test_user/following{/other_user}",
        "gists_url": "https://api.github.com/users/test_user/gists{/gist_id}",
        "html_url": "https://github.com/test_user",
        "id": 157107299,
        "login": "test_user",
        "node_id": "U_kgDOCV1EYw",
        "organizations_url": "https://api.github.com/users/test_user/orgs",
        "received_events_url": "https://api.github.com/users/test_user/received_events",
        "repos_url": "https://api.github.com/users/test_user/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/test_user/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/test_user"
      },
      "assignees": [
        {
          "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
          "events_url": "https://api.github.com/users/test_user/events{/privacy}",
          "followers_url": "https://api.github.com/users/test_user/followers",
          "following_url": "https://api.github.com/users/test_user/following{/other_user}",
          "gists_url": "https://api.github.com/users/test_user/gists{/gist_id}",
          "html_url": "https://github.com/test_user",
          "id": 157107299,
          "login": "test_user",
          "node_id": "U_kgDOCV1EYw",
          "organizations_url": "https://api.github.com/users/test_user/orgs",
          "received_events_url": "https://api.github.com/users/test_user/received_events",
          "repos_url": "https://api.github.com/users/test_user/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/test_user/subscriptions",
          "type": "User",
          "url": "https://api.github.com/users/test_user"
        }
      ],
      "author_association": "COLLABORATOR",
      "body": "eehqweiueqiyeq",
      "comments": 0,
      "comments_url": "https://api.github.com/repos/test_organization/test_repo/issues/6/comments",
      "created_at": "2024-01-23T14:10:18Z",
      "events_url": "https://api.github.com/repos/test_organization/test_repo/issues/6/events",
      "html_url": "https://github.com/test_organization/test_repo/issues/6",
      "id": 2096177224,
      "labels": [],
      "labels_url": "https://api.github.com/repos/test_organization/test_repo/issues/6/labels{/name}",
      "locked": false,
      "node_id": "I_kwDOLIAEx8588SBI",
      "number": 6,
      "reactions": {
        "+1": 0,
        "-1": 0,
        "confused": 0,
        "eyes": 0,
        "heart": 0,
        "hooray": 0,
        "laugh": 0,
        "rocket": 0,
        "total_count": 0,
        "url": "https://api.github.com/repos/test_organization/test_repo/issues/6/reactions"
      },
      "repository": {
        "allow_forking": false,
        "archive_url": "https://api.github.com/repos/test_organization/test_repo/{archive_format}{/ref}",
        "archived": false,
        "assignees_url": "https://api.github.com/repos/test_organization/test_repo/assignees{/user}",
        "blobs_url": "https://api.github.com/repos/test_organization/test_repo/git/blobs{/sha}",
        "branches_url": "https://api.github.com/repos/test_organization/test_repo/branches{/branch}",
        "clone_url": "https://github.com/test_organization/test_repo.git",
        "collaborators_url": "https://api.github.com/repos/test_organization/test_repo/collaborators{/collaborator}",
        "comments_url": "https://api.github.com/repos/test_organization/test_repo/comments{/number}",
        "commits_url": "https://api.github.com/repos/test_organization/test_repo/commits{/sha}",
        "compare_url": "https://api.github.com/repos/test_organization/test_repo/compare/{base}...{head}",
        "contents_url": "https://api.github.com/repos/test_organization/test_repo/contents/{+path}",
        "contributors_url": "https://api.github.com/repos/test_organization/test_repo/contributors",
        "created_at": "2024-01-22T10:02:32Z",
        "default_branch": "main",
        "deployments_url": "https://api.github.com/repos/test_organization/test_repo/deployments",
        "description": "test for insight connect plugins",
        "disabled": false,
        "downloads_url": "https://api.github.com/repos/test_organization/test_repo/downloads",
        "events_url": "https://api.github.com/repos/test_organization/test_repo/events",
        "fork": false,
        "forks": 0,
        "forks_count": 0,
        "forks_url": "https://api.github.com/repos/test_organization/test_repo/forks",
        "full_name": "test_organization/test_repo",
        "git_commits_url": "https://api.github.com/repos/test_organization/test_repo/git/commits{/sha}",
        "git_refs_url": "https://api.github.com/repos/test_organization/test_repo/git/refs{/sha}",
        "git_tags_url": "https://api.github.com/repos/test_organization/test_repo/git/tags{/sha}",
        "git_url": "git://github.com/test_organization/test_repo.git",
        "has_discussions": false,
        "has_downloads": true,
        "has_issues": true,
        "has_pages": false,
        "has_projects": true,
        "has_wiki": false,
        "hooks_url": "https://api.github.com/repos/test_organization/test_repo/hooks",
        "html_url": "https://github.com/test_organization/test_repo",
        "id": 746587335,
        "is_template": false,
        "issue_comment_url": "https://api.github.com/repos/test_organization/test_repo/issues/comments{/number}",
        "issue_events_url": "https://api.github.com/repos/test_organization/test_repo/issues/events{/number}",
        "issues_url": "https://api.github.com/repos/test_organization/test_repo/issues{/number}",
        "keys_url": "https://api.github.com/repos/test_organization/test_repo/keys{/key_id}",
        "labels_url": "https://api.github.com/repos/test_organization/test_repo/labels{/name}",
        "languages_url": "https://api.github.com/repos/test_organization/test_repo/languages",
        "merges_url": "https://api.github.com/repos/test_organization/test_repo/merges",
        "milestones_url": "https://api.github.com/repos/test_organization/test_repo/milestones{/number}",
        "name": "test_repo",
        "node_id": "R_kgDOLIAExw",
        "notifications_url": "https://api.github.com/repos/test_organization/test_repo/notifications{?since,all,participating}",
        "open_issues": 6,
        "open_issues_count": 6,
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/157362711?v=4",
          "events_url": "https://api.github.com/users/test_organization/events{/privacy}",
          "followers_url": "https://api.github.com/users/test_organization/followers",
          "following_url": "https://api.github.com/users/test_organization/following{/other_user}",
          "gists_url": "https://api.github.com/users/test_organization/gists{/gist_id}",
          "html_url": "https://github.com/test_organization",
          "id": 157362711,
          "login": "test_organization",
          "node_id": "O_kgDOCWEqFw",
          "organizations_url": "https://api.github.com/users/test_organization/orgs",
          "received_events_url": "https://api.github.com/users/test_organization/received_events",
          "repos_url": "https://api.github.com/users/test_organization/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/test_organization/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/test_organization/subscriptions",
          "type": "Organization",
          "url": "https://api.github.com/users/test_organization"
        },
        "permissions": {
          "admin": true,
          "maintain": true,
          "pull": true,
          "push": true,
          "triage": true
        },
        "private": true,
        "pulls_url": "https://api.github.com/repos/test_organization/test_repo/pulls{/number}",
        "pushed_at": "2024-01-22T10:02:32Z",
        "releases_url": "https://api.github.com/repos/test_organization/test_repo/releases{/id}",
        "size": 0,
        "ssh_url": "github.com:test_organization/test_repo.git",
        "stargazers_count": 0,
        "stargazers_url": "https://api.github.com/repos/test_organization/test_repo/stargazers",
        "statuses_url": "https://api.github.com/repos/test_organization/test_repo/statuses/{sha}",
        "subscribers_url": "https://api.github.com/repos/test_organization/test_repo/subscribers",
        "subscription_url": "https://api.github.com/repos/test_organization/test_repo/subscription",
        "svn_url": "https://github.com/test_organization/test_repo",
        "tags_url": "https://api.github.com/repos/test_organization/test_repo/tags",
        "teams_url": "https://api.github.com/repos/test_organization/test_repo/teams",
        "topics": [],
        "trees_url": "https://api.github.com/repos/test_organization/test_repo/git/trees{/sha}",
        "updated_at": "2024-01-22T13:28:12Z",
        "url": "https://api.github.com/repos/test_organization/test_repo",
        "visibility": "private",
        "watchers": 0,
        "watchers_count": 0,
        "web_commit_signoff_required": false
      },
      "repository_url": "https://api.github.com/repos/test_organization/test_repo",
      "state": "open",
      "timeline_url": "https://api.github.com/repos/test_organization/test_repo/issues/6/timeline",
      "title": "fshksdhkfsh",
      "updated_at": "2024-01-23T14:10:18Z",
      "url": "https://api.github.com/repos/test_organization/test_repo/issues/6",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
        "events_url": "https://api.github.com/users/test_user/events{/privacy}",
        "followers_url": "https://api.github.com/users/test_user/followers",
        "following_url": "https://api.github.com/users/test_user/following{/other_user}",
        "gists_url": "https://api.github.com/users/test_user/gists{/gist_id}",
        "html_url": "https://github.com/test_user",
        "id": 157107299,
        "login": "test_user",
        "node_id": "U_kgDOCV1EYw",
        "organizations_url": "https://api.github.com/users/test_user/orgs",
        "received_events_url": "https://api.github.com/users/test_user/received_events",
        "repos_url": "https://api.github.com/users/test_user/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/test_user/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/test_user"
      }
    }
  ]
}
```

#### Get Repo
  
This action is used to retrieve details, including ID, about a specific repo

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|owner|string|None|True|Owner of the repository|None|test_owner|
|title|string|None|True|Name of the repository|None|test_title|
  
Example input:

```
{
  "owner": "test_owner",
  "title": "test_title"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|repo|True|Repository details and data|{'allow_auto_merge': False, 'allow_forking': True, 'allow_merge_commit': True, 'allow_rebase_merge': True, 'allow_squash_merge': True, 'allow_update_branch': False, 'archive_url': 'https://api.github.com/repos/test_owner/test_repo/{archive_format}{/ref}', 'archived': False, 'assignees_url': 'https://api.github.com/repos/test_owner/test_repo/assignees{/user}', 'blobs_url': 'https://api.github.com/repos/test_owner/test_repo/git/blobs{/sha}', 'branches_url': 'https://api.github.com/repos/test_owner/test_repo/branches{/branch}', 'clone_url': 'https://github.com/test_owner/test_repo.git', 'collaborators_url': 'https://api.github.com/repos/test_owner/test_repo/collaborators{/collaborator}', 'comments_url': 'https://api.github.com/repos/test_owner/test_repo/comments{/number}', 'commits_url': 'https://api.github.com/repos/test_owner/test_repo/commits{/sha}', 'compare_url': 'https://api.github.com/repos/test_owner/test_repo/compare/{base}...{head}', 'contents_url': 'https://api.github.com/repos/test_owner/test_repo/contents/{+path}', 'contributors_url': 'https://api.github.com/repos/test_owner/test_repo/contributors', 'created_at': '2024-01-22T09:39:26Z', 'default_branch': 'main', 'delete_branch_on_merge': False, 'deployments_url': 'https://api.github.com/repos/test_owner/test_repo/deployments', 'description': 'This is a test repo for insight connect', 'disabled': False, 'downloads_url': 'https://api.github.com/repos/test_owner/test_repo/downloads', 'events_url': 'https://api.github.com/repos/test_owner/test_repo/events', 'fork': False, 'forks': 0, 'forks_count': 0, 'forks_url': 'https://api.github.com/repos/test_owner/test_repo/forks', 'full_name': 'test_owner/test_repo', 'git_commits_url': 'https://api.github.com/repos/test_owner/test_repo/git/commits{/sha}', 'git_refs_url': 'https://api.github.com/repos/test_owner/test_repo/git/refs{/sha}', 'git_tags_url': 'https://api.github.com/repos/test_owner/test_repo/git/tags{/sha}', 'git_url': 'git://github.com/test_owner/test_repo.git', 'has_discussions': False, 'has_downloads': True, 'has_issues': True, 'has_pages': False, 'has_projects': True, 'has_wiki': False, 'hooks_url': 'https://api.github.com/repos/test_owner/test_repo/hooks', 'html_url': 'https://github.com/test_owner/test_repo', 'id': 746577821, 'is_template': False, 'issue_comment_url': 'https://api.github.com/repos/test_owner/test_repo/issues/comments{/number}', 'issue_events_url': 'https://api.github.com/repos/test_owner/test_repo/issues/events{/number}', 'issues_url': 'https://api.github.com/repos/test_owner/test_repo/issues{/number}', 'keys_url': 'https://api.github.com/repos/test_owner/test_repo/keys{/key_id}', 'labels_url': 'https://api.github.com/repos/test_owner/test_repo/labels{/name}', 'languages_url': 'https://api.github.com/repos/test_owner/test_repo/languages', 'merge_commit_message': 'PR_TITLE', 'merge_commit_title': 'MERGE_MESSAGE', 'merges_url': 'https://api.github.com/repos/test_owner/test_repo/merges', 'milestones_url': 'https://api.github.com/repos/test_owner/test_repo/milestones{/number}', 'name': 'test_repo', 'network_count': 0, 'node_id': 'R_kgDOLH_fnQ', 'notifications_url': 'https://api.github.com/repos/test_owner/test_repo/notifications{?since,all,participating}', 'open_issues': 1, 'open_issues_count': 1, 'owner': {'avatar_url': 'https://avatars.githubusercontent.com/u/157107299?v=4', 'events_url': 'https://api.github.com/users/test_owner/events{/privacy}', 'followers_url': 'https://api.github.com/users/test_owner/followers', 'following_url': 'https://api.github.com/users/test_owner/following{/other_user}', 'gists_url': 'https://api.github.com/users/test_owner/gists{/gist_id}', 'html_url': 'https://github.com/test_owner', 'id': 157107299, 'login': 'test_owner', 'node_id': 'U_kgDOCV1EYw', 'organizations_url': 'https://api.github.com/users/test_owner/orgs', 'received_events_url': 'https://api.github.com/users/test_owner/received_events', 'repos_url': 'https://api.github.com/users/test_owner/repos', 'site_admin': False, 'starred_url': 'https://api.github.com/users/test_owner/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/test_owner/subscriptions', 'type': 'User', 'url': 'https://api.github.com/users/test_owner'}, 'permissions': {'admin': True, 'maintain': True, 'pull': True, 'push': True, 'triage': True}, 'private': True, 'pulls_url': 'https://api.github.com/repos/test_owner/test_repo/pulls{/number}', 'pushed_at': '2024-01-22T09:39:26Z', 'releases_url': 'https://api.github.com/repos/test_owner/test_repo/releases{/id}', 'size': 0, 'squash_merge_commit_message': 'COMMIT_MESSAGES', 'squash_merge_commit_title': 'COMMIT_OR_PR_TITLE', 'ssh_url': 'github.com:test_owner/test_repo.git', 'stargazers_count': 0, 'stargazers_url': 'https://api.github.com/repos/test_owner/test_repo/stargazers', 'statuses_url': 'https://api.github.com/repos/test_owner/test_repo/statuses/{sha}', 'subscribers_count': 1, 'subscribers_url': 'https://api.github.com/repos/test_owner/test_repo/subscribers', 'subscription_url': 'https://api.github.com/repos/test_owner/test_repo/subscription', 'svn_url': 'https://github.com/test_owner/test_repo', 'tags_url': 'https://api.github.com/repos/test_owner/test_repo/tags', 'teams_url': 'https://api.github.com/repos/test_owner/test_repo/teams', 'temp_clone_token': 'BFOUIY4BKKABTTP7Q4Z5G4TFV7IDE', 'topics': [], 'trees_url': 'https://api.github.com/repos/test_owner/test_repo/git/trees{/sha}', 'updated_at': '2024-01-22T09:39:26Z', 'url': 'https://api.github.com/repos/test_owner/test_repo', 'use_squash_pr_title_as_default': False, 'visibility': 'private', 'watchers': 0, 'watchers_count': 0, 'web_commit_signoff_required': False}|
  
Example output:

```
{
  "data": {
    "allow_auto_merge": false,
    "allow_forking": true,
    "allow_merge_commit": true,
    "allow_rebase_merge": true,
    "allow_squash_merge": true,
    "allow_update_branch": false,
    "archive_url": "https://api.github.com/repos/test_owner/test_repo/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/test_owner/test_repo/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/test_owner/test_repo/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/test_owner/test_repo/branches{/branch}",
    "clone_url": "https://github.com/test_owner/test_repo.git",
    "collaborators_url": "https://api.github.com/repos/test_owner/test_repo/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/test_owner/test_repo/comments{/number}",
    "commits_url": "https://api.github.com/repos/test_owner/test_repo/commits{/sha}",
    "compare_url": "https://api.github.com/repos/test_owner/test_repo/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/test_owner/test_repo/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/test_owner/test_repo/contributors",
    "created_at": "2024-01-22T09:39:26Z",
    "default_branch": "main",
    "delete_branch_on_merge": false,
    "deployments_url": "https://api.github.com/repos/test_owner/test_repo/deployments",
    "description": "This is a test repo for insight connect",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/test_owner/test_repo/downloads",
    "events_url": "https://api.github.com/repos/test_owner/test_repo/events",
    "fork": false,
    "forks": 0,
    "forks_count": 0,
    "forks_url": "https://api.github.com/repos/test_owner/test_repo/forks",
    "full_name": "test_owner/test_repo",
    "git_commits_url": "https://api.github.com/repos/test_owner/test_repo/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/test_owner/test_repo/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/test_owner/test_repo/git/tags{/sha}",
    "git_url": "git://github.com/test_owner/test_repo.git",
    "has_discussions": false,
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": false,
    "hooks_url": "https://api.github.com/repos/test_owner/test_repo/hooks",
    "html_url": "https://github.com/test_owner/test_repo",
    "id": 746577821,
    "is_template": false,
    "issue_comment_url": "https://api.github.com/repos/test_owner/test_repo/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/test_owner/test_repo/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/test_owner/test_repo/issues{/number}",
    "keys_url": "https://api.github.com/repos/test_owner/test_repo/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/test_owner/test_repo/labels{/name}",
    "languages_url": "https://api.github.com/repos/test_owner/test_repo/languages",
    "merge_commit_message": "PR_TITLE",
    "merge_commit_title": "MERGE_MESSAGE",
    "merges_url": "https://api.github.com/repos/test_owner/test_repo/merges",
    "milestones_url": "https://api.github.com/repos/test_owner/test_repo/milestones{/number}",
    "name": "test_repo",
    "network_count": 0,
    "node_id": "R_kgDOLH_fnQ",
    "notifications_url": "https://api.github.com/repos/test_owner/test_repo/notifications{?since,all,participating}",
    "open_issues": 1,
    "open_issues_count": 1,
    "owner": {
      "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
      "events_url": "https://api.github.com/users/test_owner/events{/privacy}",
      "followers_url": "https://api.github.com/users/test_owner/followers",
      "following_url": "https://api.github.com/users/test_owner/following{/other_user}",
      "gists_url": "https://api.github.com/users/test_owner/gists{/gist_id}",
      "html_url": "https://github.com/test_owner",
      "id": 157107299,
      "login": "test_owner",
      "node_id": "U_kgDOCV1EYw",
      "organizations_url": "https://api.github.com/users/test_owner/orgs",
      "received_events_url": "https://api.github.com/users/test_owner/received_events",
      "repos_url": "https://api.github.com/users/test_owner/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/test_owner/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/test_owner/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/test_owner"
    },
    "permissions": {
      "admin": true,
      "maintain": true,
      "pull": true,
      "push": true,
      "triage": true
    },
    "private": true,
    "pulls_url": "https://api.github.com/repos/test_owner/test_repo/pulls{/number}",
    "pushed_at": "2024-01-22T09:39:26Z",
    "releases_url": "https://api.github.com/repos/test_owner/test_repo/releases{/id}",
    "size": 0,
    "squash_merge_commit_message": "COMMIT_MESSAGES",
    "squash_merge_commit_title": "COMMIT_OR_PR_TITLE",
    "ssh_url": "github.com:test_owner/test_repo.git",
    "stargazers_count": 0,
    "stargazers_url": "https://api.github.com/repos/test_owner/test_repo/stargazers",
    "statuses_url": "https://api.github.com/repos/test_owner/test_repo/statuses/{sha}",
    "subscribers_count": 1,
    "subscribers_url": "https://api.github.com/repos/test_owner/test_repo/subscribers",
    "subscription_url": "https://api.github.com/repos/test_owner/test_repo/subscription",
    "svn_url": "https://github.com/test_owner/test_repo",
    "tags_url": "https://api.github.com/repos/test_owner/test_repo/tags",
    "teams_url": "https://api.github.com/repos/test_owner/test_repo/teams",
    "temp_clone_token": "BFOUIY4BKKABTTP7Q4Z5G4TFV7IDE",
    "topics": [],
    "trees_url": "https://api.github.com/repos/test_owner/test_repo/git/trees{/sha}",
    "updated_at": "2024-01-22T09:39:26Z",
    "url": "https://api.github.com/repos/test_owner/test_repo",
    "use_squash_pr_title_as_default": false,
    "visibility": "private",
    "watchers": 0,
    "watchers_count": 0,
    "web_commit_signoff_required": false
  }
}
```

#### Remove User
  
This action is used to remove user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|organization|string|None|False|Remove from organization|None|test_organization|
|repository|string|None|False|Remove from repository|None|test_repository|
|username|string|None|True|Username to remove|None|test_user|
  
Example input:

```
{
  "organization": "test_organization",
  "repository": "test_repository",
  "username": "test_user"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|string|False|Status|Successfully removed test_user from the repo test_repository in test_organization|
  
Example output:

```
{
  "status": "Successfully removed test_user from the repo test_repository in test_organization"
}
```

#### Search
  
This action is used to search GitHub for data

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|False|Query to match against|None|repo:test_organization/test_repo test_search_query|
|search_type|string|None|False|The type of search to perform|["Repositories", "Commits", "Code", "Issues"]|Issues|
  
Example input:

```
{
  "query": "repo:test_organization/test_repo test_search_query",
  "search_type": "Issues"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|object|False|Results|{'total_count': 1, 'incomplete_results': False, 'items': [{'url': 'https://api.github.com/repos/test_organization/test_repo/issues/1', 'repository_url': 'https://api.github.com/repos/test_organization/test_repo', 'labels_url': 'https://api.github.com/repos/test_organization/test_repo/issues/1/labels{/name}', 'comments_url': 'https://api.github.com/repos/test_organization/test_repo/issues/1/comments', 'events_url': 'https://api.github.com/repos/test_organization/test_repo/issues/1/events', 'html_url': 'https://github.com/test_organization/test_repo/issues/1', 'id': 2093498528, 'node_id': 'I_kwDOLH_fnc58yECg', 'number': 1, 'title': 'This is a test issue', 'user': {'login': 'test_organization', 'id': 157107299, 'node_id': 'U_kgDOCV1EYw', 'avatar_url': 'https://avatars.githubusercontent.com/u/157107299?v=4', 'url': 'https://api.github.com/users/test_organization', 'html_url': 'https://github.com/test_organization', 'followers_url': 'https://api.github.com/users/test_organization/followers', 'following_url': 'https://api.github.com/users/test_organization/following{/other_user}', 'gists_url': 'https://api.github.com/users/test_organization/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/test_organization/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/test_organization/subscriptions', 'organizations_url': 'https://api.github.com/users/test_organization/orgs', 'repos_url': 'https://api.github.com/users/test_organization/repos', 'events_url': 'https://api.github.com/users/test_organization/events{/privacy}', 'received_events_url': 'https://api.github.com/users/test_organization/received_events', 'type': 'User', 'site_admin': False}, 'labels': [{'id': 6460729259, 'node_id': 'LA_kwDOLH_fnc8AAAABgRbnqw', 'url': 'https://api.github.com/repos/test_organization/test_repo/labels/bug', 'name': 'bug', 'color': 'd73a4a', 'default': True, 'description': "Something isn't working"}, {'id': 6460729262, 'node_id': 'LA_kwDOLH_fnc8AAAABgRbnrg', 'url': 'https://api.github.com/repos/test_organization/test_repo/labels/documentation', 'name': 'documentation', 'color': '0075ca', 'default': True, 'description': 'Improvements or additions to documentation'}, {'id': 6460729265, 'node_id': 'LA_kwDOLH_fnc8AAAABgRbnsQ', 'url': 'https://api.github.com/repos/test_organization/test_repo/labels/duplicate', 'name': 'duplicate', 'color': 'cfd3d7', 'default': True, 'description': 'This issue or pull request already exists'}], 'state': 'open', 'locked': False, 'assignee': {'login': 'test_organization', 'id': 157107299, 'node_id': 'U_kgDOCV1EYw', 'avatar_url': 'https://avatars.githubusercontent.com/u/157107299?v=4', 'url': 'https://api.github.com/users/test_organization', 'html_url': 'https://github.com/test_organization', 'followers_url': 'https://api.github.com/users/test_organization/followers', 'following_url': 'https://api.github.com/users/test_organization/following{/other_user}', 'gists_url': 'https://api.github.com/users/test_organization/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/test_organization/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/test_organization/subscriptions', 'organizations_url': 'https://api.github.com/users/test_organization/orgs', 'repos_url': 'https://api.github.com/users/test_organization/repos', 'events_url': 'https://api.github.com/users/test_organization/events{/privacy}', 'received_events_url': 'https://api.github.com/users/test_organization/received_events', 'type': 'User', 'site_admin': False}, 'assignees': [{'login': 'test_organization', 'id': 157107299, 'node_id': 'U_kgDOCV1EYw', 'avatar_url': 'https://avatars.githubusercontent.com/u/157107299?v=4', 'url': 'https://api.github.com/users/test_organization', 'html_url': 'https://github.com/test_organization', 'followers_url': 'https://api.github.com/users/test_organization/followers', 'following_url': 'https://api.github.com/users/test_organization/following{/other_user}', 'gists_url': 'https://api.github.com/users/test_organization/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/test_organization/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/test_organization/subscriptions', 'organizations_url': 'https://api.github.com/users/test_organization/orgs', 'repos_url': 'https://api.github.com/users/test_organization/repos', 'events_url': 'https://api.github.com/users/test_organization/events{/privacy}', 'received_events_url': 'https://api.github.com/users/test_organization/received_events', 'type': 'User', 'site_admin': False}], 'comments': 0, 'created_at': '2024-01-22T09:42:18Z', 'updated_at': '2024-01-22T09:42:19Z', 'author_association': 'OWNER', 'body': 'This was created so we can see if issues are pulled in correctly', 'reactions': {'url': 'https://api.github.com/repos/test_organization/test_repo/issues/1/reactions', 'total_count': 0, '+1': 0, '-1': 0, 'laugh': 0, 'hooray': 0, 'confused': 0, 'heart': 0, 'rocket': 0, 'eyes': 0}, 'timeline_url': 'https://api.github.com/repos/test_organization/test_repo/issues/1/timeline', 'score': 1.0}]}|
  
Example output:

```
{
  "results": {
    "incomplete_results": false,
    "items": [
      {
        "assignee": {
          "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
          "events_url": "https://api.github.com/users/test_organization/events{/privacy}",
          "followers_url": "https://api.github.com/users/test_organization/followers",
          "following_url": "https://api.github.com/users/test_organization/following{/other_user}",
          "gists_url": "https://api.github.com/users/test_organization/gists{/gist_id}",
          "html_url": "https://github.com/test_organization",
          "id": 157107299,
          "login": "test_organization",
          "node_id": "U_kgDOCV1EYw",
          "organizations_url": "https://api.github.com/users/test_organization/orgs",
          "received_events_url": "https://api.github.com/users/test_organization/received_events",
          "repos_url": "https://api.github.com/users/test_organization/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/test_organization/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/test_organization/subscriptions",
          "type": "User",
          "url": "https://api.github.com/users/test_organization"
        },
        "assignees": [
          {
            "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
            "events_url": "https://api.github.com/users/test_organization/events{/privacy}",
            "followers_url": "https://api.github.com/users/test_organization/followers",
            "following_url": "https://api.github.com/users/test_organization/following{/other_user}",
            "gists_url": "https://api.github.com/users/test_organization/gists{/gist_id}",
            "html_url": "https://github.com/test_organization",
            "id": 157107299,
            "login": "test_organization",
            "node_id": "U_kgDOCV1EYw",
            "organizations_url": "https://api.github.com/users/test_organization/orgs",
            "received_events_url": "https://api.github.com/users/test_organization/received_events",
            "repos_url": "https://api.github.com/users/test_organization/repos",
            "site_admin": false,
            "starred_url": "https://api.github.com/users/test_organization/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/test_organization/subscriptions",
            "type": "User",
            "url": "https://api.github.com/users/test_organization"
          }
        ],
        "author_association": "OWNER",
        "body": "This was created so we can see if issues are pulled in correctly",
        "comments": 0,
        "comments_url": "https://api.github.com/repos/test_organization/test_repo/issues/1/comments",
        "created_at": "2024-01-22T09:42:18Z",
        "events_url": "https://api.github.com/repos/test_organization/test_repo/issues/1/events",
        "html_url": "https://github.com/test_organization/test_repo/issues/1",
        "id": 2093498528,
        "labels": [
          {
            "color": "d73a4a",
            "default": true,
            "description": "Something isn't working",
            "id": 6460729259,
            "name": "bug",
            "node_id": "LA_kwDOLH_fnc8AAAABgRbnqw",
            "url": "https://api.github.com/repos/test_organization/test_repo/labels/bug"
          },
          {
            "color": "0075ca",
            "default": true,
            "description": "Improvements or additions to documentation",
            "id": 6460729262,
            "name": "documentation",
            "node_id": "LA_kwDOLH_fnc8AAAABgRbnrg",
            "url": "https://api.github.com/repos/test_organization/test_repo/labels/documentation"
          },
          {
            "color": "cfd3d7",
            "default": true,
            "description": "This issue or pull request already exists",
            "id": 6460729265,
            "name": "duplicate",
            "node_id": "LA_kwDOLH_fnc8AAAABgRbnsQ",
            "url": "https://api.github.com/repos/test_organization/test_repo/labels/duplicate"
          }
        ],
        "labels_url": "https://api.github.com/repos/test_organization/test_repo/issues/1/labels{/name}",
        "locked": false,
        "node_id": "I_kwDOLH_fnc58yECg",
        "number": 1,
        "reactions": {
          "+1": 0,
          "-1": 0,
          "confused": 0,
          "eyes": 0,
          "heart": 0,
          "hooray": 0,
          "laugh": 0,
          "rocket": 0,
          "total_count": 0,
          "url": "https://api.github.com/repos/test_organization/test_repo/issues/1/reactions"
        },
        "repository_url": "https://api.github.com/repos/test_organization/test_repo",
        "score": 1.0,
        "state": "open",
        "timeline_url": "https://api.github.com/repos/test_organization/test_repo/issues/1/timeline",
        "title": "This is a test issue",
        "updated_at": "2024-01-22T09:42:19Z",
        "url": "https://api.github.com/repos/test_organization/test_repo/issues/1",
        "user": {
          "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
          "events_url": "https://api.github.com/users/test_organization/events{/privacy}",
          "followers_url": "https://api.github.com/users/test_organization/followers",
          "following_url": "https://api.github.com/users/test_organization/following{/other_user}",
          "gists_url": "https://api.github.com/users/test_organization/gists{/gist_id}",
          "html_url": "https://github.com/test_organization",
          "id": 157107299,
          "login": "test_organization",
          "node_id": "U_kgDOCV1EYw",
          "organizations_url": "https://api.github.com/users/test_organization/orgs",
          "received_events_url": "https://api.github.com/users/test_organization/received_events",
          "repos_url": "https://api.github.com/users/test_organization/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/test_organization/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/test_organization/subscriptions",
          "type": "User",
          "url": "https://api.github.com/users/test_organization"
        }
      }
    ],
    "total_count": 1
  }
}
```

#### Unblock User
  
This action is used to unblock a user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|username|string|None|True|Username to unblock|None|test_username|
  
Example input:

```
{
  "username": "test_username"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the user was unblocked|True|
  
Example output:

```
{
  "success": true
}
```

#### Get User
  
This action is used to get user information

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|username|string|None|True|GitHub username|None|test_user|
  
Example input:

```
{
  "username": "test_user"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|avatar|string|False|Avatar|https://avatars.githubusercontent.com/u/1234567?v=4|
|bio|string|False|Bio|test_bio|
|email|string|False|Email|user@example.com|
|name|string|False|Name|example_username|
|url|string|False|URL|https://github.com/test_user|
  
Example output:

```
{
  "avatar": "https://avatars.githubusercontent.com/u/1234567?v=4",
  "bio": "test_bio",
  "email": "user@example.com",
  "name": "example_username",
  "url": "https://github.com/test_user"
}
```
### Triggers


#### Issue
  
This trigger is used to monitor new issues

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assignee|string|None|False|Username of assignee|None|test_username|
|frequency|integer|300|False|Poll frequency in seconds|None|300|
|organization|string|None|False|Return issues of a specific organization|None|test_organization|
|repository|string|None|True|Return issues of a specific repository|None|test_repository|
  
Example input:

```
{
  "assignee": "test_username",
  "frequency": 300,
  "organization": "test_organization",
  "repository": "test_repository"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|issue|object|False|Issue|{'assignee': {'avatar_url': 'https://avatars.githubusercontent.com/u/157107299?v=4', 'events_url': 'https://api.github.com/users/test_user/events{/privacy}', 'followers_url': 'https://api.github.com/users/test_user/followers', 'following_url': 'https://api.github.com/users/test_user/following{/other_user}', 'gists_url': 'https://api.github.com/users/test_user/gists{/gist_id}', 'html_url': 'https://github.com/test_user', 'id': 157107299, 'login': 'test_user', 'node_id': 'U_kgDOCV1EYw', 'organizations_url': 'https://api.github.com/users/test_user/orgs', 'received_events_url': 'https://api.github.com/users/test_user/received_events', 'repos_url': 'https://api.github.com/users/test_user/repos', 'site_admin': False, 'starred_url': 'https://api.github.com/users/test_user/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/test_user/subscriptions', 'type': 'User', 'url': 'https://api.github.com/users/test_user'}, 'assignees': [{'avatar_url': 'https://avatars.githubusercontent.com/u/157107299?v=4', 'events_url': 'https://api.github.com/users/test_user/events{/privacy}', 'followers_url': 'https://api.github.com/users/test_user/followers', 'following_url': 'https://api.github.com/users/test_user/following{/other_user}', 'gists_url': 'https://api.github.com/users/test_user/gists{/gist_id}', 'html_url': 'https://github.com/test_user', 'id': 157107299, 'login': 'test_user', 'node_id': 'U_kgDOCV1EYw', 'organizations_url': 'https://api.github.com/users/test_user/orgs', 'received_events_url': 'https://api.github.com/users/test_user/received_events', 'repos_url': 'https://api.github.com/users/test_user/repos', 'site_admin': False, 'starred_url': 'https://api.github.com/users/test_user/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/test_user/subscriptions', 'type': 'User', 'url': 'https://api.github.com/users/test_user'}], 'author_association': 'COLLABORATOR', 'body': 'eehqweiueqiyeq', 'comments': 0, 'comments_url': 'https://api.github.com/repos/test_organization/test_repo/issues/6/comments', 'created_at': '2024-01-23T14:10:18Z', 'events_url': 'https://api.github.com/repos/test_organization/test_repo/issues/6/events', 'html_url': 'https://github.com/test_organization/test_repo/issues/6', 'id': 2096177224, 'labels': [], 'labels_url': 'https://api.github.com/repos/test_organization/test_repo/issues/6/labels{/name}', 'locked': False, 'node_id': 'I_kwDOLIAEx8588SBI', 'number': 6, 'reactions': {'+1': 0, '-1': 0, 'confused': 0, 'eyes': 0, 'heart': 0, 'hooray': 0, 'laugh': 0, 'rocket': 0, 'total_count': 0, 'url': 'https://api.github.com/repos/test_organization/test_repo/issues/6/reactions'}, 'repository': {'allow_forking': False, 'archive_url': 'https://api.github.com/repos/test_organization/test_repo/{archive_format}{/ref}', 'archived': False, 'assignees_url': 'https://api.github.com/repos/test_organization/test_repo/assignees{/user}', 'blobs_url': 'https://api.github.com/repos/test_organization/test_repo/git/blobs{/sha}', 'branches_url': 'https://api.github.com/repos/test_organization/test_repo/branches{/branch}', 'clone_url': 'https://github.com/test_organization/test_repo.git', 'collaborators_url': 'https://api.github.com/repos/test_organization/test_repo/collaborators{/collaborator}', 'comments_url': 'https://api.github.com/repos/test_organization/test_repo/comments{/number}', 'commits_url': 'https://api.github.com/repos/test_organization/test_repo/commits{/sha}', 'compare_url': 'https://api.github.com/repos/test_organization/test_repo/compare/{base}...{head}', 'contents_url': 'https://api.github.com/repos/test_organization/test_repo/contents/{+path}', 'contributors_url': 'https://api.github.com/repos/test_organization/test_repo/contributors', 'created_at': '2024-01-22T10:02:32Z', 'default_branch': 'main', 'deployments_url': 'https://api.github.com/repos/test_organization/test_repo/deployments', 'description': 'test for insight connect plugins', 'disabled': False, 'downloads_url': 'https://api.github.com/repos/test_organization/test_repo/downloads', 'events_url': 'https://api.github.com/repos/test_organization/test_repo/events', 'fork': False, 'forks': 0, 'forks_count': 0, 'forks_url': 'https://api.github.com/repos/test_organization/test_repo/forks', 'full_name': 'test_organization/test_repo', 'git_commits_url': 'https://api.github.com/repos/test_organization/test_repo/git/commits{/sha}', 'git_refs_url': 'https://api.github.com/repos/test_organization/test_repo/git/refs{/sha}', 'git_tags_url': 'https://api.github.com/repos/test_organization/test_repo/git/tags{/sha}', 'git_url': 'git://github.com/test_organization/test_repo.git', 'has_discussions': False, 'has_downloads': True, 'has_issues': True, 'has_pages': False, 'has_projects': True, 'has_wiki': False, 'hooks_url': 'https://api.github.com/repos/test_organization/test_repo/hooks', 'html_url': 'https://github.com/test_organization/test_repo', 'id': 746587335, 'is_template': False, 'issue_comment_url': 'https://api.github.com/repos/test_organization/test_repo/issues/comments{/number}', 'issue_events_url': 'https://api.github.com/repos/test_organization/test_repo/issues/events{/number}', 'issues_url': 'https://api.github.com/repos/test_organization/test_repo/issues{/number}', 'keys_url': 'https://api.github.com/repos/test_organization/test_repo/keys{/key_id}', 'labels_url': 'https://api.github.com/repos/test_organization/test_repo/labels{/name}', 'languages_url': 'https://api.github.com/repos/test_organization/test_repo/languages', 'merges_url': 'https://api.github.com/repos/test_organization/test_repo/merges', 'milestones_url': 'https://api.github.com/repos/test_organization/test_repo/milestones{/number}', 'name': 'test_repo', 'node_id': 'R_kgDOLIAExw', 'notifications_url': 'https://api.github.com/repos/test_organization/test_repo/notifications{?since,all,participating}', 'open_issues': 6, 'open_issues_count': 6, 'owner': {'avatar_url': 'https://avatars.githubusercontent.com/u/157362711?v=4', 'events_url': 'https://api.github.com/users/test_organization/events{/privacy}', 'followers_url': 'https://api.github.com/users/test_organization/followers', 'following_url': 'https://api.github.com/users/test_organization/following{/other_user}', 'gists_url': 'https://api.github.com/users/test_organization/gists{/gist_id}', 'html_url': 'https://github.com/test_organization', 'id': 157362711, 'login': 'test_organization', 'node_id': 'O_kgDOCWEqFw', 'organizations_url': 'https://api.github.com/users/test_organization/orgs', 'received_events_url': 'https://api.github.com/users/test_organization/received_events', 'repos_url': 'https://api.github.com/users/test_organization/repos', 'site_admin': False, 'starred_url': 'https://api.github.com/users/test_organization/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/test_organization/subscriptions', 'type': 'Organization', 'url': 'https://api.github.com/users/test_organization'}, 'permissions': {'admin': True, 'maintain': True, 'pull': True, 'push': True, 'triage': True}, 'private': True, 'pulls_url': 'https://api.github.com/repos/test_organization/test_repo/pulls{/number}', 'pushed_at': '2024-01-22T10:02:32Z', 'releases_url': 'https://api.github.com/repos/test_organization/test_repo/releases{/id}', 'size': 0, 'ssh_url': 'github.com:test_organization/test_repo.git', 'stargazers_count': 0, 'stargazers_url': 'https://api.github.com/repos/test_organization/test_repo/stargazers', 'statuses_url': 'https://api.github.com/repos/test_organization/test_repo/statuses/{sha}', 'subscribers_url': 'https://api.github.com/repos/test_organization/test_repo/subscribers', 'subscription_url': 'https://api.github.com/repos/test_organization/test_repo/subscription', 'svn_url': 'https://github.com/test_organization/test_repo', 'tags_url': 'https://api.github.com/repos/test_organization/test_repo/tags', 'teams_url': 'https://api.github.com/repos/test_organization/test_repo/teams', 'topics': [], 'trees_url': 'https://api.github.com/repos/test_organization/test_repo/git/trees{/sha}', 'updated_at': '2024-01-22T13:28:12Z', 'url': 'https://api.github.com/repos/test_organization/test_repo', 'visibility': 'private', 'watchers': 0, 'watchers_count': 0, 'web_commit_signoff_required': False}, 'repository_url': 'https://api.github.com/repos/test_organization/test_repo', 'state': 'open', 'timeline_url': 'https://api.github.com/repos/test_organization/test_repo/issues/6/timeline', 'title': 'fshksdhkfsh', 'updated_at': '2024-01-23T14:10:18Z', 'url': 'https://api.github.com/repos/test_organization/test_repo/issues/6', 'user': {'avatar_url': 'https://avatars.githubusercontent.com/u/157107299?v=4', 'events_url': 'https://api.github.com/users/test_user/events{/privacy}', 'followers_url': 'https://api.github.com/users/test_user/followers', 'following_url': 'https://api.github.com/users/test_user/following{/other_user}', 'gists_url': 'https://api.github.com/users/test_user/gists{/gist_id}', 'html_url': 'https://github.com/test_user', 'id': 157107299, 'login': 'test_user', 'node_id': 'U_kgDOCV1EYw', 'organizations_url': 'https://api.github.com/users/test_user/orgs', 'received_events_url': 'https://api.github.com/users/test_user/received_events', 'repos_url': 'https://api.github.com/users/test_user/repos', 'site_admin': False, 'starred_url': 'https://api.github.com/users/test_user/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/test_user/subscriptions', 'type': 'User', 'url': 'https://api.github.com/users/test_user'}}|
  
Example output:

```
{
  "issue": {
    "assignee": {
      "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
      "events_url": "https://api.github.com/users/test_user/events{/privacy}",
      "followers_url": "https://api.github.com/users/test_user/followers",
      "following_url": "https://api.github.com/users/test_user/following{/other_user}",
      "gists_url": "https://api.github.com/users/test_user/gists{/gist_id}",
      "html_url": "https://github.com/test_user",
      "id": 157107299,
      "login": "test_user",
      "node_id": "U_kgDOCV1EYw",
      "organizations_url": "https://api.github.com/users/test_user/orgs",
      "received_events_url": "https://api.github.com/users/test_user/received_events",
      "repos_url": "https://api.github.com/users/test_user/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/test_user/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/test_user"
    },
    "assignees": [
      {
        "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
        "events_url": "https://api.github.com/users/test_user/events{/privacy}",
        "followers_url": "https://api.github.com/users/test_user/followers",
        "following_url": "https://api.github.com/users/test_user/following{/other_user}",
        "gists_url": "https://api.github.com/users/test_user/gists{/gist_id}",
        "html_url": "https://github.com/test_user",
        "id": 157107299,
        "login": "test_user",
        "node_id": "U_kgDOCV1EYw",
        "organizations_url": "https://api.github.com/users/test_user/orgs",
        "received_events_url": "https://api.github.com/users/test_user/received_events",
        "repos_url": "https://api.github.com/users/test_user/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/test_user/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/test_user"
      }
    ],
    "author_association": "COLLABORATOR",
    "body": "eehqweiueqiyeq",
    "comments": 0,
    "comments_url": "https://api.github.com/repos/test_organization/test_repo/issues/6/comments",
    "created_at": "2024-01-23T14:10:18Z",
    "events_url": "https://api.github.com/repos/test_organization/test_repo/issues/6/events",
    "html_url": "https://github.com/test_organization/test_repo/issues/6",
    "id": 2096177224,
    "labels": [],
    "labels_url": "https://api.github.com/repos/test_organization/test_repo/issues/6/labels{/name}",
    "locked": false,
    "node_id": "I_kwDOLIAEx8588SBI",
    "number": 6,
    "reactions": {
      "+1": 0,
      "-1": 0,
      "confused": 0,
      "eyes": 0,
      "heart": 0,
      "hooray": 0,
      "laugh": 0,
      "rocket": 0,
      "total_count": 0,
      "url": "https://api.github.com/repos/test_organization/test_repo/issues/6/reactions"
    },
    "repository": {
      "allow_forking": false,
      "archive_url": "https://api.github.com/repos/test_organization/test_repo/{archive_format}{/ref}",
      "archived": false,
      "assignees_url": "https://api.github.com/repos/test_organization/test_repo/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/test_organization/test_repo/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/test_organization/test_repo/branches{/branch}",
      "clone_url": "https://github.com/test_organization/test_repo.git",
      "collaborators_url": "https://api.github.com/repos/test_organization/test_repo/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/test_organization/test_repo/comments{/number}",
      "commits_url": "https://api.github.com/repos/test_organization/test_repo/commits{/sha}",
      "compare_url": "https://api.github.com/repos/test_organization/test_repo/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/test_organization/test_repo/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/test_organization/test_repo/contributors",
      "created_at": "2024-01-22T10:02:32Z",
      "default_branch": "main",
      "deployments_url": "https://api.github.com/repos/test_organization/test_repo/deployments",
      "description": "test for insight connect plugins",
      "disabled": false,
      "downloads_url": "https://api.github.com/repos/test_organization/test_repo/downloads",
      "events_url": "https://api.github.com/repos/test_organization/test_repo/events",
      "fork": false,
      "forks": 0,
      "forks_count": 0,
      "forks_url": "https://api.github.com/repos/test_organization/test_repo/forks",
      "full_name": "test_organization/test_repo",
      "git_commits_url": "https://api.github.com/repos/test_organization/test_repo/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/test_organization/test_repo/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/test_organization/test_repo/git/tags{/sha}",
      "git_url": "git://github.com/test_organization/test_repo.git",
      "has_discussions": false,
      "has_downloads": true,
      "has_issues": true,
      "has_pages": false,
      "has_projects": true,
      "has_wiki": false,
      "hooks_url": "https://api.github.com/repos/test_organization/test_repo/hooks",
      "html_url": "https://github.com/test_organization/test_repo",
      "id": 746587335,
      "is_template": false,
      "issue_comment_url": "https://api.github.com/repos/test_organization/test_repo/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/test_organization/test_repo/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/test_organization/test_repo/issues{/number}",
      "keys_url": "https://api.github.com/repos/test_organization/test_repo/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/test_organization/test_repo/labels{/name}",
      "languages_url": "https://api.github.com/repos/test_organization/test_repo/languages",
      "merges_url": "https://api.github.com/repos/test_organization/test_repo/merges",
      "milestones_url": "https://api.github.com/repos/test_organization/test_repo/milestones{/number}",
      "name": "test_repo",
      "node_id": "R_kgDOLIAExw",
      "notifications_url": "https://api.github.com/repos/test_organization/test_repo/notifications{?since,all,participating}",
      "open_issues": 6,
      "open_issues_count": 6,
      "owner": {
        "avatar_url": "https://avatars.githubusercontent.com/u/157362711?v=4",
        "events_url": "https://api.github.com/users/test_organization/events{/privacy}",
        "followers_url": "https://api.github.com/users/test_organization/followers",
        "following_url": "https://api.github.com/users/test_organization/following{/other_user}",
        "gists_url": "https://api.github.com/users/test_organization/gists{/gist_id}",
        "html_url": "https://github.com/test_organization",
        "id": 157362711,
        "login": "test_organization",
        "node_id": "O_kgDOCWEqFw",
        "organizations_url": "https://api.github.com/users/test_organization/orgs",
        "received_events_url": "https://api.github.com/users/test_organization/received_events",
        "repos_url": "https://api.github.com/users/test_organization/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/test_organization/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/test_organization/subscriptions",
        "type": "Organization",
        "url": "https://api.github.com/users/test_organization"
      },
      "permissions": {
        "admin": true,
        "maintain": true,
        "pull": true,
        "push": true,
        "triage": true
      },
      "private": true,
      "pulls_url": "https://api.github.com/repos/test_organization/test_repo/pulls{/number}",
      "pushed_at": "2024-01-22T10:02:32Z",
      "releases_url": "https://api.github.com/repos/test_organization/test_repo/releases{/id}",
      "size": 0,
      "ssh_url": "github.com:test_organization/test_repo.git",
      "stargazers_count": 0,
      "stargazers_url": "https://api.github.com/repos/test_organization/test_repo/stargazers",
      "statuses_url": "https://api.github.com/repos/test_organization/test_repo/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/test_organization/test_repo/subscribers",
      "subscription_url": "https://api.github.com/repos/test_organization/test_repo/subscription",
      "svn_url": "https://github.com/test_organization/test_repo",
      "tags_url": "https://api.github.com/repos/test_organization/test_repo/tags",
      "teams_url": "https://api.github.com/repos/test_organization/test_repo/teams",
      "topics": [],
      "trees_url": "https://api.github.com/repos/test_organization/test_repo/git/trees{/sha}",
      "updated_at": "2024-01-22T13:28:12Z",
      "url": "https://api.github.com/repos/test_organization/test_repo",
      "visibility": "private",
      "watchers": 0,
      "watchers_count": 0,
      "web_commit_signoff_required": false
    },
    "repository_url": "https://api.github.com/repos/test_organization/test_repo",
    "state": "open",
    "timeline_url": "https://api.github.com/repos/test_organization/test_repo/issues/6/timeline",
    "title": "fshksdhkfsh",
    "updated_at": "2024-01-23T14:10:18Z",
    "url": "https://api.github.com/repos/test_organization/test_repo/issues/6",
    "user": {
      "avatar_url": "https://avatars.githubusercontent.com/u/157107299?v=4",
      "events_url": "https://api.github.com/users/test_user/events{/privacy}",
      "followers_url": "https://api.github.com/users/test_user/followers",
      "following_url": "https://api.github.com/users/test_user/following{/other_user}",
      "gists_url": "https://api.github.com/users/test_user/gists{/gist_id}",
      "html_url": "https://github.com/test_user",
      "id": 157107299,
      "login": "test_user",
      "node_id": "U_kgDOCV1EYw",
      "organizations_url": "https://api.github.com/users/test_user/orgs",
      "received_events_url": "https://api.github.com/users/test_user/received_events",
      "repos_url": "https://api.github.com/users/test_user/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/test_user/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/test_user/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/test_user"
    }
  }
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**git_hub_credentials**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|avatar_url|string|None|False|None|None|
|events_url|string|None|False|None|None|
|followers_url|string|None|False|None|None|
|following_url|string|None|False|None|None|
|gists_url|string|None|False|None|None|
|gravatar_id|string|None|False|None|None|
|html_url|string|None|False|None|None|
|id|integer|None|False|None|None|
|login|string|None|False|None|None|
|organizations_url|string|None|False|None|None|
|Github Personal Token|credential_secret_key|None|True|GitHub personal token|None|
|received_events_url|string|None|False|None|None|
|repos_url|string|None|False|None|None|
|site_admin|boolean|None|False|None|None|
|starred_url|string|None|False|None|None|
|subscriptions_url|string|None|False|None|None|
|type|string|None|False|None|None|
|url|string|None|False|None|None|
|Username|string|None|True|GitHub username|None|
  
**permissions**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|admin|boolean|None|False|None|None|
|pull|boolean|None|False|None|None|
|push|boolean|None|False|None|None|
  
**parent**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|allow_merge_commit|boolean|None|False|None|None|
|allow_rebase_merge|boolean|None|False|None|None|
|allow_squash_merge|boolean|None|False|None|None|
|archive_url|string|None|False|None|None|
|assignees_url|string|None|False|None|None|
|blobs_url|string|None|False|None|None|
|branches_url|string|None|False|None|None|
|clone_url|string|None|False|None|None|
|collaborators_url|string|None|False|None|None|
|comments_url|string|None|False|None|None|
|commits_url|string|None|False|None|None|
|compare_url|string|None|False|None|None|
|contents_url|string|None|False|None|None|
|contributors_url|string|None|False|None|None|
|created_at|string|None|False|None|None|
|default_branch|string|None|False|None|None|
|deployments_url|string|None|False|None|None|
|description|string|None|False|None|None|
|downloads_url|string|None|False|None|None|
|events_url|string|None|False|None|None|
|fork|boolean|None|False|None|None|
|forks_count|integer|None|False|None|None|
|forks_url|string|None|False|None|None|
|full_name|string|None|False|None|None|
|git_commits_url|string|None|False|None|None|
|git_refs_url|string|None|False|None|None|
|git_tags_url|string|None|False|None|None|
|git_url|string|None|False|None|None|
|has_downloads|boolean|None|False|None|None|
|has_issues|boolean|None|False|None|None|
|has_pages|boolean|None|False|None|None|
|has_wiki|boolean|None|False|None|None|
|homepage|string|None|False|None|None|
|hooks_url|string|None|False|None|None|
|html_url|string|None|False|None|None|
|id|integer|None|False|None|None|
|issue_comment_url|string|None|False|None|None|
|issue_events_url|string|None|False|None|None|
|issues_url|string|None|False|None|None|
|keys_url|string|None|False|None|None|
|labels_url|string|None|False|None|None|
|languages_url|string|None|False|None|None|
|merges_url|string|None|False|None|None|
|milestones_url|string|None|False|None|None|
|mirror_url|string|None|False|None|None|
|name|string|None|False|None|None|
|network_count|integer|None|False|None|None|
|notifications_url|string|None|False|None|None|
|open_issues_count|integer|None|False|None|None|
|owner|organization|None|False|None|None|
|permissions|permissions|None|False|None|None|
|private|boolean|None|False|None|None|
|pulls_url|string|None|False|None|None|
|pushed_at|string|None|False|None|None|
|releases_url|string|None|False|None|None|
|size|integer|None|False|None|None|
|ssh_url|string|None|False|None|None|
|stargazers_count|integer|None|False|None|None|
|stargazers_url|string|None|False|None|None|
|statuses_url|string|None|False|None|None|
|subscribers_count|integer|None|False|None|None|
|subscribers_url|string|None|False|None|None|
|subscription_url|string|None|False|None|None|
|svn_url|string|None|False|None|None|
|tags_url|string|None|False|None|None|
|teams_url|string|None|False|None|None|
|topics|[]string|None|False|None|None|
|trees_url|string|None|False|None|None|
|updated_at|string|None|False|None|None|
|url|string|None|False|None|None|
|watchers_count|integer|None|False|None|None|
  
**repo**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|allow_merge_commit|boolean|None|False|None|None|
|allow_rebase_merge|boolean|None|False|None|None|
|allow_squash_merge|boolean|None|False|None|None|
|archive_url|string|None|False|None|None|
|assignees_url|string|None|False|None|None|
|blobs_url|string|None|False|None|None|
|branches_url|string|None|False|None|None|
|clone_url|string|None|False|None|None|
|collaborators_url|string|None|False|None|None|
|comments_url|string|None|False|None|None|
|commits_url|string|None|False|None|None|
|compare_url|string|None|False|None|None|
|contents_url|string|None|False|None|None|
|contributors_url|string|None|False|None|None|
|created_at|string|None|False|None|None|
|default_branch|string|None|False|None|None|
|deployments_url|string|None|False|None|None|
|description|string|None|False|None|None|
|downloads_url|string|None|False|None|None|
|events_url|string|None|False|None|None|
|fork|boolean|None|False|None|None|
|forks_count|integer|None|False|None|None|
|forks_url|string|None|False|None|None|
|full_name|string|None|False|None|None|
|git_commits_url|string|None|False|None|None|
|git_refs_url|string|None|False|None|None|
|git_tags_url|string|None|False|None|None|
|git_url|string|None|False|None|None|
|has_downloads|boolean|None|False|None|None|
|has_issues|boolean|None|False|None|None|
|has_pages|boolean|None|False|None|None|
|has_wiki|boolean|None|False|None|None|
|homepage|string|None|False|None|None|
|hooks_url|string|None|False|None|None|
|html_url|string|None|False|None|None|
|id|integer|None|False|None|None|
|issue_comment_url|string|None|False|None|None|
|issue_events_url|string|None|False|None|None|
|issues_url|string|None|False|None|None|
|keys_url|string|None|False|None|None|
|labels_url|string|None|False|None|None|
|languages_url|string|None|False|None|None|
|merges_url|string|None|False|None|None|
|milestones_url|string|None|False|None|None|
|mirror_url|string|None|False|None|None|
|name|string|None|False|None|None|
|network_count|integer|None|False|None|None|
|notifications_url|string|None|False|None|None|
|open_issues_count|integer|None|False|None|None|
|organization|organization|None|False|None|None|
|owner|organization|None|False|None|None|
|parent|parent|None|False|None|None|
|permissions|permissions|None|False|None|None|
|private|boolean|None|False|None|None|
|pulls_url|string|None|False|None|None|
|pushed_at|string|None|False|None|None|
|releases_url|string|None|False|None|None|
|size|integer|None|False|None|None|
|source|parent|None|False|None|None|
|ssh_url|string|None|False|None|None|
|stargazers_count|integer|None|False|None|None|
|stargazers_url|string|None|False|None|None|
|statuses_url|string|None|False|None|None|
|subscribers_count|integer|None|False|None|None|
|subscribers_url|string|None|False|None|None|
|subscription_url|string|None|False|None|None|
|svn_url|string|None|False|None|None|
|tags_url|string|None|False|None|None|
|teams_url|string|None|False|None|None|
|topics|[]string|None|False|None|None|
|trees_url|string|None|False|None|None|
|updated_at|string|None|False|None|None|
|url|string|None|False|None|None|
|watchers_count|integer|None|False|None|None|
  
**assignee**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|avatar_url|string|None|False|None|None|
|events_url|string|None|False|None|None|
|followers_url|string|None|False|None|None|
|following_url|string|None|False|None|None|
|gists_url|string|None|False|None|None|
|gravatar_id|string|None|False|None|None|
|html_url|string|None|False|None|None|
|id|integer|None|False|None|None|
|login|string|None|False|None|None|
|organizations_url|string|None|False|None|None|
|received_events_url|string|None|False|None|None|
|repos_url|string|None|False|None|None|
|site_admin|boolean|None|False|None|None|
|starred_url|string|None|False|None|None|
|subscriptions_url|string|None|False|None|None|
|type|string|None|False|None|None|
|url|string|None|False|None|None|
  
**label**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|color|string|None|False|None|None|
|default|boolean|None|False|None|None|
|id|integer|None|False|None|None|
|name|string|None|False|None|None|
|url|string|None|False|None|None|
  
**milestone**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|closed_at|string|None|False|None|None|
|closed_issues|integer|None|False|None|None|
|created_at|string|None|False|None|None|
|creator|assignee|None|False|None|None|
|description|string|None|False|None|None|
|due_on|string|None|False|None|None|
|html_url|string|None|False|None|None|
|id|integer|None|False|None|None|
|labels_url|string|None|False|None|None|
|number|integer|None|False|None|None|
|open_issues|integer|None|False|None|None|
|state|string|None|False|None|None|
|title|string|None|False|None|None|
|updated_at|string|None|False|None|None|
|url|string|None|False|None|None|
  
**pull_request**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|diff_url|string|None|False|None|None|
|html_url|string|None|False|None|None|
|patch_url|string|None|False|None|None|
|url|string|None|False|None|None|
  
**issue**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|assignee|assignee|None|False|None|None|
|assignees|[]assignee|None|False|None|None|
|body|string|None|False|None|None|
|comments|integer|None|False|None|None|
|comments_url|string|None|False|None|None|
|created_at|string|None|False|None|None|
|events_url|string|None|False|None|None|
|html_url|string|None|False|None|None|
|id|integer|None|False|None|None|
|labels|[]label|None|False|None|None|
|labels_url|string|None|False|None|None|
|locked|boolean|None|False|None|None|
|milestone|milestone|None|False|None|None|
|number|integer|None|False|None|None|
|pull_request|pull_request|None|False|None|None|
|repository_url|string|None|False|None|None|
|state|string|None|False|None|None|
|title|string|None|False|None|None|
|updated_at|string|None|False|None|None|
|url|string|None|False|None|None|
|user|assignee|None|False|None|None|
  
**collaborator_repository**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|archive_url|string|None|False|None|None|
|assignees_url|string|None|False|None|None|
|blobs_url|string|None|False|None|None|
|branches_url|string|None|False|None|None|
|collaborators_url|string|None|False|None|None|
|comments_url|string|None|False|None|None|
|commits_url|string|None|False|None|None|
|compare_url|string|None|False|None|None|
|contents_url|string|None|False|None|None|
|contributors_url|string|None|False|None|None|
|deployments_url|string|None|False|None|None|
|description|string|None|False|None|None|
|downloads_url|string|None|False|None|None|
|events_url|string|None|False|None|None|
|fork|boolean|None|False|None|None|
|forks_url|string|None|False|None|None|
|full_name|string|None|False|None|None|
|git_commits_url|string|None|False|None|None|
|git_refs_url|string|None|False|None|None|
|git_tags_url|string|None|False|None|None|
|git_url|string|None|False|None|None|
|html_url|string|None|False|None|None|
|id|integer|None|False|None|None|
|issue_comment_url|string|None|False|None|None|
|issue_events_url|string|None|False|None|None|
|issues_url|string|None|False|None|None|
|keys_url|string|None|False|None|None|
|labels_url|string|None|False|None|None|
|languages_url|string|None|False|None|None|
|merges_url|string|None|False|None|None|
|milestones_url|string|None|False|None|None|
|name|string|None|False|None|None|
|node_id|string|None|False|None|None|
|notifications_url|string|None|False|None|None|
|owner|organization|None|False|None|None|
|private|boolean|None|False|None|None|
|pulls_url|string|None|False|None|None|
|releases_url|string|None|False|None|None|
|ssh_url|string|None|False|None|None|
|stargazers_url|string|None|False|None|None|
|statuses_url|string|None|False|None|None|
|subscribers_url|string|None|False|None|None|
|subscription_url|string|None|False|None|None|
|tags_url|string|None|False|None|None|
|teams_url|string|None|False|None|None|
|trees_url|string|None|False|None|None|
|url|string|None|False|None|None|
  
**collaborator_invite**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|avatar_url|string|None|False|None|None|
|events_url|string|None|False|None|None|
|followers_url|string|None|False|None|None|
|following_url|string|None|False|None|None|
|gists_url|string|None|False|None|None|
|gravatar_id|string|None|False|None|None|
|html_url|string|None|False|None|None|
|id|integer|None|False|None|None|
|login|string|None|False|None|None|
|node_id|string|None|False|None|None|
|organizations_url|string|None|False|None|None|
|received_events_url|string|None|False|None|None|
|repos_url|string|None|False|None|None|
|site_admin|boolean|None|False|None|None|
|starred_url|string|None|False|None|None|
|subscriptions_url|string|None|False|None|None|
|type|string|None|False|None|None|
|url|string|None|False|None|None|
  
**add_collaborator**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|created_at|string|None|False|None|None|
|html_url|string|None|False|None|None|
|id|integer|None|False|None|None|
|invitee|collaborator_invite|None|False|None|None|
|inviter|collaborator_invite|None|False|None|None|
|permission|string|None|False|None|None|
|repository|collaborator_repository|None|False|None|None|
|url|string|None|False|None|None|
  
**membership_user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Avatar URL|string|None|False|Avatar URL|None|
|Events URL|string|None|False|Events URL|None|
|Followers URL|string|None|False|Followers URL|None|
|Following URL|string|None|False|Following URL|None|
|Gists URL|string|None|False|Gists URL|None|
|Gravatar ID|string|None|False|Gravatar ID|None|
|HTML URL|string|None|False|HTML URL|None|
|ID|integer|None|False|ID|None|
|Login|string|None|False|Login|None|
|Node ID|string|None|False|Node ID|None|
|Organizations URL|string|None|False|Organizations URL|None|
|Received Events URL|string|None|False|Received Events URL|None|
|Repos URL|string|None|False|Repos URL|None|
|Site Admin|boolean|None|False|Site admin|None|
|Starred URL|string|None|False|Starred URL|None|
|Subscriptions URL|string|None|False|Subscriptions URL|None|
|Type|string|None|False|Type|None|
|URL|string|None|False|URL|None|
  
**membership_organization**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Membership Organization|string|None|False|Membership organization|None|
|Description|string|None|False|Description|None|
|Events URL|string|None|False|Events URL|None|
|Hooks URL|string|None|False|Hooks URL|None|
|ID|integer|None|False|ID|None|
|Issues URL|string|None|False|Issues URL|None|
|Login|string|None|False|Login|None|
|Members URL|string|None|False|Members URL|None|
|Node ID|string|None|False|Node ID|None|
|Public Members URL|string|None|False|Public Members URL|None|
|Repos URL|string|None|False|Repos URL|None|
|URL|string|None|False|URL|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 3.0.0 - Update to use GitHub personal tokn rather than password | update the HTTP requests to auth header rather than name and password | update to the newest SDK version | add unit tests | bump requiremnts | fixed the connection test  
* 2.1.2 - Fix broken action "Close Issue"  
* 2.1.1 - New spec and help.md format for the Extension Library  
* 2.1.0 - New actions: Create Issue Comment, Close Issue, Add Issue Label  
* 2.0.1 - Fix missing Search action | Pin pygithub and python-dateutil libraries | Update to use the `komand/python-3-37-slim-plugin` Docker image to reduce plugin size | Enable verification of SSL/TLS certificates for GitHub.com  
* 2.0.0 - Rename "User" action to "Get User"  
* 1.2.1 - Update connection documentation and add example outputs to remaining actions and triggers  
* 1.2.0 - Add Block User and Unblock User action  
* 1.1.0 - Add Membership action  
* 1.0.0 - Add Collaborator action | Update to v2 Python plugin architecture | Support web server mode  
* 0.2.3 - SSL bug fix in SDK  
* 0.2.2 - New optional Milestone input to Create Issue action  
* 0.2.1 - New optional Assignee input to Create Issue action  
* 0.2.0 - New actions: Get Repo, Get My Issues, Get Issues by Repo, and Search  
* 0.1.0 - Initial plugin

# Links

* [GitHub](https://github.com)
* [GitHub REST API](https://developer.github.com/v3/)

## References
  
* [GitHub](https://github.com)  
* [GitHub REST API](https://developer.github.com/v3/)