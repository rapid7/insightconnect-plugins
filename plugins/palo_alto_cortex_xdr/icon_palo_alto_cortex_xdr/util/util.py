import time
import random

from functools import wraps
from _datetime import datetime
from typing import List, Dict
from insightconnect_plugin_runtime import Trigger


class Util:
    @staticmethod
    def now_ms():
        # Return the current epoch time in ms
        return int(time.time() * 1000)

    @staticmethod
    def send_items_to_platform_for_trigger(
        trigger: Trigger,
        items: List[Dict],
        output_type: str,
        last_event_processed_time_ms: int,
        time_field: str = "creation_time",
    ) -> [int]:
        for item in items:
            item_time = item.get(time_field, -1)
            # Check incident time to ensure we don't send dupes on to the platform
            if item_time > last_event_processed_time_ms:
                # Record time of this incident so we don't request events older than the one we
                # just sent on next iteration
                last_event_processed_time_ms = item_time
                trigger.send({output_type: item})
                yield last_event_processed_time_ms

    def retry(tries: int, timeout: int, exceptions, backoff_seconds: int = 1):
        """Function retries passed function based on input values
        :param tries: Amount of times function is to be retried
        :type tries: int, required
        :param timeout: Timeout period in seconds. Retries will cease after this period
        :type timeout: int, required
        :param exceptions: Increment number of function attempts if these exceptions are raised
        :type exceptions: []Exception, required
        :param backoff_seconds: Time in seconds to be used in sleep algorithm for backoff. Value will be multiplied by
        2, multiplied again by the number of attempts, and have a randomised ms value as an addition. Defaults to 1.
        :type backoff_seconds: int, required
        :return: Itself
        :rtype: func
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

                return func(*args, **kwargs)

            return f_retry

        return decorator
