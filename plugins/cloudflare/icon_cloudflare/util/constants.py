class Cause:
    INVALID_TARGET = "Invalid target was provided: {target}."
    INVALID_TOKEN = "Invalid API token was provided."  # nosec B105
    NOT_FOUND = "Resource not found."


class Assistance:
    INVALID_TARGET = "Only IPv4, IPv6, IP range, AS number and two-letter ISO-3166-1 alpha-2 country code are supported. For IP ranges, you can only use prefix lengths /16 and /24 for IPv4 ranges, and prefix lengths /32, /48, and /64 for IPv6 ranges."
    INVALID_TOKEN = "Verify your API token configured in your connection is correct or the required permissions have been granted for the given token and try again."  # nosec B105
    NOT_FOUND = (
        "Verify your input is correct and not malformed and try again. If the issue persists, please contact support."
    )


configuration_target = {
    "IP address": "ip",
    "IP range": "ip_range",
    "ASN": "asn",
    "country": "country",
}

mode = {
    "block": "block",
    "challenge": "challenge",
    "whitelist": "whitelist",
    "JS challenge": "js_challenge",
    "managed challenge": "managed_challenge",
}

order_by = {
    "account ID": "account.id",
    "account name": "account.name",
    "configuration target": "configuration.target",
    "configuration value": "configuration.value",
    "name": "name",
    "mode": "mode",
    "status": "status",
}
