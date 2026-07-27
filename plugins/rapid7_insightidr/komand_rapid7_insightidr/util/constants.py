# Constants for query/action.py

# The way data indexing works changed on the 24/11/2022.
# For any search with most_recent_first=true 'from' must not be older than 24/11/2022
TWENTY_FOURTH_NOVEMBER = 1669248000
# 7776000 - is for three months from now.
# It is here because InsightDR keep logs for three months in hot storage
THREE_MONTHS_SECONDS = 7776000

# Constants for resource_helper.py
DEFAULT_ERROR_MESSAGE = "Unknown error occurred. Please contact support or try again later."

# Retry/backoff for transient 5xx responses from InsightIDR. A newly created record can
# take a short time to become searchable (~1-2s indexing lag), so a follow-up request can
# transiently return a 5xx. Retrying with backoff over a ~5s window (2s + 3s across the
# gaps) resolves the vast majority of these.
RETRY_MAX_ATTEMPTS = 3
RETRY_BACKOFF_SECONDS = [2, 3]
# Additive jitter (0 to N seconds) on top of each backoff so concurrent jobs that hit a
# 5xx at the same moment don't retry in lockstep. Kept additive (never subtractive) so a
# retry can't fire before the ~1-2s indexing window the backoff is sized to cover.
RETRY_JITTER_SECONDS = 1
# Transient/gateway 5xx worth retrying. Permanent 5xx (e.g. 501, 505) are excluded since
# retrying cannot help.
RETRYABLE_STATUS_CODES = {500, 502, 503, 504}
# Only retry requests that are safe to repeat. POST is excluded (a committed-then-5xx
# create must not be duplicated) EXCEPT for read-only search endpoints, which are the
# primary source of the transient 5xx (e.g. investigations/_search after a just-created
# record). All other methods the plugin issues (GET, DELETE) are idempotent.
RETRYABLE_POST_ENDPOINT_SUFFIXES = ("_search", "/search")

# Constants for Get New Alerts trigger.py
TOTAL_SIZE = 100
