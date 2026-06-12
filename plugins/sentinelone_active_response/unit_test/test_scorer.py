import sys
import os

sys.path.append(os.path.abspath("../"))

from komand_sentinelone_active_response.util.scorer import (
    BestMatchScorer,
    ScoringResult,
    CONFIDENCE_THRESHOLD,
    QUERY_PARAM_TO_AGENT_FIELD,
)


class TestComputeScore:
    def setup_method(self):
        self.scorer = BestMatchScorer()

    def test_identical_strings_returns_1(self):
        assert self.scorer.compute_score("hello", "hello") == 1.0

    def test_case_insensitive_match_returns_1(self):
        assert self.scorer.compute_score("Hello", "hello") == 1.0
        assert self.scorer.compute_score("WORKSTATION-01", "workstation-01") == 1.0

    def test_completely_different_strings_returns_low_score(self):
        score = self.scorer.compute_score("abc", "xyz")
        assert score < 0.5


class TestScoreAgents:
    def setup_method(self):
        self.scorer = BestMatchScorer()

    def test_selects_unique_winner_above_threshold(self):
        agents = [
            {"id": "1", "computerName": "WORKSTATION-01"},
            {"id": "2", "computerName": "SERVER-99"},
        ]
        result = self.scorer.score_agents("WORKSTATION-01", agents, "computerName")
        assert result.is_success
        assert result.selected_agent == agents[0]
        assert result.confidence_score >= CONFIDENCE_THRESHOLD
        assert result.error is None

    def test_returns_error_when_below_threshold(self):
        agents = [
            {"id": "1", "computerName": "alpha"},
            {"id": "2", "computerName": "beta"},
        ]
        result = self.scorer.score_agents("zzzzzzzzzzz", agents, "computerName")
        assert not result.is_success
        assert result.selected_agent is None
        assert result.confidence_score < CONFIDENCE_THRESHOLD
        assert "confidence threshold" in result.error

    def test_returns_error_on_tie(self):
        agents = [
            {"id": "1", "computerName": "host"},
            {"id": "2", "computerName": "host"},
        ]
        result = self.scorer.score_agents("host", agents, "computerName")
        assert not result.is_success
        assert result.selected_agent is None
        assert "tie" in result.error.lower()
        assert result.tied_agents is not None
        assert len(result.tied_agents) == 2


class TestExtractField:
    def setup_method(self):
        self.scorer = BestMatchScorer()

    def test_extract_ip_address(self):
        agent = {
            "networkInterfaces": [{"inet": ["192.168.1.100", "10.0.0.1"], "physical": "aa:bb:cc:dd:ee:ff"}]
        }
        result = BestMatchScorer._extract_field(agent, "_ip_address")
        assert result == "192.168.1.100"

    def test_extract_mac_address(self):
        agent = {
            "networkInterfaces": [{"inet": ["192.168.1.100"], "physical": "aa:bb:cc:dd:ee:ff"}]
        }
        result = BestMatchScorer._extract_field(agent, "_mac_address")
        assert result == "aa:bb:cc:dd:ee:ff"

    def test_extract_standard_field(self):
        agent = {"computerName": "WORKSTATION-01", "id": "123"}
        result = BestMatchScorer._extract_field(agent, "computerName")
        assert result == "WORKSTATION-01"

    def test_extract_ip_missing_network_interfaces(self):
        agent = {}
        result = BestMatchScorer._extract_field(agent, "_ip_address")
        assert result == ""

    def test_extract_mac_missing_network_interfaces(self):
        agent = {}
        result = BestMatchScorer._extract_field(agent, "_mac_address")
        assert result == ""

    def test_extract_standard_field_missing(self):
        agent = {"id": "123"}
        result = BestMatchScorer._extract_field(agent, "computerName")
        assert result == ""
