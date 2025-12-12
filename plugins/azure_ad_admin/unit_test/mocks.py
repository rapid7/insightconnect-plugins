from typing import Dict


class MockRequest:
    def __init__(self, status_code) -> None:
        self.status_code = status_code

    def json(self) -> Dict:
        return {
            "accountEnabled": True,
            "mobilePhone": None,
            "manager": {
                "@odata.type": "#microsoft.graph.user",
                "city": None,
                "companyName": None,
            },
        }

    def text(self) -> Dict:
        return {"text": "sample response"}

    def raise_for_status(self):
        if 400 <= self.status_code:
            raise Exception("HTTPError")
