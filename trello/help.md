# Description

[Trello](https://trello.com) is an excellent tool for managing your projects and productivity. 
The Trello plugin allows you to manage users, view members, remove members, gets boards by member, and more in your Trello project by leveraging the [Trello API](https://developers.trello.com/advanced-reference).

# Key Features

* Manage users in Trello

# Requirements

* A Trello API key
* A Trello API Token
* The Trello version

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API key|None|
|api_token|credential_token|None|True|API Token|None|
|version|integer|1|True|Version|None|

## Technical Details

### Actions

#### Remove Member from Cards

This action is used to remove member from cards.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|card_id|string|None|True|Card id or shortlink|None|
|id_member|string|None|True|The id of the member to remove from the card|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]object|False|Trello return an array json, result variable is used for response|

#### Remove Member from Organization

This action is used to this will remove a member from your organization.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id_member|string|None|True|The id of the member to remove from the organization|None|
|id_or_name|string|None|True|ID or name of organization|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|desc|string|False|Description about organization|
|descData|object|False|Desc data|
|displayName|string|False|Name using show in dashboard|
|id|string|False|Organization id|
|members|[]object|False|List all members|
|name|string|False|Organization name|
|powerUps|[]integer|False|Power ups|
|products|[]integer|False|List all products|
|url|string|False|Organization URL|

#### Deactivated List

This action is used to list deactivated users and requires a Trello Business Class account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|string|deactivated|False|Filter status of user, default: deactivated|['all', 'active', 'admin', 'deactivated', 'me', 'normal']|
|id_or_name|string|None|True|ID or name of organization|None|
|member|boolean|False|False|Response with member or none|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]object|False|Trello return an array json, result variable is used for response|

#### Boards Member

This action is used to list members of a board.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|action_fields|string|all|False|List all fields of actions|['all', 'data', 'date', 'idMemberCreator', 'type']|
|actions|string|None|False|List actions|['', 'all', 'addAttachmentToCard', 'addChecklistToCard', 'addMemberToBoard', 'addMemberToCard', 'addMemberToOrganization', 'addToOrganizationBoard', 'commentCard', 'convertToCardFromCheckItem', 'copyBoard', 'copyCard', 'copyCommentCard', 'createBoard', 'createCard', 'createList', 'createOrganization', 'deleteAttachmentFromCard', 'deleteBoardInvitation', 'deleteCard', 'deleteOrganizationInvitation', 'disablePowerUp', 'emailCard', 'enablePowerUp', 'makeAdminOfBoard', 'makeNormalMemberOfBoard', 'makeNormalMemberOfOrganization', 'makeObserverOfBoard', 'memberJoinedTrello', 'moveCardFromBoard', 'moveCardToBoard', 'moveListFromBoard', 'moveListToBoard', 'removeChecklistFromCard', 'removeFromOrganizationBoard', 'removeMemberFromCard', 'unconfirmedBoardInvitation', 'unconfirmedOrganizationInvitation', 'updateBoard', 'updateCard', 'updateCard:closed', 'updateCard:desc', 'updateCard:idList', 'updateCard:name', 'updateCheckItemStateOnCard', 'updateChecklist', 'updateList', 'updateList:closed', 'updateList:name', 'updateMember', 'updateOrganization']|
|actions_entities|boolean|False|False|Actions entities|None|
|actions_format|string|list|False|Format of actions|['count', 'list', 'minimal']|
|actions_limit|integer|50|False|A number from 0 to 1000, default: 50|None|
|actions_since|string|None|False|Filter by a date, null or lastView|None|
|fields|string|all|False|Fields of member, default: all|['all', 'closed', 'dateLastActivity', 'dateLastView', 'desc', 'descData', 'idOrganization', 'invitations', 'invited', 'labelNames', 'memberships', 'name', 'pinned', 'powerUps', 'prefs', 'shortLink', 'shortUrl', 'starred', 'subscribed', 'url']|
|filter|string|all|False|Filter boards with any status of board, default: all|['all', 'closed', 'members', 'open', 'organization', 'pinned', 'public', 'starred', 'unpinned']|
|id_or_name|string|None|True|ID or name of member|None|
|lists|string|none|False|Format lists|['all', 'closed', 'none', 'open']|
|memberships|string|None|False|List status of memberships|['', 'all', 'active', 'admin', 'deactivated', 'me', 'normal']|
|organization|boolean|False|False|Response with organization or none|None|
|organization_fields|string|None|False|Response with one or more member fields|['', 'all', 'billableMemberCount', 'desc', 'descData', 'displayName', 'idBoards', 'invitations', 'invited', 'logoHash', 'memberships', 'name', 'powerUps', 'prefs', 'premiumFeatures', 'products', 'url', 'website']|

Value of the parameter `actions_since` is valid with:

* a date as example: 2017-01-05T08:21:43.338Z
* null
* lastView

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]object|False|Trello return an array json, result variable is used for response|

#### Deactivate User

This action is used to deactivate a user and requires a Trello Business Class account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id_member|string|None|True|The id of the member to deactivated from organization|None|
|id_or_name|string|None|True|ID or name of organization|None|
|value|boolean|True|False|Value|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|

#### Members List

This action is used to list members of an organization.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|action_fields|string|all|False|List all fields of actions|['all', 'data', 'date', 'idMemberCreator', 'type']|
|actions|string|None|False|List actions|['', 'addAttachmentToCard', 'addChecklistToCard', 'addMemberToBoard', 'addMemberToCard', 'addMemberToOrganization', 'addToOrganizationBoard', 'commentCard', 'convertToCardFromCheckItem', 'copyBoard', 'copyCard', 'copyCommentCard', 'createBoard', 'createCard', 'createList', 'createOrganization', 'deleteAttachmentFromCard', 'deleteBoardInvitation', 'deleteCard', 'deleteOrganizationInvitation', 'disablePowerUp', 'emailCard', 'enablePowerUp', 'makeAdminOfBoard', 'makeNormalMemberOfBoard', 'makeNormalMemberOfOrganization', 'makeObserverOfBoard', 'memberJoinedTrello', 'moveCardFromBoard', 'moveCardToBoard', 'moveListFromBoard', 'moveListToBoard', 'removeChecklistFromCard', 'removeFromOrganizationBoard', 'removeMemberFromCard', 'unconfirmedBoardInvitation', 'unconfirmedOrganizationInvitation', 'updateBoard', 'updateCard', 'updateCard:closed', 'updateCard:desc', 'updateCard:idList', 'updateCard:name', 'updateCheckItemStateOnCard', 'updateChecklist', 'updateList', 'updateList:closed', 'updateList:name', 'updateMember', 'updateOrganization']|
|actions_display|boolean|False|False|Actions display|None|
|actions_entities|boolean|False|False|Actions entities|None|
|actions_limit|integer|50|False|A number from 0 to 1000, default: 50|None|
|board_action_fields|string|all|False|Fields of board actions|['all', 'data', 'date', 'idMemberCreator', 'type']|
|board_actions|string|None|False|Board actions|['', 'all', 'addAttachmentToCard', 'addChecklistToCard', 'addMemberToBoard', 'addMemberToCard', 'addMemberToOrganization', 'addToOrganizationBoard', 'commentCard', 'convertToCardFromCheckItem', 'copyBoard', 'copyCard', 'copyCommentCard', 'createBoard', 'createCard', 'createList', 'createOrganization', 'deleteAttachmentFromCard', 'deleteBoardInvitation', 'deleteCard', 'deleteOrganizationInvitation', 'disablePowerUp', 'emailCard', 'enablePowerUp', 'makeAdminOfBoard', 'makeNormalMemberOfBoard', 'makeNormalMemberOfOrganization', 'makeObserverOfBoard', 'memberJoinedTrello', 'moveCardFromBoard', 'moveCardToBoard', 'moveListFromBoard', 'moveListToBoard', 'removeChecklistFromCard', 'removeFromOrganizationBoard', 'removeMemberFromCard', 'unconfirmedBoardInvitation', 'unconfirmedOrganizationInvitation', 'updateBoard', 'updateCard', 'updateCard:closed', 'updateCard:desc', 'updateCard:idList', 'updateCard:name', 'updateCheckItemStateOnCard', 'updateChecklist', 'updateList', 'updateList:closed', 'updateList:name', 'updateMember', 'updateOrganization']|
|board_actions_display|boolean|False|False|Board actions display|None|
|board_actions_entities|boolean|False|False|Board actions entities|None|
|board_actions_format|string|list|False|Format of board actions|['count', 'list', 'minimal']|
|board_actions_limit|integer|50|False|A number from 0 to 1000, default: 50|None|
|board_actions_since|string|None|False|Filter by a date, null or lastView|None|
|board_fields|string|all|False|Response with one or more fields of boards, default: all|['all', 'closed', 'dateLastActivity', 'dateLastView', 'desc', 'descData', 'idOrganization', 'invitations', 'invited', 'labelNames', 'memberships', 'name', 'pinned', 'powerUps', 'prefs', 'shortLink', 'shortUrl', 'starred', 'subscribed', 'url']|
|board_lists|string|none|False|List board with status of: all, closed, open, none, default: none|['all', 'closed', 'none', 'open']|
|board_pluginData|boolean|False|False|Board plugin data|None|
|boards|string|None|False|Filter boards with any status of board|['', 'all', 'closed', 'members', 'open', 'organization', 'pinned', 'public', 'starred', 'unpinned']|
|fields|string|None|False|Field of organization, default: name,displayName,desc,descData,URL,website,logoHash,products,powerUps|['', 'all', 'billableMemberCount', 'desc', 'descData', 'displayName', 'idBoards', 'invitations', 'invited', 'logoHash', 'memberships', 'name', 'powerUps', 'prefs', 'premiumFeatures', 'products', 'url', 'website']|
|id_or_name|string|None|True|ID or name of organization|None|
|member_activity|boolean|False|False|Response with activity of member or none, works for premium organizations only|None|
|member_fields|string|None|False|Response with one or more member fields, default: avatarHash,fullName,initials,username,confirmed|['', 'all', 'avatarHash', 'bio', 'bioData', 'confirmed', 'fullName', 'idPremOrgsAdmin', 'initials', 'memberType', 'products', 'status', 'url', 'username']|
|members|string|none|False|Filter members with roles: admins, normal, owners, none, all|['admins', 'all', 'none', 'normal', 'owners']|
|membersInvited|string|none|False|Filter invited members by roles: admins, normal, owners, none, all, default: none|['admins', 'all', 'none', 'normal', 'owners']|
|membersInvited_fields|string|None|False|Response with one or more fields of invited members, default: avatarHash,fullName,initials,username,confirmed|['', 'all', 'avatarHash', 'bio', 'bioData', 'confirmed', 'fullName', 'idPremOrgsAdmin', 'initials', 'memberType', 'products', 'status', 'url', 'username']|
|memberships|string|none|False|List status of memberships|['none', 'all', 'active', 'admin', 'deactivated', 'me', 'normal']|
|memberships_member|boolean|False|False|Response with memberships or none|None|
|memberships_member_fields|string|None|False|Response with one or more member fields, default: fullName,username|['', 'all', 'avatarHash', 'bio', 'bioData', 'confirmed', 'fullName', 'idPremOrgsAdmin', 'initials', 'memberType', 'products', 'status', 'url', 'username']|
|paid_account|boolean|False|False|Paid account|None|
|pluginData|boolean|False|False|Plugin data|None|

Value of the parameter `board_actions_since` is valid with:

* a date as example: 2017-01-05T08:21:43.338Z
* null
* lastView

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|activeBillableMemberCount|integer|False|Active billable member count|
|billableMemberCount|integer|False|Billable member count|
|boards|[]string|False|Boards|
|desc|string|False|The description about organization|
|descData|object|False|Desc data|
|displayName|string|False|Display name organization|
|id|string|True|ID organization|
|idBoards|[]string|False|ID boards|
|invitations|[]string|False|Invitations|
|invited|boolean|False|Invited|
|members|[]string|False|Members|
|membersInvited|[]string|False|The members invited|
|memberships|[]string|False|Memberships|
|name|string|False|Name organization|
|pluginData|[]string|False|Plugin's data|
|powerUps|[]integer|False|Power ups|
|prefs|object|False|Prefs|
|premiumFeatures|[]string|False|Premium features|
|products|[]integer|False|Products|
|url|string|False|Url|

#### Remove Member from Board

This action is used to remove member from board.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|board_id|string|None|False|The id of board|None|
|id_member|string|None|True|The id of the member to remove from the board|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|closed|boolean|False|Closed|
|desc|string|False|Description about board|
|id|string|False|The id of board|
|idOrganization|string|False|The id of organization|
|labelNames|object|False|Label names|
|members|[]object|False|List all members on board|
|name|string|False|Name of board|
|pinned|boolean|False|Pinned|
|prefs|object|False|Prefs|
|shortUrl|string|False|Short URL|
|url|string|False|URL|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 3.0.0 - Update spec titles and descriptions for AcronymValidator to pass
* 2.0.2 - New spec and help.md format for the Hub
* 2.0.1 - Remove erroneous data from plugin spec
* 2.0.0 - Update to new secret key credential type
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Trello](https://trello.com)
* [Trello API](https://developers.trello.com/advanced-reference)
* [Trello Business Class](https://trello.com/business-class)

