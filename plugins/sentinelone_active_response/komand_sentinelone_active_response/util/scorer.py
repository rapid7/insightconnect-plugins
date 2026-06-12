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
