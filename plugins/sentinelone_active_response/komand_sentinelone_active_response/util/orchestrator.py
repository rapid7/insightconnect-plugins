import time
from datetime import datetime
from logging import Logger

from insightconnect_plugin_runtime.exceptions import PluginException

from .constants import (
    INTENT_CONTAIN,
    INTENT_UNCONTAIN,
    INTENT_STATUS,
    INTENT_INFO,
    STATUS_CONNECTED,
    STATUS_DISCONNECTED,
    RESULT_SUCCESS,
    RESULT_ALREADY_ACTIONED,
    RESULT_TIMEOUT,
    RESULT_ERROR,
)
from .resolver import ResolutionMetadata


class ResponseOrchestrator:
    """
    Coordinates the full response lifecycle.

    Methods:
    - execute(endpoint_identifier: str, intent: str, timeout: int, polling_interval: int) -> dict

    Internal phases:
    - _resolve_phase(identifier: str) -> dict
    - _validate_state(agent: dict, intent: str) -> tuple[bool, str]
    - _execute_phase(agent_id: str, intent: str) -> dict
    - _monitor_phase(agent_id: str, target_status: str, timeout: int, interval: int) -> dict
    - _build_report(agent: dict, intent: str, result_status: str, **kwargs) -> dict
    """

    def __init__(self, api_client, resolver, logger: Logger):
        """
        Initialize the orchestrator with dependencies.

        :param api_client: SentinelOneAPI client instance
        :param resolver: IdentifierResolver instance
        :param logger: Logger instance
        """
        self.api_client = api_client
        self.resolver = resolver
        self.logger = logger

    def execute(self, endpoint_identifier: str, intent: str, timeout: int, polling_interval: int) -> dict:
        """
        Execute the full response lifecycle for the given identifier and intent.

        :param endpoint_identifier: The endpoint identifier to resolve
        :param intent: The desired operation (contain, uncontain, status, info)
        :param timeout: Maximum seconds to wait during monitoring phase
        :param polling_interval: Seconds between status checks during monitoring
        :return: Structured response report dict
        """
        # Phase 1: Resolve the endpoint identifier to an agent
        resolve_result = self._resolve_phase(endpoint_identifier, intent)
        if resolve_result.get("result_status") == RESULT_ERROR:
            return resolve_result

        # Extract agent and resolution_metadata from the new return format
        agent = resolve_result["agent"]
        resolution_metadata = resolve_result["resolution_metadata"]

        # For status intent: return current status without state change
        if intent == INTENT_STATUS:
            return self._build_report(
                agent=agent,
                intent=intent,
                result_status=RESULT_SUCCESS,
                summary=f"Agent {agent.get('computerName', 'unknown')} network status is "
                f"{agent.get('networkStatus', 'unknown')}",
                resolution_metadata=resolution_metadata,
            )

        # For info intent: return full agent details without state change
        if intent == INTENT_INFO:
            return self._build_report(
                agent=agent,
                intent=intent,
                result_status=RESULT_SUCCESS,
                summary=f"Retrieved full details for agent {agent.get('computerName', 'unknown')}",
                resolution_metadata=resolution_metadata,
            )

        # Phase 2: Validate current state vs desired state
        should_skip, reason = self._validate_state(agent, intent)
        if should_skip:
            return self._build_report(
                agent=agent,
                intent=intent,
                result_status=RESULT_ALREADY_ACTIONED,
                summary=f"Agent {agent.get('computerName', 'unknown')} is {reason}",
                resolution_metadata=resolution_metadata,
            )

        # Phase 3: Execute the state-changing operation
        agent_id = agent.get("id", "")
        try:
            self._execute_phase(agent_id, intent)
        except PluginException as error:
            return self._build_report(
                agent=agent,
                intent=intent,
                result_status=RESULT_ERROR,
                error_cause=error.cause,
                error_remediation=error.assistance,
                summary=f"Failed to execute {intent} on agent {agent.get('computerName', 'unknown')}: {error.cause}",
                resolution_metadata=resolution_metadata,
            )

        # Phase 4: Monitor for confirmation
        target_status = STATUS_DISCONNECTED if intent == INTENT_CONTAIN else STATUS_CONNECTED
        monitor_result = self._monitor_phase(agent_id, target_status, timeout, polling_interval)

        # Build final report based on monitoring outcome
        if monitor_result.get("status") == "success":
            return self._build_report(
                agent=monitor_result.get("agent", agent),
                intent=intent,
                result_status=RESULT_SUCCESS,
                elapsed_time=monitor_result.get("elapsed_time", 0.0),
                summary=f"Successfully {'contained' if intent == INTENT_CONTAIN else 'uncontained'} endpoint "
                f"{agent.get('computerName', 'unknown')} "
                f"({target_status} confirmed in {monitor_result.get('elapsed_time', 0):.1f}s)",
                resolution_metadata=resolution_metadata,
            )

        if monitor_result.get("status") == "timeout":
            return self._build_report(
                agent=monitor_result.get("agent", agent),
                intent=intent,
                result_status=RESULT_TIMEOUT,
                elapsed_time=monitor_result.get("elapsed_time", 0.0),
                summary=f"Timeout waiting for agent {agent.get('computerName', 'unknown')} to reach "
                f"{target_status} status. Last observed: {monitor_result.get('last_status', 'unknown')}",
                resolution_metadata=resolution_metadata,
            )

        # Error during monitoring
        return self._build_report(
            agent=monitor_result.get("agent", agent),
            intent=intent,
            result_status=RESULT_ERROR,
            elapsed_time=monitor_result.get("elapsed_time", 0.0),
            error_cause=monitor_result.get("error_cause", ""),
            error_remediation=monitor_result.get("error_remediation", ""),
            summary=f"Error during monitoring of agent {agent.get('computerName', 'unknown')}: "
            f"{monitor_result.get('error_cause', 'unknown error')}",
            resolution_metadata=resolution_metadata,
        )

    def _resolve_phase(self, identifier: str, intent: str) -> dict:
        """
        Resolve an endpoint identifier to a single agent.

        :param identifier: The endpoint identifier string
        :param intent: The intent being executed (for error reports)
        :return: Dict with 'agent' and 'resolution_metadata' on success, or error report dict on failure
        """
        try:
            agent, metadata = self.resolver.resolve(identifier)
        except PluginException as error:
            error_metadata = ResolutionMetadata(
                resolution_method="error",
                successful_strategy="",
                fallback_chain_attempted=[],
                confidence_score=None,
            )
            return self._build_report(
                agent={},
                intent=intent,
                result_status=RESULT_ERROR,
                error_cause=error.cause,
                error_remediation=error.assistance,
                summary=f"Failed to resolve endpoint identifier '{identifier}': {error.cause}",
                resolution_metadata=error_metadata.to_dict(),
            )

        if agent is None:
            return self._build_report(
                agent={},
                intent=intent,
                result_status=RESULT_ERROR,
                error_cause="No matching agent found.",
                error_remediation=f"Verify the identifier '{identifier}' is correct and the agent is registered "
                f"in SentinelOne. Strategies attempted: {metadata.fallback_chain_attempted}",
                summary=f"No agent resolved for '{identifier}' after exhausting all strategies",
                resolution_metadata=metadata.to_dict(),
            )

        return {"agent": agent, "resolution_metadata": metadata.to_dict()}

    def _validate_state(self, agent: dict, intent: str) -> tuple:
        """
        Check if the agent is already in the desired state.

        :param agent: The resolved agent dict
        :param intent: The desired operation
        :return: Tuple of (should_skip: bool, reason: str)
        """
        network_status = agent.get("networkStatus", "")

        if intent == INTENT_CONTAIN and network_status == STATUS_DISCONNECTED:
            return (True, "already contained")

        if intent == INTENT_UNCONTAIN and network_status == STATUS_CONNECTED:
            return (True, "already connected")

        return (False, "")

    def _execute_phase(self, agent_id: str, intent: str) -> dict:
        """
        Execute the state-changing API call.

        :param agent_id: The SentinelOne agent ID
        :param intent: The desired operation (contain or uncontain)
        :return: API response dict
        :raises PluginException: If the API call fails
        """
        if intent == INTENT_CONTAIN:
            return self.api_client.disconnect_agents([agent_id])
        return self.api_client.connect_agents([agent_id])

    def _monitor_phase(self, agent_id: str, target_status: str, timeout: int, interval: int) -> dict:
        """
        Poll agent status until target state is reached or timeout expires.

        :param agent_id: The SentinelOne agent ID to monitor
        :param target_status: The desired network status to wait for
        :param timeout: Maximum seconds to poll
        :param interval: Seconds between polls
        :return: Dict with status, elapsed_time, agent, and optionally error info
        """
        start_time = time.time()
        last_status = ""
        last_agent = {}

        while True:
            elapsed = time.time() - start_time

            if elapsed >= timeout:
                return {
                    "status": "timeout",
                    "elapsed_time": elapsed,
                    "last_status": last_status,
                    "agent": last_agent,
                }

            try:
                agent = self.api_client.get_agent_by_id(agent_id)
                if not agent:
                    return {
                        "status": "error",
                        "elapsed_time": time.time() - start_time,
                        "error_cause": "Agent not found during monitoring.",
                        "error_remediation": "The agent may have been removed from the SentinelOne console.",
                        "agent": last_agent,
                    }

                last_agent = agent
                last_status = agent.get("networkStatus", "")

                if last_status == target_status:
                    return {
                        "status": "success",
                        "elapsed_time": time.time() - start_time,
                        "agent": agent,
                    }

            except PluginException as error:
                # Transient 5xx errors: log and continue polling
                error_cause_lower = (error.cause or "").lower()
                if "server error" in error_cause_lower or "unavailable" in error_cause_lower:
                    self.logger.warning(f"Transient error during monitoring (will retry): {error.cause}")
                else:
                    # Non-transient errors (401/403/404): abort immediately
                    return {
                        "status": "error",
                        "elapsed_time": time.time() - start_time,
                        "error_cause": error.cause,
                        "error_remediation": error.assistance,
                        "agent": last_agent,
                    }

            time.sleep(interval)

    def _build_report(self, agent: dict, intent: str, result_status: str, **kwargs) -> dict:
        """
        Construct the response_report dict with all required fields.

        :param agent: The raw agent dict from SentinelOne API
        :param intent: The action that was performed
        :param result_status: The outcome (success, already_actioned, timeout, error)
        :param kwargs: Additional fields (summary, elapsed_time, error_cause, error_remediation)
        :return: Structured response_report dict
        """
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

    @staticmethod
    def _extract_agent_details(agent: dict) -> dict:
        """
        Map SentinelOne agent fields to our agent_details schema.

        :param agent: Raw agent dict from SentinelOne API
        :return: Mapped agent_details dict
        """
        if not agent:
            return {}

        # Extract IP and MAC from networkInterfaces
        ip_address = ""
        mac_address = ""
        network_interfaces = agent.get("networkInterfaces", [])
        if network_interfaces:
            first_interface = network_interfaces[0]
            inet_list = first_interface.get("inet", [])
            if inet_list:
                ip_address = inet_list[0]
            mac_address = first_interface.get("physical", "")

        return {
            "agent_id": agent.get("id", ""),
            "hostname": agent.get("computerName", ""),
            "ip_address": ip_address,
            "mac_address": mac_address,
            "operating_system": agent.get("osName", ""),
            "network_status": agent.get("networkStatus", ""),
            "site_name": agent.get("siteName", ""),
            "group_name": agent.get("groupName", ""),
            "active_threats": agent.get("activeThreats", 0),
            "agent_version": agent.get("agentVersion", ""),
        }
