import regex
import base64
import tldextract
import validators
from datetime import datetime


class Regex:
    Domain = r"\b(?:(?=[\p{L}\p{N}-]{1,63}\.)[\p{L}\p{N}]+(?:-[\p{L}\p{N}]+)*\.)+[\p{Ll}]{2,63}\b(?:\/[\p{L}\p{N}@:%_\-+.~]*)?"
    Date = r"\d{1,2}/\d{1,2}/\d{4}"
    FilePath = r"/\S+"
    Email = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    IPv4 = r"((?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3})"
    IPv6 = r"(?:(?:(?:[0-9A-Fa-f]{1,4}:){7}(?:[0-9A-Fa-f]{1,4}|:))|(?:(?:[0-9A-Fa-f]{1,4}:){6}(?::[0-9A-Fa-f]{1,4}|(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(?:(?:[0-9A-Fa-f]{1,4}:){5}(?:(?:(?::[0-9A-Fa-f]{1,4}){1,2})|:(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(?:(?:[0-9A-Fa-f]{1,4}:){4}(?:(?:(?::[0-9A-Fa-f]{1,4}){1,3})|(?:(?::[0-9A-Fa-f]{1,4})?:(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(?:(?:[0-9A-Fa-f]{1,4}:){3}(?:(?:(?::[0-9A-Fa-f]{1,4}){1,4})|(?:(?::[0-9A-Fa-f]{1,4}){0,2}:(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(?:(?:[0-9A-Fa-f]{1,4}:){2}(?:(?:(?::[0-9A-Fa-f]{1,4}){1,5})|(?:(?::[0-9A-Fa-f]{1,4}){0,3}:(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(?:(?:[0-9A-Fa-f]{1,4}:){1}(?:(?:(?::[0-9A-Fa-f]{1,4}){1,6})|(?:(?::[0-9A-Fa-f]{1,4}){0,4}:(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(?::(?:(?:(?::[0-9A-Fa-f]{1,4}){1,7})|(?:(?::[0-9A-Fa-f]{1,4}){0,5}:(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))"
    MACAddress = r"\b((?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2})\b"
    MD5 = r"\b([A-Fa-f0-9]{32})\b"
    SHA1 = r"\b([A-Fa-f0-9]{40})\b"
    SHA256 = r"\b([A-Fa-f0-9]{64})\b"
    SHA512 = r"\b([A-Fa-f0-9]{128})\b"
    URL = r"(?<![a-zA-Z0-9/])(?:(?:(?:https?|ftp):)?\/\/)?(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z0-9\u00a1-\uffff][a-z0-9\u00a1-\uffff_-]{0,62})?[a-z0-9\u00a1-\uffff]\.)+(?:[a-z\u00a1-\uffff]{2,}\.?))(?::\d{2,5})?(?:[/?#-]\S*)?"


class Extractor:
    @staticmethod
    def extract(provided_regex: str, provided_string: str, provided_file: str) -> list:
        matches = []
        if provided_string:
            matches = regex.findall(provided_regex, provided_string)
        elif provided_file:
            matches = regex.findall(provided_regex, base64.b64decode(provided_file.encode("utf-8")).decode("utf-8"))
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

    @staticmethod
    def strip_subdomains(matches: list) -> list:
        for i in range(len(matches)):
            stripped_domain = tldextract.extract(matches[i])
            matches[i] = ".".join(stripped_domain[1:3])
        return list(dict.fromkeys(matches))

    @staticmethod
    def clear_domains(matches: list) -> list:
        for i in range(len(matches)):
            matches[i] = matches[i].split("/")[0]
        return matches

    @staticmethod
    def clear_urls(matches: list) -> list:
        new_matches = []
        for i in range(len(matches)):
            if not validators.ip_address.ipv4(matches[i]) and not validators.email(matches[i]):
                new_matches.append(matches[i])
        return new_matches

    @staticmethod
    def parse_time(dates: list) -> list:
        for i in range(len(dates)):
            date_time_obj = datetime.strptime(dates[i], "%d/%m/%Y")
            dates[i] = date_time_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
        return dates
