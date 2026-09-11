class MockConnection:
    """Fake connection used by unit tests -- .call() returns a canned
    response keyed by path instead of making a real HTTP request."""

    def __init__(self, responses: dict):
        self.api_key = "test_api_key"
        self._responses = responses

    def call(self, path: str, payload: dict) -> dict:
        return self._responses[path]
