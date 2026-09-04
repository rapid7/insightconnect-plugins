"""Shared test data for enable_users and disable_users actions."""

NOT_FOUND_ERROR = (
    "An error occurred during plugin execution! "
    "The DN CN=empty_search,DC=example,DC=com was not found. "
    "Please provide a valid DN and try again."
)

MANAGE_USERS_TEST_CASES = [
    (
        {"distinguished_names": ["CN=empty_search,DC=example,DC=com"]},
        {
            "completed": [],
            "failed": [{"dn": "CN=empty_search,DC=example,DC=com", "error": NOT_FOUND_ERROR}],
        },
    ),
    (
        {"distinguished_names": ["CN=empty_search,DC=example,DC=com", "CN=Users,DC=example,DC=com"]},
        {
            "completed": ["CN=Users,DC=example,DC=com"],
            "failed": [{"dn": "CN=empty_search,DC=example,DC=com", "error": NOT_FOUND_ERROR}],
        },
    ),
    (
        {"distinguished_names": ["CN=Users,DC=example,DC=com"]},
        {
            "completed": ["CN=Users,DC=example,DC=com"],
            "failed": [],
        },
    ),
]
