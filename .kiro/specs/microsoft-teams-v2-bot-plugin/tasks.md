# Implementation Plan: Microsoft Teams v2 Bot Plugin

## Overview

This plan implements the Microsoft Teams v2 InsightConnect plugin from scratch. The plugin uses Azure Bot Service for authentication (client credentials grant), communicates via Microsoft Graph API v1.0 and Bot Framework, and supports commercial, GCC, GCC High, and DoD environments. Implementation follows the insightconnect-plugins monorepo conventions with `plugin.spec.yaml` as the source of truth, `insight-plugin` tooling for scaffolding, and Python 3.11 with the `insightconnect-plugin-runtime` SDK.

## Tasks

- [ ] 1. Create plugin.spec.yaml and scaffold project structure
  - [ ] 1.1 Write the complete plugin.spec.yaml defining connection, all 19 actions, 1 trigger, custom types, and metadata
    - Define connection inputs: application_id, directory_id, bot_id, application_secret (credential_secret_key), endpoint (enum: Normal, GCC, GCC High, DoD)
    - Define all custom types: team, channel, chatMessage, itemBody, from, channelIdentity, indicators, hashes, ip_addresses, group, interactiveMessageResponse, chatMessageReaction
    - Define all 19 actions with inputs, outputs, and example values
    - Define the new_message_received trigger with inputs and outputs
    - Set vendor/support to rapid7, version to 1.0.0, supported_versions to ["Microsoft Graph API v1.0"]
    - _Requirements: 1.1, 1.3, 2.1, 2.2, 2.3, 3.1-3.7, 4.1-4.5, 5.1-5.5, 6.1-6.7, 7.1-7.4, 8.1-8.5, 9.1-9.5, 10.1-10.5, 11.1-11.5, 12.1-12.5, 13.1-13.5, 14.1-14.5, 15.1-15.5, 16.1-16.4, 17.1-17.4, 18.1-18.3, 19.1-19.4, 20.1-20.3, 21.1-21.5, 22.1-22.7_

  - [ ] 1.2 Run insight-plugin create to scaffold the project directory structure
    - Execute `PYENV_VERSION=3.11.12 insight-plugin create` from the plugins directory
    - Verify generated folder structure under `plugins/microsoft_teams_v2/`
    - _Requirements: 24.1_

  - [ ] 1.3 Create requirements.txt with pinned dependencies
    - Add `hypothesis==6.92.2` for property-based testing
    - Add `PyJWT==2.8.0` for Bot Framework token validation
    - Add `cryptography==41.0.7` for JWT signature verification
    - Do NOT add `requests` (included in SDK transitively)
    - _Requirements: 1.2, 23.6_

  - [ ] 1.4 Create util/constants.py with environment endpoint maps and shared constants
    - Define ENDPOINT_MAP with login URLs and Graph resource URLs for Normal, GCC, GCC High, DoD
    - Define TIMEOUT = 120 for token requests
    - Define HTTP_ERROR_MAP with cause/assistance for 400, 401, 403, 404, 409, 429, 500, 503
    - Define TOKEN_REFRESH_BUFFER = 300
    - Define INTERACTIVE_TIMEOUT_MIN = 30, INTERACTIVE_TIMEOUT_MAX = 3600, INTERACTIVE_TIMEOUT_DEFAULT = 300
    - Define BUTTON_COUNT_MIN = 2, BUTTON_COUNT_MAX = 10
    - _Requirements: 1.3, 1.5, 1.7, 6.2, 6.7_

- [ ] 2. Implement connection and token management
  - [ ] 2.1 Implement util/token_manager.py
    - Implement TokenManager class with __init__(app_id, app_secret, tenant_id, endpoint_env, logger)
    - Implement get_token() that returns cached token or refreshes when within 300s of expiry
    - Implement _request_token() that performs client_credentials grant POST to the environment-specific token endpoint
    - Raise ConnectionTestException on HTTP errors with status code and error description
    - Raise ConnectionTestException on network errors/timeouts
    - _Requirements: 1.2, 1.5, 1.6, 1.7_

  - [ ]* 2.2 Write property test for token refresh decision boundary
    - **Property 1: Token refresh decision boundary**
    - **Validates: Requirements 1.7**
    - Use hypothesis to generate random (current_time, expires_at) pairs
    - Assert get_token() refreshes iff expires_at - current_time <= 300

  - [ ] 2.3 Implement connection/connection.py
    - Implement connect() to store parameters, initialize TokenManager, GraphClient, BotClient
    - Implement test() to call token_manager.get_token() and verify success
    - Convert PluginException to ConnectionTestException in test()
    - Strip all string credential inputs
    - _Requirements: 1.1, 1.2, 1.4, 1.5, 1.6_

  - [ ]* 2.4 Write unit tests for connection (test_connection.py)
    - Test successful token acquisition
    - Test auth failure (invalid credentials)
    - Test network timeout
    - Test each environment endpoint URL resolution
    - _Requirements: 1.1, 1.2, 1.3, 1.5, 1.6_

- [ ] 3. Checkpoint - Ensure connection tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 4. Implement Graph API client and name resolution utilities
  - [ ] 4.1 Implement util/graph_client.py
    - Implement GraphClient class with requests.Session
    - Implement _make_request(method, endpoint, **kwargs) with Bearer token from TokenManager
    - Implement _handle_status() mapping HTTP codes to PluginException with cause/assistance
    - Implement 401-retry pattern (refresh token once, retry request)
    - Implement pagination via @odata.nextLink
    - Implement all team, channel, member, message, and chat methods per design interface
    - _Requirements: 2.6, 3.1, 3.4, 3.5, 7.1, 8.1, 9.1, 10.1, 11.1, 12.1, 13.1, 14.1, 15.1, 16.1, 17.1, 18.1, 19.1, 20.1, 21.1_

  - [ ]* 4.2 Write property test for error response context inclusion
    - **Property 2: Error responses include identifying context**
    - **Validates: Requirements 1.5, 2.6, 3.5, 5.5**
    - Use hypothesis to generate random HTTP status codes and error body strings
    - Assert resulting exception contains both status code and error description

  - [ ] 4.3 Implement util/name_resolver.py
    - Implement resolve_team(team_name) using GraphClient.list_teams with regex filter
    - Implement resolve_channel(team_id, channel_name) using GraphClient.list_channels with regex filter
    - Implement resolve_user(email) using GraphClient.resolve_user_by_email
    - Raise PluginException with cause/assistance when resource not found
    - _Requirements: 3.1, 3.5, 7.2, 7.3, 8.2, 8.3, 9.1, 9.4, 9.5, 10.1, 10.4, 10.5_

  - [ ]* 4.4 Write property test for regex name filter
    - **Property 7: Regex name filter returns first matching resource**
    - **Validates: Requirements 7.2, 7.3, 8.2, 8.4**
    - Use hypothesis to generate lists of display names and valid regex patterns
    - Assert filter returns first resource whose name contains a substring match

  - [ ]* 4.5 Write property test for invalid regex detection
    - **Property 8: Invalid regex pattern raises PluginException**
    - **Validates: Requirements 7.4, 8.5, 22.3**
    - Use hypothesis to generate strings with unbalanced brackets and invalid escapes
    - Assert PluginException is raised indicating invalid pattern

- [ ] 5. Implement Bot Framework client and webhook handler
  - [ ] 5.1 Implement util/bot_client.py
    - Implement BotClient class with send_to_channel, send_to_chat, send_adaptive_card methods
    - Construct Bot Framework conversation references from team/channel/chat IDs
    - Use Bot Framework REST API to send activities
    - Support plain text and HTML content types
    - Support thread replies via replyToId
    - _Requirements: 3.1, 3.2, 3.3, 4.1, 4.2, 4.3, 5.1, 5.3, 6.1_

  - [ ]* 5.2 Write property test for content type flag
    - **Property 3: Content type flag controls message payload**
    - **Validates: Requirements 5.2**
    - Use hypothesis to generate random content strings and boolean is_html flags
    - Assert payload contentType is "html" when is_html=True, "text" otherwise

  - [ ] 5.3 Implement util/webhook_handler.py
    - Implement handle_activity() to route by Activity type (invoke, message)
    - Implement register_card_waiter(card_id, callback) for interactive message blocking
    - Implement register_message_trigger(channel_id, callback) for new message trigger
    - Implement validate_auth_token() using Bot Connector JWT validation
    - Return HTTP 200 for all valid activities, HTTP 401 for invalid auth
    - _Requirements: 23.1, 23.2, 23.3, 23.4, 23.5, 23.6, 23.7_

  - [ ] 5.4 Implement util/adaptive_card_builder.py
    - Implement build_card(question, buttons, header=None, body_text=None) returning Adaptive Card JSON
    - Generate unique card_id for each card
    - Include Action.Execute elements with selection data per button label
    - Validate button count [2, 10] and raise PluginException if out of range
    - _Requirements: 6.1, 6.5, 6.7_

  - [ ]* 5.5 Write property test for Adaptive Card payload structure
    - **Property 4: Adaptive Card payload structure matches inputs**
    - **Validates: Requirements 6.1**
    - Use hypothesis to generate question strings and lists of 2-10 button labels
    - Assert card contains exactly one question TextBlock and N Action.Execute elements matching labels

  - [ ]* 5.6 Write property test for timeout range validation
    - **Property 5: Timeout range validation**
    - **Validates: Requirements 6.2**
    - Use hypothesis to generate random integers
    - Assert acceptance iff value in [30, 3600], PluginException otherwise

  - [ ]* 5.7 Write property test for button label count validation
    - **Property 6: Button label count validation**
    - **Validates: Requirements 6.7**
    - Use hypothesis to generate random string lists of varying length
    - Assert acceptance iff length in [2, 10], PluginException otherwise

- [ ] 6. Checkpoint - Ensure utility tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 7. Implement messaging actions
  - [ ] 7.1 Implement actions/send_message/action.py
    - Resolve team/channel by name OR accept chat_id
    - Validate that at least one destination is provided
    - Support optional thread_id for replies
    - Return message object with id, timestamp, webUrl
    - Raise PluginException for missing destination, not-found resources
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7_

  - [ ] 7.2 Implement actions/send_html_message/action.py
    - Resolve team/channel by name OR accept chat_id
    - Send with contentType html
    - Support optional thread_id for replies
    - Validate HTML content <= 200,000 characters
    - Return message object with id, timestamp, webUrl
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5_

  - [ ] 7.3 Implement actions/send_message_by_guid/action.py
    - Accept team_guid, channel_guid directly (no name resolution)
    - Use is_html boolean flag to set contentType
    - Support optional thread_id for replies
    - Return message object with id, timestamp, webUrl
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_

  - [ ] 7.4 Implement actions/send_interactive_message/action.py
    - Build Adaptive Card from question + button labels
    - Validate timeout in [30, 3600], button count in [2, 10]
    - Register card waiter with webhook handler
    - Block until response received or timeout expires
    - Return interactiveMessageResponse (answer, user_name, user_id, timed_out)
    - Accept only first response, ignore subsequent clicks
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7_

  - [ ]* 7.5 Write unit tests for messaging actions
    - Test send_message with team/channel, with chat_id, with thread_id, missing destination
    - Test send_html_message with valid HTML, oversized content
    - Test send_message_by_guid with is_html true/false
    - Test send_interactive_message with valid buttons, timeout, first-response-only
    - _Requirements: 3.1-3.7, 4.1-4.5, 5.1-5.5, 6.1-6.7_

- [ ] 8. Implement team and channel management actions
  - [ ] 8.1 Implement actions/get_teams/action.py
    - List all teams accessible to the bot
    - Apply optional regex name filter (substring match, return first match)
    - Raise PluginException for no match or invalid regex
    - Return array of team objects (displayName, id, description)
    - _Requirements: 7.1, 7.2, 7.3, 7.4_

  - [ ] 8.2 Implement actions/get_channels/action.py
    - Resolve team by name, list channels
    - Apply optional regex channel name filter
    - Raise PluginException for team not found, no channel match, invalid regex
    - Return array of channel objects
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_

  - [ ] 8.3 Implement actions/add_channel_to_team/action.py
    - Resolve team by name, create channel with name (max 50 chars), description (max 1024 chars), type (Standard/Private)
    - Raise PluginException for team not found, channel name conflict
    - Return boolean success
    - _Requirements: 11.1, 11.2, 11.3, 11.4, 11.5_

  - [ ] 8.4 Implement actions/remove_channel_from_team/action.py
    - Resolve team and channel by name, delete channel
    - Raise PluginException for team not found, channel not found, General channel deletion attempt
    - Return boolean success
    - _Requirements: 12.1, 12.2, 12.3, 12.4, 12.5_

  - [ ] 8.5 Implement actions/create_teams_enabled_group/action.py
    - Create Azure AD group with Teams enabled via Graph API
    - Accept group name (1-256 chars), description (up to 1024), mail_nickname (up to 64, alphanumeric+hyphens), mail_enabled flag
    - Assign optional owners and members by email
    - Return group object (id, displayName, mail, createdDateTime)
    - _Requirements: 13.1, 13.2, 13.3, 13.4, 13.5_

  - [ ] 8.6 Implement actions/delete_team/action.py
    - Resolve team name to group ID, delete M365 group
    - Raise PluginException for not found, ambiguous name (multiple matches), other API errors
    - Return boolean success
    - _Requirements: 14.1, 14.2, 14.3, 14.4, 14.5_

  - [ ]* 8.7 Write unit tests for team and channel management actions
    - Test get_teams with/without filter, no match, invalid regex
    - Test get_channels with/without filter, team not found
    - Test add/remove channel, create group, delete team — happy path and error cases
    - _Requirements: 7.1-7.4, 8.1-8.5, 11.1-11.5, 12.1-12.5, 13.1-13.5, 14.1-14.5_

- [ ] 9. Implement membership management actions
  - [ ] 9.1 Implement actions/add_member_to_team/action.py
    - Resolve team by name, resolve user by email, add membership
    - Return success=true (including if already a member)
    - Raise PluginException for team not found, user not found
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.5_

  - [ ] 9.2 Implement actions/remove_member_from_team/action.py
    - Resolve team by name, resolve user by email, remove membership
    - Return success=true
    - Raise PluginException for team not found, user not found, user not a member
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5_

  - [ ] 9.3 Implement actions/add_group_owner/action.py
    - Resolve group by name, resolve user by email, add as owner
    - Return success (including if already an owner)
    - Raise PluginException for group not found, user not found
    - _Requirements: 15.1, 15.2, 15.3, 15.4, 15.5_

  - [ ] 9.4 Implement actions/add_member_to_channel/action.py
    - Resolve group, channel, and user by name/email
    - Add user to private channel with specified role (Owner/Member)
    - Return success (including if already a member)
    - Raise PluginException for missing resources
    - _Requirements: 16.1, 16.2, 16.3, 16.4_

  - [ ]* 9.5 Write unit tests for membership actions
    - Test add/remove member, add owner, add channel member — happy path and error cases
    - Test idempotent behavior (already a member returns success)
    - _Requirements: 9.1-9.5, 10.1-10.5, 15.1-15.5, 16.1-16.4_

- [ ] 10. Checkpoint - Ensure action tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 11. Implement message retrieval actions
  - [ ] 11.1 Implement actions/get_message_in_channel/action.py
    - Accept team_id, channel_id, message_id, optional reply_id
    - Return full message object (body, sender, timestamps, attachments, mentions, reactions, webUrl)
    - Raise PluginException for not-found resources
    - _Requirements: 17.1, 17.2, 17.3, 17.4_

  - [ ] 11.2 Implement actions/get_message_in_chat/action.py
    - Accept chat_id, message_id
    - Return full message object
    - Raise PluginException for chat not found/not accessible, message not found
    - _Requirements: 18.1, 18.2, 18.3_

  - [ ] 11.3 Implement actions/get_reply_list/action.py
    - Resolve team and channel by name, accept message_id
    - Return up to 50 reply messages as full message objects
    - Return empty list when no replies exist
    - Raise PluginException for not-found resources
    - _Requirements: 19.1, 19.2, 19.3, 19.4_

  - [ ] 11.4 Implement actions/list_messages_in_chat/action.py
    - Accept chat_id, return up to 50 messages ordered most recent to oldest
    - Return each as full message object
    - Raise PluginException for chat not found/not accessible
    - _Requirements: 20.1, 20.2, 20.3_

  - [ ] 11.5 Implement actions/create_teams_chat/action.py
    - Accept list of 2-250 members with roles, optional topic
    - Set chatType to oneOnOne (2 members) or group (3+)
    - Include topic only for group chats, ignore for oneOnOne
    - Return chat object (id, chatType, createdDateTime, webUrl)
    - Raise PluginException for unresolved member emails
    - _Requirements: 21.1, 21.2, 21.3, 21.4, 21.5_

  - [ ]* 11.6 Write property test for chat type and topic determination
    - **Property 9: Chat type and topic determination**
    - **Validates: Requirements 21.1, 21.2, 21.5**
    - Use hypothesis to generate member lists (2-250) and optional topic strings
    - Assert chatType is oneOnOne when count=2, group when count>=3; topic included only for group

  - [ ]* 11.7 Write unit tests for message retrieval and chat actions
    - Test get_message_in_channel with/without reply_id, not found
    - Test get_message_in_chat, list_messages_in_chat
    - Test get_reply_list with replies and empty list
    - Test create_teams_chat with 2 members, 3+ members, topic handling
    - _Requirements: 17.1-17.4, 18.1-18.3, 19.1-19.4, 20.1-20.3, 21.1-21.5_

- [ ] 12. Implement new message trigger and indicator extraction
  - [ ] 12.1 Implement util/indicator_extractor.py
    - Implement extract_all(message_body) returning dict of deduplicated indicator lists
    - Extract: domains, URLs, email addresses, IPv4, IPv6, MD5, SHA1, SHA256, MAC addresses, CVEs, UUIDs
    - Strip HTML tags before extraction
    - Deduplicate each list
    - _Requirements: 22.4_

  - [ ]* 12.2 Write property test for security indicator extraction completeness
    - **Property 11: Security indicator extraction completeness**
    - **Validates: Requirements 22.4**
    - Use hypothesis to generate message bodies with embedded IOC patterns
    - Assert each IOC appears in its corresponding output list with no duplicates

  - [ ] 12.3 Implement util/message_utils.py
    - Implement strip_html(text) to remove HTML tags
    - Implement extract_first_word(stripped_text) returning first whitespace-delimited token
    - Implement extract_words(stripped_text) returning all whitespace-delimited tokens
    - _Requirements: 22.6_

  - [ ]* 12.4 Write property test for word extraction from message body
    - **Property 12: Word extraction from message body**
    - **Validates: Requirements 22.6**
    - Use hypothesis to generate random HTML strings
    - Assert first_word equals first token of stripped text, words equals all tokens

  - [ ] 12.5 Implement triggers/new_message_received/trigger.py
    - Register with webhook handler for configured channel
    - Apply optional message content regex filter (on stripped plain text)
    - Validate regex pattern on startup, raise PluginException if invalid
    - Extract indicators, first_word, words from message body
    - Include channel_name and team_name in every trigger output
    - Emit trigger event with full message object and indicators
    - _Requirements: 22.1, 22.2, 22.3, 22.4, 22.5, 22.6, 22.7_

  - [ ]* 12.6 Write property test for message content regex filtering
    - **Property 10: Message content regex filtering**
    - **Validates: Requirements 22.2**
    - Use hypothesis to generate message body strings and valid regex patterns
    - Assert trigger emits event iff stripped text contains a substring match for pattern

  - [ ]* 12.7 Write unit tests for trigger and indicator extraction
    - Test trigger with matching regex, non-matching regex, no regex configured
    - Test indicator extraction for each IOC type
    - Test word extraction with HTML content
    - Test invalid regex raises PluginException
    - _Requirements: 22.1-22.7_

- [ ] 13. Checkpoint - Ensure trigger and indicator tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 14. Write help.md documentation and finalize plugin
  - [ ] 14.1 Write help.md with Azure Bot setup documentation
    - Document Azure Bot registration process as numbered steps
    - Document all required Graph API permissions with purpose of each
    - Document Bot Framework messaging endpoint URL configuration
    - Document admin consent granting process
    - Document prerequisites (Azure AD role, Azure subscription)
    - Document InsightConnect connection configuration (app_id, bot_id, secret, environment)
    - Include troubleshooting guidance for token errors, permission errors, bot not responding
    - _Requirements: 24.1, 24.2, 24.3, 24.4, 24.5, 24.6, 24.7_

  - [ ] 14.2 Run insight-plugin validate and fix any issues
    - Execute `PYENV_VERSION=3.11.12 insight-plugin validate` from the plugin directory
    - Fix any schema validation, help.md sync, or Docker validation errors
    - Ensure all .py files have 644 permissions
    - _Requirements: All_

- [ ] 15. Final checkpoint - Ensure all tests pass and validation succeeds
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties from the design document (12 total)
- Unit tests validate specific examples and edge cases
- The plugin uses Python 3.11 with the `insightconnect-plugin-runtime` SDK
- All generated files (schema.py, setup.py, __init__.py, help.md, .CHECKSUM) must NOT be hand-edited
- `plugin.spec.yaml` is the source of truth — always edit it first, then run `insight-plugin refresh`
- Use `self.logger` for all logging, never `print()`
- Use `Output.FIELD_NAME` constants for all output keys
- Wrap API response data in `insightconnect_plugin_runtime.helper.clean()` before returning

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["1.2"] },
    { "id": 2, "tasks": ["1.3", "1.4"] },
    { "id": 3, "tasks": ["2.1", "2.3"] },
    { "id": 4, "tasks": ["2.2", "2.4"] },
    { "id": 5, "tasks": ["4.1", "5.1", "5.3", "5.4"] },
    { "id": 6, "tasks": ["4.2", "4.3", "5.2", "5.5", "5.6", "5.7"] },
    { "id": 7, "tasks": ["4.4", "4.5", "7.1", "7.2", "7.3", "7.4"] },
    { "id": 8, "tasks": ["7.5", "8.1", "8.2", "8.3", "8.4", "8.5", "8.6"] },
    { "id": 9, "tasks": ["8.7", "9.1", "9.2", "9.3", "9.4"] },
    { "id": 10, "tasks": ["9.5", "11.1", "11.2", "11.3", "11.4", "11.5"] },
    { "id": 11, "tasks": ["11.6", "11.7", "12.1", "12.3"] },
    { "id": 12, "tasks": ["12.2", "12.4", "12.5"] },
    { "id": 13, "tasks": ["12.6", "12.7"] },
    { "id": 14, "tasks": ["14.1"] },
    { "id": 15, "tasks": ["14.2"] }
  ]
}
```
