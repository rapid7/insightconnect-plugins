# Requirements Document

## Introduction

This feature enhances the SentinelOne Active Response plugin's endpoint resolution phase. Currently, the `IdentifierResolver` classifies an identifier by regex and queries a single SentinelOne API parameter — returning an error when zero or multiple agents match. The fallback-resolution feature introduces three capabilities: sequential fallback queries when the primary classification yields zero results, best-match scoring with a confidence threshold when multiple agents are returned, and a structured `resolution_metadata` field appended to the response report for full traceability.

## Glossary

- **Resolver**: The `IdentifierResolver` component responsible for classifying endpoint identifiers and querying the SentinelOne API to locate matching agents.
- **Fallback_Chain**: A fixed-priority ordered list of alternative query parameters that the Resolver attempts sequentially when the primary classification query returns zero results.
- **Classification_Type**: The category assigned to an identifier by regex pattern matching — one of `ip`, `mac`, `agent_id`, `uuid`, or `hostname`.
- **Confidence_Score**: A numeric value on a 0–1 scale representing how closely a returned agent matches the original identifier.
- **Confidence_Threshold**: A fixed numeric boundary (e.g. 0.7) that a Confidence_Score must meet or exceed for an agent to be considered a valid match.
- **Best_Match_Scorer**: The component that computes a Confidence_Score for each agent returned by a query and selects the top-scoring agent.
- **Resolution_Metadata**: A structured field added to the response_report output containing the successful strategy name, the Fallback_Chain attempted, the Confidence_Score (if scoring was used), and the resolution method.
- **Orchestrator**: The `ResponseOrchestrator` component that coordinates the full response lifecycle including resolution, execution, monitoring, and reporting phases.

## Requirements

### Requirement 1: Sequential Fallback on Zero Results

**User Story:** As an incident responder, I want the resolver to automatically try alternative query strategies when the primary classification yields no results, so that transient data gaps (e.g. a missing computerName record) do not block containment.

#### Acceptance Criteria

1. WHEN the primary classification query returns zero agents, THE Resolver SHALL attempt the next query parameter in the Fallback_Chain for the given Classification_Type.
2. WHEN a Fallback_Chain query returns one or more agents, THE Resolver SHALL stop traversing the remaining Fallback_Chain and return the result set.
3. WHEN all queries in the Fallback_Chain for a Classification_Type return zero agents, THE Resolver SHALL return an error indicating no matching agent was found and list all strategies attempted.
4. THE Resolver SHALL use the following fixed Fallback_Chain ordering:
   - `uuid` miss → try `computerName` → try `networkInterfaceInet__contains`
   - `hostname` miss → try `uuid` → try `networkInterfaceInet__contains`
   - `ip` miss → try `computerName` → try `uuid`
   - `mac` miss → try `computerName` → try `uuid`
   - `agent_id` miss → no fallback (return error immediately)
5. WHEN the Resolver initiates a fallback query, THE Resolver SHALL log the transition at INFO level including the Classification_Type, the failed strategy, and the next strategy to attempt.

### Requirement 2: Best-Match Scoring for Multiple Results

**User Story:** As an incident responder, I want the system to score multiple matching agents and select the best one with high confidence, so that ambiguous identifiers resolve deterministically without manual intervention.

#### Acceptance Criteria

1. WHEN a query (primary or fallback) returns more than one agent, THE Best_Match_Scorer SHALL compute a Confidence_Score for each returned agent.
2. THE Best_Match_Scorer SHALL compute the Confidence_Score by comparing the original identifier value against the corresponding agent field using a defined similarity metric on a 0–1 scale.
3. WHEN the highest Confidence_Score is below the Confidence_Threshold, THE Resolver SHALL return an error indicating that no agent met the confidence requirement and report the top score and threshold value.
4. WHEN two or more agents share the same highest Confidence_Score at or above the Confidence_Threshold, THE Resolver SHALL return an error indicating an ambiguous tie and list the tied agents.
5. WHEN exactly one agent has the highest Confidence_Score at or above the Confidence_Threshold, THE Resolver SHALL select that agent as the resolved match.
6. THE Best_Match_Scorer SHALL use a Confidence_Threshold value of 0.7.

### Requirement 3: Resolution Metadata in Report

**User Story:** As an incident responder, I want the response report to include metadata about how the endpoint was resolved, so that I have full traceability for incident documentation and debugging.

#### Acceptance Criteria

1. THE Orchestrator SHALL include a `resolution_metadata` field in every response_report output.
2. THE `resolution_metadata` field SHALL contain the following sub-fields: `successful_strategy` (string), `fallback_chain_attempted` (list of strings), `confidence_score` (float or null), and `resolution_method` (string).
3. WHEN the primary classification query succeeds with a single agent match, THE Orchestrator SHALL set `resolution_method` to "direct", `successful_strategy` to the primary query parameter name, `fallback_chain_attempted` to a list containing only the primary strategy, and `confidence_score` to null.
4. WHEN a fallback query produces the final match, THE Orchestrator SHALL set `resolution_method` to "fallback", `successful_strategy` to the query parameter name that yielded results, and `fallback_chain_attempted` to the ordered list of all strategies attempted including the successful one.
5. WHEN the Best_Match_Scorer selects an agent, THE Orchestrator SHALL set `resolution_method` to "scored", `confidence_score` to the winning agent's Confidence_Score value, and `successful_strategy` to the query parameter name that produced the scored result set.
6. WHEN resolution fails (no agent found or ambiguous), THE Orchestrator SHALL still include `resolution_metadata` with `resolution_method` set to "error", `successful_strategy` set to an empty string, `fallback_chain_attempted` listing all strategies attempted, and `confidence_score` set to null.

### Requirement 4: Fallback and Scoring Integration

**User Story:** As an incident responder, I want fallback and scoring to work together seamlessly, so that the resolver exhausts all reasonable strategies before erroring.

#### Acceptance Criteria

1. WHEN a fallback query returns multiple agents, THE Resolver SHALL invoke the Best_Match_Scorer on that result set before continuing to the next fallback strategy.
2. WHEN the Best_Match_Scorer fails to select a single agent from a fallback query result (score below threshold or tie), THE Resolver SHALL continue to the next strategy in the Fallback_Chain.
3. WHEN the Best_Match_Scorer successfully selects an agent from any query in the Fallback_Chain, THE Resolver SHALL stop traversal and return the selected agent.

### Requirement 5: Backward Compatibility

**User Story:** As an existing user of the plugin, I want the new fallback logic to preserve existing single-match behavior, so that current integrations continue to work without modification.

#### Acceptance Criteria

1. WHEN the primary classification query returns exactly one agent, THE Resolver SHALL return that agent without invoking the Best_Match_Scorer or Fallback_Chain.
2. THE Resolver SHALL preserve the existing Classification_Type regex patterns and their priority ordering (IP → MAC → agent_id → UUID → hostname).
3. WHEN `agent_id` is the Classification_Type, THE Resolver SHALL return an error on zero results without attempting any fallback, preserving deterministic ID-based lookup behavior.
