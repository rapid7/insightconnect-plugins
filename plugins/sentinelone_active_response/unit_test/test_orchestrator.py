import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException

from komand_sentinelone_active_response.util.orchestrator import ResponseOrchestrator
from komand_sentinelone_active_response.util.resolver import ResolutionMetadata
from komand_sentinelone_active_response.util.constants import (
    INTENT_CONTAIN,
    INTENT_UNCONTAIN,
    INTENT_STATUS,
    INTENT_INFO,
    RESULT_SUCCESS,
    RESULT_ALREADY_ACTIONED,
    RESULT_TIMEOUT,
    RESULT_ERROR,
)

# --- Fixtures ---

AGENT_CONNECTED = {
    "id": "1234567890123456789",
    "computerName": "WORKSTATION-01",
    "networkStatus": "connected",
    "osName": "Windows 10 Pro",
    "siteName": "Default Site",
    "groupName": "Default Group",
    "activeThreats": 0,
    "agentVersion": "23.1.2.400",
    "networkInterfaces": [{"inet": ["192.168.1.100"], "physical": "00:1A:2B:3C:4D:5E"}],
}

AGENT_DISCONNECTED = {**AGENT_CONNECTED, "networkStatus": "disconnected"}

AGENT_SECOND = {
    "id": "9876543210987654321",
    "computerName": "WORKSTATION-02",
    "networkStatus": "connected",
    "osName": "Windows 11 Pro",
    "siteName": "Default Site",
    "groupName": "Default Group",
    "activeThreats": 0,
    "agentVersion": "23.1.2.400",
    "networkInterfaces": [{"inet": ["192.168.1.101"], "physical": "00:1A:2B:3C:4D:5F"}],
}


def _make_orchestrator(mock_client=None, mock_resolver=None):
    """Helper to create an orchestrator with mocked dependencies."""
    if mock_client is None:
        mock_client = MagicMock()
    if mock_resolver is None:
        mock_resolver = MagicMock()
    return ResponseOrchestrator(mock_client, mock_resolver, MagicMock())


def _direct_metadata(strategy="computerName"):
    """Helper to create a direct resolution metadata."""
    return ResolutionMetadata(
        resolution_method="direct",
        successful_strategy=strategy,
        fallback_chain_attempted=[strategy],
        confidence_score=None,
    )


def _error_metadata(strategies_attempted=None):
    """Helper to create an error resolution metadata."""
    if strategies_attempted is None:
        strategies_attempted = ["computerName"]
    return ResolutionMetadata(
        resolution_method="error",
        successful_strategy="",
        fallback_chain_attempted=strategies_attempted,
        confidence_score=None,
    )


class TestContainSuccessFlow:
    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    @patch("komand_sentinelone_active_response.util.orchestrator.time.time")
    def test_contain_success_flow(self, mock_time, mock_sleep):
        """Contain flow: resolve -> check state -> execute -> monitor -> success report."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        # Resolver returns a single connected agent
        mock_resolver.resolve.return_value = (AGENT_CONNECTED, _direct_metadata())

        # disconnect_agents succeeds
        mock_client.disconnect_agents.return_value = {"data": {"affected": 1}}

        # Monitoring: agent transitions to disconnected
        mock_client.get_agent_by_id.return_value = AGENT_DISCONNECTED

        # Time progression: start=0, first check=1 (within timeout)
        mock_time.side_effect = [0, 1, 1]

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION-01", INTENT_CONTAIN, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_SUCCESS
        assert report["action_performed"] == INTENT_CONTAIN
        assert report["network_status"] == "disconnected"
        assert "WORKSTATION-01" in report["summary"]
        mock_client.disconnect_agents.assert_called_once_with(["1234567890123456789"])
        mock_resolver.resolve.assert_called_once_with("WORKSTATION-01")


class TestUncontainSuccessFlow:
    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    @patch("komand_sentinelone_active_response.util.orchestrator.time.time")
    def test_uncontain_success_flow(self, mock_time, mock_sleep):
        """Uncontain flow: resolve -> check state -> execute -> monitor -> success report."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        # Resolver returns a single disconnected agent
        mock_resolver.resolve.return_value = (AGENT_DISCONNECTED, _direct_metadata())

        # connect_agents succeeds
        mock_client.connect_agents.return_value = {"data": {"affected": 1}}

        # Monitoring: agent transitions to connected
        mock_client.get_agent_by_id.return_value = AGENT_CONNECTED

        # Time progression
        mock_time.side_effect = [0, 1, 1]

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION-01", INTENT_UNCONTAIN, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_SUCCESS
        assert report["action_performed"] == INTENT_UNCONTAIN
        assert report["network_status"] == "connected"
        assert "WORKSTATION-01" in report["summary"]
        mock_client.connect_agents.assert_called_once_with(["1234567890123456789"])


class TestAlreadyActioned:
    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    def test_contain_already_actioned(self, mock_sleep):
        """Agent already disconnected, intent=contain -> skip API call."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        # Resolver returns an already-disconnected agent
        mock_resolver.resolve.return_value = (AGENT_DISCONNECTED, _direct_metadata())

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION-01", INTENT_CONTAIN, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_ALREADY_ACTIONED
        assert report["action_performed"] == INTENT_CONTAIN
        assert "already contained" in report["summary"]
        # No state-changing API calls should be made
        mock_client.disconnect_agents.assert_not_called()
        mock_client.connect_agents.assert_not_called()

    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    def test_uncontain_already_actioned(self, mock_sleep):
        """Agent already connected, intent=uncontain -> skip API call."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        # Resolver returns an already-connected agent
        mock_resolver.resolve.return_value = (AGENT_CONNECTED, _direct_metadata())

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION-01", INTENT_UNCONTAIN, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_ALREADY_ACTIONED
        assert report["action_performed"] == INTENT_UNCONTAIN
        assert "already connected" in report["summary"]
        mock_client.disconnect_agents.assert_not_called()
        mock_client.connect_agents.assert_not_called()


class TestTimeout:
    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    @patch("komand_sentinelone_active_response.util.orchestrator.time.time")
    def test_timeout(self, mock_time, mock_sleep):
        """Polling exceeds timeout -> timeout report."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        # Resolver returns connected agent
        mock_resolver.resolve.return_value = (AGENT_CONNECTED, _direct_metadata())

        # disconnect succeeds
        mock_client.disconnect_agents.return_value = {"data": {"affected": 1}}

        # Agent stays in "connecting" state (never reaches disconnected)
        connecting_agent = {**AGENT_CONNECTED, "networkStatus": "connecting"}
        mock_client.get_agent_by_id.return_value = connecting_agent

        # Time progression: start=0, first poll elapsed=0.5 (continue), second poll elapsed=2 (exceeds timeout=1)
        mock_time.side_effect = [0, 0.5, 2]

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION-01", INTENT_CONTAIN, timeout=1, polling_interval=1)

        assert report["result_status"] == RESULT_TIMEOUT
        assert report["action_performed"] == INTENT_CONTAIN
        assert "Timeout" in report["summary"] or "timeout" in report["summary"].lower()


class TestNoMatch:
    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    def test_no_match_error(self, mock_sleep):
        """Empty agent list -> error report with identifier."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        # Resolver returns no agent (resolution failed)
        mock_resolver.resolve.return_value = (None, _error_metadata(["computerName", "uuid", "networkInterfaceInet__contains"]))

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("nonexistent-host", INTENT_CONTAIN, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_ERROR
        assert "nonexistent-host" in report["summary"]
        # No state-changing calls
        mock_client.disconnect_agents.assert_not_called()
        mock_client.connect_agents.assert_not_called()


class TestMultiMatch:
    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    def test_multi_match_error(self, mock_sleep):
        """Scoring failure (ambiguous) -> error report."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        # Resolver returns None when scoring fails (ambiguous tie or below threshold)
        mock_resolver.resolve.return_value = (None, _error_metadata(["computerName"]))

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION", INTENT_CONTAIN, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_ERROR
        assert "No matching agent found" in report["error_cause"] or "No agent" in report["summary"]
        mock_client.disconnect_agents.assert_not_called()


class TestStatusIntent:
    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    def test_status_intent(self, mock_sleep):
        """Status intent returns status report without state change."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        mock_resolver.resolve.return_value = (AGENT_CONNECTED, _direct_metadata())

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION-01", INTENT_STATUS, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_SUCCESS
        assert report["action_performed"] == INTENT_STATUS
        assert "connected" in report["summary"]
        # No state-changing calls
        mock_client.disconnect_agents.assert_not_called()
        mock_client.connect_agents.assert_not_called()
        mock_client.get_agent_by_id.assert_not_called()


class TestInfoIntent:
    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    def test_info_intent(self, mock_sleep):
        """Info intent returns full agent details report without state change."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        mock_resolver.resolve.return_value = (AGENT_CONNECTED, _direct_metadata())

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION-01", INTENT_INFO, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_SUCCESS
        assert report["action_performed"] == INTENT_INFO
        assert "WORKSTATION-01" in report["summary"]
        # Agent details should be populated
        assert report["agent"]["agent_id"] == "1234567890123456789"
        assert report["agent"]["hostname"] == "WORKSTATION-01"
        assert report["agent"]["ip_address"] == "192.168.1.100"
        assert report["agent"]["mac_address"] == "00:1A:2B:3C:4D:5E"
        # No state-changing calls
        mock_client.disconnect_agents.assert_not_called()
        mock_client.connect_agents.assert_not_called()
        mock_client.get_agent_by_id.assert_not_called()


class TestApiErrorDuringExecution:
    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    def test_api_error_during_execution(self, mock_sleep):
        """API error during execution -> error propagated to report."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        # Resolver returns connected agent
        mock_resolver.resolve.return_value = (AGENT_CONNECTED, _direct_metadata())

        # disconnect_agents raises PluginException
        mock_client.disconnect_agents.side_effect = PluginException(
            cause="SentinelOne server error.",
            assistance="An internal error occurred on the SentinelOne side.",
        )

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION-01", INTENT_CONTAIN, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_ERROR
        assert "SentinelOne server error" in report["error_cause"]
        assert report["action_performed"] == INTENT_CONTAIN


class TestTransientErrorDuringMonitoring:
    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    @patch("komand_sentinelone_active_response.util.orchestrator.time.time")
    def test_transient_error_during_monitoring(self, mock_time, mock_sleep):
        """Transient error during monitoring -> polling continues and eventually succeeds."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        # Resolver returns connected agent
        mock_resolver.resolve.return_value = (AGENT_CONNECTED, _direct_metadata())

        # disconnect succeeds
        mock_client.disconnect_agents.return_value = {"data": {"affected": 1}}

        # First poll raises transient error, second poll returns target status
        mock_client.get_agent_by_id.side_effect = [
            PluginException(
                cause="SentinelOne server error.",
                assistance="An internal error occurred on the SentinelOne side.",
            ),
            AGENT_DISCONNECTED,
        ]

        # Time progression: start=0, first poll=1 (transient error, retry), second poll=2 (success), final=2
        mock_time.side_effect = [0, 1, 2, 2]

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION-01", INTENT_CONTAIN, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_SUCCESS
        assert report["action_performed"] == INTENT_CONTAIN
        # Verify polling was attempted twice
        assert mock_client.get_agent_by_id.call_count == 2


class TestResolvePhaseResolutionMetadataOnSuccess:
    """Test that _resolve_phase returns resolution_metadata on successful resolution."""

    def test_resolve_phase_success_has_resolution_metadata(self):
        """Successful resolution includes resolution_metadata with all expected fields."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        metadata = _direct_metadata("computerName")
        mock_resolver.resolve.return_value = (AGENT_CONNECTED, metadata)

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        result = orchestrator._resolve_phase("WORKSTATION-01", INTENT_CONTAIN)

        # Should not be an error report
        assert "result_status" not in result
        assert "agent" in result
        assert "resolution_metadata" in result

        rm = result["resolution_metadata"]
        assert rm["resolution_method"] == "direct"
        assert rm["successful_strategy"] == "computerName"
        assert rm["fallback_chain_attempted"] == ["computerName"]
        assert rm["confidence_score"] is None

    def test_resolve_phase_scored_has_confidence_score(self):
        """Scored resolution includes confidence_score in resolution_metadata."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        metadata = ResolutionMetadata(
            resolution_method="scored",
            successful_strategy="computerName",
            fallback_chain_attempted=["computerName"],
            confidence_score=0.92,
        )
        mock_resolver.resolve.return_value = (AGENT_CONNECTED, metadata)

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        result = orchestrator._resolve_phase("WORKSTATION-01", INTENT_CONTAIN)

        assert "resolution_metadata" in result
        rm = result["resolution_metadata"]
        assert rm["resolution_method"] == "scored"
        assert rm["confidence_score"] == 0.92
        assert rm["successful_strategy"] == "computerName"

    def test_resolve_phase_fallback_has_full_chain(self):
        """Fallback resolution includes all attempted strategies in chain."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        metadata = ResolutionMetadata(
            resolution_method="fallback",
            successful_strategy="networkInterfaceInet__contains",
            fallback_chain_attempted=["uuid", "computerName", "networkInterfaceInet__contains"],
            confidence_score=None,
        )
        mock_resolver.resolve.return_value = (AGENT_CONNECTED, metadata)

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        result = orchestrator._resolve_phase("some-uuid-value", INTENT_CONTAIN)

        assert "resolution_metadata" in result
        rm = result["resolution_metadata"]
        assert rm["resolution_method"] == "fallback"
        assert rm["successful_strategy"] == "networkInterfaceInet__contains"
        assert rm["fallback_chain_attempted"] == ["uuid", "computerName", "networkInterfaceInet__contains"]
        assert rm["confidence_score"] is None


class TestResolvePhaseResolutionMetadataOnError:
    """Test that _resolve_phase returns resolution_metadata on error."""

    def test_resolve_phase_no_agent_has_error_metadata(self):
        """When resolver returns None, error report has resolution_metadata with method='error'."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        metadata = _error_metadata(["computerName", "uuid", "networkInterfaceInet__contains"])
        mock_resolver.resolve.return_value = (None, metadata)

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        result = orchestrator._resolve_phase("nonexistent-host", INTENT_CONTAIN)

        assert result["result_status"] == RESULT_ERROR
        assert "resolution_metadata" in result

        rm = result["resolution_metadata"]
        assert rm["resolution_method"] == "error"
        assert rm["successful_strategy"] == ""
        assert rm["fallback_chain_attempted"] == ["computerName", "uuid", "networkInterfaceInet__contains"]
        assert rm["confidence_score"] is None

    def test_resolve_phase_plugin_exception_has_error_metadata(self):
        """When resolver raises PluginException, error report has resolution_metadata."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        mock_resolver.resolve.side_effect = PluginException(
            cause="Connection timeout.",
            assistance="Check network connectivity.",
        )

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        result = orchestrator._resolve_phase("some-host", INTENT_CONTAIN)

        assert result["result_status"] == RESULT_ERROR
        assert "resolution_metadata" in result

        rm = result["resolution_metadata"]
        assert rm["resolution_method"] == "error"
        assert rm["successful_strategy"] == ""
        assert rm["fallback_chain_attempted"] == []
        assert rm["confidence_score"] is None


class TestBuildReportResolutionMetadata:
    """Test that _build_report always includes resolution_metadata field."""

    def test_build_report_with_explicit_metadata(self):
        """_build_report includes provided resolution_metadata."""
        orchestrator = _make_orchestrator()
        metadata_dict = {
            "resolution_method": "fallback",
            "successful_strategy": "uuid",
            "fallback_chain_attempted": ["computerName", "uuid"],
            "confidence_score": None,
        }

        report = orchestrator._build_report(
            agent=AGENT_CONNECTED,
            intent=INTENT_CONTAIN,
            result_status=RESULT_SUCCESS,
            summary="Test",
            resolution_metadata=metadata_dict,
        )

        assert "resolution_metadata" in report
        assert report["resolution_metadata"] == metadata_dict

    def test_build_report_without_metadata_uses_default(self):
        """_build_report uses default resolution_metadata when none provided."""
        orchestrator = _make_orchestrator()

        report = orchestrator._build_report(
            agent=AGENT_CONNECTED,
            intent=INTENT_CONTAIN,
            result_status=RESULT_SUCCESS,
            summary="Test without metadata",
        )

        assert "resolution_metadata" in report
        rm = report["resolution_metadata"]
        assert rm["resolution_method"] == "direct"
        assert rm["successful_strategy"] == ""
        assert rm["fallback_chain_attempted"] == []
        assert rm["confidence_score"] is None

    def test_build_report_error_path_includes_metadata(self):
        """_build_report for error path includes resolution_metadata."""
        orchestrator = _make_orchestrator()
        metadata_dict = {
            "resolution_method": "error",
            "successful_strategy": "",
            "fallback_chain_attempted": ["computerName", "uuid"],
            "confidence_score": None,
        }

        report = orchestrator._build_report(
            agent={},
            intent=INTENT_CONTAIN,
            result_status=RESULT_ERROR,
            error_cause="No matching agent found.",
            error_remediation="Check identifier.",
            summary="Failed to resolve",
            resolution_metadata=metadata_dict,
        )

        assert "resolution_metadata" in report
        assert report["resolution_metadata"]["resolution_method"] == "error"
        assert report["resolution_metadata"]["fallback_chain_attempted"] == ["computerName", "uuid"]


class TestExecuteFlowResolutionMetadata:
    """Test full execute() flow includes resolution_metadata in final report."""

    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    @patch("komand_sentinelone_active_response.util.orchestrator.time.time")
    def test_contain_success_includes_resolution_metadata(self, mock_time, mock_sleep):
        """Successful contain flow report includes resolution_metadata."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        metadata = _direct_metadata("computerName")
        mock_resolver.resolve.return_value = (AGENT_CONNECTED, metadata)
        mock_client.disconnect_agents.return_value = {"data": {"affected": 1}}
        mock_client.get_agent_by_id.return_value = AGENT_DISCONNECTED
        mock_time.side_effect = [0, 1, 1]

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION-01", INTENT_CONTAIN, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_SUCCESS
        assert "resolution_metadata" in report
        rm = report["resolution_metadata"]
        assert rm["resolution_method"] == "direct"
        assert rm["successful_strategy"] == "computerName"
        assert rm["fallback_chain_attempted"] == ["computerName"]
        assert rm["confidence_score"] is None

    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    def test_error_flow_includes_resolution_metadata(self, mock_sleep):
        """Error flow (no agent found) report includes resolution_metadata."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        metadata = _error_metadata(["computerName", "uuid"])
        mock_resolver.resolve.return_value = (None, metadata)

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("bad-host", INTENT_CONTAIN, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_ERROR
        assert "resolution_metadata" in report
        rm = report["resolution_metadata"]
        assert rm["resolution_method"] == "error"
        assert rm["successful_strategy"] == ""
        assert rm["fallback_chain_attempted"] == ["computerName", "uuid"]
        assert rm["confidence_score"] is None

    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    def test_already_actioned_includes_resolution_metadata(self, mock_sleep):
        """Already-actioned flow report includes resolution_metadata."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        metadata = _direct_metadata("computerName")
        mock_resolver.resolve.return_value = (AGENT_DISCONNECTED, metadata)

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION-01", INTENT_CONTAIN, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_ALREADY_ACTIONED
        assert "resolution_metadata" in report
        rm = report["resolution_metadata"]
        assert rm["resolution_method"] == "direct"
        assert rm["successful_strategy"] == "computerName"

    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    @patch("komand_sentinelone_active_response.util.orchestrator.time.time")
    def test_timeout_includes_resolution_metadata(self, mock_time, mock_sleep):
        """Timeout flow report includes resolution_metadata."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        metadata = ResolutionMetadata(
            resolution_method="fallback",
            successful_strategy="uuid",
            fallback_chain_attempted=["computerName", "uuid"],
            confidence_score=None,
        )
        mock_resolver.resolve.return_value = (AGENT_CONNECTED, metadata)
        mock_client.disconnect_agents.return_value = {"data": {"affected": 1}}

        connecting_agent = {**AGENT_CONNECTED, "networkStatus": "connecting"}
        mock_client.get_agent_by_id.return_value = connecting_agent
        mock_time.side_effect = [0, 0.5, 2]

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION-01", INTENT_CONTAIN, timeout=1, polling_interval=1)

        assert report["result_status"] == RESULT_TIMEOUT
        assert "resolution_metadata" in report
        rm = report["resolution_metadata"]
        assert rm["resolution_method"] == "fallback"
        assert rm["successful_strategy"] == "uuid"
        assert rm["fallback_chain_attempted"] == ["computerName", "uuid"]

    @patch("komand_sentinelone_active_response.util.orchestrator.time.sleep")
    def test_scored_resolution_metadata_in_execute(self, mock_sleep):
        """Execute with scored resolution includes confidence_score in metadata."""
        mock_client = MagicMock()
        mock_resolver = MagicMock()

        metadata = ResolutionMetadata(
            resolution_method="scored",
            successful_strategy="computerName",
            fallback_chain_attempted=["computerName"],
            confidence_score=0.85,
        )
        mock_resolver.resolve.return_value = (AGENT_CONNECTED, metadata)

        orchestrator = _make_orchestrator(mock_client, mock_resolver)
        report = orchestrator.execute("WORKSTATION-01", INTENT_STATUS, timeout=30, polling_interval=5)

        assert report["result_status"] == RESULT_SUCCESS
        assert "resolution_metadata" in report
        rm = report["resolution_metadata"]
        assert rm["resolution_method"] == "scored"
        assert rm["confidence_score"] == 0.85
        assert rm["successful_strategy"] == "computerName"
        assert rm["fallback_chain_attempted"] == ["computerName"]
