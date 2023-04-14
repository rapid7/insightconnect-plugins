# Constants for query/action.py

# The way data indexing works changed on the 24/11/2022.
# For any search with most_recent_first=true 'from' must not be older than 24/11/2022
TWENTY_FOURTH_NOVEMBER = 1669248000
# 7776000 - is for three months from now.
# It is here because InsightDR keep logs for three months in hot storage
THREE_MONTHS_SECONDS = 7776000
