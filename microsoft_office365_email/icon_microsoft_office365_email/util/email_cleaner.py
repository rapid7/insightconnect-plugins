import re

_regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                     "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                     "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))


def get_emails_as_list(s: str) -> list:
    """Returns an iterator of matched emails found in string s."""
    # Removing lines that start with '//' because the regular expression
    # mistakenly matches patterns like 'http://foo@bar.com' as '//foo@bar.com'.
    return [email[0] for email in re.findall(_regex, s) if not email[0].startswith('//')]


def get_emails_as_string(s: str) -> str:
    """Returns an iterator of matched emails found in string s."""
    # Removing lines that start with '//' because the regular expression
    # mistakenly matches patterns like 'http://foo@bar.com' as '//foo@bar.com'.
    comma = ", "
    return comma.join(get_emails_as_list(s))
