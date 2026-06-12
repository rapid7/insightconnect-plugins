import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import MagicMock, patch, call
from komand_sentinelone_active_response.util.resolver import IdentifierResolver, ResolutionMetadata


class TestIdentifierResolver:
    def setup_method(self):
        self.mock_logger = MagicMock()

    def test_classify_ipv4(self):
        resolver = IdentifierResolver(MagicMock(), self.mock_logger)
        assert resolver.classify("192.168.1.100") == "ip"
        assert resolver.classify("10.0.0.1") == "ip"
        assert resolver.classify("255.255.255.255") == "ip"

    def test_classify_mac_colon(self):
        resolver = IdentifierResolver(MagicMock(), self.mock_logger)
        assert resolver.classify("00:1A:2B:3C:4D:5E") == "mac"
        assert resolver.classify("aa:bb:cc:dd:ee:ff") == "mac"

    def test_classify_mac_hyphen(self):
        resolver = IdentifierResolver(MagicMock(), self.mock_logger)
        assert resolver.classify("00-1A-2B-3C-4D-5E") == "mac"

    def test_classify_agent_id(self):
        resolver = IdentifierResolver(MagicMock(), self.mock_logger)
        assert resolver.classify("1234567890123456789") == "agent_id"
        assert resolver.classify("999") == "agent_id"

    def test_classify_hostname(self):
        resolver = IdentifierResolver(MagicMock(), self.mock_logger)
        assert resolver.classify("WORKSTATION-01") == "hostname"
        assert resolver.classify("server.example.com") == "hostname"
        assert resolver.classify("my-host") == "hostname"

    def test_resolve_ip_uses_correct_param(self):
        mock_client = MagicMock()
        agent = {"id": "1", "computerName": "host1", "networkInterfaces": [{"inet": ["192.168.1.100"]}]}
        mock_client.search_agents.return_value = [agent]
        resolver = IdentifierResolver(mock_client, self.mock_logger)
        resolver.resolve("192.168.1.100")
        mock_client.search_agents.assert_called_with({"networkInterfaceInet__contains": "192.168.1.100"})

    def test_resolve_mac_uses_correct_param(self):
        mock_client = MagicMock()
        agent = {"id": "1", "computerName": "host1", "networkInterfaces": [{"physical": "00:1A:2B:3C:4D:5E"}]}
        mock_client.search_agents.return_value = [agent]
        resolver = IdentifierResolver(mock_client, self.mock_logger)
        resolver.resolve("00:1A:2B:3C:4D:5E")
        mock_client.search_agents.assert_called_with({"networkInterfacePhysical__contains": "00:1A:2B:3C:4D:5E"})

    def test_resolve_agent_id_uses_correct_param(self):
        mock_client = MagicMock()
        mock_client.search_agents.return_value = []
        resolver = IdentifierResolver(mock_client, self.mock_logger)
        resolver.resolve("1234567890123456789")
        mock_client.search_agents.assert_called_with({"ids": "1234567890123456789"})

    def test_resolve_hostname_uses_correct_param(self):
        mock_client = MagicMock()
        agent = {"id": "1", "computerName": "WORKSTATION-01"}
        mock_client.search_agents.return_value = [agent]
        resolver = IdentifierResolver(mock_client, self.mock_logger)
        resolver.resolve("WORKSTATION-01")
        mock_client.search_agents.assert_called_with({"computerName": "WORKSTATION-01"})

    def test_resolve_single_match_returns_agent_and_metadata(self):
        mock_client = MagicMock()
        agent = {"id": "123", "computerName": "HOST"}
        mock_client.search_agents.return_value = [agent]
        resolver = IdentifierResolver(mock_client, self.mock_logger)
        result_agent, metadata = resolver.resolve("HOST")
        assert result_agent == agent
        assert metadata.resolution_method == "direct"
        assert metadata.successful_strategy == "computerName"
        assert metadata.fallback_chain_attempted == ["computerName"]
        assert metadata.confidence_score is None

    def test_resolve_zero_results_hostname_triggers_fallback(self):
        mock_client = MagicMock()
        agent = {"id": "456", "uuid": "nonexistent"}
        # Primary (computerName) returns empty, fallback uuid returns the agent
        mock_client.search_agents.side_effect = [[], [agent]]
        resolver = IdentifierResolver(mock_client, self.mock_logger)
        result_agent, metadata = resolver.resolve("nonexistent")
        assert result_agent == agent
        assert metadata.resolution_method == "fallback"
        assert metadata.successful_strategy == "uuid"
        assert metadata.fallback_chain_attempted == ["computerName", "uuid"]
        assert metadata.confidence_score is None

    def test_resolve_agent_id_zero_results_no_fallback(self):
        mock_client = MagicMock()
        mock_client.search_agents.return_value = []
        resolver = IdentifierResolver(mock_client, self.mock_logger)
        result_agent, metadata = resolver.resolve("1234567890123456789")
        assert result_agent is None
        assert metadata.resolution_method == "error"
        assert metadata.successful_strategy == ""
        assert metadata.fallback_chain_attempted == ["ids"]
        # Only one call — no fallback attempted
        mock_client.search_agents.assert_called_once_with({"ids": "1234567890123456789"})

    def test_resolve_all_strategies_exhausted_returns_error(self):
        mock_client = MagicMock()
        # hostname fallback chain: computerName -> uuid -> networkInterfaceInet__contains
        # All return empty
        mock_client.search_agents.return_value = []
        resolver = IdentifierResolver(mock_client, self.mock_logger)
        result_agent, metadata = resolver.resolve("nonexistent-host")
        assert result_agent is None
        assert metadata.resolution_method == "error"
        assert metadata.successful_strategy == ""
        assert metadata.fallback_chain_attempted == [
            "computerName", "uuid", "networkInterfaceInet__contains"
        ]

    def test_resolve_multi_result_triggers_scoring(self):
        mock_client = MagicMock()
        agents = [
            {"id": "1", "computerName": "WORKSTATION-01"},
            {"id": "2", "computerName": "WORKSTATION-02"},
        ]
        mock_client.search_agents.return_value = agents
        resolver = IdentifierResolver(mock_client, self.mock_logger)
        result_agent, metadata = resolver.resolve("WORKSTATION-01")
        # Scorer should pick the exact match
        assert result_agent == agents[0]
        assert metadata.resolution_method == "scored"
        assert metadata.successful_strategy == "computerName"
        assert metadata.confidence_score is not None
        assert metadata.confidence_score >= 0.7

    def test_classify_strips_whitespace(self):
        resolver = IdentifierResolver(MagicMock(), self.mock_logger)
        assert resolver.classify("  192.168.1.1  ") == "ip"
        assert resolver.classify("  WORKSTATION-01  ") == "hostname"

    def test_resolve_fallback_logs_transitions(self):
        mock_client = MagicMock()
        agent = {"id": "1", "computerName": "host1"}
        # Primary (computerName) returns empty, first fallback (uuid) returns agent
        mock_client.search_agents.side_effect = [[], [agent]]
        resolver = IdentifierResolver(mock_client, self.mock_logger)
        resolver.resolve("host1")
        # Verify INFO log was emitted for the fallback transition
        self.mock_logger.info.assert_called()

    def test_resolve_direct_single_match_no_scorer_no_fallback(self):
        """Direct single-match returns without fallback or scoring (Req 5.1)."""
        mock_client = MagicMock()
        agent = {"id": "abc", "computerName": "MY-SERVER"}
        mock_client.search_agents.return_value = [agent]
        resolver = IdentifierResolver(mock_client, self.mock_logger)

        with patch.object(resolver.scorer, "score_agents") as mock_scorer:
            result_agent, metadata = resolver.resolve("MY-SERVER")

        # Single match returned directly
        assert result_agent == agent
        assert metadata.resolution_method == "direct"
        assert metadata.successful_strategy == "computerName"
        assert metadata.confidence_score is None
        # Scorer was never invoked
        mock_scorer.assert_not_called()
        # Only one API call made (no fallback)
        mock_client.search_agents.assert_called_once()

    def test_resolve_zero_result_traverses_full_fallback_chain(self):
        """Zero-result on primary triggers fallback chain traversal (Req 1.1, 1.3)."""
        mock_client = MagicMock()
        agent = {"id": "99", "computerName": "target", "networkInterfaces": [{"inet": ["10.0.0.5"]}]}
        # hostname chain: computerName (0) → uuid (0) → networkInterfaceInet__contains (1)
        mock_client.search_agents.side_effect = [[], [], [agent]]
        resolver = IdentifierResolver(mock_client, self.mock_logger)

        result_agent, metadata = resolver.resolve("target")

        assert result_agent == agent
        assert metadata.resolution_method == "fallback"
        assert metadata.successful_strategy == "networkInterfaceInet__contains"
        assert metadata.fallback_chain_attempted == [
            "computerName", "uuid", "networkInterfaceInet__contains"
        ]
        # Verify all three queries were made in order
        assert mock_client.search_agents.call_count == 3

    def test_resolve_fallback_multi_result_scoring_failure_continues(self):
        """Fallback with multi-result scoring failure continues to next strategy (Req 4.1, 4.2)."""
        mock_client = MagicMock()
        # hostname chain: computerName → uuid → networkInterfaceInet__contains
        # Primary (computerName): 0 results
        # First fallback (uuid): 2 agents that TIE (scoring fails)
        # Second fallback (networkInterfaceInet__contains): 1 agent (success)
        tied_agent_1 = {"id": "1", "uuid": "aaa"}
        tied_agent_2 = {"id": "2", "uuid": "aaa"}  # Same uuid → tie
        final_agent = {"id": "3", "computerName": "target", "networkInterfaces": [{"inet": ["10.0.0.1"]}]}

        mock_client.search_agents.side_effect = [
            [],                          # Primary computerName → 0 results
            [tied_agent_1, tied_agent_2],  # Fallback uuid → 2 results (tie)
            [final_agent],               # Fallback networkInterfaceInet__contains → 1 result
        ]
        resolver = IdentifierResolver(mock_client, self.mock_logger)

        result_agent, metadata = resolver.resolve("target")

        # Should have continued past the tie and found the agent on the third strategy
        assert result_agent == final_agent
        assert metadata.resolution_method == "fallback"
        assert metadata.successful_strategy == "networkInterfaceInet__contains"
        assert metadata.fallback_chain_attempted == [
            "computerName", "uuid", "networkInterfaceInet__contains"
        ]
        # All three API calls were made
        assert mock_client.search_agents.call_count == 3

    def test_resolve_multi_result_scoring_selects_best(self):
        """Multi-result triggers scoring and picks the best match (Req 2.5)."""
        mock_client = MagicMock()
        # Two agents with distinct computerNames — one matches identifier closely
        agents = [
            {"id": "1", "computerName": "web-server-prod"},
            {"id": "2", "computerName": "web-server-production-01"},
        ]
        mock_client.search_agents.return_value = agents
        resolver = IdentifierResolver(mock_client, self.mock_logger)

        result_agent, metadata = resolver.resolve("web-server-prod")

        # Scorer should select the exact match
        assert result_agent == agents[0]
        assert metadata.resolution_method == "scored"
        assert metadata.successful_strategy == "computerName"
        assert metadata.confidence_score is not None
        assert metadata.confidence_score >= 0.7
        # Only one API call — scoring resolved it without fallback
        mock_client.search_agents.assert_called_once()

    def test_resolve_agent_id_zero_results_returns_error_immediately(self):
        """agent_id with zero results returns error immediately, no fallback (Req 5.3)."""
        mock_client = MagicMock()
        mock_client.search_agents.return_value = []
        resolver = IdentifierResolver(mock_client, self.mock_logger)

        result_agent, metadata = resolver.resolve("9876543210")

        assert result_agent is None
        assert metadata.resolution_method == "error"
        assert metadata.successful_strategy == ""
        assert metadata.fallback_chain_attempted == ["ids"]
        assert metadata.confidence_score is None
        # Only one API call made — no fallback
        mock_client.search_agents.assert_called_once_with({"ids": "9876543210"})

    def test_resolve_all_strategies_exhausted_returns_error_with_full_chain(self):
        """All strategies exhausted returns error with full chain in metadata (Req 1.3)."""
        mock_client = MagicMock()
        # IP fallback chain: networkInterfaceInet__contains → computerName → uuid
        # All return empty
        mock_client.search_agents.return_value = []
        resolver = IdentifierResolver(mock_client, self.mock_logger)

        result_agent, metadata = resolver.resolve("10.20.30.40")

        assert result_agent is None
        assert metadata.resolution_method == "error"
        assert metadata.successful_strategy == ""
        assert metadata.fallback_chain_attempted == [
            "networkInterfaceInet__contains", "computerName", "uuid"
        ]
        assert metadata.confidence_score is None
        # 3 API calls: primary + 2 fallback strategies
        assert mock_client.search_agents.call_count == 3
