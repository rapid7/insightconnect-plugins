import sys
import os

sys.path.append(os.path.abspath("../"))

from komand_sentinelone_active_response.util.fallback_chain import get_fallback_chain


class TestGetFallbackChain:
    def test_uuid_returns_correct_chain(self):
        assert get_fallback_chain("uuid") == ["computerName", "networkInterfaceInet__contains"]

    def test_hostname_returns_correct_chain(self):
        assert get_fallback_chain("hostname") == ["uuid", "networkInterfaceInet__contains"]

    def test_ip_returns_correct_chain(self):
        assert get_fallback_chain("ip") == ["computerName", "uuid"]

    def test_mac_returns_correct_chain(self):
        assert get_fallback_chain("mac") == ["computerName", "uuid"]

    def test_agent_id_returns_empty_chain(self):
        assert get_fallback_chain("agent_id") == []

    def test_unknown_classification_returns_empty_list(self):
        assert get_fallback_chain("unknown_type") == []
