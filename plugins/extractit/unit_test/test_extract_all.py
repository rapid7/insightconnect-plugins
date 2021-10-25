from unittest import TestCase
from icon_extractit.actions.extract_all import ExtractAll
from icon_extractit.actions.extract_all.schema import Input, Output


class TestIocExtractor(TestCase):
    def test_extract_no_all_from_string(self):
        action = ExtractAll()
        actual = action.run(
            {
                Input.STR: "aaaaa,1111\nbbbbb,2222",
            }
        )
        expected = {
            Output.INDICATORS: {
                "cves": [],
                "dates": [],
                "domains": [],
                "email_addresses": [],
                "filepaths": [],
                "hashes": {"md5_hashes": [], "sha1_hashes": [], "sha256_hashes": [], "sha512_hashes": []},
                "ip_addresses": {"ipv4_addresses": [], "ipv6_addresses": []},
                "mac_addresses": [],
                "urls": [],
                "uuids": [],
            }
        }
        self.assertEqual(actual, expected)

    def test_extract_no_all_from_file(self):
        action = ExtractAll()
        actual = action.run(
            {
                Input.FILE: "YWFhYWEsMTExMVxuYmJiYmIsMjIyMg==",
            }
        )
        expected = {
            Output.INDICATORS: {
                "cves": [],
                "dates": [],
                "domains": [],
                "email_addresses": [],
                "filepaths": [],
                "hashes": {"md5_hashes": [], "sha1_hashes": [], "sha256_hashes": [], "sha512_hashes": []},
                "ip_addresses": {"ipv4_addresses": [], "ipv6_addresses": []},
                "mac_addresses": [],
                "urls": [],
                "uuids": [],
            }
        }
        self.assertEqual(actual, expected)

    def test_extract_all_from_string(self):
        action = ExtractAll()
        actual = action.run(
            {
                Input.STR: "dsfdfj fgfdf gf fg 12/12/2312 https://www.google.com http://vbfmhgsdfhsgfmwww.mem.pl dvfngfdsfgghgtest@user.com hdg fd hsgfd sdfsfgyfdhfgg123e4567-e89b-12d3-a456-426614174001 fg dgsfsdfghcvhdgfhkdhhefrhwfjhfmhtest@usere.com123e4567-e89b-12d3-a456-426614174000 cve-6543-75633hmfgsdhfgshfgSHFg fdshfsmcve-7564-5463729 test.pl bhfskhgfksfygewfhgkt google.comgdgfjhmjhdfgb,jhghbg,vfhgfhtihtl;l[proi98756476rtedfgvsbjko m,hlpiou8y756ew4678960i[op]]A94A8FE5CCB19BA61C4C0873D391E987982FBBD3 gvfhsfhdsfv vfgvfrhgf109F4B3C50D7B0DF729D299BC6F8E9EF9066971F hgvfkagrefjeg eggfy60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752 gvfjeagfjehggfjrgutga140c0c1eda2def2b830363ba362aa4d7d255c262960544821f556e16661b6ffhgkugghltybv 2257aab44b42813142aa8ac4767116ad5bd41e94a79aa0672cc962128ed4809f50ed38d35ba945a80799976c9efa9b686f28d18036134bc2bb0ac2de96ec6280hfg sfgsjfgsfhvbgffhsjhgi687q67jhkgfhdvytfh9d8c92f94dfc83818245501756afcfb5ca850ebd488a9b0bc195f1c026d98306e13a9c86aa423ca1c2e87c9e0f187bd465306930c25b596ff4e23be21b6037b0gfygerktjhaiurgtierlghbd1901231b0822a59c64c48ca3757fb5\nfhegwf,jhewfgbsjgkerjgbrjgbrejhbjryjrvfbnghrugfcffb9c1f93b6337e59444dbafbd62369hdgfkuaerghkerjhyb ryjltkjuyiluytfwdh;oulr 192.168.1.2 fgywegkwehfgb.skbfgkgvc,jhbskfvfw1.1.1.12001:db8:3333:4444:5555:6666:7777:8888 gefjegwfbkgerhyi56987y4ouyfgbvnhjoytrivuwrbgkqu gtkhtykuibtvt kgku54yl6i. ijli t 2001:db8:3333:4444:5555:6666:7777:6666 gyfhgwvfgkyewtflhwbluo4tyjiy;ehgjsdgk 2C:54:91:88:C9:E3 tjrdhh cjgjytrdyjgkjj n2c-54-91-88-c9-e3tdfhgvjcd;fohugw4uer743ytbgfjgjhi vgh;byo8hjdpoy uig2013-02-07 jdbfgsfbsj,ghbjghSun May 20 21:00:00 PDT 2013vghvdfj 02699626f388ed830012e5b787640e71c56d42d8 whfggkgtkeugftrdnfb shgv 9de5069c5afe602b2ea0a04b66beb2c0  cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab  275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f jbjky vjv:c/test/usersc/test/users/fdfgsefrjefgjhyv/eyrtewgjg/grug",
            }
        )
        expected = {
            Output.INDICATORS: {
                "cves": ["cve-6543-75633", "cve-7564-5463729"],
                "dates": ["2312-12-12T00:00:00Z"],
                "domains": [
                    "www.google.com",
                    "vbfmhgsdfhsgfmwww.mem.pl",
                    "user.com",
                    "usere.com",
                    "test.pl",
                    "google.comgdgfjhmjhdfgb",
                    "fgywegkwehfgb.skbfgkgvc",
                ],
                "email_addresses": [
                    "dvfngfdsfgghgtest@user.com",
                    "dgsfsdfghcvhdgfhkdhhefrhwfjhfmhtest@usere.com123e4567-e89b-12d3-a456-426614174000",
                ],
                "filepaths": ["/test/usersc/test/users/fdfgsefrjefgjhyv/eyrtewgjg/grug"],
                "hashes": {
                    "md5_hashes": ["9de5069c5afe602b2ea0a04b66beb2c0"],
                    "sha1_hashes": [
                        "A94A8FE5CCB19BA61C4C0873D391E987982FBBD3",
                        "02699626f388ed830012e5b787640e71c56d42d8",
                    ],
                    "sha256_hashes": ["275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"],
                    "sha512_hashes": [
                        "cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab"
                    ],
                },
                "ip_addresses": {
                    "ipv4_addresses": ["192.168.1.2", "1.1.1.120"],
                    "ipv6_addresses": [
                        "2001:db8:3333:4444:5555:6666:7777:8888",
                        "2001:db8:3333:4444:5555:6666:7777:6666",
                    ],
                },
                "mac_addresses": ["2C:54:91:88:C9:E3"],
                "urls": ["https://www.google.com", "http://vbfmhgsdfhsgfmwww.mem.pl"],
                "uuids": ["123e4567-e89b-12d3-a456-426614174001", "123e4567-e89b-12d3-a456-426614174000"],
            }
        }
        self.assertEqual(actual, expected)

    def test_extract_all_from_file(self):
        action = ExtractAll()
        actual = action.run(
            {
                Input.FILE: "ZHNmZGZqIGZnZmRmIGdmIGZnIDEyLzEyLzIzMTIgaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbSBodHRwOi8vdmJmbWhnc2RmaHNnZm13d3cubWVtLnBsIGR2Zm5nZmRzZmdnaGd0ZXN0QHVzZXIuY29tIGhkZyBmZCBoc2dmZCBzZGZzZmd5ZmRoZmdnMTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDAxIGZnIGRnc2ZzZGZnaGN2aGRnZmhrZGhoZWZyaHdmamhmbWh0ZXN0QHVzZXJlLmNvbTEyM2U0NTY3LWU4OWItMTJkMy1hNDU2LTQyNjYxNDE3NDAwMCBjdmUtNjU0My03NTYzM2htZmdzZGhmZ3NoZmdTSEZnIGZkc2hmc21jdmUtNzU2NC01NDYzNzI5IHRlc3QucGwgYmhmc2toZ2Zrc2Z5Z2V3Zmhna3QgZ29vZ2xlLmNvbWdkZ2ZqaG1qaGRmZ2IsamhnaGJnLHZmaGdmaHRpaHRsO2xbcHJvaTk4NzU2NDc2cnRlZGZndnNiamtvIG0saGxwaW91OHk3NTZldzQ2Nzg5NjBpW29wXV1BOTRBOEZFNUNDQjE5QkE2MUM0QzA4NzNEMzkxRTk4Nzk4MkZCQkQzIGd2ZmhzZmhkc2Z2IHZmZ3ZmcmhnZjEwOUY0QjNDNTBEN0IwREY3MjlEMjk5QkM2RjhFOUVGOTA2Njk3MUYgaGd2ZmthZ3JlZmplZyBlZ2dmeTYwMzAzYWUyMmI5OTg4NjFiY2UzYjI4ZjMzZWVjMWJlNzU4YTIxM2M4NmM5M2MwNzZkYmU5ZjU1OGMxMWM3NTIgZ3ZmamVhZ2ZqZWhnZ2Zqcmd1dGdhMTQwYzBjMWVkYTJkZWYyYjgzMDM2M2JhMzYyYWE0ZDdkMjU1YzI2Mjk2MDU0NDgyMWY1NTZlMTY2NjFiNmZmaGdrdWdnaGx0eWJ2IDIyNTdhYWI0NGI0MjgxMzE0MmFhOGFjNDc2NzExNmFkNWJkNDFlOTRhNzlhYTA2NzJjYzk2MjEyOGVkNDgwOWY1MGVkMzhkMzViYTk0NWE4MDc5OTk3NmM5ZWZhOWI2ODZmMjhkMTgwMzYxMzRiYzJiYjBhYzJkZTk2ZWM2MjgwaGZnIHNmZ3NqZmdzZmh2YmdmZmhzamhnaTY4N3E2N2poa2dmaGR2eXRmaDlkOGM5MmY5NGRmYzgzODE4MjQ1NTAxNzU2YWZjZmI1Y2E4NTBlYmQ0ODhhOWIwYmMxOTVmMWMwMjZkOTgzMDZlMTNhOWM4NmFhNDIzY2ExYzJlODdjOWUwZjE4N2JkNDY1MzA2OTMwYzI1YjU5NmZmNGUyM2JlMjFiNjAzN2IwZ2Z5Z2Vya3RqaGFpdXJndGllcmxnaGJkMTkwMTIzMWIwODIyYTU5YzY0YzQ4Y2EzNzU3ZmI1XG5maGVnd2Ysamhld2ZnYnNqZ2tlcmpnYnJqZ2JyZWpoYmpyeWpydmZibmdocnVnZmNmZmI5YzFmOTNiNjMzN2U1OTQ0NGRiYWZiZDYyMzY5aGRnZmt1YWVyZ2hrZXJqaHliIHJ5amx0a2p1eWlsdXl0ZndkaDtvdWxyIDE5Mi4xNjguMS4yIGZneXdlZ2t3ZWhmZ2Iuc2tiZmdrZ3ZjLGpoYnNrZnZmdzEuMS4xLjEyMDAxOmRiODozMzMzOjQ0NDQ6NTU1NTo2NjY2Ojc3Nzc6ODg4OCBnZWZqZWd3ZmJrZ2VyaHlpNTY5ODd5NG91eWZnYnZuaGpveXRyaXZ1d3JiZ2txdSBndGtodHlrdWlidHZ0IGtna3U1NHlsNmkuIGlqbGkgdCAyMDAxOmRiODozMzMzOjQ0NDQ6NTU1NTo2NjY2Ojc3Nzc6NjY2NiBneWZoZ3d2ZmdreWV3dGZsaHdibHVvNHR5aml5O2VoZ2pzZGdrIDJDOjU0OjkxOjg4OkM5OkUzIHRqcmRoaCBjamdqeXRyZHlqZ2tqaiBuMmMtNTQtOTEtODgtYzktZTN0ZGZoZ3ZqY2Q7Zm9odWd3NHVlcjc0M3l0YmdmamdqaGkgdmdoO2J5bzhoamRwb3kgdWlnMjAxMy0wMi0wNyBqZGJmZ3NmYnNqLGdoYmpnaFN1biBNYXkgMjAgMjE6MDA6MDAgUERUIDIwMTN2Z2h2ZGZqIDAyNjk5NjI2ZjM4OGVkODMwMDEyZTViNzg3NjQwZTcxYzU2ZDQyZDggd2hmZ2drZ3RrZXVnZnRyZG5mYiBzaGd2IDlkZTUwNjljNWFmZTYwMmIyZWEwYTA0YjY2YmViMmMwICBjYzgwNWQ1ZmFiMWZkNzFhNGFiMzUyYTljNTMzZTY1ZmIyZDViODg1NTE4ZjRlNTY1ZTY4ODQ3MjIzYjhlNmI4NWNiNDhmM2FmYWQ4NDI3MjZkOTkyMzljOWUzNjUwNWM2NGIwZGM5YTA2MWQ5ZTUwN2Q4MzMyNzdhZGEzMzZhYiAgMjc1YTAyMWJiZmI2NDg5ZTU0ZDQ3MTg5OWY3ZGI5ZDE2NjNmYzY5NWVjMmZlMmEyYzQ1MzhhYWJmNjUxZmQwZiBqYmpreSB2anY6Yy90ZXN0L3VzZXJzYy90ZXN0L3VzZXJzL2ZkZmdzZWZyamVmZ2poeXYvZXlydGV3Z2pnL2dydWc=",
            }
        )
        expected = {
            Output.INDICATORS: {
                "cves": ["cve-6543-75633", "cve-7564-5463729"],
                "dates": ["2312-12-12T00:00:00Z"],
                "domains": [
                    "www.google.com",
                    "vbfmhgsdfhsgfmwww.mem.pl",
                    "user.com",
                    "usere.com",
                    "test.pl",
                    "google.comgdgfjhmjhdfgb",
                    "fgywegkwehfgb.skbfgkgvc",
                ],
                "email_addresses": [
                    "dvfngfdsfgghgtest@user.com",
                    "dgsfsdfghcvhdgfhkdhhefrhwfjhfmhtest@usere.com123e4567-e89b-12d3-a456-426614174000",
                ],
                "filepaths": ["/test/usersc/test/users/fdfgsefrjefgjhyv/eyrtewgjg/grug"],
                "hashes": {
                    "md5_hashes": ["9de5069c5afe602b2ea0a04b66beb2c0"],
                    "sha1_hashes": [
                        "A94A8FE5CCB19BA61C4C0873D391E987982FBBD3",
                        "02699626f388ed830012e5b787640e71c56d42d8",
                    ],
                    "sha256_hashes": ["275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"],
                    "sha512_hashes": [
                        "cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab"
                    ],
                },
                "ip_addresses": {
                    "ipv4_addresses": ["192.168.1.2", "1.1.1.120"],
                    "ipv6_addresses": [
                        "2001:db8:3333:4444:5555:6666:7777:8888",
                        "2001:db8:3333:4444:5555:6666:7777:6666",
                    ],
                },
                "mac_addresses": ["2C:54:91:88:C9:E3"],
                "urls": [
                    "https://www.google.com",
                    "http://vbfmhgsdfhsgfmwww.mem.pl",
                ],
                "uuids": ["123e4567-e89b-12d3-a456-426614174001", "123e4567-e89b-12d3-a456-426614174000"],
            }
        }
        self.assertEqual(actual, expected)
