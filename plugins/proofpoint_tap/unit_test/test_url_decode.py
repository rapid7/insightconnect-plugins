import sys
import os
from unittest import TestCase
from unittest.mock import patch
from komand_proofpoint_tap.actions.url_decode import UrlDecode
from komand_proofpoint_tap.actions.url_decode.schema import Input, Output
from unit_test.test_util import Util

sys.path.append(os.path.abspath("../"))


class TestUrlDecode(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UrlDecode())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_url_decode(self, mock_request):
        actual = self.action.run(
            {
                Input.URLS: [
                    "https://urldefense.com/v3/__https://google.com:443/search?q=a*test\u0026gs=ps__;Kw!-612Flbf0JvQ3kNJkRi5Jg!Ue6tQudNKaShHg93trcdjqDP8se2ySE65jyCIe2K1D_uNjZ1Lnf6YLQERujngZv9UWf66ujQIQ$"
                ]
            }
        )
        expected = {
            Output.RESULTS: {
                "urls": [
                    {
                        "encodedUrl": "https://urldefense.com/v3/__https://google.com:443/search?q=a*test\u0026gs=ps__;Kw!-612Flbf0JvQ3kNJkRi5Jg!Ue6tQudNKaShHg93trcdjqDP8se2ySE65jyCIe2K1D_uNjZ1Lnf6YLQERujngZv9UWf66ujQIQ$",
                        "decodedUrl": "https://google.com:443/search?q=a+test&gs=ps",
                        "success": True,
                    }
                ]
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_url_decode_few_urls(self, mock_request):
        actual = self.action.run(
            {
                Input.URLS: [
                    "https://urldefense.com/v3/__https://google.com:443/search?q=a*test\u0026gs=ps__;Kw!-612Flbf0JvQ3kNJkRi5Jg!Ue6tQudNKaShHg93trcdjqDP8se2ySE65jyCIe2K1D_uNjZ1Lnf6YLQERujngZv9UWf66ujQIQ$",
                    "https://urldefense.proofpoint.com/v2/url?u=http-3A__www.adobe.com\u0026d=DwMFAg\u0026c=euGZstcaTDllvimEN8b7jXrwqOf-v5A_CdpgnVfiiMM\u0026r=qz5Nye49FfyB5hGQyu28CmCl4j-JuT-5fRrqkD5GgOM\u0026m=QyWbhzT6tTSmG0PkgURbBDFXWsffEz6VJtOFlHPGs5A\u0026s=rK9Hy_NPWtw6vwc7yG4zoBSWS_nOtkzg4pbYpJGfFb0\u0026e=",
                ]
            }
        )
        expected = {
            Output.RESULTS: {
                "urls": [
                    {
                        "encodedUrl": "https://urldefense.com/v3/__https://google.com:443/search?q=a*test\u0026gs=ps__;Kw!-612Flbf0JvQ3kNJkRi5Jg!Ue6tQudNKaShHg93trcdjqDP8se2ySE65jyCIe2K1D_uNjZ1Lnf6YLQERujngZv9UWf66ujQIQ$",
                        "decodedUrl": "https://google.com:443/search?q=a+test&gs=ps",
                        "success": True,
                    },
                    {
                        "encodedUrl": "https://urldefense.proofpoint.com/v2/url?u=http-3A__www.adobe.com\u0026d=DwMFAg\u0026c=euGZstcaTDllvimEN8b7jXrwqOf-v5A_CdpgnVfiiMM\u0026r=qz5Nye49FfyB5hGQyu28CmCl4j-JuT-5fRrqkD5GgOM\u0026m=QyWbhzT6tTSmG0PkgURbBDFXWsffEz6VJtOFlHPGs5A\u0026s=rK9Hy_NPWtw6vwc7yG4zoBSWS_nOtkzg4pbYpJGfFb0\u0026e=",
                        "decodedUrl": "http://www.adobe.com",
                        "success": True,
                    },
                ]
            }
        }
        self.assertEqual(actual, expected)
