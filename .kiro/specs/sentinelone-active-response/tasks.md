# Implementation Plan: SentinelOne Active Response Plugin

## Overview

Build a single-action orchestrator plugin (`sentinelone_active_response`) that exposes one `execute_response` action. The action autonomously resolves an endpoint identifier, validates state, executes contain/uncontain/status/info operations against the SentinelOne API, monitors for confirmation, and returns a structured report. Implementation follows the standard plugin workflow: spec first, refresh, then hand-written code.

## Tasks

- [x] 1. Define plugin spec and generate scaffolding
  - [x] 1.1 Write plugin.spec.yaml with connection, execute_response action, and custom types
    - Define connection inputs (instance subdomain, api_key credential_secret_key)
    - Define execute_response action with inputs (endpoint_identifier, intent enum, timeout, polling_interval) and output (report of type response_report)
    - Define custom types: agent_details, response_report
    - Set version 1.0.0, sdk version 6.4.3, cloud_ready false, vendor rapid7
    - Add version_history, supported_versions, key_features, requirements, tags, hub_tags
    - _Requirements: 1.1, 2.1, 2.2, 2.3, 2.4, 7.1, 7.2, 8.1_

  - [x] 1.2 Run insight-plugin refresh and create requirements.txt
    - Run `insight-plugin refresh` from the plugin directory to generate schema.py, setup.py, Dockerfile, Makefile, help.md, bin/, __init__.py files
    - Create `requirements.txt` with pinned dependencies (requests==2.31.0, hypothesis for dev)
    - _Requirements: 1.1_

- [x] 2. Implement utility modules
  - [x] 2.1 Implement constants module (`util/constants.py`)
    - Define TIMEOUT, DEFAULT_MONITORING_TIMEOUT, DEFAULT_POLLING_INTERVAL, API_VERSION
    - Define intent constants: INTENT_CONTAIN, INTENT_UNCONTAIN, INTENT_STATUS, INTENT_INFO
    - Define status constants: STATUS_CONNECTED, STATUS_DISCONNECTED
    - Define result constants: RESULT_SUCCESS, RESULT_ALREADY_ACTIONED, RESULT_TIMEOUT, RESULT_ERROR
    - Define HTTP_ERROR_MAP covering 400, 401, 403, 404, 429, 500, 503
    - _Requirements: 2.3, 2.4, 4.1, 5.1, 9.1, 9.2, 9.3_

  - [x] 2.2 Implement endpoints module (`util/endpoints.py`)
    - Define VIEWER_AUTH_CHECK, SEARCH_AGENTS, DISCONNECT_AGENTS, CONNECT_AGENTS endpoint paths
    - _Requirements: 1.2, 3.1, 4.1, 5.1_

  - [x] 2.3 Implement input validator (`util/validators.py`)
    - Create InputValidator class with validate_execute_response_inputs method
    - Validate endpoint_identifier is not empty/whitespace-only
    - Validate intent is one of contain, uncontain, status, info
    - Validate timeout is a positive integer
    - Validate polling_interval is a positive integer
    - Raise PluginException with cause and assistance on failure
    - _Requirements: 2.5, 2.6_

  - [x] 2.4 Implement identifier resolver (`util/resolver.py`)
    - Create IdentifierResolver class with classify() and resolve() methods
    - Classify IPv4 pattern -> ip, MAC pattern -> mac, numeric-only -> agent_id, other -> hostname
    - Map classifications to SentinelOne query parameters (networkInterfaceInet__contains, networkInterfacePhysical__contains, ids, computerName)
    - Return (agents_list, classification) tuple from resolve()
    - _Requirements: 3.1, 3.2, 3.3_

  - [x] 2.5 Implement SentinelOneAPI client (`util/api.py`)
    - Create SentinelOneAPI class accepting base_url, api_key, and logger
    - Implement _make_request(method, endpoint, **kwargs) with error handling
    - Implement test_connection() -> dict via GET users/viewer-auth-check
    - Implement search_agents(query_params) -> list[dict]
    - Implement disconnect_agents(agent_ids) -> dict
    - Implement connect_agents(agent_ids) -> dict
    - Implement get_agent_by_id(agent_id) -> dict
    - Use plain requests.request() calls, Authorization: APIToken header
    - Map HTTP errors via HTTP_ERROR_MAP, handle Timeout, ConnectionError, JSON decode
    - _Requirements: 1.2, 1.4, 3.1, 4.1, 4.4, 5.1, 5.4, 9.1, 9.2, 9.3, 9.4_

  - [x] 2.6 Implement orchestrator engine (`util/orchestrator.py`)
    - Create ResponseOrchestrator class accepting api_client, resolver, and logger
    - Implement execute(endpoint_identifier, intent, timeout, polling_interval) -> dict
    - Implement _resolve_phase: call resolver, handle zero/multi-match with error reports
    - Implement _validate_state: check current network_status vs desired, return (should_skip, reason)
    - Implement _execute_phase: call disconnect_agents or connect_agents based on intent
    - Implement _monitor_phase: poll agent status until target state or timeout, track elapsed time
    - Implement _build_report: construct response_report dict with all required fields (agent, action_performed, result_status, network_status, summary, timestamp, elapsed_time, error fields)
    - Handle transient 5xx errors during monitoring by continuing; abort on 401/403/404
    - Never raise to caller - always return structured report
    - _Requirements: 3.3, 3.4, 3.5, 4.1, 4.2, 4.3, 4.4, 4.5, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 7.1, 7.2, 8.1, 8.2, 8.3, 8.4, 8.5_

- [x] 3. Implement connection and action
  - [x] 3.1 Implement connection (`connection/connection.py`)
    - In connect(): extract instance and api_key (strip whitespace), construct base_url, instantiate SentinelOneAPI client, store on self.client
    - In test(): call self.client.test_connection(), catch PluginException and convert to ConnectionTestException
    - _Requirements: 1.1, 1.2, 1.3, 1.4_

  - [x] 3.2 Implement execute_response action (`actions/execute_response/action.py`)
    - In run(): extract inputs using Input constants and params.get() with defaults for optional fields
    - Instantiate InputValidator and validate inputs
    - Instantiate IdentifierResolver with self.connection.client
    - Instantiate ResponseOrchestrator with self.connection.client, resolver, and self.logger
    - Call orchestrator.execute() and return result using Output constants
    - Use clean() to strip None/empty values from the output
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 8.1_

- [x] 4. Checkpoint - Validate plugin structure
  - Ensure all tests pass, ask the user if questions arise.
  - Run `insight-plugin validate` to verify spec and generated files are consistent

- [x] 5. Implement unit tests for utility modules
  - [x] 5.1 Create test infrastructure (`unit_test/util.py` and `unit_test/responses/`)
    - Create MockResponse class (status_code, filename-based JSON loading)
    - Create default_connector helper that sets up ExecuteResponse action with mocked connection
    - Create mock JSON response fixtures: agent_single.json, agent_multiple.json, agent_contained.json, disconnect_success.json, connect_success.json, auth_check_success.json, error_401.json, error_429.json
    - _Requirements: 1.2, 3.1, 4.1, 5.1_

  - [x] 5.2 Write unit tests for validators (`unit_test/test_validators.py`)
    - Test valid inputs pass without exception
    - Test empty/whitespace identifier raises PluginException
    - Test invalid intent raises PluginException
    - Test zero/negative timeout raises PluginException
    - Test zero/negative polling_interval raises PluginException
    - _Requirements: 2.5, 2.6_

  - [x] 5.3 Write unit tests for resolver (`unit_test/test_resolver.py`)
    - Test classify: IPv4 addresses -> ip, MAC addresses (colon and hyphen) -> mac, numeric strings -> agent_id, hostnames -> hostname
    - Test resolve: verify correct query parameter used per classification
    - Test resolve with mocked single-agent response returns agent
    - Test resolve with empty response returns empty list
    - _Requirements: 3.1, 3.2, 3.3_

  - [x] 5.4 Write unit tests for API client (`unit_test/test_api_client.py`)
    - Test test_connection success and auth failure (401)
    - Test search_agents constructs correct URL and params
    - Test disconnect_agents and connect_agents post correct body
    - Test HTTP error mapping (401, 403, 404, 429, 500, 503)
    - Test Timeout and ConnectionError handling
    - Test JSON decode failure handling
    - Mock at requests.request level
    - _Requirements: 1.2, 1.3, 9.1, 9.2, 9.3, 9.4_

  - [x] 5.5 Write unit tests for orchestrator (`unit_test/test_orchestrator.py`)
    - Test contain flow: resolve -> check state -> execute -> monitor -> success report
    - Test uncontain flow: resolve -> check state -> execute -> monitor -> success report
    - Test already_actioned: agent already contained, intent=contain -> skip API call
    - Test already_actioned: agent already connected, intent=uncontain -> skip API call
    - Test timeout: polling exceeds timeout -> timeout report
    - Test no-match: empty agent list -> error report with identifier
    - Test multi-match: multiple agents -> error report listing all
    - Test status intent: returns status report without state change
    - Test info intent: returns full agent details report
    - Test API error during execution: error propagated to report
    - Test transient error during monitoring: polling continues
    - _Requirements: 3.3, 3.4, 3.5, 4.1, 4.2, 4.3, 4.4, 4.5, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 7.1, 7.2, 8.1, 8.4, 8.5_

  - [x] 5.6 Write unit tests for execute_response action (`unit_test/test_execute_response.py`)
    - Test all four intents with mocked orchestrator returning success reports
    - Test validation failure returns error report
    - Test output uses Output constants and clean() strips empty fields
    - Mock at client level (self.connection.client methods)
    - _Requirements: 2.1, 2.2, 2.5, 2.6, 8.1, 8.2, 8.3_

- [x] 6. Checkpoint - Run tests and verify coverage
  - Ensure all tests pass, ask the user if questions arise.
  - Run `python -m pytest unit_test/ --cov=icon_sentinelone_active_response --cov-report=term-missing`
  - Verify 80% minimum coverage on all modules

- [x] 7. Property-based tests
  - [ ]* 7.1 Write property test for identifier classification (Property 1)
    - **Property 1: Identifier Classification Correctness**
    - Generate random IPv4 strings, MAC strings (colon/hyphen), numeric strings, general hostnames
    - Verify classifier returns correct classification for each category
    - **Validates: Requirements 2.1, 3.1, 3.2**

  - [ ]* 7.2 Write property test for input validation rejection (Property 2)
    - **Property 2: Input Validation Rejection**
    - Generate whitespace-only and empty strings, zero/negative integers
    - Verify validation produces error without API call
    - **Validates: Requirements 2.5, 2.6**

  - [ ]* 7.3 Write property test for resolution parameter mapping (Property 3)
    - **Property 3: Resolution Parameter Mapping**
    - Generate identifiers of each class, verify correct API parameter used in query
    - **Validates: Requirements 3.1, 3.2**

  - [ ]* 7.4 Write property test for no-match error includes identifier (Property 4)
    - **Property 4: No-Match Error Includes Identifier**
    - Generate random identifiers, mock empty API response, verify identifier appears in report
    - **Validates: Requirements 3.4**

  - [ ]* 7.5 Write property test for multi-match error lists all agents (Property 5)
    - **Property 5: Multi-Match Error Lists All Agents**
    - Generate lists of N > 1 agents with unique IDs/hostnames, verify all appear in report
    - **Validates: Requirements 3.5**

  - [ ]* 7.6 Write property test for polling convergence (Property 6)
    - **Property 6: Polling Convergence**
    - Generate status sequences ending in target status within timeout, verify success report
    - **Validates: Requirements 4.2, 5.2**

  - [ ]* 7.7 Write property test for idempotent state skip (Property 7)
    - **Property 7: Idempotent State Skip**
    - Generate agents already in desired state, verify no mutation API call and already_actioned report
    - **Validates: Requirements 4.3, 5.3**

  - [ ]* 7.8 Write property test for API error propagation (Property 8)
    - **Property 8: API Error Propagation to Report**
    - Generate random error messages, mock API errors, verify errors appear in report fields
    - **Validates: Requirements 4.4, 5.4, 9.1, 9.2, 9.3, 9.4**

  - [ ]* 7.9 Write property test for timeout behavior (Property 9)
    - **Property 9: Timeout Behavior**
    - Generate non-matching status sequences that never reach target, verify timeout report
    - **Validates: Requirements 4.5, 5.5**

  - [ ]* 7.10 Write property test for report structure completeness (Property 10)
    - **Property 10: Report Structure Completeness**
    - Generate random execution contexts (all result statuses), verify action_performed, result_status, summary, timestamp are present and valid
    - **Validates: Requirements 8.1, 8.2, 8.3**

  - [ ]* 7.11 Write property test for monitoring elapsed time (Property 11)
    - **Property 11: Monitoring Elapsed Time**
    - For contain/uncontain operations that monitor, verify elapsed_time is non-negative float
    - **Validates: Requirements 8.5**

- [x] 8. Final validation
  - [x] 8.1 Run insight-plugin validate and fix any issues
    - Run `insight-plugin validate` from the plugin directory
    - Fix any spec validation errors, encoding issues, or missing fields
    - Verify help.md was generated correctly
    - _Requirements: 1.1, 1.2, 1.3, 1.4_

  - [x] 8.2 Run full test suite with coverage report
    - Run `python -m pytest unit_test/ --cov=icon_sentinelone_active_response --cov-report=term-missing`
    - Verify 80% minimum coverage across all modules
    - Run `prospector` on modified files and fix any issues
    - _Requirements: all_

- [x] 9. Final checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional property-based tests and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties from the design document
- Unit tests validate specific examples and edge cases
- Plugin workflow: spec first → refresh → implement hand-written files only → test → validate
- Never edit generated files (schema.py, setup.py, Dockerfile, Makefile, help.md, bin/, __init__.py, .CHECKSUM, .dockerignore)
- Internal polling is appropriate here (bounded orchestrator pattern, not pagination)
- The orchestrator never raises to the action — all errors become structured reports

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["1.2"] },
    { "id": 2, "tasks": ["2.1", "2.2"] },
    { "id": 3, "tasks": ["2.3", "2.4"] },
    { "id": 4, "tasks": ["2.5"] },
    { "id": 5, "tasks": ["2.6"] },
    { "id": 6, "tasks": ["3.1", "3.2"] },
    { "id": 7, "tasks": ["5.1"] },
    { "id": 8, "tasks": ["5.2", "5.3", "5.4", "5.5", "5.6"] },
    { "id": 9, "tasks": ["7.1", "7.2", "7.3", "7.4", "7.5", "7.6", "7.7", "7.8", "7.9", "7.10", "7.11"] },
    { "id": 10, "tasks": ["8.1", "8.2"] }
  ]
}
```
