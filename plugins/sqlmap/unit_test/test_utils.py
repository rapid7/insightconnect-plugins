import os
import sys
import unittest
from unittest.mock import MagicMock, patch

sys.path.append(os.path.abspath("../"))

from icon_sqlmap.util.utils import delay


class TestDelay(unittest.TestCase):
    @patch("icon_sqlmap.util.utils.time.sleep")
    def test_delay_calls_sleep(self, mock_sleep: MagicMock) -> None:
        @delay(seconds=5)
        def sample_function() -> str:
            return "done"

        result = sample_function()
        self.assertEqual(result, "done")
        mock_sleep.assert_called_once_with(5)

    def test_delay_negative_raises(self) -> None:
        with self.assertRaises(ValueError) as context:

            @delay(seconds=-1)
            def sample_function() -> None:
                pass

        self.assertIn("non-negative", str(context.exception))

    @patch("icon_sqlmap.util.utils.time.sleep")
    def test_delay_zero_seconds(self, mock_sleep: MagicMock) -> None:
        @delay(seconds=0)
        def sample_function() -> str:
            return "instant"

        result = sample_function()
        self.assertEqual(result, "instant")
        mock_sleep.assert_called_once_with(0)
