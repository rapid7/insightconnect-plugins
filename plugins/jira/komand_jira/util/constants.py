REQUESTS_TIMEOUT = 20
DEFAULT_JIRA_API_VERSION = "3"

# OAuth2 endpoints for Atlassian Cloud
OAUTH2_TOKEN_URL = "https://auth.atlassian.com/oauth/token"  # noqa: B105
OAUTH2_ACCESSIBLE_RESOURCES_URL = "https://api.atlassian.com/oauth/token/accessible-resources"

# Jira cloud instance domain patterns for URL matching
JIRA_CLOUD_SUFFIX = ".jira.com"
ATLASSIAN_CLOUD_SUFFIX = ".atlassian.net"
ATLASSIAN_API_DOMAIN = "api.atlassian.com"
CLOUD_DOMAIN_PATTERNS = [JIRA_CLOUD_SUFFIX, ATLASSIAN_CLOUD_SUFFIX, ATLASSIAN_API_DOMAIN]
