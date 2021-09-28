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
                Input.STR: "dsfdfj fgfdf gf fg 12/12/2312 www.google.com vbfmhgsdfhsgfmwww.mem.pl dvfngfdsfgghgtest@user.com hdg fd hsgfd sdfsfgyfdhfgg123e4567-e89b-12d3-a456-426614174001 fg dgsfsdfghcvhdgfhkdhhefrhwfjhfmhtest@usere.com123e4567-e89b-12d3-a456-426614174000 cve-6543-75633hmfgsdhfgshfgSHFg fdshfsmcve-7564-5463729 test.pl/test bhfskhgfksfygewfhgkt google.comgdgfjhmjhdfgb,jhghbg,vfhgfhtihtl;l[proi98756476rtedfgvsbjko m,hlpiou8y756ew4678960i[op]]A94A8FE5CCB19BA61C4C0873D391E987982FBBD3 gvfhsfhdsfv vfgvfrhgf109F4B3C50D7B0DF729D299BC6F8E9EF9066971F hgvfkagrefjeg eggfy60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752 gvfjeagfjehggfjrgutga140c0c1eda2def2b830363ba362aa4d7d255c262960544821f556e16661b6ffhgkugghltybv 2257aab44b42813142aa8ac4767116ad5bd41e94a79aa0672cc962128ed4809f50ed38d35ba945a80799976c9efa9b686f28d18036134bc2bb0ac2de96ec6280hfg sfgsjfgsfhvbgffhsjhgi687q67jhkgfhdvytfh9d8c92f94dfc83818245501756afcfb5ca850ebd488a9b0bc195f1c026d98306e13a9c86aa423ca1c2e87c9e0f187bd465306930c25b596ff4e23be21b6037b0gfygerktjhaiurgtierlghbd1901231b0822a59c64c48ca3757fb5\nfhegwf,jhewfgbsjgkerjgbrjgbrejhbjryjrvfbnghrugfcffb9c1f93b6337e59444dbafbd62369hdgfkuaerghkerjhyb ryjltkjuyiluytfwdh;oulr 192.168.1.2 fgywegkwehfgb.skbfgkgvc,jhbskfvfw1.1.1.12001:db8:3333:4444:5555:6666:7777:8888 gefjegwfbkgerhyi56987y4ouyfgbvnhjoytrivuwrbgkqu gtkhtykuibtvt kgku54yl6i. ijli t 2001:db8:3333:4444:5555:6666:7777:6666 gyfhgwvfgkyewtflhwbluo4tyjiy;ehgjsdgk 2C:54:91:88:C9:E3 tjrdhh cjgjytrdyjgkjj n2c-54-91-88-c9-e3tdfhgvjcd;fohugw4uer743ytbgfjgjhi vgh;byo8hjdpoy uig2013-02-07 jdbfgsfbsj,ghbjghSun May 20 21:00:00 PDT 2013vghvdfj 02699626f388ed830012e5b787640e71c56d42d8 whfggkgtkeugftrdnfb shgv 9de5069c5afe602b2ea0a04b66beb2c0  cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab  275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f jbjky vjv:c/test/usersc/test/users/fdfgsefrjefgjhyv/eyrtewgjg/grug",
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
                    "www.google.com",
                    "vbfmhgsdfhsgfmwww.mem.pl",
                    "test.pl/test",
                    "google.comgdgfjhmjhdfgb",
                    "fgywegkwehfgb.skbfgkgvc",
                ],
                "uuids": ["123e4567-e89b-12d3-a456-426614174001", "123e4567-e89b-12d3-a456-426614174000"],
            }
        }
        self.assertEqual(actual, expected)

    def test_extract_all_from_file(self):
        action = ExtractAll()
        actual = action.run(
            {
                Input.FILE: "ZHNmZGZqIGZnZmRmIGdmIGZnIDEyLzEyLzIzMTIgd3d3Lmdvb2dsZS5jb20gdmJmbWhnc2RmaHNnZm13d3cubWVtLnBsIGR2Zm5nZmRzZmdnaGd0ZXN0QHVzZXIuY29tIGhkZyBmZCBoc2dmZCBzZGZzZmd5ZmRoZmdnMTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDAxIGZnIGRnc2ZzZGZnaGN2aGRnZmhrZGhoZWZyaHdmamhmbWh0ZXN0QHVzZXJlLmNvbTEyM2U0NTY3LWU4OWItMTJkMy1hNDU2LTQyNjYxNDE3NDAwMCBjdmUtNjU0My03NTYzM2htZmdzZGhmZ3NoZmdTSEZnIGZkc2hmc21jdmUtNzU2NC01NDYzNzI5IHRlc3QucGwvdGVzdCBiaGZza2hnZmtzZnlnZXdmaGdrdCBnb29nbGUuY29tZ2RnZmpobWpoZGZnYixqaGdoYmcsdmZoZ2ZodGlodGw7bFtwcm9pOTg3NTY0NzZydGVkZmd2c2Jqa28gbSxobHBpb3U4eTc1NmV3NDY3ODk2MGlbb3BdXUE5NEE4RkU1Q0NCMTlCQTYxQzRDMDg3M0QzOTFFOTg3OTgyRkJCRDMgZ3ZmaHNmaGRzZnYgdmZndmZyaGdmMTA5RjRCM0M1MEQ3QjBERjcyOUQyOTlCQzZGOEU5RUY5MDY2OTcxRiBoZ3Zma2FncmVmamVnIGVnZ2Z5NjAzMDNhZTIyYjk5ODg2MWJjZTNiMjhmMzNlZWMxYmU3NThhMjEzYzg2YzkzYzA3NmRiZTlmNTU4YzExYzc1MiBndmZqZWFnZmplaGdnZmpyZ3V0Z2ExNDBjMGMxZWRhMmRlZjJiODMwMzYzYmEzNjJhYTRkN2QyNTVjMjYyOTYwNTQ0ODIxZjU1NmUxNjY2MWI2ZmZoZ2t1Z2dobHR5YnYgMjI1N2FhYjQ0YjQyODEzMTQyYWE4YWM0NzY3MTE2YWQ1YmQ0MWU5NGE3OWFhMDY3MmNjOTYyMTI4ZWQ0ODA5ZjUwZWQzOGQzNWJhOTQ1YTgwNzk5OTc2YzllZmE5YjY4NmYyOGQxODAzNjEzNGJjMmJiMGFjMmRlOTZlYzYyODBoZmcgc2Znc2pmZ3NmaHZiZ2ZmaHNqaGdpNjg3cTY3amhrZ2ZoZHZ5dGZoOWQ4YzkyZjk0ZGZjODM4MTgyNDU1MDE3NTZhZmNmYjVjYTg1MGViZDQ4OGE5YjBiYzE5NWYxYzAyNmQ5ODMwNmUxM2E5Yzg2YWE0MjNjYTFjMmU4N2M5ZTBmMTg3YmQ0NjUzMDY5MzBjMjViNTk2ZmY0ZTIzYmUyMWI2MDM3YjBnZnlnZXJrdGpoYWl1cmd0aWVybGdoYmQxOTAxMjMxYjA4MjJhNTljNjRjNDhjYTM3NTdmYjVcbmZoZWd3ZixqaGV3Zmdic2pna2VyamdicmpnYnJlamhianJ5anJ2ZmJuZ2hydWdmY2ZmYjljMWY5M2I2MzM3ZTU5NDQ0ZGJhZmJkNjIzNjloZGdma3VhZXJnaGtlcmpoeWIgcnlqbHRranV5aWx1eXRmd2RoO291bHIgMTkyLjE2OC4xLjIgZmd5d2Vna3dlaGZnYi5za2JmZ2tndmMsamhic2tmdmZ3MS4xLjEuMTIwMDE6ZGI4OjMzMzM6NDQ0NDo1NTU1OjY2NjY6Nzc3Nzo4ODg4IGdlZmplZ3dmYmtnZXJoeWk1Njk4N3k0b3V5Zmdidm5oam95dHJpdnV3cmJna3F1IGd0a2h0eWt1aWJ0dnQga2drdTU0eWw2aS4gaWpsaSB0IDIwMDE6ZGI4OjMzMzM6NDQ0NDo1NTU1OjY2NjY6Nzc3Nzo2NjY2IGd5Zmhnd3ZmZ2t5ZXd0Zmxod2JsdW80dHlqaXk7ZWhnanNkZ2sgMkM6NTQ6OTE6ODg6Qzk6RTMgdGpyZGhoIGNqZ2p5dHJkeWpna2pqIG4yYy01NC05MS04OC1jOS1lM3RkZmhndmpjZDtmb2h1Z3c0dWVyNzQzeXRiZ2ZqZ2poaSB2Z2g7YnlvOGhqZHBveSB1aWcyMDEzLTAyLTA3IGpkYmZnc2Zic2osZ2hiamdoU3VuIE1heSAyMCAyMTowMDowMCBQRFQgMjAxM3ZnaHZkZmogMDI2OTk2MjZmMzg4ZWQ4MzAwMTJlNWI3ODc2NDBlNzFjNTZkNDJkOCB3aGZnZ2tndGtldWdmdHJkbmZiIHNoZ3YgOWRlNTA2OWM1YWZlNjAyYjJlYTBhMDRiNjZiZWIyYzAgIGNjODA1ZDVmYWIxZmQ3MWE0YWIzNTJhOWM1MzNlNjVmYjJkNWI4ODU1MThmNGU1NjVlNjg4NDcyMjNiOGU2Yjg1Y2I0OGYzYWZhZDg0MjcyNmQ5OTIzOWM5ZTM2NTA1YzY0YjBkYzlhMDYxZDllNTA3ZDgzMzI3N2FkYTMzNmFiICAyNzVhMDIxYmJmYjY0ODllNTRkNDcxODk5ZjdkYjlkMTY2M2ZjNjk1ZWMyZmUyYTJjNDUzOGFhYmY2NTFmZDBmIGpiamt5IHZqdjpjL3Rlc3QvdXNlcnNjL3Rlc3QvdXNlcnMvZmRmZ3NlZnJqZWZnamh5di9leXJ0ZXdnamcvZ3J1Zw==",
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
                    "www.google.com",
                    "vbfmhgsdfhsgfmwww.mem.pl",
                    "test.pl/test",
                    "google.comgdgfjhmjhdfgb",
                    "fgywegkwehfgb.skbfgkgvc",
                ],
                "uuids": ["123e4567-e89b-12d3-a456-426614174001", "123e4567-e89b-12d3-a456-426614174000"],
            }
        }
        self.assertEqual(actual, expected)
