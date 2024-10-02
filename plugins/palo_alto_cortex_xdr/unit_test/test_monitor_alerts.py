import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from icon_palo_alto_cortex_xdr.tasks.monitor_alerts import MonitorAlerts
from icon_palo_alto_cortex_xdr.tasks.monitor_alerts.schema import MonitorAlertsOutput

from icon_palo_alto_cortex_xdr.connection.schema import Input

from parameterized import parameterized
from jsonschema import validate
from freezegun import freeze_time
from util import Util
from mock import mock_request_200

STUB_STATE_EXPECTED_NO_PAGE = {
    "last_alert_time": 1706540499609,
    "last_alert_hash": ["a502a9c50798186882ad8dc91ac2b38eb185c404"],
}

STUB_STATE_MORE_PAGES = {
    "current_count": 75,
    "last_search_to": 75,
    "last_search_from": 0,
    "query_start_time": 1722474123000,
    "query_end_time": 1727863925000,
    "last_alert_time": 1724420374000,
    "last_alert_hash": [
        "c0ed9be4335d314b4bfc9d33ea65f0c06d0d8fbb",
        "9de3ee6d69c23d40486f3043bd01deded6130b55",
        "6ad6d3c3e79616f69304b68124f75aad03635f8e",
        "c4a3f84eda5cd8a507be387e331d15817c82e039",
        "ba3f5408a8de4fdb564b48523b43ac6f8d3091af",
        "392dd67363c580cda5a49e27a3f190f6c5a08a73",
        "f579b2119e08b25c4fb751bd6ca0f7688f9e93a7",
        "9de53e7a76f314b6b70a9ed8a6f659068129c628",
        "8a95344c081cd38d291e284f5cdbe3b10f3c7ce4",
        "f4ceaaf0a08b6e2cdae7e5c226cbd24233f99704",
        "cc8b34ce7f0a38b094feaee915ba8f1e0a22073e",
        "0a4ffb83a939718ab8f31c554d9b8d54fc9aa9d9",
        "a3f5a23871e0574d1b47118ca49974f401338501",
        "96053f0e018b3c94cb791c825a8628f19207a89f",
        "25456dd091387fc246a7c38cdc5419149ca680ee",
        "7295beab5a109516d596303fdd6fc18a83a6fd68",
        "a4201e767a60256c2f7ecc59bd050fbbad5d7d97",
        "3429172bbf4840a7a0e9121ba569ecbd5b79ef28",
        "77d9b719ee6a017d3d253540d0985b35180ba159",
        "2287b94a12894cfee23219c1f69374939dce0320",
        "20366ea0d6db5954f8ad85d85a2153b0cf07103a",
        "111ac3c84cfef70fb17a727565eeb37571d76535",
        "f638d01c981b5e974684b0b43fc1cdfbc4e1a2e4",
        "0384ba025d93a3747f2617a590f813598459c4d5",
        "79f2818cdb80fa1e70b8a8c10c195324c128434e",
        "2e781966aa58e3ab00a79f420ab9c96115aaa456",
        "256665d8dfad63153d68dda9e3130ecfeb22044b",
        "fcb60946bd5817d6c0c6b74394ffa6ae23800c6d",
        "55d899b977a857345621ed21fcbaaeda6cb3de04",
        "98c2337c3caa1aa5d7f59f6317f5ea048c5a7695",
        "f1dc38919cf8055665ffa1744ce098872d752b34",
        "6c738819d5a36a41a89f53c372af235384c17d67",
        "a66bfa99f00bd1afdb120cc19db950981152931e",
        "5c20d39b2e4a6808c0494c822faa226a38b2e5ab",
        "6251689f1ae05f6273d0b0e53eeadb33ef3764f4",
        "6179aef47bc3337a3caa6a9fef4ccbcbbf02f43d",
        "89fa3b2459591d7f7815ddf2a231651cdc3153ce",
        "9b398c17616f6f28aa1f2b7e7522d41842fd85c1",
        "957523180a2a678a5503ef9b717c5fd69ce7dd1f",
        "f284cd2b51bc4b4f490ad0419c31f2b86c54ee31",
        "3d97fd7672803db61db1e7c7e23ba5d87b632409",
        "b7fa59f15fbfcc2729ea10d3da30807ed294731e",
        "490ede604cf631b0bbb547cb00ba0b9d6266bc71",
        "191a51e0a4b7de02176bc8bb843df881e17a1b6c",
        "dd390a001ca010cd8d13dd581080978e0f229031",
        "9a0c3cbdee9a11857ea338f5a4dac2250eda135b",
        "01619409d8abb8e745dabb5016c60b8baf8ac29a",
        "932c8fbe24d889f8338246e13ff57eae608a7432",
        "c3120211d9b8dd8edba7b5383db0e2012db07beb",
        "313ad6c9b5e4162adbe0a14dc176e379973ff2b6",
        "354e6ba600a1b2765e3d091312ca5a67bca2083d",
        "55bfb70371898cb1a9e0b2cf6ce1cd2925c9c43f",
        "9fc507e3a6637b0d97b31950a4d6937da5479be9",
        "cb457fb114834a99a77c9b4c172d217c1a92fd09",
        "c104b0e4b920b2ddedffb11bb3c9759068deb8ed",
        "9333b3eee06dbfc85746b9c646c9afb4ad68df0c",
        "10505ebd4dfe0bd698b2b3ba509b9a555e55b700",
        "b54cd80b21b2a022ca3496b8eb81f5c593ca7610",
        "c133e5ac25f102b671b29a6bff40c8fa88a5713b",
        "f9acfb17f9fa63a26e1ab8de50ebf89f2620d791",
        "9268295e6fe25574361a995cdda673eb24465551",
        "ff82547c859cb60fd78a185cec3432beab04422d",
        "2f428d9c086c5fc3575d0df2ab6a15dbe17d808a",
        "342f9906f47041da2a3fac60ef4604cd444a543c",
        "ac71feb0f0c0cc3806b13f8334263bccac14079e",
        "dc11d83c78debd63f2085da1a81a80deae032f7f",
        "4b983f6be031a914749acebf0c4b5c7c8b4c239d",
        "4cf4c3e2893fde26ada4f455ab16974adb49a2a0",
        "768755590c342760739081aaeaaa3ac01d50f77a",
        "bdd8f9cf541c64d5947d24f31895ecaa95dbd72c",
        "ea4f758534b0b63e642ecb5a92f1af761a771d24",
        "1051b98f8990117a9600646b3a31926c87d79002",
        "c5686ffc40b040701a25025a0bea382a8c54620e",
        "f532c5382f2e9a825a647925cfc5f49812fc60cd",
        "8bfbc3b61cd77989a3785e0a33c7db4036c785ed",
    ],
}


@freeze_time("2024-01-29T15:01:00.000000Z")
@patch("requests.Session.send", side_effect=mock_request_200)
class TestMonitorAlerts(TestCase):
    @classmethod
    @patch("requests.Session.send", side_effect=mock_request_200)
    def setUpClass(cls, mock_post) -> None:
        _, cls.task = Util.default_connector(
            MonitorAlerts(),
            connect_params={
                Input.API_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
                Input.API_KEY_ID: 15,
                Input.SECURITY_LEVEL: "Advanced",
                Input.URL: "https://example.com/",
            },
        )

    @parameterized.expand(
        [
            [
                "starting",
                {},
                {},
                False,
                Util.load_expected("monitor_alerts"),
                STUB_STATE_EXPECTED_NO_PAGE,
                200,
                None,
            ],
            [
                "next_page",
                STUB_STATE_MORE_PAGES,
                {},
                False,
                Util.load_expected("monitor_alerts"),
                STUB_STATE_MORE_PAGES,
                200,
                None
            ],
            [
                "final_page",
                STUB_STATE_EXPECTED_NO_PAGE,
                {},
                False,
                [],
                STUB_STATE_EXPECTED_NO_PAGE,
                200,
                None
            ]
        ]
    )
    def test_monitor_alerts(
        self,
        mock_post,
        test_name,
        state,
        custom_config,
        expected_has_more_pages,
        expected_output,
        expected_state,
        expected_status_code,
        expected_error,
    ) -> None:

        output, state, has_more_pages, status_code, error = self.task.run(
            params={}, state=state, custom_config=custom_config
        )
        self.assertEqual(output, expected_output)
        self.assertEqual(state, expected_state)
        self.assertEqual(has_more_pages, expected_has_more_pages)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(error, expected_error)
        validate(output, MonitorAlertsOutput.schema)


# @parameterized.expand(Util.load_parameters("monitor_alerts_custom_config").get("parameters"))
# def test_monitor_alerts_custm_config(
#     self,
#     mock_request: Mock,
#     mock_post: Mock,
#     test_name,
#     start_time,
#     input_state,
#     input_config,
#     expected_has_more_pages,
#     expected_output,
#     expected_state,
#     expected_status_code,
#     expected_error,
# ) -> None:
#     with freeze_time(start_time):
#         actual, actual_state, has_more_pages, status_code, error = self.task.run(
#             state=input_state, custom_config=input_config
#         )
#         self.assertEqual(actual, expected_output)
#         self.assertEqual(actual_state, expected_state)
#         self.assertEqual(has_more_pages, expected_has_more_pages)
#         self.assertEqual(status_code, expected_status_code)
#         self.assertEqual(error, expected_error)

# @parameterized.expand(Util.load_parameters("monitor_alerts_error").get("parameters"))
# @patch("requests.Session.send", side_effect=mock_request_500)

# def test_monitor_alerts_error(
#     self,
#     test_name,
#     start_time,
#     input_state,
#     expected_has_more_pages,
#     expected_output,
#     expected_state,
#     expected_status_code,
#     expected_error,
#     mock_post,
# ) -> None:
#     with freeze_time(start_time):

#         mocked_request(mock_post)

#         actual, actual_state, has_more_pages, status_code, error = self.task.run(state=input_state)
#         self.assertEqual(actual, expected_output)
#         self.assertEqual(actual_state, expected_state)
#         self.assertEqual(has_more_pages, expected_has_more_pages)
#         self.assertEqual(status_code, expected_status_code)
#         self.assertEqual(error, expected_error)
#         validate(actual, MonitorAlertsOutput.schema)

# @parameterized.expand(
#         [
#             [
#                 "400",
#                 {},
#                 400,
#                 "The server is unable to process the request.",
#                 "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
#             ]
#         ]
# )
# @patch("requests.Session.send", side_effect=mock_request_error)


# def test_monitor_logs_api_errors(

#     self,
#     test_name,
#     start_time,
#     input_state,
#     expected_status_code,
#     expected_cause,
#     expected_assistance,
#     mock_post
# ):
#     with freeze_time(start_time):

#         output, state, has_more_pages, status_code, error = self.task.run(state=input_state)

#         mocked_request(mock_post)

#         self.assertEqual(False, has_more_pages)
#         self.assertEqual(expected_status_code, status_code)
#         self.assertEqual(expected_cause, error.cause)
#         self.assertEqual(expected_assistance, error.assistance)
