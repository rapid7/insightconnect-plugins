from dateutil.parser import parse, ParserError
from komand_rapid7_insightidr.util.relative_time_codes import relative_time_to_milliseconds
from komand.exceptions import PluginException
import time
import logging


def parse_dates(time_from_string: str, time_to_string: str, relative_time_from: str) -> (int, int):
    """
    Parse incoming dates and return them as millisecond epoch time

    @param time_from_string: str
    @param time_to_string: str (optional, if it's a falsey value, time to will be set to Now)
    @return: (int, int)
    """

    rel_time_milli = relative_time_to_milliseconds.get(relative_time_from, 0)
    if rel_time_milli > 0:
        time_to_string = ""

    # Parse times to epoch milliseconds
    try:
        time_from = int(parse(time_from_string).timestamp()) * 1000
        if time_to_string:
            time_to = (int(parse(time_to_string).timestamp()) * 1000)
        else:
            # Now in millisecond epoch time
            time_to = (int(time.time()) * 1000) - rel_time_milli
    except ParserError as e:
        raise PluginException(cause="Could not parse given date.",
                              assistance="The date given was in an unrecognizable format.",
                              data=e)
    return time_from, time_to
