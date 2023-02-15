from typing import Dict


class MockRequest:
    def __init__(self, status_code):
        self.status_code = status_code

    def json(self) -> Dict:
        return {
            "user": {
                "id": 4245316,
                "name": "Test user",
                "disabled": False,
                "email": "user@example.com",
                "created_at": "2018-11-22T15:18:53.337-05:00",
                "phone": "123456",
                "mobile_phone": "0012345",
                "department": {"id": 133365, "name": "Marketing"},
                "role": {
                    "id": 461182,
                    "name": "Read Only",
                    "portal": False,
                    "show_my_tasks": False,
                },
                "salt": "fc136bca03c6361bf1e564e18d70cc421b1fc582",
                "group_ids": [4492546],
                "custom_fields_values": [],
                "avatar": {"type": "initials", "color": "#fa7911", "initials": "JS"},
                "mfa_enabled": False,
            },
        }



    def text(self) -> Dict:
        return {"text": "sample response"}

    def raise_for_status(self):
        if 400 <= self.status_code:
            raise Exception("HTTPError")
