import time

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
