# Implementation Plan: Fallback Resolution

## Overview

Implement sequential fallback queries, best-match scoring, and resolution metadata for the SentinelOne Active Response plugin's endpoint resolution phase. The implementation adds two new modules (`fallback_chain.py`, `scorer.py`), modifies the resolver and orchestrator, updates the plugin spec, and adds comprehensive tests.

## Tasks

- [x] 1. Create fallback chain configuration and scorer modules
  - [x] 1.1 Create `util/fallback_chain.py` with chain definitions and lookup function
    - Define `FALLBACK_CHAINS` dict mapping each Classification_Type to its ordered list of fallback query parameters
    - Implement `get_fallback_chain(classification: str) -> List[str]` function
    - Chains: uuid→[computerName, networkInterfaceInet__contains], hostname→[uuid, networkInterfaceInet__contains], ip→[computerName, uuid], mac→[computerName, uuid], agent_id→[]
    - _Requirements: 1.4_

  - [x] 1.2 Create `util/scorer.py` with `BestMatchScorer` class and `ScoringResult` data class
    - Implement `ScoringResult` class with fields: `selected_agent`, `confidence_score`, `error`, `tied_agents`, and `is_success` property
    - Implement `BestMatchScorer.compute_score(identifier, agent_field_value) -> float` using `SequenceMatcher` (case-insensitive)
    - Implement `BestMatchScorer.score_agents(identifier, agents, query_param) -> ScoringResult` with threshold check (0.7), tie detection, and single-winner selection
    - Implement `BestMatchScorer._extract_field(agent, field_key) -> str` for pulling the correct field from agent dicts
    - Define `CONFIDENCE_THRESHOLD = 0.7` and `QUERY_PARAM_TO_AGENT_FIELD` mapping
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6_

  - [ ]* 1.3 Write property test: Score Bounds Invariant
    - **Property 3: Score Bounds Invariant**
    - **Validates: Requirements 2.2**
    - Use Hypothesis to generate arbitrary string pairs and verify `compute_score` always returns a value in [0.0, 1.0]

  - [ ]* 1.4 Write property test: Scoring Selection Correctness
    - **Property 4: Scoring Selection Correctness**
    - **Validates: Requirements 2.3, 2.4, 2.5**
    - Use Hypothesis to generate agent lists with pre-set scores and verify: unique winner above threshold → selected; below threshold → error; tie at top → error

- [x] 2. Enhance IdentifierResolver with fallback traversal and scoring
  - [x] 2.1 Add `ResolutionMetadata` class to `util/resolver.py`
    - Define `ResolutionMetadata` with fields: `resolution_method`, `successful_strategy`, `fallback_chain_attempted`, `confidence_score`
    - Implement `to_dict()` method for serialization
    - _Requirements: 3.2_

  - [x] 2.2 Update `IdentifierResolver.__init__` to accept a `logger` parameter and instantiate `BestMatchScorer`
    - Add `self.logger` and `self.scorer = BestMatchScorer()` in constructor
    - Import `get_fallback_chain` from `fallback_chain` module and `BestMatchScorer` from `scorer` module
    - _Requirements: 2.1, 1.1_

  - [x] 2.3 Rewrite `IdentifierResolver.resolve()` to return `Tuple[Optional[dict], ResolutionMetadata]`
    - Implement direct single-match fast path (return immediately, no scoring/fallback)
    - Implement multi-result path: invoke scorer on primary results
    - Implement zero-result path: traverse fallback chain with scoring at each step
    - Log fallback transitions at INFO level
    - Handle `agent_id` classification with no fallback (error immediately on zero results)
    - _Requirements: 1.1, 1.2, 1.3, 1.5, 2.1, 2.5, 4.1, 4.2, 4.3, 5.1, 5.3_

  - [ ]* 2.4 Write property test: Fallback Chain Traversal
    - **Property 1: Fallback Chain Traversal**
    - **Validates: Requirements 1.1, 1.3, 5.3**
    - Mock `api_client.search_agents` to return zero agents for all calls. Verify resolver queries each strategy in the chain in order and returns error with all strategies listed.

  - [ ]* 2.5 Write property test: Traversal Early Termination
    - **Property 2: Traversal Early Termination**
    - **Validates: Requirements 1.2, 4.3**
    - Mock API to return a single agent at a random point in the chain. Verify no subsequent strategies are queried.

  - [ ]* 2.6 Write property test: Single-Match Bypass
    - **Property 7: Single-Match Bypass**
    - **Validates: Requirements 5.1**
    - For any identifier whose primary query returns exactly 1 agent, verify scorer is never called and fallback chain is not traversed.

  - [ ]* 2.7 Write property test: Fallback and Scoring Integration
    - **Property 5: Fallback and Scoring Integration**
    - **Validates: Requirements 4.1, 4.2**
    - Mock API to return multiple agents on a fallback step. Verify scorer is invoked. If scoring fails, verify next strategy is tried. If scoring succeeds, verify traversal stops.

- [x] 3. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [x] 4. Update ResponseOrchestrator and plugin spec
  - [x] 4.1 Update `util/orchestrator.py` `_resolve_phase` to consume the new resolver signature
    - Handle new `(agent, ResolutionMetadata)` return tuple from `resolver.resolve()`
    - Build error reports with metadata when `agent is None`
    - Pass `resolution_metadata.to_dict()` through to `_build_report`
    - _Requirements: 3.1, 3.3, 3.4, 3.5, 3.6_

  - [x] 4.2 Update `util/orchestrator.py` `_build_report` to include `resolution_metadata` field
    - Add `resolution_metadata` key to the report dict (from kwargs or default)
    - Ensure all report paths (success, already_actioned, timeout, error) include resolution_metadata
    - _Requirements: 3.1_

  - [x] 4.3 Update `util/constants.py` to export `CONFIDENCE_THRESHOLD`
    - Add `CONFIDENCE_THRESHOLD = 0.7` constant
    - _Requirements: 2.6_

  - [x] 4.4 Update `plugin.spec.yaml` with `resolution_metadata` type definition
    - Add `resolution_metadata` custom type with fields: `resolution_method`, `successful_strategy`, `fallback_chain_attempted`, `confidence_score`
    - Add `resolution_metadata` field to the `response_report` type
    - _Requirements: 3.1, 3.2_

  - [ ]* 4.5 Write property test: Resolution Metadata Completeness and Accuracy
    - **Property 6: Resolution Metadata Completeness and Accuracy**
    - **Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5, 3.6**
    - For any resolution outcome (direct, fallback, scored, error), verify the report includes `resolution_metadata` with all four sub-fields populated correctly.

- [x] 5. Add unit tests for all new and modified components
  - [x] 5.1 Create `unit_test/test_fallback_chain.py`
    - Test `get_fallback_chain` returns correct chain for each Classification_Type
    - Test unknown classification returns empty list
    - Test agent_id returns empty chain
    - _Requirements: 1.4_

  - [x] 5.2 Create `unit_test/test_scorer.py`
    - Test `compute_score` with identical strings returns 1.0
    - Test `compute_score` with completely different strings returns low score
    - Test `score_agents` selects unique winner above threshold
    - Test `score_agents` returns error on tie
    - Test `score_agents` returns error when below threshold
    - Test `_extract_field` for IP, MAC, and standard fields
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6_

  - [x] 5.3 Update `unit_test/test_resolver.py` with fallback and scoring scenarios
    - Test direct single-match returns without fallback or scoring
    - Test zero-result triggers fallback chain traversal
    - Test multi-result triggers scoring
    - Test fallback with multi-result triggers scoring then continues on failure
    - Test agent_id with zero results returns error immediately (no fallback)
    - Test all strategies exhausted returns error with full chain in metadata
    - _Requirements: 1.1, 1.2, 1.3, 2.5, 4.1, 4.2, 5.1, 5.3_

  - [x] 5.4 Update `unit_test/test_orchestrator.py` with resolution_metadata scenarios
    - Test _resolve_phase returns resolution_metadata on success
    - Test _resolve_phase returns resolution_metadata on error
    - Test _build_report includes resolution_metadata field
    - Test full execute() flow includes resolution_metadata in final report
    - _Requirements: 3.1, 3.3, 3.4, 3.5, 3.6_

- [x] 6. Final checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties from the design document
- Unit tests validate specific examples and edge cases
- The plugin uses Python with pytest + unittest.mock for testing
- Hypothesis library is used for property-based tests
- All new files are created under `komand_sentinelone_active_response/util/` and `unit_test/`

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1", "1.2"] },
    { "id": 1, "tasks": ["1.3", "1.4", "2.1"] },
    { "id": 2, "tasks": ["2.2"] },
    { "id": 3, "tasks": ["2.3"] },
    { "id": 4, "tasks": ["2.4", "2.5", "2.6", "2.7", "4.3"] },
    { "id": 5, "tasks": ["4.1", "4.2"] },
    { "id": 6, "tasks": ["4.4", "4.5"] },
    { "id": 7, "tasks": ["5.1", "5.2", "5.3", "5.4"] }
  ]
}
```
