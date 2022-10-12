import os
import sys
from unittest import TestCase

sys.path.append(os.path.abspath("../"))

import logging

from icon_palo_alto_cortex_xdr.util.api import CortexXdrAPI


class TestAPI(TestCase):
    def test_get_type(self):
        api = CortexXdrAPI(1, "key", "https://fqdn", "ADVANCED", logging.getLogger())

        result = api._get_endpoint_type("1.2.3.4")
        self.assertEquals(result, api.ENDPOINT_IP_TYPE)

        result = api._get_endpoint_type("01243654cdf0444392f58ed0d251eeda")
        self.assertEquals(result, api.ENDPOINT_ID_TYPE)

        result = api._get_endpoint_type("something_else")
        self.assertEquals(result, api.ENDPOINT_HOSTNAME_TYPE)
