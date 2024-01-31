from __future__ import annotations

from typing import Any, Dict, List

EXAMPLE_EXCEPTION_MESSAGE = "An exception occurred"
EXAMPLE_JOB_HISTORY = [{"1": "Test", "2": "Test2"}]
EXAMPLE_JOB_ID = "12345"
EXAMPLE_LIST_SAVED_SEARCHES = [{"1": "Test", "2": "Test2"}]


class Job:
    def __init__(self, state: bool = False) -> None:
        self.state = state

    def is_done(self) -> bool:
        return self.state

    @staticmethod
    def results() -> List[str]:
        return []

    def readall(self) -> str:
        return '{"results":[{"_time":"2024-01-30T12:46:00","event":"example event 1"},{"_time":"2024-01-30T12:47:00","event":"example event 2"},{"_time":"2024-01-30T12:48:00","event":"example event 3"}],"preview":false}'


class Jobs:
    def __init__(self) -> None:
        pass

    def __getitem__(self, name: str) -> Job:
        if name == "error":
            raise KeyError(EXAMPLE_EXCEPTION_MESSAGE)
        return Job(state=True)

    @staticmethod
    def oneshot(query: str, count: int, *args, **kwargs) -> Job:
        return Job(state=True)


class Index:
    def __init__(self, name: str) -> None:
        self.name = name

    def submit(self, *args, **kwargs) -> List[Dict[str, Any]]:
        pass


class Indexes:
    def __init__(self) -> None:
        pass

    def __getitem__(self, name: str) -> Index:
        if name == "error":
            raise KeyError(EXAMPLE_EXCEPTION_MESSAGE)
        return Index(name)

    @staticmethod
    def create(*args, **kwargs) -> Index:
        if "error" in args:
            return Index(args[0])
        raise Exception(EXAMPLE_EXCEPTION_MESSAGE)


class SavedSearch:
    def __init__(self, name: str) -> None:
        self.name = name
        self.content = {}

    def history(self) -> List[Dict[str, Any]]:
        if self.name == "error":
            raise KeyError(EXAMPLE_EXCEPTION_MESSAGE)
        return EXAMPLE_JOB_HISTORY

    def update(self, *args, **kwargs) -> SavedSearch:
        return self

    def refresh(self, *args, **kwargs) -> SavedSearch:
        return self

    def dispatch(self) -> Dict[str, Any]:
        if self.name == "error":
            raise KeyError(EXAMPLE_EXCEPTION_MESSAGE)
        return {"sid": EXAMPLE_JOB_ID}


class SavedSearches:
    def __init__(self) -> None:
        pass

    def __getitem__(self, name: str) -> SavedSearch:
        if name == "error":
            raise KeyError(EXAMPLE_EXCEPTION_MESSAGE)
        return SavedSearch(name)

    @staticmethod
    def list() -> List[Dict[str, Any]]:
        return EXAMPLE_LIST_SAVED_SEARCHES

    @staticmethod
    def create(*args, **kwargs) -> SavedSearch:
        if "ExampleSavedSearchName" in args:
            return SavedSearch(args[0])
        raise Exception(EXAMPLE_EXCEPTION_MESSAGE)

    def delete(self, *args, **kwargs) -> SavedSearch:
        try:
            return self.create(*args, **kwargs)
        except Exception as error:
            raise KeyError(error)


class MockClient:
    def __init__(self) -> None:
        self.saved_searches = SavedSearches()
        self.indexes = Indexes()
        self.jobs = Jobs()


def connect(*args, **kwargs) -> MockClient:
    return MockClient()
