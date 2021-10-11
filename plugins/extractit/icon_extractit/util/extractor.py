import regex
import base64
import tldextract
import validators
from datetime import datetime
from icon_extractit.util.util import Regex
import urllib.parse


def extract(provided_regex: str, provided_string: str, provided_file: str) -> list:
    matches = []
    if provided_string:
        provided_string = urllib.parse.unquote(provided_string)
        matches = regex.findall(provided_regex, provided_string)
    elif provided_file:
        provided_file = urllib.parse.unquote(base64.b64decode(provided_file.encode("utf-8")).decode("utf-8"))
        matches = regex.findall(provided_regex, provided_file)
    return list(dict.fromkeys(matches))


def extract_filepath(provided_regex: str, provided_string: str, provided_file: str) -> list:
    matches = []
    if provided_string:
        new_string = regex.sub(Regex.URL, "", provided_string)
        new_string = regex.sub(Regex.Date, "", new_string)
        matches = regex.findall(provided_regex, new_string)
    elif provided_file:
        new_file = base64.b64decode(provided_file.encode("utf-8")).decode("utf-8")
        new_file = regex.sub(Regex.URL, "", new_file)
        new_file = regex.sub(Regex.Date, "", new_file)
        matches = regex.findall(provided_regex, new_file)
    return list(dict.fromkeys(matches))


def strip_subdomains(matches: list) -> list:
    for match in enumerate(matches):
        stripped_domain = tldextract.extract(match[1])
        # In some cases, tldextract recognizes a suffix as a domain, adds the domain to subdomain, and returns an empty 
        # string as suffix, so we check that tldextract extracted the suffix.
        if not stripped_domain.suffix:
            suffix = stripped_domain.domain
            subdomain = stripped_domain.subdomain
            if subdomain and suffix:
                # here we split `subdomain` and extract the domain, which is the last element from the `subdomains` list
                subdomains = subdomain.split(".")
                matches[match[0]] = f"{subdomains[len(subdomains) - 1]}.{suffix}"
        else:
            matches[match[0]] = ".".join(stripped_domain[1:3])
    return list(dict.fromkeys(matches))


def clear_domains(matches: list) -> list:
    new_matches = []
    for match in enumerate(matches):
        if not match[1].endswith("@"):
            split_match = match[1].split("/")[0]
            if not split_match.endswith("="):
                new_matches.append(split_match)
    return list(dict.fromkeys(new_matches))


def clear_urls(matches: list) -> list:
    new_matches = []
    for match in enumerate(matches):
        if not validators.ip_address.ipv4(match[1]) and not validators.email(match[1]):
            new_matches.append(match[1])
    return new_matches


def clear_emails(matches: list) -> list:
    new_matches = []
    for match in enumerate(matches):
        if validators.email(match[1]):
            new_matches.append(match[1])
    return new_matches


def parse_time(dates: list) -> list:
    for date in enumerate(dates):
        date_time_obj = datetime.strptime(date[1], "%d/%m/%Y")
        dates[date[0]] = date_time_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
    return dates
