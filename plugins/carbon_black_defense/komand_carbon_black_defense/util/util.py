from functools import wraps

from _datetime import datetime


class Util:
    def retry(tries: int, timeout: int, exceptions):
        """
        @param tries: Amount of times function is to be retried
        @param timeout: Timeout period in seconds. Retries will cease after this period
        @param exceptions: Increment number of function attempts if these exceptions are raised
        """

        def decorator(func):
            @wraps(func)
            def f_retry(*args, **kwargs):
                attempt = 0
                t1 = datetime.now()
                while attempt < tries:
                    while (datetime.now() - t1).seconds < timeout:
                        try:
                            return func(*args, **kwargs)
                        except exceptions:
                            attempt += 1

            return f_retry

        return decorator
