import random
from functools import wraps
import time
from _datetime import datetime


class Util:
    def retry(tries: int, timeout: int, exceptions, backoff_seconds: int = 1):
        """
        @param tries: Amount of times function is to be retried
        @param timeout: Timeout period in seconds. Retries will cease after this period
        @param exceptions: Increment number of function attempts if these exceptions are raised
        @param backoff_seconds: Time in seconds to be used in sleep algorithm for backoff. Value will be multiplied by
        2, multiplied again by the number of attempts, and have a randomised ms value as an addition.
        """

        def decorator(func):
            @wraps(func)
            def f_retry(*args, **kwargs):
                attempt = 1
                t1 = datetime.now()
                while attempt < tries:
                    while (datetime.now() - t1).seconds < timeout:
                        try:
                            # Sleep exponentially increases per retry
                            # # nosec prevents bandit warning
                            time.sleep(backoff_seconds * 2**attempt + random.uniform(0, 1))  # nosec
                            return func(*args, **kwargs)
                        except exceptions:
                            attempt += 1

            return f_retry

        return decorator
