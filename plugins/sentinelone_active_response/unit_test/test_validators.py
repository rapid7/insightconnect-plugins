import sys
import os

sys.path.append(os.path.abspath("../"))

import pytest
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_sentinelone_active_response.util.validators import InputValidator


class TestInputValidator:
    def test_valid_inputs_pass(self):
        # Should not raise for valid inputs
        InputValidator.validate_execute_response_inputs("WORKSTATION-01", "contain", 120, 10)

    def test_valid_all_intents(self):
        for intent in ["contain", "uncontain", "status", "info"]:
            InputValidator.validate_execute_response_inputs("host", intent, 60, 5)

    def test_empty_identifier_raises(self):
        with pytest.raises(PluginException):
            InputValidator.validate_execute_response_inputs("", "contain", 120, 10)

    def test_whitespace_identifier_raises(self):
        with pytest.raises(PluginException):
            InputValidator.validate_execute_response_inputs("   ", "contain", 120, 10)

    def test_none_identifier_raises(self):
        with pytest.raises(PluginException):
            InputValidator.validate_execute_response_inputs(None, "contain", 120, 10)

    def test_invalid_intent_raises(self):
        with pytest.raises(PluginException):
            InputValidator.validate_execute_response_inputs("host", "invalid", 120, 10)

    def test_zero_timeout_raises(self):
        with pytest.raises(PluginException):
            InputValidator.validate_execute_response_inputs("host", "contain", 0, 10)

    def test_negative_timeout_raises(self):
        with pytest.raises(PluginException):
            InputValidator.validate_execute_response_inputs("host", "contain", -5, 10)

    def test_zero_polling_interval_raises(self):
        with pytest.raises(PluginException):
            InputValidator.validate_execute_response_inputs("host", "contain", 120, 0)

    def test_negative_polling_interval_raises(self):
        with pytest.raises(PluginException):
            InputValidator.validate_execute_response_inputs("host", "contain", 120, -1)
