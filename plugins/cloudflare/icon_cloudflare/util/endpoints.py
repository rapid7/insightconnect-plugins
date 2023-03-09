BASE_URL = "https://api.cloudflare.com/client/v4"

ACCOUNTS_ENDPOINT = BASE_URL + "/accounts"
LISTS_ENDPOINT = BASE_URL + "/accounts/{account_id}/rules/lists"
ZONE_ACCESS_RULE_ENDPOINT = BASE_URL + "/zones/{zone_id}/firewall/access_rules/rules/{rule_id}"
ZONE_ACCESS_RULES_ENDPOINT = BASE_URL + "/zones/{zone_id}/firewall/access_rules/rules"
ZONES_ENDPOINT = BASE_URL + "/zones"
