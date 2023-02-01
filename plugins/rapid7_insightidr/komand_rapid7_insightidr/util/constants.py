# Constants for query/action.py

# The way data indexing works changed on the 24/11/2022.
# For any search with most_recent_first=true 'from' must not be older than 24/11/2022
twenty_fourth_november = 1669248000
# 7776000 - is for three months from now.
# It is here because InsightDR keep logs for three months in hot storage
three_months_seconds = 7776000
