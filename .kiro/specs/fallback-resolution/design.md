# Design Document: Fallback Resolution

## Overview

This feature enhances the SentinelOne Active Response plugin's endpoint resolution phase with sequential fallback queries, best-match scoring with confidence thresholds, and structured resolution metadata in response reports. The design preserves backward compatibility for single-match lookups while adding resilience for zero-result and multi-result scenarios.

## Architecture

This feature extends the existing `IdentifierResolver` with two new capabilities — sequential fallback queries and best-match scoring — and adds `resolution_metadata` to every response report produced by the `ResponseOrchestrator`. The design preserves the existing single-match fast path (backward compatibility) while layering fallback and scoring as opt-in behaviors triggered only when the primary query returns zero or multiple results.

```
┌──────────────────────────────────────────────────────────┐
│                  ResponseOrchestrator                     │
│                                                          │
│  execute() ─► _resolve_phase() ─► _build_report()       │
│                      │                    ▲              │
│                      ▼                    │              │
│              IdentifierResolver           │              │
│              (with FallbackChain          │              │
│               + BestMatchScorer)          │              │
│                      │                    │              │
│                      ▼                    │              │
│              resolution_metadata ─────────┘              │
└──────────────────────────────────────────────────────────┘
```

### Component Interaction Flow

1. `ResponseOrchestrator.execute()` calls `_resolve_phase()`
2. `_resolve_phase()` invokes `IdentifierResolver.resolve()` which now returns `(agent, resolution_metadata)` instead of `(agents, classification)`
3. The resolver internally handles fallback traversal and scoring
4. `_build_report()` injects `resolution_metadata` into every report

## Components and Interfaces

### 1. FallbackChain (new module: `fallback_chain.py`)

A data-driven configuration mapping each `Classification_Type` to its ordered list of fallback query parameters.

```python
from typing import Dict, List

FALLBACK_CHAINS: Dict[str, List[str]] = {
    "uuid": ["computerName", "networkInterfaceInet__contains"],
    "hostname": ["uuid", "networkInterfaceInet__contains"],
    "ip": ["computerName", "uuid"],
    "mac": ["computerName", "uuid"],
    "agent_id": [],  # No fallback — error immediately
}


def get_fallback_chain(classification: str) -> List[str]:
    """Return the fallback chain for the given classification type."""
    return FALLBACK_CHAINS.get(classification, [])
```

### 2. BestMatchScorer (new module: `scorer.py`)

Computes a similarity score between an identifier and each agent's corresponding field, then applies selection logic.

```python
from difflib import SequenceMatcher
from typing import List, Optional, Tuple

CONFIDENCE_THRESHOLD = 0.7

# Maps query param → agent field path for scoring
QUERY_PARAM_TO_AGENT_FIELD = {
    "computerName": "computerName",
    "networkInterfaceInet__contains": "_ip_address",
    "networkInterfacePhysical__contains": "_mac_address",
    "ids": "id",
    "uuid": "uuid",
}


class ScoringResult:
    """Result of scoring a set of agents."""

    def __init__(
        self,
        selected_agent: Optional[dict],
        confidence_score: Optional[float],
        error: Optional[str],
        tied_agents: Optional[List[dict]] = None,
    ):
        self.selected_agent = selected_agent
        self.confidence_score = confidence_score
        self.error = error
        self.tied_agents = tied_agents

    @property
    def is_success(self) -> bool:
        return self.selected_agent is not None


class BestMatchScorer:
    """Scores agents against an identifier and selects the best match."""

    def compute_score(self, identifier: str, agent_field_value: str) -> float:
        """
        Compute similarity between identifier and agent field value.

        Uses SequenceMatcher ratio normalized to [0, 1].
        Case-insensitive comparison.

        :param identifier: The original endpoint identifier
        :param agent_field_value: The agent's field value to compare
        :return: Float in [0.0, 1.0]
        """
        return SequenceMatcher(
            None, identifier.lower(), agent_field_value.lower()
        ).ratio()

    def score_agents(
        self, identifier: str, agents: List[dict], query_param: str
    ) -> ScoringResult:
        """
        Score all agents and select the best match.

        :param identifier: The original endpoint identifier
        :param agents: List of agent dicts from SentinelOne API
        :param query_param: The query parameter used (determines which field to compare)
        :return: ScoringResult with selected agent or error
        """
        field_key = QUERY_PARAM_TO_AGENT_FIELD.get(query_param, "computerName")

        scored = []
        for agent in agents:
            field_value = self._extract_field(agent, field_key)
            score = self.compute_score(identifier, field_value)
            scored.append((agent, score))

        # Sort by score descending
        scored.sort(key=lambda x: x[1], reverse=True)

        top_score = scored[0][1]

        # Check threshold
        if top_score < CONFIDENCE_THRESHOLD:
            return ScoringResult(
                selected_agent=None,
                confidence_score=top_score,
                error=f"No agent met confidence threshold {CONFIDENCE_THRESHOLD} "
                f"(top score: {top_score:.3f})",
            )

        # Check for ties at the top
        tied = [agent for agent, score in scored if score == top_score]
        if len(tied) > 1:
            return ScoringResult(
                selected_agent=None,
                confidence_score=top_score,
                error="Ambiguous tie between agents",
                tied_agents=tied,
            )

        # Unique winner
        return ScoringResult(
            selected_agent=scored[0][0],
            confidence_score=top_score,
            error=None,
        )

    @staticmethod
    def _extract_field(agent: dict, field_key: str) -> str:
        """Extract the relevant field from an agent dict for scoring."""
        if field_key == "_ip_address":
            interfaces = agent.get("networkInterfaces", [])
            if interfaces:
                inet = interfaces[0].get("inet", [])
                if inet:
                    return inet[0]
            return ""
        if field_key == "_mac_address":
            interfaces = agent.get("networkInterfaces", [])
            if interfaces:
                return interfaces[0].get("physical", "")
            return ""
        return agent.get(field_key, "")
```

### 3. Enhanced IdentifierResolver (modified: `resolver.py`)

The resolver gains fallback traversal and scorer integration while preserving the existing `classify()` method unchanged.

```python
from logging import Logger
from typing import Tuple, Optional

from .fallback_chain import get_fallback_chain, FALLBACK_CHAINS
from .scorer import BestMatchScorer, CONFIDENCE_THRESHOLD


class ResolutionMetadata:
    """Structured metadata about how an identifier was resolved."""

    def __init__(
        self,
        resolution_method: str,
        successful_strategy: str,
        fallback_chain_attempted: list,
        confidence_score: Optional[float],
    ):
        self.resolution_method = resolution_method
        self.successful_strategy = successful_strategy
        self.fallback_chain_attempted = fallback_chain_attempted
        self.confidence_score = confidence_score

    def to_dict(self) -> dict:
        return {
            "resolution_method": self.resolution_method,
            "successful_strategy": self.successful_strategy,
            "fallback_chain_attempted": self.fallback_chain_attempted,
            "confidence_score": self.confidence_score,
        }


class IdentifierResolver:
    """
    Classifies an endpoint identifier and resolves it via the SentinelOne API.
    Now supports sequential fallback and best-match scoring.
    """

    def __init__(self, api_client, logger: Logger):
        self.api_client = api_client
        self.logger = logger
        self.scorer = BestMatchScorer()

    def resolve(self, identifier: str) -> Tuple[Optional[dict], ResolutionMetadata]:
        """
        Resolve an endpoint identifier to a single agent.

        Returns (agent, metadata) on success or (None, metadata) on failure.
        """
        identifier = identifier.strip()
        classification = self.classify(identifier)
        primary_param = CLASSIFICATION_TO_QUERY_PARAM[classification]
        strategies_attempted = [primary_param]

        # Primary query
        agents = self.api_client.search_agents({primary_param: identifier})

        # Fast path: single match
        if len(agents) == 1:
            metadata = ResolutionMetadata(
                resolution_method="direct",
                successful_strategy=primary_param,
                fallback_chain_attempted=[primary_param],
                confidence_score=None,
            )
            return (agents[0], metadata)

        # Multiple results on primary: attempt scoring
        if len(agents) > 1:
            result = self.scorer.score_agents(identifier, agents, primary_param)
            if result.is_success:
                metadata = ResolutionMetadata(
                    resolution_method="scored",
                    successful_strategy=primary_param,
                    fallback_chain_attempted=[primary_param],
                    confidence_score=result.confidence_score,
                )
                return (result.selected_agent, metadata)
            # Scoring failed on primary — fall through to fallback

        # Zero results or scoring failed: attempt fallback chain
        fallback_chain = get_fallback_chain(classification)

        if not fallback_chain and len(agents) == 0:
            # No fallback available (agent_id)
            metadata = ResolutionMetadata(
                resolution_method="error",
                successful_strategy="",
                fallback_chain_attempted=strategies_attempted,
                confidence_score=None,
            )
            return (None, metadata)

        for fallback_param in fallback_chain:
            strategies_attempted.append(fallback_param)
            self.logger.info(
                f"Fallback: {classification} — "
                f"'{strategies_attempted[-2]}' yielded no match, "
                f"trying '{fallback_param}'"
            )

            fallback_agents = self.api_client.search_agents(
                {fallback_param: identifier}
            )

            if len(fallback_agents) == 1:
                metadata = ResolutionMetadata(
                    resolution_method="fallback",
                    successful_strategy=fallback_param,
                    fallback_chain_attempted=strategies_attempted,
                    confidence_score=None,
                )
                return (fallback_agents[0], metadata)

            if len(fallback_agents) > 1:
                result = self.scorer.score_agents(
                    identifier, fallback_agents, fallback_param
                )
                if result.is_success:
                    metadata = ResolutionMetadata(
                        resolution_method="scored",
                        successful_strategy=fallback_param,
                        fallback_chain_attempted=strategies_attempted,
                        confidence_score=result.confidence_score,
                    )
                    return (result.selected_agent, metadata)
                # Scoring failed — continue to next fallback

        # All strategies exhausted
        metadata = ResolutionMetadata(
            resolution_method="error",
            successful_strategy="",
            fallback_chain_attempted=strategies_attempted,
            confidence_score=None,
        )
        return (None, metadata)
```

### 4. Enhanced ResponseOrchestrator (modified: `orchestrator.py`)

The `_resolve_phase` and `_build_report` methods are updated to consume `ResolutionMetadata`.

```python
def _resolve_phase(self, identifier: str, intent: str) -> dict:
    """
    Resolve an endpoint identifier to a single agent.
    Now returns resolution_metadata alongside the agent or error report.
    """
    try:
        agent, metadata = self.resolver.resolve(identifier)
    except PluginException as error:
        metadata = ResolutionMetadata(
            resolution_method="error",
            successful_strategy="",
            fallback_chain_attempted=[],
            confidence_score=None,
        )
        report = self._build_report(
            agent={},
            intent=intent,
            result_status=RESULT_ERROR,
            error_cause=error.cause,
            error_remediation=error.assistance,
            summary=f"Failed to resolve endpoint identifier '{identifier}': {error.cause}",
            resolution_metadata=metadata.to_dict(),
        )
        return report

    if agent is None:
        report = self._build_report(
            agent={},
            intent=intent,
            result_status=RESULT_ERROR,
            error_cause="No matching agent found.",
            error_remediation=f"Verify the identifier '{identifier}' is correct. "
            f"Strategies attempted: {metadata.fallback_chain_attempted}",
            summary=f"No agent resolved for '{identifier}' after exhausting all strategies",
            resolution_metadata=metadata.to_dict(),
        )
        return report

    # Attach metadata to result for later report building
    return {"agent": agent, "resolution_metadata": metadata.to_dict()}


def _build_report(self, agent: dict, intent: str, result_status: str, **kwargs) -> dict:
    """Now includes resolution_metadata in every report."""
    agent_details = self._extract_agent_details(agent)

    report = {
        "agent": agent_details,
        "action_performed": intent,
        "result_status": result_status,
        "network_status": agent.get("networkStatus", ""),
        "summary": kwargs.get("summary", ""),
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "elapsed_time": kwargs.get("elapsed_time", 0.0),
        "error_cause": kwargs.get("error_cause", ""),
        "error_remediation": kwargs.get("error_remediation", ""),
        "resolution_metadata": kwargs.get("resolution_metadata", {
            "resolution_method": "direct",
            "successful_strategy": "",
            "fallback_chain_attempted": [],
            "confidence_score": None,
        }),
    }
    return report
```

### 5. Plugin Spec Update (`plugin.spec.yaml`)

A new `resolution_metadata` custom type and field on `response_report`:

```yaml
types:
  resolution_metadata:
    resolution_method:
      title: Resolution Method
      description: How the agent was resolved (direct, fallback, scored, error)
      type: string
      required: true
      example: "direct"
    successful_strategy:
      title: Successful Strategy
      description: The query parameter that yielded the final match
      type: string
      required: true
      example: "computerName"
    fallback_chain_attempted:
      title: Fallback Chain Attempted
      description: Ordered list of all query strategies attempted
      type: "[]string"
      required: true
      example: '["uuid", "computerName"]'
    confidence_score:
      title: Confidence Score
      description: Winning agent similarity score (null if scoring was not used)
      type: float
      required: false
      example: 0.85

  response_report:
    # ... existing fields preserved ...
    resolution_metadata:
      title: Resolution Metadata
      description: Metadata about how the endpoint identifier was resolved
      type: resolution_metadata
      required: true
      example: '{"resolution_method": "direct", "successful_strategy": "computerName", "fallback_chain_attempted": ["computerName"], "confidence_score": null}'
```

## Data Models

### ResolutionMetadata

| Field | Type | Description |
|-------|------|-------------|
| `resolution_method` | `str` | One of: `"direct"`, `"fallback"`, `"scored"`, `"error"` |
| `successful_strategy` | `str` | Query parameter name that resolved the agent, or `""` on error |
| `fallback_chain_attempted` | `List[str]` | Ordered list of all strategies tried |
| `confidence_score` | `Optional[float]` | Winning score if scoring was used, else `None` |

### ScoringResult

| Field | Type | Description |
|-------|------|-------------|
| `selected_agent` | `Optional[dict]` | The winning agent, or `None` on failure |
| `confidence_score` | `Optional[float]` | Top score computed |
| `error` | `Optional[str]` | Error message if selection failed |
| `tied_agents` | `Optional[List[dict]]` | Agents that tied (for error reporting) |

### FallbackChains Configuration

| Classification | Primary Param | Fallback Chain |
|---------------|--------------|----------------|
| `uuid` | `uuid` | `computerName` → `networkInterfaceInet__contains` |
| `hostname` | `computerName` | `uuid` → `networkInterfaceInet__contains` |
| `ip` | `networkInterfaceInet__contains` | `computerName` → `uuid` |
| `mac` | `networkInterfacePhysical__contains` | `computerName` → `uuid` |
| `agent_id` | `ids` | *(none — error immediately)* |

## Interfaces

### IdentifierResolver.resolve() (Updated Signature)

```python
def resolve(self, identifier: str) -> Tuple[Optional[dict], ResolutionMetadata]:
    """
    Resolve an endpoint identifier to a single agent with metadata.

    :param identifier: Endpoint identifier string
    :return: Tuple of (agent_dict_or_None, ResolutionMetadata)
    """
```

### BestMatchScorer.score_agents()

```python
def score_agents(
    self, identifier: str, agents: List[dict], query_param: str
) -> ScoringResult:
    """
    Score agents against identifier and select best match.

    :param identifier: Original identifier value
    :param agents: List of agent dicts (len > 1)
    :param query_param: Query parameter used (determines comparison field)
    :return: ScoringResult
    """
```

### BestMatchScorer.compute_score()

```python
def compute_score(self, identifier: str, agent_field_value: str) -> float:
    """
    Compute similarity between identifier and agent field.

    :param identifier: Original identifier
    :param agent_field_value: Agent field value to compare
    :return: Float in [0.0, 1.0]
    """
```

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Primary returns 0, no fallback chain (agent_id) | Return error with metadata listing single attempted strategy |
| All fallback strategies exhausted | Return error with metadata listing all attempted strategies |
| Scoring below threshold | On primary: fall through to fallback. On last fallback: return error with top score |
| Scoring tie | On primary: fall through to fallback. On last fallback: return error with tied agent list |
| API exception during any query | Propagate `PluginException` with metadata in error state |
| Empty identifier (after strip) | Handled by existing validation before resolve is called |

## File Structure

```
komand_sentinelone_active_response/util/
├── constants.py          # Existing — add CONFIDENCE_THRESHOLD
├── resolver.py           # Modified — add fallback + scoring integration
├── fallback_chain.py     # New — fallback chain configuration
├── scorer.py             # New — BestMatchScorer
├── orchestrator.py       # Modified — consume ResolutionMetadata, update _build_report
```

## Testing Strategy

- **Unit tests (pytest + unittest.mock)**: Verify specific scenarios — fallback chain ordering, direct match bypass, API error propagation, metadata field presence for each path.
- **Property tests (Hypothesis)**: Verify universal properties — score bounds, scoring selection logic, traversal termination, metadata accuracy across randomly generated identifiers and agent sets.
- **Integration focus**: Mock the `api_client.search_agents` method to simulate various result counts. The scorer's `compute_score` is a pure function ideal for property-based testing. The resolver's traversal logic is testable with mocked API responses.

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system — essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Fallback Chain Traversal

For any identifier whose primary classification query returns zero agents, the resolver SHALL query each strategy in the fallback chain in order until one returns results or the chain is exhausted. If the classification is `agent_id`, no fallback is attempted and an error is returned immediately.

**Validates: Requirements 1.1, 1.3, 5.3**

### Property 2: Traversal Early Termination

For any fallback or primary query that returns one or more agents where a single match is determined (either a single-agent result or a successful scoring selection), the resolver SHALL stop traversal immediately and not query any remaining strategies in the chain.

**Validates: Requirements 1.2, 4.3**

### Property 3: Score Bounds Invariant

For any identifier string and any agent field value string, the `compute_score` method SHALL return a value in the closed interval [0.0, 1.0].

**Validates: Requirements 2.2**

### Property 4: Scoring Selection Correctness

For any set of agents with computed confidence scores: if exactly one agent has the highest score and that score is at or above 0.7, that agent is selected; if the highest score is below 0.7, an error is returned; if two or more agents tie at the highest score at or above 0.7, an error is returned.

**Validates: Requirements 2.3, 2.4, 2.5**

### Property 5: Fallback and Scoring Integration

For any fallback query that returns multiple agents, the scorer SHALL be invoked on that result set. If scoring fails (below threshold or tie), traversal SHALL continue to the next strategy. If scoring succeeds, traversal SHALL stop.

**Validates: Requirements 4.1, 4.2**

### Property 6: Resolution Metadata Completeness and Accuracy

For any resolution outcome (direct, fallback, scored, or error), the response report SHALL include a `resolution_metadata` field containing `resolution_method`, `successful_strategy`, `fallback_chain_attempted`, and `confidence_score`, with values that accurately reflect the path taken during resolution.

**Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5, 3.6**

### Property 7: Single-Match Bypass

For any identifier whose primary classification query returns exactly one agent, the resolver SHALL return that agent without invoking the scorer or attempting any fallback strategy.

**Validates: Requirements 5.1**
