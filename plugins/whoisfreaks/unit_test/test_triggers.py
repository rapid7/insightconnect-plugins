import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.triggers.newly_registered_domains import NewlyRegisteredDomains
from icon_whoisfreaks.triggers.threat_feed import ThreatFeed
from util import MockResponse, connect

NRD_MODULE = "icon_whoisfreaks.triggers.newly_registered_domains.trigger"
THREAT_MODULE = "icon_whoisfreaks.triggers.threat_feed.trigger"
THREAT_HEADER = (
    "domain,threat_type,confidence,first_seen,last_seen,is_seed,is_extrapolated,is_dropped,is_parked,"
    "parked_reason,matched_pivots"
)


class TestTriggers(TestCase):
    @patch(f"{NRD_MODULE}.FeedPoller")
    def test_newly_registered_domains_both_feeds(self, poller):
        trigger = NewlyRegisteredDomains()
        connect(trigger)
        params = {
            "include_generic_tlds": True,
            "include_country_code_tlds": True,
            "include_whois": True,
            "start_date": "2026-11-01",
            "catch_up_missed_dates": True,
            "batch_size": 200,
            "poll_interval_minutes": 720,
            "domain_keywords": ["Brand"],
            "tld_filter": ["co.uk"],
        }
        trigger.input.validate(params)
        trigger.run(params)
        _, client, feeds, settings = poller.call_args[0]
        self.assertIs(trigger.connection.client, client)
        self.assertEqual(["/v3.3/stream/domainer/gtld", "/v3.3/stream/domainer/cctld"], [item.path for item in feeds])
        self.assertEqual([{"whois": "true"}] * 2, [item.params for item in feeds])
        self.assertEqual((200, 43200, True), (settings.batch_size, settings.poll_interval_seconds, settings.catch_up))
        self.assertTrue(settings.row_filter({"domain_name": "mybrand.co.uk"}, "newly.cctld"))
        self.assertFalse(settings.row_filter({"domain_name": "mybrand.com"}, "newly.gtld"))
        poller.return_value.run.assert_called_once()

    @patch(f"{NRD_MODULE}.FeedPoller")
    def test_newly_registered_domains_country_code_only(self, poller):
        trigger = NewlyRegisteredDomains()
        connect(trigger)
        trigger.run({"include_generic_tlds": False, "include_country_code_tlds": True})
        self.assertEqual(["newly.cctld"], [item.feed_id for item in poller.call_args[0][2]])

    @patch(f"{THREAT_MODULE}.FeedPoller")
    def test_threat_feed_selection(self, poller):
        trigger = ThreatFeed()
        connect(trigger)
        trigger.run(
            {
                "include_phishing": False,
                "include_malware": True,
                "include_spam": True,
                "batch_size": 1000,
                "poll_interval_minutes": 60,
                "min_confidence": 0.9,
            }
        )
        _, _, feeds, settings = poller.call_args[0]
        self.assertEqual(["/v3.4/stream/threat-feed/malware", "/v3.4/stream/threat-feed/spam"], [f.path for f in feeds])
        self.assertFalse(settings.row_filter({"domain": "a.com", "confidence": 0.5}, "threat_feed.spam"))

    def test_no_feed_enabled(self):
        for trigger, params in (
            (NewlyRegisteredDomains(), {"include_generic_tlds": False, "include_country_code_tlds": False}),
            (ThreatFeed(), {"include_phishing": False, "include_malware": False, "include_spam": False}),
        ):
            with self.subTest(trigger=trigger.name):
                connect(trigger)
                with self.assertRaises(PluginException) as context:
                    trigger.run(params)
                self.assertIn("No feed is enabled", context.exception.cause)

    def test_threat_feed_end_to_end_with_sdk_send(self):
        """Runs the real trigger, client and parser; output events are validated by the SDK send schema check."""
        trigger = ThreatFeed()
        status = {"threat_feed": {"spam": {"last_update": "2026-10-30", "available_from": "2026-07-29"}}}
        page = f"{THREAT_HEADER}\nspam.example,spam,0.7,2026-10-29 00:00:00+00,2026-10-30 00:00:00+00,f,t,f,f,,\n"
        connect(trigger, MockResponse(200, status), MockResponse(200, page), MockResponse(200, status))
        trigger.dispatcher, trigger.log_stream = MagicMock(), MagicMock()
        trigger.log_stream.getvalue.return_value = ""
        trigger.state, trigger.state_file = {}, ""
        with patch.object(ThreatFeed, "run_trigger", new_callable=MagicMock) as run_trigger, patch(
            "icon_whoisfreaks.util.feed_poller.time.sleep"
        ):
            run_trigger.__bool__ = MagicMock(side_effect=[True, True, False])
            trigger.run(
                {"include_phishing": False, "include_spam": True, "batch_size": 10, "poll_interval_minutes": 60}
            )
        message = trigger.dispatcher.write.call_args[0][0]
        output = message["body"]["output"]
        self.assertEqual("trigger_event", message["type"])
        self.assertEqual("threat_feed.spam", output["feed"])
        self.assertEqual("2026-10-30", output["feed_date"])
        self.assertEqual(
            [
                {
                    "domain": "spam.example",
                    "threat_type": "spam",
                    "confidence": 0.7,
                    "first_seen": "2026-10-29T00:00:00+00:00",
                    "last_seen": "2026-10-30T00:00:00+00:00",
                    "is_seed": False,
                    "is_extrapolated": True,
                    "is_dropped": False,
                    "is_parked": False,
                }
            ],
            output["events"],
        )
        self.assertEqual("2026-10-30", trigger.state["feeds"]["threat_feed.spam"]["last_completed_date"])
