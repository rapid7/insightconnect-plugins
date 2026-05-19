# Requirements Document

## Introduction

Microsoft Teams v2 is a next-generation InsightConnect plugin that replaces the existing Microsoft Teams plugin (v1). The v2 plugin uses Azure Bot Service for authentication instead of user-delegated OAuth, eliminating MFA requirements, per-user license costs, and customer friction. It communicates with Microsoft Teams via the Bot Framework and Microsoft Graph API using application-level permissions with least privilege. The plugin replicates all existing v1 actions (messaging, team/channel management, member management) and introduces a new interactive messaging capability that sends Adaptive Card messages with clickable answer buttons, returning the user's selection as plugin output.

## Glossary

- **Plugin**: An InsightConnect integration component that connects to a third-party service
- **Bot_Service**: Azure Bot Service registration that provides application-identity-based access to Microsoft Teams without user credentials
- **Graph_API**: Microsoft Graph REST API v1.0 used for team, channel, and membership operations
- **Bot_Framework**: Microsoft Bot Framework SDK/protocol used for sending and receiving messages in Teams channels and chats
- **Adaptive_Card**: A JSON-based card format supported by Microsoft Teams that renders interactive UI elements including buttons, text inputs, and choice sets
- **Application_Permission**: Microsoft Graph permission granted to the application identity (not delegated to a user), enabling service-to-service calls
- **Proactive_Message**: A message sent by the bot to a Teams channel or chat without a prior user message, using a stored conversation reference
- **Conversation_Reference**: A Bot Framework object containing the service URL, conversation ID, and tenant information needed to send proactive messages
- **Webhook_Endpoint**: An HTTPS endpoint exposed by the plugin to receive Bot Framework activity callbacks (message responses, card submissions)
- **InsightConnect_Orchestrator**: The InsightConnect platform runtime that executes plugin actions and triggers within workflows

## Requirements

### Requirement 1: Bot-Based Connection

**User Story:** As a security operations engineer, I want to connect the plugin using an Azure Bot registration, so that I do not need to provide user credentials or deal with MFA prompts.

#### Acceptance Criteria

1. THE Plugin SHALL authenticate to Microsoft Teams using an Azure Bot Service application identity with the following required connection inputs: application ID, tenant (directory) ID, bot ID, client secret, and endpoint environment selection
2. WHEN a connection is configured, THE Plugin SHALL validate the credentials by requesting an access token from the Microsoft identity platform token endpoint using the OAuth 2.0 client credentials grant flow, with a request timeout of 120 seconds
3. THE Plugin SHALL support the following endpoint environments: Normal (commercial), GCC, GCC High, and DoD, each resolving to the corresponding Microsoft login and Graph resource URLs
4. THE Plugin SHALL NOT require user credentials (username and password) for any operation
5. IF the token request returns an HTTP error response, THEN THE Plugin SHALL return a ConnectionTestException that includes the HTTP status code and the error description returned by the identity platform
6. IF the token request fails due to a network error or timeout, THEN THE Plugin SHALL return a ConnectionTestException indicating the connection to the token endpoint could not be established
7. WHILE the Plugin is performing operations, THE Plugin SHALL refresh the access token when the current token is within 300 seconds of expiry, before making the next API call

### Requirement 2: Least Privilege Permissions

**User Story:** As a security administrator, I want the plugin to request only the minimum Graph API permissions needed, so that I can approve the app registration with confidence.

#### Acceptance Criteria

1. THE Plugin SHALL use only the following application permissions for messaging operations: ChannelMessage.Send, ChatMessage.Send, Chat.ReadWrite.All
2. THE Plugin SHALL use only the following application permissions for team and channel management: Team.ReadBasic.All, Channel.ReadBasic.All, Channel.Create, Channel.Delete.All
3. THE Plugin SHALL use only the following application permissions for membership operations: TeamMember.ReadWrite.All, ChannelMember.ReadWrite.All, Group.ReadWrite.All
4. THE Plugin SHALL NOT use delegated permissions for any operation
5. THE Plugin SHALL document all required permissions in the plugin help file, stating for each permission which plugin action or actions depend on it
6. IF a required permission has not been granted to the application, THEN THE Plugin SHALL return a PluginException indicating the missing permission name and the operation that requires it

### Requirement 3: Send Message to Channel

**User Story:** As a workflow author, I want to send a plain text message to a Teams channel, so that I can notify teams about security events.

#### Acceptance Criteria

1. WHEN a team name, channel name, and message body (maximum 28 KB) are provided, THE Plugin SHALL resolve the team and channel to their respective IDs and send the message body as plain text to that channel
2. WHEN a thread ID is provided alongside a channel or chat destination, THE Plugin SHALL send the message as a reply to the specified thread within that destination
3. WHEN a chat ID is provided instead of team and channel names, THE Plugin SHALL send the message to the specified chat
4. THE Plugin SHALL return the created message object including the message ID, timestamp, and web URL
5. IF the specified team or channel does not exist, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the missing resource
6. IF the specified chat ID does not exist or the specified thread ID does not exist, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the missing resource
7. IF neither team and channel names nor a chat ID are provided, THEN THE Plugin SHALL raise a PluginException indicating that a message destination is required

### Requirement 4: Send HTML Message

**User Story:** As a workflow author, I want to send HTML-formatted messages to a Teams channel, so that I can include rich formatting in notifications.

#### Acceptance Criteria

1. WHEN a team name, channel name, and HTML content of 200,000 characters or fewer are provided, THE Plugin SHALL resolve the team and channel to their respective IDs and send the HTML content as a message with contentType set to html
2. WHEN a thread ID is provided, THE Plugin SHALL send the HTML message as a reply to the specified thread
3. WHEN a chat ID is provided instead of team and channel names, THE Plugin SHALL send the HTML message to the specified chat
4. THE Plugin SHALL return the created message object including the message ID, timestamp, and web URL
5. IF the specified team or channel does not exist, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the missing resource

### Requirement 5: Send Message by GUID

**User Story:** As a workflow author, I want to send a message using team and channel GUIDs directly, so that I can avoid name-resolution overhead in high-volume workflows.

#### Acceptance Criteria

1. WHEN a team GUID, channel GUID, and message content are provided, THE Plugin SHALL send the message to the specified channel without performing name resolution
2. WHEN a boolean is_html flag is set to true, THE Plugin SHALL send the message content with contentType html; WHEN the flag is set to false or omitted, THE Plugin SHALL send the message content with contentType text
3. WHEN a thread ID is provided, THE Plugin SHALL send the message as a reply to the specified thread
4. THE Plugin SHALL return the created message object including the message ID, timestamp, and web URL
5. IF the specified team GUID or channel GUID does not correspond to an existing resource, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the invalid GUID

### Requirement 6: Send Interactive Message with Buttons

**User Story:** As a workflow author, I want to send a message with multiple answer buttons to a Teams channel, so that a human can click a response and the selection flows back into the workflow as plugin output.

#### Acceptance Criteria

1. WHEN a question text and a list of 2 to 10 button labels are provided, THE Plugin SHALL send an Adaptive Card to the specified channel or chat containing the question and one button per label
2. WHILE waiting for a button response, THE Plugin SHALL block the action for up to a configurable timeout period (default 300 seconds, minimum 30 seconds, maximum 3600 seconds) before resolving the output
3. WHEN a user clicks a button, THE Plugin SHALL return the selected button label, the responding user's display name, and the responding user's ID as action output
4. IF the timeout expires without a response, THEN THE Plugin SHALL return a timed_out boolean set to true and an empty string for the selection value
5. THE Plugin SHALL accept an optional message header (maximum 200 characters) and optional message body text (maximum 1000 characters) displayed above the buttons
6. WHEN multiple users have access to the card, THE Plugin SHALL accept only the first response and ignore subsequent clicks
7. IF the provided list of button labels contains fewer than 2 or more than 10 items, THEN THE Plugin SHALL raise a PluginException indicating the label count is outside the allowed range

### Requirement 7: Get Teams

**User Story:** As a workflow author, I want to list teams visible to the bot, so that I can discover team IDs for use in other actions.

#### Acceptance Criteria

1. THE Plugin SHALL return all teams that the bot application has access to as an array of team objects, each containing display name, ID, and description
2. WHEN an optional team name filter is provided, THE Plugin SHALL treat the filter as a regular expression and return only the first team whose display name matches the pattern using a substring search
3. IF the team name filter is provided and no team's display name matches the filter, THEN THE Plugin SHALL raise a PluginException indicating the team was not found
4. IF the team name filter is an invalid regular expression, THEN THE Plugin SHALL raise a PluginException indicating the filter pattern is invalid

### Requirement 8: Get Channels for Team

**User Story:** As a workflow author, I want to list channels in a team, so that I can discover channel IDs for use in other actions.

#### Acceptance Criteria

1. WHEN a team name is provided, THE Plugin SHALL resolve the team by display name and return all channels in that team as an array, where each channel includes display name, ID, and description
2. WHEN an optional channel name filter is provided, THE Plugin SHALL treat the filter as a regular expression and return only the first channel whose display name matches the regex pattern
3. IF the specified team name does not match any team, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the team that was not found
4. IF the channel name filter matches no channels in the team, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the filter and team
5. IF the channel name filter is not a valid regular expression, THEN THE Plugin SHALL raise a PluginException indicating the invalid regex pattern

### Requirement 9: Add Member to Team

**User Story:** As a security operations engineer, I want to add a user to a team, so that I can automate team membership provisioning during incident response.

#### Acceptance Criteria

1. WHEN a team name and member email are provided, THE Plugin SHALL resolve the team by display name, resolve the user by email address, and add the user as a member of the specified team
2. WHEN the member is successfully added, THE Plugin SHALL return a boolean success indicator set to true
3. IF the user is already a member of the team, THEN THE Plugin SHALL return success set to true without raising an error
4. IF the specified team name does not match any existing team, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the team as not found
5. IF the specified member email does not resolve to a valid user in the directory, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the user as not found

### Requirement 10: Remove Member from Team

**User Story:** As a security operations engineer, I want to remove a user from a team, so that I can automate access revocation during offboarding or incident containment.

#### Acceptance Criteria

1. WHEN a team name and member email are provided, THE Plugin SHALL resolve the team by display name, resolve the user by email address, and remove the user from the specified team
2. WHEN the member is successfully removed, THE Plugin SHALL return a boolean success indicator set to true
3. IF the user is not a member of the team, THEN THE Plugin SHALL raise a PluginException indicating the user was not found in the team membership
4. IF the specified team name does not match any existing team, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the team as not found
5. IF the specified member email does not resolve to a valid user in the directory, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the user as not found

### Requirement 11: Add Channel to Team

**User Story:** As a workflow author, I want to create a new channel in a team, so that I can set up dedicated channels for incidents automatically.

#### Acceptance Criteria

1. WHEN a team name, channel name (maximum 50 characters), and channel description (maximum 1024 characters) are provided, THE Plugin SHALL create a new channel in the specified team
2. THE Plugin SHALL accept a channel type parameter with values Standard or Private, defaulting to Standard when not specified
3. THE Plugin SHALL return a boolean success indicator set to true when the channel is created
4. IF a channel with the same name already exists in the team, THEN THE Plugin SHALL raise a PluginException indicating the conflict
5. IF the specified team does not exist, THEN THE Plugin SHALL raise a PluginException identifying the team that was not found

### Requirement 12: Remove Channel from Team

**User Story:** As a workflow author, I want to delete a channel from a team, so that I can clean up temporary incident channels after resolution.

#### Acceptance Criteria

1. WHEN a team name and channel name are provided, THE Plugin SHALL delete the specified channel from the team
2. THE Plugin SHALL return a boolean success indicator
3. IF the channel does not exist in the specified team, THEN THE Plugin SHALL raise a PluginException indicating the channel was not found
4. IF the specified team does not exist, THEN THE Plugin SHALL raise a PluginException indicating the team was not found
5. IF the specified channel cannot be deleted because it is the General channel, THEN THE Plugin SHALL raise a PluginException indicating that the General channel cannot be deleted

### Requirement 13: Create Teams-Enabled Group

**User Story:** As a security operations engineer, I want to create a new team (with underlying Azure AD group), so that I can spin up collaboration spaces for new projects or incidents.

#### Acceptance Criteria

1. WHEN a group name (1 to 256 characters), description (up to 1024 characters), mail nickname (up to 64 characters, alphanumeric and hyphens only), and mail-enabled flag are provided, THE Plugin SHALL create an Azure AD group with Teams enabled via the Graph API
2. WHEN optional owner and member lists are provided as email addresses, THE Plugin SHALL assign those users as owners and members of the new group
3. THE Plugin SHALL return the created group object including ID, display name, mail, and creation timestamp
4. IF the group creation fails due to a conflict such as a duplicate mail nickname, THEN THE Plugin SHALL raise a PluginException indicating the conflict
5. IF a specified owner or member email does not resolve to a valid user in the directory, THEN THE Plugin SHALL raise a PluginException identifying the invalid user

### Requirement 14: Delete Team

**User Story:** As a security operations engineer, I want to delete a team, so that I can remove collaboration spaces that are no longer needed.

#### Acceptance Criteria

1. WHEN a team name is provided, THE Plugin SHALL resolve the team name to its group ID and delete the associated Microsoft 365 group (which deletes the team and Azure AD group)
2. WHEN the deletion succeeds, THE Plugin SHALL return a boolean success indicator set to true
3. IF the team does not exist, THEN THE Plugin SHALL raise a PluginException indicating the team was not found
4. IF multiple teams match the provided team name, THEN THE Plugin SHALL raise a PluginException indicating that the team name is ambiguous and multiple matches were found
5. IF the Graph API returns an error other than not found, THEN THE Plugin SHALL raise a PluginException with the HTTP status code and a descriptive error message indicating the failure reason

### Requirement 15: Add Group Owner

**User Story:** As a workflow author, I want to add an owner to a team's underlying group, so that I can delegate team administration.

#### Acceptance Criteria

1. WHEN a group name and member email are provided, THE Plugin SHALL add the user as an owner of the group
2. THE Plugin SHALL return a boolean success indicator
3. IF the specified group does not exist, THEN THE Plugin SHALL raise a PluginException indicating the group was not found
4. IF the specified user is already an owner of the group, THEN THE Plugin SHALL return success without raising an error
5. IF the specified user cannot be resolved from the provided email, THEN THE Plugin SHALL raise a PluginException indicating the user was not found

### Requirement 16: Add Member to Channel

**User Story:** As a workflow author, I want to add a member to a private channel, so that I can grant access to restricted channels during incident response.

#### Acceptance Criteria

1. WHEN a group name, channel name, member email, and role are provided, THE Plugin SHALL resolve the group and channel by name, resolve the user by email, and add the user to the private channel with the specified role (Owner or Member)
2. THE Plugin SHALL return a boolean success indicator
3. IF the specified group, channel, or user does not exist, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the missing resource
4. IF the user is already a member of the channel, THEN THE Plugin SHALL return success without raising an error

### Requirement 17: Get Message in Channel

**User Story:** As a workflow author, I want to retrieve a specific message from a channel, so that I can inspect message content in automated workflows.

#### Acceptance Criteria

1. WHEN a team ID, channel ID, and message ID are provided, THE Plugin SHALL return the message object including body (content and content type), sender (display name and user ID), created date time, last modified date time, attachments, mentions, reactions, message ID, and web URL
2. WHEN an optional reply ID is provided in addition to team ID, channel ID, and message ID, THE Plugin SHALL return the specific reply message instead of the parent message
3. IF the specified team ID, channel ID, or message ID does not correspond to an existing resource, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the resource that was not found
4. IF a reply ID is provided but does not correspond to an existing reply under the specified message, THEN THE Plugin SHALL raise a PluginException with cause and assistance text indicating the reply was not found

### Requirement 18: Get Message in Chat

**User Story:** As a workflow author, I want to retrieve a specific message from a chat, so that I can process chat messages in automated workflows.

#### Acceptance Criteria

1. WHEN a chat ID and message ID are provided, THE Plugin SHALL return the message object including body content, body content type, sender display name, sender user ID, created timestamp, last modified timestamp, attachments, mentions, and reactions
2. IF the specified chat ID does not exist or the bot does not have access to the chat, THEN THE Plugin SHALL raise a PluginException with cause and assistance text indicating the chat was not found or not accessible
3. IF the specified message ID does not exist within the chat, THEN THE Plugin SHALL raise a PluginException with cause and assistance text indicating the message was not found

### Requirement 19: Get Reply List

**User Story:** As a workflow author, I want to list all replies to a channel message, so that I can process threaded conversations in workflows.

#### Acceptance Criteria

1. WHEN a team name, channel name, and message ID are provided, THE Plugin SHALL resolve the team and channel to their respective IDs and return up to 50 reply messages for the specified parent message
2. THE Plugin SHALL return each reply as a full message object including body, sender, timestamps, attachments, mentions, and reactions
3. IF the specified team, channel, or message ID does not exist, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the missing resource
4. WHEN the parent message has no replies, THE Plugin SHALL return an empty list

### Requirement 20: List Messages in Chat

**User Story:** As a workflow author, I want to retrieve recent messages from a chat, so that I can process chat history in workflows.

#### Acceptance Criteria

1. WHEN a chat ID is provided, THE Plugin SHALL return up to the last 50 messages in the chat ordered from most recent to oldest
2. THE Plugin SHALL return each message as a full message object including body, sender, timestamps, attachments, mentions, and reactions
3. IF the specified chat ID does not exist or is not accessible, THEN THE Plugin SHALL raise a PluginException with cause and assistance text identifying the inaccessible chat

### Requirement 21: Create Teams Chat

**User Story:** As a workflow author, I want to create a new chat conversation, so that I can initiate direct or group chats programmatically.

#### Acceptance Criteria

1. WHEN a list of at least 2 and at most 250 members identified by email address with roles (Owner or Guest) is provided, THE Plugin SHALL create a new chat with those members, where 2 members creates a oneOnOne chat and 3 or more members creates a group chat
2. WHEN an optional topic of up to 250 characters is provided and the chat type is group, THE Plugin SHALL set the topic on the created group chat
3. THE Plugin SHALL return the created chat object including chat ID, chat type (oneOnOne or group), creation timestamp, and web URL
4. IF any specified member email address cannot be resolved to a valid Teams user, THEN THE Plugin SHALL raise a PluginException identifying the unresolved member
5. IF a topic is provided and the chat type is oneOnOne, THEN THE Plugin SHALL ignore the topic and create the chat without it

### Requirement 22: New Message Received Trigger

**User Story:** As a workflow author, I want to trigger a workflow when a new message is posted in a Teams channel, so that I can build chat-driven automation.

#### Acceptance Criteria

1. WHEN a new message is posted in the configured team and channel, THE Plugin SHALL emit a trigger event containing the message object including message ID, body content, body content type, sender display name, sender ID, created date time, web URL, importance, message type, locale, and channel identity
2. WHEN an optional message content regex is configured, THE Plugin SHALL emit events only for messages whose plain-text content (with HTML tags stripped) matches the regex pattern
3. IF the configured message content regex is invalid, THEN THE Plugin SHALL raise a PluginException indicating the invalid regular expression and the pattern that failed compilation
4. THE Plugin SHALL extract security indicators from the message body and include them in the trigger output: domains, URLs, email addresses, IPv4 addresses, IPv6 addresses, MD5 hashes, SHA1 hashes, SHA256 hashes, MAC addresses, CVEs, and UUIDs, each as a deduplicated list
5. THE Plugin SHALL include the channel name and team name in every trigger output regardless of whether a message content regex is configured
6. THE Plugin SHALL extract the first word (first whitespace-delimited token after stripping HTML tags) and a word list (all whitespace-delimited tokens after stripping HTML tags) from the message body and include them in the message object
7. IF the configured team or channel cannot be resolved by name, THEN THE Plugin SHALL raise a PluginException identifying the team or channel that was not found

### Requirement 23: Webhook Endpoint for Bot Callbacks

**User Story:** As a platform engineer, I want the plugin to expose a webhook endpoint for Bot Framework callbacks, so that interactive card responses and message events can be received.

#### Acceptance Criteria

1. THE Plugin SHALL expose an HTTPS webhook endpoint that accepts Bot Framework Activity objects and returns HTTP 200 within 5 seconds of receiving the request
2. WHEN an Activity of type invoke with name adaptiveCard/action is received and a matching interactive message action is waiting, THE Plugin SHALL extract the card action data, route it to the waiting action, and return an invoke response with status code 200
3. IF an Activity of type invoke is received and no matching interactive message action is waiting, THEN THE Plugin SHALL return an invoke response with status code 200 and discard the activity
4. WHEN an Activity of type message is received and a new message trigger is configured for the source channel, THE Plugin SHALL route the message to the new message trigger
5. IF an Activity is received with a type other than invoke or message, THEN THE Plugin SHALL return HTTP 200 and take no further action
6. THE Plugin SHALL validate the Bot Framework authentication token on all incoming requests using the Bot Connector authentication protocol
7. IF the authentication token is invalid or missing, THEN THE Plugin SHALL reject the request with HTTP 401 and not process the activity

### Requirement 24: Customer Setup Documentation

**User Story:** As a customer, I want clear documentation on how to register the Azure Bot and configure permissions, so that I can set up the plugin without support assistance.

#### Acceptance Criteria

1. THE Plugin SHALL include a help.md file documenting the Azure Bot registration process as a numbered sequence of steps covering: creating the Azure Bot resource, obtaining the application ID and client secret, configuring the messaging endpoint, assigning Microsoft Graph permissions, and granting admin consent
2. THE Plugin SHALL document all required Microsoft Graph application permissions (as defined in Requirement 2) with the purpose of each permission
3. THE Plugin SHALL document the Bot Framework messaging endpoint URL that must be configured in the Azure Bot registration
4. THE Plugin SHALL document the process for granting admin consent for the application permissions
5. THE Plugin SHALL include troubleshooting guidance for the following setup failures: token errors, permission errors, and bot not responding in channels, where each failure entry includes the observable symptom, the likely cause, and a resolution action
6. THE Plugin SHALL document the prerequisites required before beginning setup, including the required Azure AD role (Global Administrator or Application Administrator) and an active Azure subscription
7. THE Plugin SHALL document how to configure the InsightConnect plugin connection using the credentials obtained during Azure Bot registration, including the application ID, bot ID, client secret, and the selection of the appropriate endpoint environment (Normal, GCC, GCC High, or DoD)
