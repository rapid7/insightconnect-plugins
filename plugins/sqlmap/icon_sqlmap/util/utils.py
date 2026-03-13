import time
import functools
from typing import Any, Callable, TypeVar

ReturnType = TypeVar("ReturnType")


def delay(seconds: int) -> Callable[[Callable[..., ReturnType]], Callable[..., ReturnType]]:
    # Check if seconds are less than zero
    # If so, raise an exception
    if seconds < 0:
        raise ValueError(f"Delay seconds must be non-negative, got {seconds}")

    def decorator(function_: Callable[..., ReturnType]) -> Callable[..., ReturnType]:
        @functools.wraps(function_)
        def wrapper(*args: Any, **kwargs: Any) -> ReturnType:
            time.sleep(seconds)
            return function_(*args, **kwargs)

        return wrapper

    return decorator
