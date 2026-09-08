import os
import sys

sys.path.append(os.path.abspath("../"))

from time import perf_counter
from typing import Any, Dict, List
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_servicenow.actions.get_incident_comments_worknotes import GetIncidentCommentsWorknotes
from icon_servicenow.actions.get_incident_comments_worknotes.schema import GetIncidentCommentsWorknotesOutput
from icon_servicenow.util.journal_helper import parse_journal_display_value
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import JOURNAL_FIELDS, JOURNAL_URL, Util


@patch("requests.get", side_effect=Util.mocked_requests)
@patch("requests.post", side_effect=Util.mocked_requests)
class TestGetIncidentCommentsWorknotes(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetIncidentCommentsWorknotes())

    @parameterized.expand(
        [
            [
                "journal_readable",
                Util.read_file_to_dict("inputs/get_incident_comments_worknotes_journal.json.inp"),
                Util.read_file_to_dict("expected/get_incident_comments_worknotes_journal.json.exp"),
            ],
            [
                "journal_not_readable_all",
                Util.read_file_to_dict("inputs/get_incident_comments_worknotes_fallback_all.json.inp"),
                Util.read_file_to_dict("expected/get_incident_comments_worknotes_fallback_all.json.exp"),
            ],
            [
                "journal_not_readable_comments",
                Util.read_file_to_dict("inputs/get_incident_comments_worknotes_fallback_comments.json.inp"),
                Util.read_file_to_dict("expected/get_incident_comments_worknotes_fallback_comments.json.exp"),
            ],
            [
                "journal_not_readable_work_notes",
                Util.read_file_to_dict("inputs/get_incident_comments_worknotes_fallback_work_notes.json.inp"),
                Util.read_file_to_dict("expected/get_incident_comments_worknotes_fallback_work_notes.json.exp"),
            ],
            [
                "journal_not_readable_and_work_notes_suppressed",
                Util.read_file_to_dict("inputs/get_incident_comments_worknotes_field_suppressed.json.inp"),
                Util.read_file_to_dict("expected/get_incident_comments_worknotes_field_suppressed.json.exp"),
            ],
            [
                "no_comments_or_work_notes",
                Util.read_file_to_dict("inputs/get_incident_comments_worknotes_no_entries.json.inp"),
                Util.read_file_to_dict("expected/get_incident_comments_worknotes_empty.json.exp"),
            ],
            [
                "incident_not_readable",
                Util.read_file_to_dict("inputs/get_incident_comments_worknotes_incident_not_found.json.inp"),
                Util.read_file_to_dict("expected/get_incident_comments_worknotes_empty.json.exp"),
            ],
            [
                "incident_in_unexpected_format",
                Util.read_file_to_dict("inputs/get_incident_comments_worknotes_unexpected_format.json.inp"),
                Util.read_file_to_dict("expected/get_incident_comments_worknotes_empty.json.exp"),
            ],
            [
                "invalid_system_id",
                Util.read_file_to_dict("inputs/get_incident_comments_worknotes_invalid_id.json.inp"),
                Util.read_file_to_dict("expected/get_incident_comments_worknotes_empty.json.exp"),
            ],
        ]
    )
    def test_get_incident_comments_worknotes(
        self,
        mock_post: MagicMock,
        mock_get: MagicMock,
        test_name: str,
        input_params: Dict[str, Any],
        expected: Dict[str, Any],
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, GetIncidentCommentsWorknotesOutput.schema)
        self.assertDictEqual(actual, expected)

    def test_get_incident_comments_worknotes_leaves_readable_journal_alone(
        self, mock_post: MagicMock, mock_get: MagicMock
    ) -> None:
        self.action.run(Util.read_file_to_dict("inputs/get_incident_comments_worknotes_journal.json.inp"))
        self.assertEqual(
            [call.kwargs.get("url") for call in mock_get.call_args_list],
            [f"{JOURNAL_URL}?sysparm_query=element_id=j1&sysparm_fields={JOURNAL_FIELDS}"],
        )

    def test_get_incident_comments_worknotes_reads_the_record_as_display_values(
        self, mock_post: MagicMock, mock_get: MagicMock
    ) -> None:
        # A journal field read off the record holds its entries only when it is read as a display
        # value; read as a raw value it is the most recent entry alone.
        self.action.run(Util.read_file_to_dict("inputs/get_incident_comments_worknotes_fallback_all.json.inp"))
        self.assertEqual(
            mock_get.call_args_list[-1].kwargs.get("params"),
            {"sysparm_fields": "comments,work_notes", "sysparm_display_value": "true"},
        )

    @parameterized.expand(
        [
            [
                "journal_query_forbidden",
                Util.read_file_to_dict("inputs/get_incident_comments_worknotes_journal_forbidden.json.inp"),
                "Error in API request to ServiceNow. ",
                "Status code: 403, Error: {'error': {'message': 'Insufficient rights', 'detail': "
                "'Insufficient rights to query records'}, 'status': 'failure'}",
            ],
            [
                "journal_query_answered_without_json",
                Util.read_file_to_dict("inputs/get_incident_comments_worknotes_journal_not_json.json.inp"),
                "Received an unexpected response from the server.",
                "(non-JSON or no response was received).",
            ],
        ]
    )
    def test_get_incident_comments_worknotes_raise_exception(
        self,
        mock_post: MagicMock,
        mock_get: MagicMock,
        test_name: str,
        input_params: Dict[str, Any],
        cause: str,
        assistance: str,
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)


class TestParseJournalDisplayValue(TestCase):
    @parameterized.expand(
        [
            [
                "single_entry",
                "2019-09-26 21:19:11 - System Administrator (Work notes)\nTeam is actively looking into it.\n\n",
                [("2019-09-26 21:19:11", "System Administrator", "Team is actively looking into it.")],
            ],
            [
                "blank_line_within_an_entry",
                "2019-09-26 21:19:11 - Joe Employee (Work notes)\nFirst line\n\nSecond paragraph\n\n",
                [("2019-09-26 21:19:11", "Joe Employee", "First line\n\nSecond paragraph")],
            ],
            [
                "carriage_returns",
                "2019-09-26 21:19:11 - Joe Employee (Work notes)\r\nCalled the user\r\n\r\n",
                [("2019-09-26 21:19:11", "Joe Employee", "Called the user")],
            ],
            [
                "author_containing_a_separator",
                "2019-09-26 21:19:11 - Smith - Jones (Work notes)\nCalled the user\n\n",
                [("2019-09-26 21:19:11", "Smith - Jones", "Called the user")],
            ],
            [
                "localized_field_label",
                "26.09.2019 21:19:11 - Max Mustermann (Zusätzliche Kommentare)\nBearbeitet\n\n",
                [("26.09.2019 21:19:11", "Max Mustermann", "Bearbeitet")],
            ],
            [
                "twelve_hour_timestamp",
                "26/09/2019 9:19:11 PM - Joe Employee (Additional comments)\nCalled the user\n\n",
                [("26/09/2019 9:19:11 PM", "Joe Employee", "Called the user")],
            ],
            [
                "month_name_within_the_date",
                "11-Sep-2026 21:19:11 - Joe Employee (Work notes)\nCalled the user\n\n",
                [("11-Sep-2026 21:19:11", "Joe Employee", "Called the user")],
            ],
            [
                "author_with_no_last_name",
                "2019-09-26 21:19:11 - Sam  (Additional comments)\nCalled the user\n\n",
                [("2019-09-26 21:19:11", "Sam", "Called the user")],
            ],
            [
                "author_containing_parentheses",
                "2019-09-26 21:19:11 - Administrator (itil_user) (Work notes)\nCalled the user\n\n",
                [("2019-09-26 21:19:11", "Administrator (itil_user)", "Called the user")],
            ],
            [
                "renamed_label_containing_parentheses",
                "2019-09-26 21:19:11 - Joe Employee (Comments (public))\nCalled the user\n\n",
                [("2019-09-26 21:19:11", "Joe Employee", "Called the user")],
            ],
            [
                "author_and_renamed_label_both_containing_parentheses",
                "2019-09-26 21:19:11 - Administrator (itil_user) (Comments (public))\nCalled the user\n\n",
                [("2019-09-26 21:19:11", "Administrator (itil_user)", "Called the user")],
            ],
            [
                "renamed_label_containing_two_parentheses",
                # A label holding more than one parenthesised part is not read as a label, so the
                # header keeps its text and is returned without an author or a creation date rather
                # than with the label read into the author.
                "2019-09-26 21:19:11 - Joe Employee (Comments (public) (internal))\nCalled the user\n\n",
                [("", "", "2019-09-26 21:19:11 - Joe Employee (Comments (public) (internal))\nCalled the user")],
            ],
            [
                "entry_ending_in_a_blank_line",
                "2019-09-26 21:19:11 - Joe Employee (Work notes)\nCalled the user\n\n\n"
                "2019-09-25 08:00:00 - Ann Employee (Work notes)\nRaised the incident\n\n",
                [
                    ("2019-09-26 21:19:11", "Joe Employee", "Called the user"),
                    ("2019-09-25 08:00:00", "Ann Employee", "Raised the incident"),
                ],
            ],
            [
                "entry_text_resembling_a_header",
                "2019-09-26 21:19:11 - Joe Employee (Work notes)\nCalled user - no answer (voicemail)\n\n",
                [("2019-09-26 21:19:11", "Joe Employee", "Called user - no answer (voicemail)")],
            ],
            [
                "entry_text_with_a_clock_but_no_date",
                "2019-09-26 21:19:11 - Joe Employee (Work notes)\n12:30 - lunch (canceled)\n\n",
                [("2019-09-26 21:19:11", "Joe Employee", "12:30 - lunch (canceled)")],
            ],
            [
                "entry_text_with_a_separator_but_no_clock",
                "2019-09-26 21:19:11 - Joe Employee (Work notes)\n1:1 with mgr - Bob Smith (HR)\n\n",
                [("2019-09-26 21:19:11", "Joe Employee", "1:1 with mgr - Bob Smith (HR)")],
            ],
            [
                "entry_text_reading_as_a_header",
                "2019-09-26 21:19:11 - Joe Employee (Work notes)\nCalled at 10:15:00 - no answer (voicemail)\n\n",
                [("2019-09-26 21:19:11", "Joe Employee", "Called at 10:15:00 - no answer (voicemail)")],
            ],
            [
                "quoted_header_within_an_entry",
                "2019-09-26 21:19:11 - Joe Employee (Work notes)\n2019-09-01 08:00:00 - Ann (Work notes) wrote:\n\n",
                [("2019-09-26 21:19:11", "Joe Employee", "2019-09-01 08:00:00 - Ann (Work notes) wrote:")],
            ],
            [
                "unrecognized_header",
                "26-Sep-2019 - Joe Employee (Work notes)\nCalled the user\n\n",
                [("", "", "26-Sep-2019 - Joe Employee (Work notes)\nCalled the user")],
            ],
            [
                "date_beginning_with_the_month_name",
                "Sep-26-2019 21:19:11 - Joe Employee (Work notes)\nCalled the user\n\n",
                [("", "", "Sep-26-2019 21:19:11 - Joe Employee (Work notes)\nCalled the user")],
            ],
            [
                "header_shaped_line_ending_an_entry",
                "2019-09-26 21:19:11 - Joe Employee (Work notes)\nQuoting the note below\n"
                "2019-09-01 08:00:00 - Ann Employee (Work notes)\n\n",
                [
                    ("2019-09-26 21:19:11", "Joe Employee", "Quoting the note below"),
                    ("", "", "2019-09-01 08:00:00 - Ann Employee (Work notes)"),
                ],
            ],
            [
                "header_with_no_text_under_it",
                "2019-09-26 21:19:11 - Joe Employee (Work notes)\n\n",
                [("", "", "2019-09-26 21:19:11 - Joe Employee (Work notes)")],
            ],
            ["no_entries", "", []],
            ["whitespace_only", "   \n\n\t\n", []],
        ]
    )
    def test_parse_journal_display_value(self, test_name: str, display_value: str, expected: List[tuple]) -> None:
        actual = parse_journal_display_value(display_value, "work_notes", "j1")
        self.assertEqual(
            [(entry["sys_created_on"], entry["sys_created_by"], entry["value"]) for entry in actual], expected
        )
        for entry in actual:
            self.assertEqual(
                {"sys_id": "", "sys_tags": "", "name": "incident", "element": "work_notes", "element_id": "j1"},
                {key: entry[key] for key in ("sys_id", "sys_tags", "name", "element", "element_id")},
            )

    def test_parse_journal_display_value_with_a_pasted_log(self) -> None:
        # An entry the user built out of nothing but the characters a header is made of has to stay
        # one entry, and the bounded repetitions of journal_entry_header have to reject it without
        # backtracking over it: unbind them and matching this one line takes more than ten seconds.
        pasted_log = "10:15:00 - x (" * 300
        started = perf_counter()
        entries = parse_journal_display_value(
            f"2019-09-26 21:19:11 - Joe Employee (Work notes)\n{pasted_log}\n\n", "work_notes", "j1"
        )
        self.assertLess(perf_counter() - started, 5)
        self.assertEqual([entry["value"] for entry in entries], [pasted_log.strip()])

    @parameterized.expand([["none", None], ["display_value_all_shape", {"display_value": "Comment"}], ["number", 1]])
    def test_parse_journal_display_value_without_a_string(self, test_name: str, display_value: Any) -> None:
        self.assertEqual(parse_journal_display_value(display_value, "comments", "j1"), [])
