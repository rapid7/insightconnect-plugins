from unittest import TestCase
from unittest.mock import patch

from jsonschema import Draft7Validator

from icon_ipgeolocation_io.actions.abuse_contact import AbuseContact
from icon_ipgeolocation_io.actions.abuse_contact.schema import Input as AbuseInput
from icon_ipgeolocation_io.actions.asn_lookup import AsnLookup
from icon_ipgeolocation_io.actions.asn_lookup.schema import Input as AsnInput
from icon_ipgeolocation_io.actions.ip_geolocation import IpGeolocation
from icon_ipgeolocation_io.actions.ip_geolocation.schema import Input as GeoInput
from icon_ipgeolocation_io.actions.ip_geolocation_bulk import IpGeolocationBulk
from icon_ipgeolocation_io.actions.ip_geolocation_bulk.schema import Input as GeoBulkInput
from icon_ipgeolocation_io.actions.ip_security import IpSecurity
from icon_ipgeolocation_io.actions.ip_security.schema import Input as SecInput
from icon_ipgeolocation_io.actions.ip_security_bulk import IpSecurityBulk
from icon_ipgeolocation_io.actions.ip_security_bulk.schema import Input as SecBulkInput
from unit_test.mock import (
    DOMAIN,
    IP_ABUSE,
    IP_BOGON,
    IP_HETZNER,
    IP_MALICIOUS,
    IP_SWEDEN,
    make_action,
    mock_request,
)
import os
import sys

sys.path.append(os.path.abspath("../"))



# One representative invocation per action, covering the response shapes that
# differ structurally: domain lookups, bulk results with per-entry messages,
# and ASN lookups with and without the heavier included objects.
CASES = [
    ("ip_geolocation full enrichment", IpGeolocation, {GeoInput.IP: IP_SWEDEN, GeoInput.INCLUDE: ["*"]}),
    ("ip_geolocation domain", IpGeolocation, {GeoInput.IP: DOMAIN}),
    ("ip_geolocation caller IP", IpGeolocation, {}),
    ("ip_geolocation_bulk", IpGeolocationBulk, {GeoBulkInput.IPS: [IP_SWEDEN, IP_BOGON, DOMAIN]}),
    ("ip_security", IpSecurity, {SecInput.IP: IP_MALICIOUS}),
    ("ip_security_bulk", IpSecurityBulk, {SecBulkInput.IPS: [IP_MALICIOUS, IP_BOGON]}),
    ("asn_lookup by ASN", AsnLookup, {AsnInput.ASN: "AS24940"}),
    (
        "asn_lookup by IP with include",
        AsnLookup,
        {AsnInput.IP: IP_HETZNER, AsnInput.INCLUDE: ["peers", "routes"]},
    ),
    ("abuse_contact", AbuseContact, {AbuseInput.IP: IP_ABUSE}),
]


@patch("requests.Session.request", side_effect=mock_request)
class TestSchemaConformance(TestCase):
    """
    Guard the contract between the action code and plugin.spec.yaml.

    The ICON runtime validates inputs before run() and outputs after it, so any
    drift between what an action emits and what the generated schema declares
    surfaces as a runtime failure in production. Checking both directions here
    turns that into a test failure instead.
    """

    def test_action_inputs_satisfy_the_generated_schemas(self, _mocked):
        for label, action_class, params in CASES:
            with self.subTest(action=label):
                action = make_action(action_class)
                errors = sorted(
                    Draft7Validator(action.input.schema).iter_errors(params),
                    key=lambda error: list(error.path),
                )
                self.assertEqual([], [f"{list(e.path)}: {e.message}" for e in errors])

    def test_action_outputs_satisfy_the_generated_schemas(self, _mocked):
        for label, action_class, params in CASES:
            with self.subTest(action=label):
                action = make_action(action_class)
                result = action.run(params)
                errors = sorted(
                    Draft7Validator(action.output.schema).iter_errors(result),
                    key=lambda error: list(error.path),
                )
                self.assertEqual([], [f"{list(e.path)}: {e.message}" for e in errors])

    def test_every_action_in_the_spec_is_covered(self, _mocked):
        covered = {action_class for _, action_class, _ in CASES}
        expected = {
            IpGeolocation,
            IpGeolocationBulk,
            IpSecurity,
            IpSecurityBulk,
            AsnLookup,
            AbuseContact,
        }
        self.assertEqual(expected, covered)
