
# Trello

## About

[Trello](https://trello.com) gives you perspective over all your projects, at work and at home.
Whether it's managing a team, writing an epic screenplay, or just making a grocery list,
This plugin accesses the [Trello API](https://developers.trello.com/advanced-reference)
The output of this plugin is the JSON data returned by Trello.

## Actions

### Remove Member from Cards

This action is used to remove member from cards.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id_member|string|None|True|The id of the member to remove from the card|None|
|card_id|string|None|True|Card id or shortlink|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]object|False|Trello return an array json, result variable is used for response|

### Remove Member from Organization

This action is used to this will remove a member from your organization.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id_member|string|None|True|The id of the member to remove from the organization|None|
|id_or_name|string|None|True|ID or name of organization|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|descData|object|False|None|
|displayName|string|False|Name using show in dashboard|
|name|string|False|Organization name|
|url|string|False|Organization url|
|products|[]integer|False|List all products|
|members|[]object|False|List all members|
|powerUps|[]integer|False|None|
|id|string|False|Organization id|
|desc|string|False|Description about organization|

### Deactivated List

This action is used to list deactivated users and requires a Trello Business Class account.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|string|deactivated|False|Filter status of user, default\: deactivated|['all', 'active', 'admin', 'deactivated', 'me', 'normal']|
|member|boolean|False|False|Response with member or none|None|
|id_or_name|string|None|True|ID or name of organization|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]object|False|Trello return an array json, result variable is used for response|

### Boards Member

This action is used to list members of a board.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|string|all|False|Filter boards with any status of board, default\: all|['all', 'closed', 'members', 'open', 'organization', 'pinned', 'public', 'starred', 'unpinned']|
|actions_entities|boolean|False|False|None|None|
|id_or_name|string|None|True|ID or name of member|None|
|fields|string|all|False|Fields of member, default\: all|['all', 'closed', 'dateLastActivity', 'dateLastView', 'desc', 'descData', 'idOrganization', 'invitations', 'invited', 'labelNames', 'memberships', 'name', 'pinned', 'powerUps', 'prefs', 'shortLink', 'shortUrl', 'starred', 'subscribed', 'url']|
|actions|string|None|False|List actions|['', 'all', 'addAttachmentToCard', 'addChecklistToCard', 'addMemberToBoard', 'addMemberToCard', 'addMemberToOrganization', 'addToOrganizationBoard', 'commentCard', 'convertToCardFromCheckItem', 'copyBoard', 'copyCard', 'copyCommentCard', 'createBoard', 'createCard', 'createList', 'createOrganization', 'deleteAttachmentFromCard', 'deleteBoardInvitation', 'deleteCard', 'deleteOrganizationInvitation', 'disablePowerUp', 'emailCard', 'enablePowerUp', 'makeAdminOfBoard', 'makeNormalMemberOfBoard', 'makeNormalMemberOfOrganization', 'makeObserverOfBoard', 'memberJoinedTrello', 'moveCardFromBoard', 'moveCardToBoard', 'moveListFromBoard', 'moveListToBoard', 'removeChecklistFromCard', 'removeFromOrganizationBoard', 'removeMemberFromCard', 'unconfirmedBoardInvitation', 'unconfirmedOrganizationInvitation', 'updateBoard', 'updateCard', 'updateCard:closed', 'updateCard:desc', 'updateCard:idList', 'updateCard:name', 'updateCheckItemStateOnCard', 'updateChecklist', 'updateList', 'updateList:closed', 'updateList:name', 'updateMember', 'updateOrganization']|
|action_fields|string|all|False|List all fields of actions|['all', 'data', 'date', 'idMemberCreator', 'type']|
|memberships|string|None|False|List status of memberships|['', 'all', 'active', 'admin', 'deactivated', 'me', 'normal']|
|lists|string|none|False|Format lists|['all', 'closed', 'none', 'open']|
|actions_since|string|None|False|Filter by a date, null or lastView|None|
|actions_limit|integer|50|False|A number from 0 to 1000, default\: 50|None|
|organization|boolean|False|False|Response with organization or none|None|
|actions_format|string|list|False|Format of actions|['count', 'list', 'minimal']|
|organization_fields|string|None|False|Response with one or more member fields|['', 'all', 'billableMemberCount', 'desc', 'descData', 'displayName', 'idBoards', 'invitations', 'invited', 'logoHash', 'memberships', 'name', 'powerUps', 'prefs', 'premiumFeatures', 'products', 'url', 'website']|

Value of the parameter `actions_since` is valid with:

* a date as example: 2017-01-05T08:21:43.338Z
* null
* lastView

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]object|False|Trello return an array json, result variable is used for response|

### Deactivate User

This action is used to deactivate a user and requires a Trello Business Class account.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id_member|string|None|True|The id of the member to deactivated from organization|None|
|value|boolean|True|False|None|None|
|id_or_name|string|None|True|ID or name of organization|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|Http status code|

### Members List

This action is used to list members of an organization.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|memberships_member_fields|string|None|False|Response with one or more member fields, default\: fullName,username|['', 'all', 'avatarHash', 'bio', 'bioData', 'confirmed', 'fullName', 'idPremOrgsAdmin', 'initials', 'memberType', 'products', 'status', 'url', 'username']|
|actions_entities|boolean|False|False|None|None|
|board_actions_format|string|list|False|Format of board actions|['count', 'list', 'minimal']|
|board_lists|string|none|False|List board with status of\: all, closed, open, none, default\: none|['all', 'closed', 'none', 'open']|
|actions_display|boolean|False|False|None|None|
|board_actions_limit|integer|50|False|A number from 0 to 1000, default\: 50|None|
|actions|string|None|False|List actions|['', 'addAttachmentToCard', 'addChecklistToCard', 'addMemberToBoard', 'addMemberToCard', 'addMemberToOrganization', 'addToOrganizationBoard', 'commentCard', 'convertToCardFromCheckItem', 'copyBoard', 'copyCard', 'copyCommentCard', 'createBoard', 'createCard', 'createList', 'createOrganization', 'deleteAttachmentFromCard', 'deleteBoardInvitation', 'deleteCard', 'deleteOrganizationInvitation', 'disablePowerUp', 'emailCard', 'enablePowerUp', 'makeAdminOfBoard', 'makeNormalMemberOfBoard', 'makeNormalMemberOfOrganization', 'makeObserverOfBoard', 'memberJoinedTrello', 'moveCardFromBoard', 'moveCardToBoard', 'moveListFromBoard', 'moveListToBoard', 'removeChecklistFromCard', 'removeFromOrganizationBoard', 'removeMemberFromCard', 'unconfirmedBoardInvitation', 'unconfirmedOrganizationInvitation', 'updateBoard', 'updateCard', 'updateCard:closed', 'updateCard:desc', 'updateCard:idList', 'updateCard:name', 'updateCheckItemStateOnCard', 'updateChecklist', 'updateList', 'updateList:closed', 'updateList:name', 'updateMember', 'updateOrganization']|
|action_fields|string|all|False|List all fields of actions|['all', 'data', 'date', 'idMemberCreator', 'type']|
|memberships_member|boolean|False|False|Response with memberships or none|None|
|members|string|none|False|Filter members with roles\: admins, normal, owners, none, all|['admins', 'all', 'none', 'normal', 'owners']|
|member_fields|string|None|False|Response with one or more member fields, default\: avatarHash,fullName,initials,username,confirmed|['', 'all', 'avatarHash', 'bio', 'bioData', 'confirmed', 'fullName', 'idPremOrgsAdmin', 'initials', 'memberType', 'products', 'status', 'url', 'username']|
|actions_limit|integer|50|False|A number from 0 to 1000, default\: 50|None|
|board_action_fields|string|all|False|Fields of board actions|['all', 'data', 'date', 'idMemberCreator', 'type']|
|board_actions_display|boolean|False|False|None|None|
|board_fields|string|all|False|Response with one or more fields of boards, default\: all|['all', 'closed', 'dateLastActivity', 'dateLastView', 'desc', 'descData', 'idOrganization', 'invitations', 'invited', 'labelNames', 'memberships', 'name', 'pinned', 'powerUps', 'prefs', 'shortLink', 'shortUrl', 'starred', 'subscribed', 'url']|
|memberships|string|none|False|List status of memberships|['none', 'all', 'active', 'admin', 'deactivated', 'me', 'normal']|
|membersInvited|string|none|False|Filter invited members by roles\: admins, normal, owners, none, all, default\: none|['admins', 'all', 'none', 'normal', 'owners']|
|boards|string|None|False|Filter boards with any status of board|['', 'all', 'closed', 'members', 'open', 'organization', 'pinned', 'public', 'starred', 'unpinned']|
|fields|string|None|False|Field of organization, default\: name,displayName,desc,descData,url,website,logoHash,products,powerUps|['', 'all', 'billableMemberCount', 'desc', 'descData', 'displayName', 'idBoards', 'invitations', 'invited', 'logoHash', 'memberships', 'name', 'powerUps', 'prefs', 'premiumFeatures', 'products', 'url', 'website']|
|id_or_name|string|None|True|ID or name of organization|None|
|member_activity|boolean|False|False|Response with activity of member or none, works for premium organizations only|None|
|paid_account|boolean|False|False|None|None|
|board_actions_since|string|None|False|Filter by a date, null or lastView|None|
|pluginData|boolean|False|False|None|None|
|board_actions_entities|boolean|False|False|None|None|
|board_pluginData|boolean|False|False|None|None|
|board_actions|string|None|False|Board actions|['', 'all', 'addAttachmentToCard', 'addChecklistToCard', 'addMemberToBoard', 'addMemberToCard', 'addMemberToOrganization', 'addToOrganizationBoard', 'commentCard', 'convertToCardFromCheckItem', 'copyBoard', 'copyCard', 'copyCommentCard', 'createBoard', 'createCard', 'createList', 'createOrganization', 'deleteAttachmentFromCard', 'deleteBoardInvitation', 'deleteCard', 'deleteOrganizationInvitation', 'disablePowerUp', 'emailCard', 'enablePowerUp', 'makeAdminOfBoard', 'makeNormalMemberOfBoard', 'makeNormalMemberOfOrganization', 'makeObserverOfBoard', 'memberJoinedTrello', 'moveCardFromBoard', 'moveCardToBoard', 'moveListFromBoard', 'moveListToBoard', 'removeChecklistFromCard', 'removeFromOrganizationBoard', 'removeMemberFromCard', 'unconfirmedBoardInvitation', 'unconfirmedOrganizationInvitation', 'updateBoard', 'updateCard', 'updateCard:closed', 'updateCard:desc', 'updateCard:idList', 'updateCard:name', 'updateCheckItemStateOnCard', 'updateChecklist', 'updateList', 'updateList:closed', 'updateList:name', 'updateMember', 'updateOrganization']|
|membersInvited_fields|string|None|False|Response with one or more fields of invited members, default\: avatarHash,fullName,initials,username,confirmed|['', 'all', 'avatarHash', 'bio', 'bioData', 'confirmed', 'fullName', 'idPremOrgsAdmin', 'initials', 'memberType', 'products', 'status', 'url', 'username']|

Value of the parameter `board_actions_since` is valid with:

* a date as example: 2017-01-05T08:21:43.338Z
* null
* lastView

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|premiumFeatures|[]string|False|None|
|invitations|[]string|False|None|
|members|[]string|False|None|
|powerUps|[]integer|False|None|
|idBoards|[]string|False|None|
|membersInvited|[]string|False|None|
|desc|string|False|None|
|id|string|False|None|
|boards|[]string|False|None|
|descData|object|False|None|
|displayName|string|False|None|
|name|string|False|None|
|url|string|False|None|
|invited|boolean|False|None|
|billableMemberCount|integer|False|None|
|memberships|[]string|False|None|
|pluginData|[]string|False|None|
|products|[]integer|False|None|
|prefs|object|False|None|
|activeBillableMemberCount|integer|False|None|

### Remove Member from Board

This action is used to remove member from board.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|board_id|string|None|False|The id of board|None|
|id_member|string|None|True|The id of the member to remove from the board|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|labelNames|object|False|None|
|name|string|False|Name of board|
|idOrganization|string|False|The id of organization|
|pinned|boolean|False|None|
|shortUrl|string|False|Short url|
|url|string|False|URL|
|closed|boolean|False|None|
|prefs|object|False|None|
|members|[]object|False|List all members on board|
|id|string|False|The id of board|
|desc|string|False|Description about board|

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API key|None|
|version|integer|1|True|Version|None|
|api_token|credential_token|None|True|API Token|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* User deprovisioning
* Project management

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 2.0.0 - Update to new secret key credential type
* 2.0.1 - Remove erroneous data from plugin spec

## References

* [Trello](https://trello.com)
* [Trello API](https://developers.trello.com/advanced-reference)
* [Trello Business Class](https://trello.com/business-class)
