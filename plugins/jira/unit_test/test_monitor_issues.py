import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Callable, Optional
from unittest import TestCase, mock
from unittest.mock import patch

import timeout_decorator
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_jira.triggers.monitor_issues import MonitorIssues

import util


def timeout_pass(error_callback: Optional[Callable] = None):
    def func_timeout(func):
        def func_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except timeout_decorator.timeout_decorator.TimeoutError:
                if error_callback:
                    return error_callback()

                return None

        return func_wrapper

    return func_timeout


# Test class
class TestMonitorIssues(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.action = util.Util.default_connector(MonitorIssues())

    @timeout_pass(error_callback=util.Util.check_error_with_fields)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=util.MockTrigger.send)
    def test_monitor_issues_with_fields(self, mock_send: mock.Mock) -> None:
        action_params = {
            "get_attachments": False,
            "jql": "reporter='Bob Smith'",
            "interval": 60,
            "projects": ["projectName", "projectName"],
            "include_fields": True,
        }
        self.action.run(action_params)

    @timeout_pass(error_callback=util.Util.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=util.MockTrigger.send)
    def test_monitor_issues(self, mock_send: mock.Mock) -> None:
        action_params = {
            "get_attachments": False,
            "jql": "reporter='Bob Smith'",
            "interval": 60,
            "projects": ["projectName", "projectName"],
            "include_fields": False,
        }
        self.action.run(action_params)

    @timeout_pass(error_callback=util.Util.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=util.MockTrigger.send)
    def test_monitor_issues_invalid_project(self, mock_send: mock.Mock) -> None:
        action_params = {
            "get_attachments": False,
            "jql": "",
            "poll_timeout": 60,
            "projects": ["projectName2"],
        }
        with self.assertRaises(PluginException) as e:
            self.action.run(action_params)
        self.assertEqual(
            e.exception.cause,
            "Project 'projectName2' does not exist or the user does not have permission to access the project.",
        )
        self.assertEqual(
            e.exception.assistance,
            "Please provide a valid project ID/name or make sure the project is accessible to the user.",
        )

    @timeout_pass(error_callback=util.Util.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=util.MockTrigger.send)
    def test_monitor_issues_only_project(self, mock_send: mock.Mock) -> None:
        action_params = {
            "get_attachments": False,
            "jql": "",
            "interval": 60,
            "projects": ["projectName"],
        }
        self.action.run(action_params)

    @timeout_pass(error_callback=util.Util.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=util.MockTrigger.send)
    def test_monitor_issues_only_jql(self, mock_send: mock.Mock) -> None:
        action_params = {
            "get_attachments": False,
            "jql": "reporter='Bob Smith'",
            "interval": 60,
            "projects": "",
        }
        self.action.run(action_params)

    @timeout_pass(error_callback=util.Util.check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=util.MockTrigger.send)
    def test_monitor_issues_without_jql_and_project(self, mock_send: mock.Mock) -> None:
        action_params = {
            "get_attachments": False,
            "jql": "",
            "interval": 60,
            "projects": "",
        }
        self.action.run(action_params)
