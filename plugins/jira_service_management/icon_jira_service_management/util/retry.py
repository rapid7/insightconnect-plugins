import time
from functools import wraps

from typing import Callable

from insightconnect_plugin_runtime.exceptions import PluginException

RETRY_MESSAGE = "Rate limiting error occurred. Retrying in {delay:.1f} seconds ({attempts_counter}/{max_tries})"


def rate_limiting(max_tries: int = 5):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            attempts, delay = 0, 0
            while attempts < max_tries:
                if attempts > 0:
                    time.sleep(delay)
                try:
                    return func(self, *args, **kwargs)
                except PluginException as error:
                    attempts += 1
                    delay = 2 ** (attempts * 0.6)
                    if error.cause == PluginException.causes[PluginException.Preset.RATE_LIMIT]:
                        self.logger.info(
                            RETRY_MESSAGE.format(delay=delay, attempts_counter=attempts, max_tries=max_tries)
                        )
                        continue
                    raise
            return func(self, *args, **kwargs)

        return wrapper

    return decorator
