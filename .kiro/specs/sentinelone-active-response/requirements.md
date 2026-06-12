# Requirements Document

## Introduction

The SentinelOne Active Response plugin for InsightConnect exposes a single autonomous action that orchestrates endpoint response operations end-to-end. An analyst provides an endpoint identifier and a desired intent (contain, uncontain, check status, get info), and the action autonomously resolves the endpoint, executes the appropriate SentinelOne API operations, monitors the result, and returns a comprehensive report. This "AI agent" pattern eliminates the need for multi-step workflow chaining - one action handles the full lifecycle: resolve, validate, execute, monitor, report.

## Glossary

- **Plugin**: An InsightConnect integration component that communicates with an external service via its API
- **SentinelOne_API**: The RESTful API provided by SentinelOne for managing endpoints, agents, and security operations
- **Agent**: A SentinelOne software agent installed on an endpoint that reports to the SentinelOne management console
- **Endpoint**: A computing device (workstation, server, laptop) managed by a SentinelOne agent
- **Containment**: The act of isolating an endpoint from the network while maintaining communication with the SentinelOne management console
- **Uncontainment**: The act of restoring full network connectivity to a previously contained endpoint
- **Network_Status**: The current network state of an agent as reported by SentinelOne (connected, disconnected, connecting, disconnecting)
- **Orchestrator_Action**: The single plugin action that autonomously resolves endpoints, determines required API calls, executes operations, monitors results, and produces a comprehensive report
- **Endpoint_Identifier**: A flexible input that can be a hostname, IP address, MAC address, or SentinelOne agent ID used to resolve an endpoint
- **Intent**: The desired operation the analyst wants performed (contain, uncontain, status, info)
- **Connection**: The plugin configuration that stores authentication credentials and the SentinelOne instance URL
- **Resolution_Phase**: The internal step where the Orchestrator_Action resolves an Endpoint_Identifier to a specific SentinelOne agent record
- **Execution_Phase**: The internal step where the Orchestrator_Action performs the requested API operation against the resolved agent
- **Monitoring_Phase**: The internal step where the Orchestrator_Action polls for status confirmation after a state-changing operation

## Requirements

### Requirement 1: Plugin Connection Configuration

**User Story:** As a security analyst, I want to configure the plugin with my SentinelOne instance credentials, so that the Orchestrator_Action can authenticate with the SentinelOne API.

#### Acceptance Criteria

1. THE Connection SHALL accept an API key credential and a SentinelOne instance URL as configuration inputs
2. WHEN a connection test is performed, THE Connection SHALL validate the API key by making a test request to the SentinelOne_API
3. IF the API key is invalid or the instance URL is unreachable, THEN THE Connection SHALL return a descriptive error message indicating the authentication failure
4. THE Connection SHALL use HTTPS for all communication with the SentinelOne_API

### Requirement 2: Single Orchestrator Action Interface

**User Story:** As a security analyst, I want a single action that accepts an endpoint identifier and my desired intent, so that I can perform endpoint response without chaining multiple workflow steps.

#### Acceptance Criteria

1. THE Orchestrator_Action SHALL accept an Endpoint_Identifier input as a free-form string supporting hostname, IP address, MAC address, or SentinelOne agent ID
2. THE Orchestrator_Action SHALL accept an Intent input specifying the desired operation from the set: contain, uncontain, status, info
3. THE Orchestrator_Action SHALL accept an optional timeout input (in seconds) that controls the maximum duration of the Monitoring_Phase, with a default value of 120 seconds
4. THE Orchestrator_Action SHALL accept an optional polling interval input (in seconds) that controls the frequency of status checks during the Monitoring_Phase, with a default value of 10 seconds
5. WHEN an empty or null Endpoint_Identifier is provided, THE Orchestrator_Action SHALL return a validation error before making any API call
6. WHEN an invalid timeout or polling interval value (non-positive number) is provided, THE Orchestrator_Action SHALL return a validation error before making any API call

### Requirement 3: Endpoint Resolution

**User Story:** As a security analyst, I want the action to automatically resolve any endpoint identifier I provide to the correct SentinelOne agent, so that I do not need to know the exact agent ID ahead of time.

#### Acceptance Criteria

1. WHEN an Endpoint_Identifier is provided, THE Orchestrator_Action SHALL query the SentinelOne_API to resolve it to a matching agent record
2. THE Orchestrator_Action SHALL attempt resolution by querying against hostname, IP address, MAC address, and agent ID fields until a match is found
3. WHEN exactly one agent matches the Endpoint_Identifier, THE Orchestrator_Action SHALL proceed to the Execution_Phase using that agent
4. IF no agent matches the Endpoint_Identifier, THEN THE Orchestrator_Action SHALL return a comprehensive error report indicating no agent was found and include the identifier that was searched
5. IF multiple agents match the Endpoint_Identifier, THEN THE Orchestrator_Action SHALL return a comprehensive error report listing all matching agents with their agent IDs and hostnames so the analyst can provide a more specific identifier

### Requirement 4: Autonomous Contain Operation

**User Story:** As a security analyst, I want to say "contain endpoint X" and have the action handle the full containment lifecycle, so that I get a confirmed result without managing intermediate steps.

#### Acceptance Criteria

1. WHEN the Intent is "contain" and the resolved agent is not already contained, THE Orchestrator_Action SHALL send a network disconnect request to the SentinelOne_API
2. WHEN the containment request is accepted, THE Orchestrator_Action SHALL enter the Monitoring_Phase and poll the SentinelOne_API until the agent Network_Status transitions to disconnected or the timeout is reached
3. IF the resolved agent is already in a contained state, THEN THE Orchestrator_Action SHALL skip the API call and return a success report indicating the agent was already contained with its current details
4. IF the containment request is rejected by the SentinelOne_API, THEN THE Orchestrator_Action SHALL return an error report with the failure reason from the API response
5. IF the agent does not reach disconnected status within the configured timeout, THEN THE Orchestrator_Action SHALL return a report indicating timeout with the last observed Network_Status

### Requirement 5: Autonomous Uncontain Operation

**User Story:** As a security analyst, I want to say "uncontain endpoint X" and have the action handle the full restoration lifecycle, so that I get a confirmed result without managing intermediate steps.

#### Acceptance Criteria

1. WHEN the Intent is "uncontain" and the resolved agent is currently contained, THE Orchestrator_Action SHALL send a network reconnect request to the SentinelOne_API
2. WHEN the uncontainment request is accepted, THE Orchestrator_Action SHALL enter the Monitoring_Phase and poll the SentinelOne_API until the agent Network_Status transitions to connected or the timeout is reached
3. IF the resolved agent is already in a connected state, THEN THE Orchestrator_Action SHALL skip the API call and return a success report indicating the agent was already connected with its current details
4. IF the uncontainment request is rejected by the SentinelOne_API, THEN THE Orchestrator_Action SHALL return an error report with the failure reason from the API response
5. IF the agent does not reach connected status within the configured timeout, THEN THE Orchestrator_Action SHALL return a report indicating timeout with the last observed Network_Status

### Requirement 6: Status Check Operation

**User Story:** As a security analyst, I want to check the current containment status of an endpoint without changing it, so that I can assess the situation before deciding on a response action.

#### Acceptance Criteria

1. WHEN the Intent is "status", THE Orchestrator_Action SHALL query the SentinelOne_API for the resolved agent current Network_Status without performing any state-changing operation
2. WHEN the status is retrieved, THE Orchestrator_Action SHALL return a report containing the agent Network_Status, hostname, and a human-readable interpretation of the state

### Requirement 7: Info Retrieval Operation

**User Story:** As a security analyst, I want to retrieve comprehensive details about an endpoint, so that I can make informed decisions about response actions.

#### Acceptance Criteria

1. WHEN the Intent is "info", THE Orchestrator_Action SHALL query the SentinelOne_API for the resolved agent full details without performing any state-changing operation
2. WHEN agent details are retrieved, THE Orchestrator_Action SHALL return a report containing agent ID, hostname, IP address, MAC address, operating system, Network_Status, site name, group name, active threat count, and agent version

### Requirement 8: Comprehensive Output Report

**User Story:** As a security analyst, I want every invocation to return a structured comprehensive report, so that I can use the output directly in incident documentation and downstream workflow steps.

#### Acceptance Criteria

1. THE Orchestrator_Action SHALL produce a structured output containing: agent details (agent ID, hostname, IP address, MAC address, operating system, site name, group name), the action performed, result status (success, already_actioned, timeout, error), and a timestamp
2. THE Orchestrator_Action SHALL include the agent Network_Status at the time the report is generated
3. THE Orchestrator_Action SHALL include a human-readable summary message suitable for display in a workflow artifact or notification
4. IF the operation encounters an error, THEN THE Orchestrator_Action SHALL include error details (cause and recommended remediation) in the report output
5. WHEN a contain or uncontain operation completes with monitoring, THE Orchestrator_Action SHALL include the elapsed monitoring time in the report

### Requirement 9: API Error Handling

**User Story:** As a security analyst, I want the action to handle API errors gracefully and include actionable context in the report, so that I understand what went wrong without needing to inspect raw API responses.

#### Acceptance Criteria

1. IF the SentinelOne_API returns a rate limit response, THEN THE Orchestrator_Action SHALL include the rate limit details in the error report
2. IF the SentinelOne_API returns an authentication error, THEN THE Orchestrator_Action SHALL return a clear message indicating the API key may be invalid or expired
3. IF the SentinelOne_API is unreachable due to a network error, THEN THE Orchestrator_Action SHALL return a connection error report with the instance URL that was attempted
4. IF the SentinelOne_API returns an unexpected response format, THEN THE Orchestrator_Action SHALL return an error report indicating the response could not be parsed
