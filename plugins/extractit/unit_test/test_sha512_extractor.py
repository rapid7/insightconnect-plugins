from unittest import TestCase
from icon_extractit.actions.sha512_extractor import Sha512Extractor
from icon_extractit.actions.sha512_extractor.schema import Input, Output


class TestSha512Extractor(TestCase):
    def test_extract_sha512_from_string(self):
        action = Sha512Extractor()
        actual = action.run(
            {
                Input.STR: "cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab and CC805D5FAB1FD71A4AB352A9C533E65FB2D5B885518F4E565E68847223B8E6B85CB48F3AFAD842726D99239C9E36505C64B0DC9A061D9E507D833277ADA336AB are example SHA512 hashes"
            }
        )
        expected = {
            Output.SHA512: [
                "cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab",
                "CC805D5FAB1FD71A4AB352A9C533E65FB2D5B885518F4E565E68847223B8E6B85CB48F3AFAD842726D99239C9E36505C64B0DC9A061D9E507D833277ADA336AB",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_sha512_from_file(self):
        action = Sha512Extractor()
        actual = action.run(
            {
                Input.FILE: "Y2M4MDVkNWZhYjFmZDcxYTRhYjM1MmE5YzUzM2U2NWZiMmQ1Yjg4NTUxOGY0ZTU2NWU2ODg0NzIyM2I4ZTZiODVjYjQ4ZjNhZmFkODQyNzI2ZDk5MjM5YzllMzY1MDVjNjRiMGRjOWEwNjFkOWU1MDdkODMzMjc3YWRhMzM2YWIgYW5kIENDODA1RDVGQUIxRkQ3MUE0QUIzNTJBOUM1MzNFNjVGQjJENUI4ODU1MThGNEU1NjVFNjg4NDcyMjNCOEU2Qjg1Q0I0OEYzQUZBRDg0MjcyNkQ5OTIzOUM5RTM2NTA1QzY0QjBEQzlBMDYxRDlFNTA3RDgzMzI3N0FEQTMzNkFCIGFyZSBleGFtcGxlIFNIQTUxMiBoYXNoZXM=",
            }
        )
        expected = {
            Output.SHA512: [
                "cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab",
                "CC805D5FAB1FD71A4AB352A9C533E65FB2D5B885518F4E565E68847223B8E6B85CB48F3AFAD842726D99239C9E36505C64B0DC9A061D9E507D833277ADA336AB",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_sha512_from_string_bad(self):
        action = Sha512Extractor()
        actual = action.run(
            {
                Input.STR: "cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d and CC805D5FAB1FD71A4AB352A9C533E65FB2D5B885518F4E565E68847223B8E6B85CB48F3AFAD842726D99239C9E36505C64B0DC9A061D9E507D833277ADA336ABADA336AB are not example SHA512 hashes"
            }
        )
        expected = {Output.SHA512: []}
        self.assertEqual(actual, expected)

    def test_extract_sha512_from_file_bad(self):
        action = Sha512Extractor()
        actual = action.run(
            {
                Input.FILE: "Y2M4MDVkNWZhYjFmZDcxYTRhYjM1MmE5YzUzM2U2NWZiMmQ1Yjg4NTUxOGY0ZTU2NWU2ODg0NzIyM2I4ZTZiODVjYjQ4ZjNhZmFkODQyNzI2ZDk5MjM5YzllMzY1MDVjNjRiMGRjOWEwNjFkOWU1MDdkIGFuZCBDQzgwNUQ1RkFCMUZENzFBNEFCMzUyQTlDNTMzRTY1RkIyRDVCODg1NTE4RjRFNTY1RTY4ODQ3MjIzQjhFNkI4NUNCNDhGM0FGQUQ4NDI3MjZEOTkyMzlDOUUzNjUwNUM2NEIwREM5QTA2MUQ5RTUwN0Q4MzMyNzdBREEzMzZBQkFEQTMzNkFCIGFyZSBub3QgZXhhbXBsZSBTSEE1MTIgaGFzaGVz",
            }
        )
        expected = {Output.SHA512: []}
        self.assertEqual(actual, expected)
