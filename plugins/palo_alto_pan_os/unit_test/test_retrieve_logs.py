import sys
import os
from unittest import TestCase
from komand_palo_alto_pan_os.actions.retrieve_logs import RetrieveLogs
from komand_palo_alto_pan_os.actions.retrieve_logs.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
@patch("requests.get", side_effect=Util.mocked_requests)
class TestRetrieveLogs(TestCase):
    @parameterized.expand(
        [
            [
                "config",
                "config",
                1,
                0,
                "receive_time geq '2021/12/22 08:00:00'",
                0.5,
                25,
                "backward",
                {
                    "response": {
                        "logs": {
                            "@count": "1",
                            "@progress": "100",
                            "entry": {
                                "@logid": "7044309865149235243",
                                "domain": "1",
                                "receive_time": "2021/12/22 08:54:51",
                                "serial": "0000000000000001",
                                "seqno": "1550",
                                "actionflags": "0x0",
                                "is-logging-service": "no",
                                "type": "CONFIG",
                                "subtype": "0",
                                "config_ver": "0",
                                "time_generated": "2021/12/22 08:54:51",
                                "dg_hier_level_1": "0",
                                "dg_hier_level_2": "0",
                                "dg_hier_level_3": "0",
                                "dg_hier_level_4": "0",
                                "device_name": "TEST",
                                "vsys_id": "0",
                                "host": "198.51.100.100",
                                "cmd": "delete",
                                "admin": "admin",
                                "client": "Web",
                                "result": "Succeeded",
                                "path": "vsys  vsys1 external-list  Test Domain List",
                                "dg_id": "0",
                                "full-path": "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/external-list/entry[@name='Test Domain List']",
                            },
                        }
                    }
                },
            ],
            [
                "system",
                "system",
                1,
                0,
                "receive_time geq '2021/12/22 08:00:00'",
                0.5,
                25,
                "forward",
                {
                    "response": {
                        "logs": {
                            "@count": "1",
                            "@progress": "100",
                            "entry": {
                                "@logid": "7044309865149247490",
                                "domain": "1",
                                "receive_time": "2021/12/22 08:00:12",
                                "serial": "000000000000002",
                                "seqno": "8144908",
                                "actionflags": "0x0",
                                "is-logging-service": "no",
                                "type": "SYSTEM",
                                "subtype": "syslog",
                                "config_ver": "0",
                                "time_generated": "2021/12/22 08:00:12",
                                "dg_hier_level_1": "0",
                                "dg_hier_level_2": "0",
                                "dg_hier_level_3": "0",
                                "dg_hier_level_4": "0",
                                "device_name": "TEST",
                                "vsys_id": "0",
                                "eventid": "syslog-conn-status",
                                "fmt": "0",
                                "id": "0",
                                "module": "mgmt",
                                "severity": "high",
                                "opaque": "Syslog connection failed to server['TEST']",
                            },
                        }
                    }
                },
            ],
            [
                "threat",
                "threat",
                1,
                0,
                "receive_time geq '2021/12/22 08:00:00'",
                0.5,
                25,
                "forward",
                {
                    "response": {
                        "logs": {
                            "@count": "1",
                            "@progress": "100",
                            "entry": {
                                "@logid": "191242123113213",
                                "domain": "1",
                                "receive_time": "2021/12/22 12:50:24",
                                "serial": "000000000000003",
                                "seqno": "8210416",
                                "actionflags": "0x0",
                                "type": "THREAT",
                                "subtype": "vulnerability",
                                "config_ver": "1",
                                "time_generated": "2021/12/22 10:50:24",
                                "src": "xxx.xxx.xxx.xxx",
                                "dst": "xxx.xxx.xxx.xxx",
                                "rule": "CorporationHQ",
                                "srcloc": "United States",
                                "dstloc": "xxx.xxx.xxx.xxx-xxx.xxx.xxx.xxx",
                                "app": "smtp",
                                "vsys": "vsys1",
                                "from": "trust",
                                "to": "trust",
                                "inbound_if": "ethernet1/5",
                                "outbound_if": "ethernet1/6",
                                "logset": "Logs",
                                "time_received": "2021/12/22 12:50:24",
                                "sessionid": "135193",
                                "repeatcnt": "1",
                                "sport": "52252",
                                "dport": "25",
                                "action": "reset-both",
                                "dg_hier_level_1": "11",
                                "dg_hier_level_2": "0",
                                "dg_hier_level_3": "0",
                                "dg_hier_level_4": "0",
                                "device_name": "TEST",
                                "vsys_id": "1",
                                "threatid": "User Login Brute Force Attempt",
                                "tid": "0",
                                "reportid": "0",
                                "category": "any",
                                "severity": "high",
                                "direction": "client-to-server",
                            },
                        }
                    }
                },
            ],
            [
                "traffic_empty",
                "traffic",
                1,
                None,
                None,
                None,
                10,
                None,
                {"response": {"logs": {"@count": "0", "@progress": "100"}}},
            ],
        ]
    )
    def test_retrieve_logs(
        self, mock_get, mock_get2, name, log_type, count, skip, query_filter, interval, max_tries, direction, expected
    ):
        action = Util.default_connector(RetrieveLogs())
        actual = action.run(
            {
                Input.LOG_TYPE: log_type,
                Input.COUNT: count,
                Input.SKIP: skip,
                Input.FILTER: query_filter,
                Input.INTERVAL: interval,
                Input.MAX_TRIES: max_tries,
                Input.DIRECTION: direction,
            }
        )
        self.assertEqual(actual, expected)
