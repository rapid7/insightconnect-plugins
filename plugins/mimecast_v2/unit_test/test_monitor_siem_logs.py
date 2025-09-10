import os
import sys
from typing import Any, Dict, Optional

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from freezegun import freeze_time
from icon_mimecast_v2.tasks.monitor_siem_logs import MonitorSiemLogs
from icon_mimecast_v2.tasks.monitor_siem_logs.schema import MonitorSiemLogsOutput
from jsonschema import validate
from parameterized import parameterized

from util import Util

STUB_STATE_EXPECTED = {
    "query_config": {
        "attachment protect": {
            "caught_up": True,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "NDU1NA==",
            "query_date": "2000-01-06",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "receipt": {
            "caught_up": True,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "NDU1NA==",
            "query_date": "2000-01-06",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "ttp_attachment": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_impersonation": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_url": {"caught_up": True, "query_date": "2000-01-07T00:00:00+00:00"},
        "url protect": {
            "caught_up": True,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "NDU1NA==",
            "query_date": "2000-01-06",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
    }
}

STUB_STATE_EXPECTED_DUPLICATES = {
    "query_config": {
        "attachment protect": {
            "caught_up": True,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "NDU1NA==",
            "query_date": "2000-01-03",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "receipt": {
            "caught_up": True,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "NDU1NA==",
            "query_date": "2000-01-03",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "ttp_attachment": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_impersonation": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_url": {"caught_up": True, "query_date": "2000-01-07T00:00:00+00:00"},
        "url protect": {
            "caught_up": True,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "NDU1NA==",
            "query_date": "2000-01-03",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
    }
}

STUB_STATE_EXPECTED_INVALID_RECEIPT = {
    "query_config": {
        "attachment protect": {
            "caught_up": True,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "NDU1NA==",
            "query_date": "2000-01-06",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "receipt": {
            "caught_up": True,
            "log_hashes": [],
            "next_page": "NDU1NA==",
            "query_date": "2000-01-05",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "ttp_attachment": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_impersonation": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_url": {"caught_up": True, "query_date": "2000-01-07T00:00:00+00:00"},
        "url protect": {
            "caught_up": True,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "NDU1NA==",
            "query_date": "2000-01-06",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
    }
}

STUB_STATE_BATCH_DUPLICATES = {
    "query_config": {
        "attachment protect": {
            "caught_up": True,
            "log_hashes": [],
            "next_page": "NDU1NA==",
            "query_date": "2000-01-02",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "receipt": {
            "caught_up": True,
            "log_hashes": [],
            "next_page": "NDU1NA==",
            "query_date": "2000-01-02",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "url protect": {
            "caught_up": True,
            "log_hashes": [],
            "next_page": "NDU1NA==",
            "query_date": "2000-01-02",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
    }
}

STUB_STATE_PAGINATING = {
    "query_config": {
        "attachment protect": {
            "caught_up": False,
            "next_page": "NDU1NA==",
            "query_date": "2000-01-06",
        },
        "receipt": {
            "caught_up": False,
            "next_page": "NDU1NA==",
            "query_date": "2000-01-06",
        },
        "url protect": {
            "caught_up": False,
            "next_page": "NDU1NA==",
            "query_date": "2000-01-06",
        },
    },
}

STUB_STATE_PAGINATING_CUTOFF = {
    "query_config": {
        "attachment protect": {
            "caught_up": False,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
        },
        "receipt": {
            "caught_up": False,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
        },
        "url protect": {
            "caught_up": False,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
        },
    },
}

STUB_STATE_PAGINATING_CUTOFF_EXPECTED = {
    "query_config": {
        "attachment protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "saved_file_url": None,
            "saved_file_position": 0,
        },
        "receipt": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "saved_file_url": None,
            "saved_file_position": 0,
        },
        "ttp_attachment": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_impersonation": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_url": {"caught_up": True, "query_date": "2000-01-07T00:00:00+00:00"},
        "url protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "saved_file_url": None,
            "saved_file_position": 0,
        },
    }
}


STUB_STATE_DECODE_ERROR = {
    "query_config": {
        "attachment protect": {
            "caught_up": False,
            "next_page": "NDU1NA==",
            "query_date": "2000-01-06",
        },
        "receipt": {
            "caught_up": False,
            "next_page": "JDU1NA==",
            "query_date": "2000-01-05",
        },
        "url protect": {
            "caught_up": False,
            "next_page": "NDU1NA==",
            "query_date": "2000-01-06",
        },
    },
}

STUB_STATE_PAGINATING_LAST_PAGE = {
    "query_config": {
        "attachment protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "2000-01-06",
        },
        "receipt": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "2000-01-06",
        },
        "ttp_attachment": {
            "caught_up": False,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_impersonation": {
            "caught_up": False,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_url": {"caught_up": False, "query_date": "2000-01-07T00:00:00+00:00"},
        "url protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "2000-01-06",
        },
    },
}

STUB_STATE_LIMIT_LOGS = {
    "query_config": {
        "attachment protect": {
            "caught_up": False,
            "log_hashes": ["e98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "KDU1NA==",
            "query_date": "1999-12-31",
            "saved_file_position": 1,
            "saved_file_url": "https://exampleadditional.com",
        },
        "receipt": {
            "caught_up": False,
            "log_hashes": ["e98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "KDU1NA==",
            "query_date": "1999-12-31",
            "saved_file_position": 1,
            "saved_file_url": "https://exampleadditional.com",
        },
        "url protect": {
            "caught_up": False,
            "log_hashes": ["e98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "KDU1NA==",
            "query_date": "1999-12-31",
            "saved_file_position": 1,
            "saved_file_url": "https://exampleadditional.com",
        },
    }
}

STUB_STATE_SECOND_RUN_EXPECTED = {
    "query_config": {
        "attachment protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "2000-01-07",
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "receipt": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "2000-01-07",
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "ttp_attachment": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_impersonation": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_url": {"caught_up": True, "query_date": "2000-01-07T00:00:00+00:00"},
        "url protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "2000-01-07",
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "saved_file_position": 0,
            "saved_file_url": None,
        },
    },
}

STUB_STATE_EXPECTED_CUSTOM_CONFIG = {
    "query_config": {
        "attachment protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-31",
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "receipt": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-31",
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "ttp_attachment": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_impersonation": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_url": {"caught_up": True, "query_date": "2000-01-07T00:00:00+00:00"},
        "url protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-31",
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "saved_file_position": 0,
            "saved_file_url": None,
        },
    },
}

STUB_STATE_EXPECTED_LOG_LIMIT = {
    "query_config": {
        "attachment protect": {
            "caught_up": False,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": None,
            "query_date": "1999-12-31",
            "saved_file_position": 1,
            "saved_file_url": "https://example.com",
        },
        "receipt": {
            "caught_up": False,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": None,
            "query_date": "1999-12-31",
            "saved_file_position": 1,
            "saved_file_url": "https://example.com",
        },
        "ttp_attachment": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_impersonation": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_url": {"caught_up": True, "query_date": "2000-01-07T00:00:00+00:00"},
        "url protect": {
            "caught_up": False,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": None,
            "query_date": "1999-12-31",
            "saved_file_position": 1,
            "saved_file_url": "https://example.com",
        },
    }
}

STUB_STATE_EXPECTED_LOG_LIMIT_SECOND_RUN = {
    "query_config": {
        "attachment protect": {
            "caught_up": True,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "NDU1NA==",
            "query_date": "1999-12-31",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "receipt": {
            "caught_up": True,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "NDU1NA==",
            "query_date": "1999-12-31",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
        "ttp_attachment": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_impersonation": {
            "caught_up": True,
            "query_date": "2000-01-07T00:00:00+00:00",
        },
        "ttp_url": {"caught_up": True, "query_date": "2000-01-07T00:00:00+00:00"},
        "url protect": {
            "caught_up": True,
            "log_hashes": ["d98dafb4f13b3bb70539a6c251a8a9b42ea80de1"],
            "next_page": "NDU1NA==",
            "query_date": "1999-12-31",
            "saved_file_position": 0,
            "saved_file_url": None,
        },
    }
}

STUB_CUSTOM_CONFIG = {
    "query_config": {
        "attachment protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-31",
        },
        "receipt": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-31",
        },
        "url protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-31",
        },
    },
    "page_size": 1,
    "thread_count": 1,
}

STUB_CUSTOM_CONFIG_EXCEED_DATE = {
    "query_config": {
        "attachment protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
        },
        "receipt": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
        },
        "url protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
        },
    },
    "page_size": 1,
    "thread_count": 1,
}

STUB_CUSTOM_CONFIG_LIMIT_LOGS = {
    "query_config": {
        "attachment protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
        },
        "receipt": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
        },
        "url protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
        },
    },
    "page_size": 1,
    "thread_count": 1,
    "log_limits": {"receipt": 1, "url protect": 1, "attachment protect": 1},
}


STUB_CUSTOM_CONFIG_LIMIT_LOGS_SECOND_RUN = {
    "query_config": {
        "attachment protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
        },
        "receipt": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
        },
        "url protect": {
            "caught_up": True,
            "next_page": "NDU1NA==",
            "query_date": "1999-12-30",
        },
    },
    "page_size": 1,
    "thread_count": 1,
    "log_limits": {"receipt": 100, "url protect": 100, "attachment protect": 100},
}


@freeze_time("2000-01-07T00:00:00.000000Z")
class TestMonitorLogs(TestCase):
    @classmethod
    @patch("requests.Session.send", side_effect=Util.mocked_request)
    def setUpClass(cls, mocked_request) -> None:
        cls.task = Util.default_connector(MonitorSiemLogs())

    @parameterized.expand(
        [
            [
                "starting",
                {},
                {},
                None,
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_EXPECTED,
                True,
                200,
                None,
            ],
            [
                "paginating",
                STUB_STATE_PAGINATING,
                {},
                "2000-01-06",
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_EXPECTED,
                True,
                200,
                None,
            ],
            [
                "paginating_last_page",
                STUB_STATE_PAGINATING_LAST_PAGE,
                {},
                "2000-01-06",
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_SECOND_RUN_EXPECTED,
                False,
                200,
                None,
            ],
            [
                "custom_config",
                {},
                STUB_CUSTOM_CONFIG,
                "1999-12-31",
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_EXPECTED_CUSTOM_CONFIG,
                True,
                200,
                None,
            ],
            [
                "custom_config_past_cutoff",
                {},
                STUB_CUSTOM_CONFIG_EXCEED_DATE,
                "1999-12-30",
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_EXPECTED_CUSTOM_CONFIG,
                True,
                200,
                None,
            ],
            [
                "stop_parsing_file",
                {},
                STUB_CUSTOM_CONFIG_LIMIT_LOGS,
                "1999-12-30",
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_EXPECTED_LOG_LIMIT,
                True,
                200,
                None,
            ],
            [
                "continue_parsing_file",
                STUB_STATE_LIMIT_LOGS,
                STUB_CUSTOM_CONFIG_LIMIT_LOGS_SECOND_RUN,
                "1999-12-31",
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_EXPECTED_LOG_LIMIT_SECOND_RUN,
                True,
                200,
                None,
            ],
            [
                "json_decode_error",
                STUB_STATE_DECODE_ERROR,
                {},
                "2000-01-05",
                Util.read_file_to_dict("expected/monitor_siem_logs_invalid_receipt.json.exp"),
                STUB_STATE_EXPECTED_INVALID_RECEIPT,
                True,
                200,
                None,
            ],
            [
                "remove_duplicates",
                STUB_STATE_BATCH_DUPLICATES,
                {},
                "2000-01-02",
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_EXPECTED_DUPLICATES,
                True,
                200,
                None,
            ],
            [
                "paginating_cutoff_headroom",
                STUB_STATE_PAGINATING_CUTOFF,
                {},
                "1999-12-30",
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_PAGINATING_CUTOFF_EXPECTED,
                True,
                200,
                None,
            ],
        ]
    )
    @patch("requests.Session.send", side_effect=Util.mocked_request)
    def test_monitor_logs(
        self,
        test_name: str,
        state: Dict[str, Any],
        custom_config: Dict[str, Any],
        furthest_query_date: Optional[str],
        expected_output: Dict[str, Any],
        expected_state: Dict[str, Any],
        expected_has_more_pages: bool,
        expected_status_code: int,
        expected_error: Optional[Any],
        mock_request: MagicMock,
    ) -> None:
        output, state, has_more_pages, status_code, error = self.task.run(
            params={}, state=state, custom_config=custom_config
        )
        expected_state["furthest_query_date"] = furthest_query_date
        self.assertEqual(expected_output, output)
        self.assertEqual(expected_state, state)
        self.assertEqual(expected_has_more_pages, has_more_pages)
        self.assertEqual(expected_status_code, status_code)
        self.assertEqual(expected_error, error)
        validate(output, MonitorSiemLogsOutput.schema)

    @parameterized.expand(
        [
            ["start_ttp_paginating", {}, {}, True, 200, "PAGINATION"],
            [
                "second_page_and_finish_pagination",
                {
                    **STUB_STATE_EXPECTED,
                    "query_config": {
                        **STUB_STATE_EXPECTED["query_config"],
                        "ttp_url": {
                            "caught_up": False,
                            "query_date": "2000-01-06T00:00:00+00:00",
                            "next_page": "EXAMPLE_TOKEN",
                        },
                    },
                },
                {},
                False,
                200,
                "PAGINATION",
            ],
            [
                "third_run_to_get_updated_query_date",
                {
                    **STUB_STATE_EXPECTED,
                    "query_config": {
                        **STUB_STATE_EXPECTED["query_config"],
                        "ttp_url": {
                            "caught_up": False,
                            "query_date": "2000-01-07T00:00:00+00:00",
                        },
                    },
                },
                {},
                False,
                200,
                "NORMAL",
            ],
        ]
    )
    @patch("requests.Session.send")
    def test_monitor_logs_ttp_pagination(
        self,
        test_name: str,
        state: Dict[str, Any],
        custom_config: Dict[str, Any],
        expected_has_more_pages: bool,
        expected_status_code: int,
        request_type: str,
        mock_request: MagicMock,
    ) -> None:
        # Setup type of request to mock
        mock_request.side_effect = lambda request, **kwargs: Util.mocked_request(request, type=request_type, **kwargs)
        output, state, has_more_pages, status_code, error = self.task.run(
            params={}, state=state, custom_config=custom_config
        )
        self.assertEqual(expected_has_more_pages, has_more_pages)
        self.assertEqual(expected_status_code, status_code)

        # If there are more pages, ensure the next_page token is present in state
        if expected_has_more_pages:
            self.assertIn("next_page", state["query_config"]["ttp_url"])
            self.assertEqual("EXAMPLE_TOKEN", state["query_config"]["ttp_url"]["next_page"])

    @parameterized.expand(
        [
            [
                "401",
                {
                    "query_config": {
                        "receipt": {
                            "caught_up": True,
                            "next_page": "NDU1NA==",
                            "query_date": "2000-01-01",
                        }
                    }
                },
                "Invalid API key provided.",
                "Verify your API key configured in your connection is correct.",
                401,
            ],
            [
                "500",
                {
                    "query_config": {
                        "receipt": {
                            "caught_up": True,
                            "next_page": "NDU1NA==",
                            "query_date": "2000-01-02",
                        }
                    }
                },
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                500,
            ],
            [
                "json_decode",
                {
                    "query_config": {
                        "receipt": {
                            "caught_up": True,
                            "next_page": "NDU1NA==",
                            "query_date": "2000-01-03",
                        }
                    }
                },
                "Received an unexpected response from the server.",
                "(non-JSON or no response was received).",
                500,
            ],
            [
                "unknown",
                {
                    "query_config": {
                        "receipt": {
                            "caught_up": True,
                            "next_page": "NDU1NA==",
                            "query_date": "2000-01-04",
                        }
                    }
                },
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                500,
            ],
        ]
    )
    @patch("requests.Session.send", side_effect=Util.mocked_request)
    def test_monitor_logs_errors(
        self,
        test_name: str,
        state: Dict[str, Any],
        expected_cause: str,
        expected_assistance: str,
        expected_status_code: int,
        mock_request: MagicMock,
    ) -> None:
        output, state, has_more_pages, status_code, error = self.task.run(params={}, state=state)
        self.assertEqual(expected_status_code, status_code)
        self.assertEqual(expected_cause, error.cause)
        self.assertEqual(expected_assistance, error.assistance)
        validate(output, MonitorSiemLogsOutput.schema)
