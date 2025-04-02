from unittest import TestCase
from komand_rapid7_insightidr.util.parse_dates import parse_dates
from insightconnect_plugin_runtime.exceptions import PluginException
import time


class TestParseDates(TestCase):
    def test_parse_dates(self):
        time_test_rel = "Absolute Time To"

        time_test1 = "2005/10/31T17:11:09"
        time_test2 = "01-01-2020"
        time_test3 = "01-01-2020T18:01:01"
        time_test4 = "02/24/1978"
        time_test5 = "13:25"
        time_test6 = "01/27/2020 10:00 PM"
        time_test7 = "01-01-2020"
        time_test8 = "12-31-2020"

        res1, res2 = parse_dates(time_test1, time_test2, time_test_rel)
        res3, res4 = parse_dates(time_test3, time_test4, time_test_rel)
        res5, res6 = parse_dates(time_test5, time_test6, time_test_rel)
        res7, res8 = parse_dates(time_test7, time_test8, time_test_rel)

        self.assertEqual(res1, 1130775069000)
        self.assertEqual(res2, 1577833200000)
        self.assertEqual(res3, 1577898061000)
        self.assertEqual(res4, 257122800000)
        self.assertIsNotNone(res5)  # This will be today @ 1:25 PM.
        self.assertEqual(res6, 1580158800000)
        self.assertEqual(res7, 1577833200000)
        self.assertEqual(res8, 1609369200000)

        not_used, now_result = parse_dates(time_test1, None, time_test_rel)
        self.assertIsNotNone(now_result)

        with self.assertRaises(PluginException):
            parse_dates("AAA", None, time_test_rel)

    def test_parse_dates_relative_time(self):
        time_test1 = "2005/10/31T17:11:09"
        time_rel = "Absolute Time To"

        res1, _ = parse_dates(time_test1, time_test1, time_rel)
        self.assertEqual(res1, 1130775069000)

        time_rel = "Last 5 Minutes"
        res1, _ = parse_dates(time_test1, "", time_rel)
        expected = int(time.time()) * 1000 - 300000
        actual = res1
        self.assertTrue(expected - 1000 < actual < expected + 1000)

        time_rel = "Last 12 Hours"
        res1, _ = parse_dates(time_test1, "", time_rel)
        expected = int(time.time()) * 1000 - 4.32e7
        actual = res1
        self.assertTrue(expected - 1000 < actual < expected + 1000)

    def test_parse_dates_relative_time_no_to_date_specified(self):
        time_from = "1/1/2000"

        # This shouldn't happen, but wanted to make sure there wasn't a crash.
        not_used, res2 = parse_dates(time_from, "", "")
        expected = int(time.time()) * 1000

        # This is realtime, give us 1s leeway for expected results
        self.assertTrue(expected - 1000 < res2 < expected + 1000)
