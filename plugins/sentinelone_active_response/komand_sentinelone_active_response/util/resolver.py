import re
from logging import Logger
from typing import Optional

from .fallback_chain import get_fallback_chain, FALLBACK_CHAINS
from .scorer import BestMatchScorer, CONFIDENCE_THRESHOLD

# Classification constants
CLASSIFICATION_IP = "ip"
CLASSIFICATION_MAC = "mac"
CLASSIFICATION_AGENT_ID = "agent_id"
CLASSIFICATION_UUID = "uuid"
CLASSIFICATION_HOSTNAME = "hostname"

# Regex patterns for identifier classification
IPV4_PATTERN = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
MAC_PATTERN = re.compile(r"^([0-9A-Fa-f]{2}[:\-]){5}[0-9A-Fa-f]{2}$")
NUMERIC_PATTERN = re.compile(r"^\d+$")
# SentinelOne agent UUIDs are 32-char hex strings (UUIDs without hyphens)
HEX_UUID_PATTERN = re.compile(r"^[0-9a-fA-F]{32}$")

# Map classification to SentinelOne API query parameter
CLASSIFICATION_TO_QUERY_PARAM = {
    CLASSIFICATION_IP: "networkInterfaceInet__contains",
    CLASSIFICATION_MAC: "networkInterfacePhysical__contains",
    CLASSIFICATION_AGENT_ID: "ids",
    CLASSIFICATION_UUID: "uuid",
    CLASSIFICATION_HOSTNAME: "computerName",
}


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
    """

    def __init__(self, api_client, logger):
        """
        Initialize the resolver with an API client and logger.

        :param api_client: SentinelOneAPI client instance with search_agents method
        :param logger: Logger instance for info/debug logging
        """
        self.api_client = api_client
        self.logger = logger
        self.scorer = BestMatchScorer()

    def classify(self, identifier: str) -> str:
        """
        Classify an endpoint identifier based on its pattern.

        :param identifier: The endpoint identifier string
        :return: Classification string (ip, mac, agent_id, or hostname)
        """
        identifier = identifier.strip()

        if IPV4_PATTERN.match(identifier):
            return CLASSIFICATION_IP

        if MAC_PATTERN.match(identifier):
            return CLASSIFICATION_MAC

        if NUMERIC_PATTERN.match(identifier):
            return CLASSIFICATION_AGENT_ID

        if HEX_UUID_PATTERN.match(identifier):
            return CLASSIFICATION_UUID

        return CLASSIFICATION_HOSTNAME

    def resolve(self, identifier: str) -> tuple:
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
