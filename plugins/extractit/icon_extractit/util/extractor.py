import logging

from insightconnect_plugin_runtime.exceptions import PluginException
import regex
import base64
import tldextract
import validators
from datetime import datetime
from icon_extractit.util.util import Regex, DateFormatStrings
import urllib.parse
import io
import zipfile
import pdfplumber
from pdfminer.pdfparser import PDFSyntaxError

DEFAULT_ENCODING = "utf-8"


def extract(provided_regex: str, provided_string: str, provided_file: str, keep_original_url: bool = False) -> list:
    matches = []
    if provided_string:
        if keep_original_url:
            matches = regex.findall(provided_regex, provided_string)  # regex finds both encoded and unencoded urls
        else:
            provided_string = urllib.parse.unquote(provided_string)
            matches = regex.findall(provided_regex, provided_string)
    elif provided_file:
        try:
            if keep_original_url:
                provided_file = base64.b64decode(provided_file.encode(DEFAULT_ENCODING)).decode(DEFAULT_ENCODING)
                matches = regex.findall(provided_regex, provided_file)
            else:
                provided_file = urllib.parse.unquote(
                    base64.b64decode(provided_file.encode(DEFAULT_ENCODING)).decode(DEFAULT_ENCODING)
                )
                matches = regex.findall(provided_regex, provided_file)
        except UnicodeDecodeError:
            file_content = extract_content_from_file(base64.b64decode(provided_file))
            matches = regex.findall(provided_regex, file_content)
    return list(dict.fromkeys(matches))


def extract_all_date_formats(provided_string: str, provided_file: str) -> list:
    matches = []
    if provided_string:
        provided_string = urllib.parse.unquote(provided_string)
        for regex_pattern in Regex.HumanToRegexPatterns.values():
            matches += regex.findall(regex_pattern, provided_string)
            provided_string = regex.sub(regex_pattern, "", provided_string)
    elif provided_file:
        try:
            provided_file = urllib.parse.unquote(
                base64.b64decode(provided_file.encode(DEFAULT_ENCODING)).decode(DEFAULT_ENCODING)
            )
            for regex_pattern in Regex.HumanToRegexPatterns.items():
                matches += regex.findall(regex_pattern, provided_file)
                provided_file = regex.sub(regex_pattern, "", provided_file)
        except UnicodeDecodeError:
            file_content = extract_content_from_file(base64.b64decode(provided_file))
            for regex_pattern in Regex.HumanToRegexPatterns.items():
                matches += regex.findall(regex_pattern, file_content)
                file_content = regex.sub(regex_pattern, "", file_content)
    return list(dict.fromkeys(matches))


def extract_filepath(provided_regex: str, provided_string: str, provided_file: str) -> list:
    matches = []
    if provided_string:
        new_string = regex.sub(Regex.URL, "", provided_string)
        new_string = regex.sub(Regex.Date, "", new_string)
        matches = regex.findall(provided_regex, new_string)
    elif provided_file:
        try:
            new_file = base64.b64decode(provided_file.encode(DEFAULT_ENCODING)).decode(DEFAULT_ENCODING)
        except UnicodeDecodeError:
            new_file = extract_content_from_file(base64.b64decode(provided_file))
        new_file = regex.sub(Regex.URL, "", new_file)
        new_file = regex.sub(Regex.Date, "", new_file)
        matches = regex.findall(provided_regex, new_file)
    return list(dict.fromkeys(matches))


def extract_content_from_file(provided_file: bytes) -> str:
    with io.BytesIO(provided_file) as f:
        try:
            # extracting content from DOCX, PPTX, XLSX, ODT, ODP, ODF files
            with zipfile.ZipFile(f) as unzip_files:
                files_content = ""
                x = unzip_files.infolist()
                for i in enumerate(x):
                    try:
                        files_content += unzip_files.read(x[i[0]]).decode(DEFAULT_ENCODING)
                    # After unpacking, may contain images for which the decoding will fail
                    except UnicodeDecodeError:
                        continue
            # remove xml tags from files content
            return regex.sub(r"<[\p{L}\p{N}\p{Lo}\p{So} :\/.\"=_%,(){}+#&;?-]*>", " ", files_content)
        except zipfile.BadZipFile:
            try:
                logging.getLogger("pdfminer").setLevel(logging.WARNING)
                # extracting content from PDF file
                pdf_file = pdfplumber.open(f)
                pages = pdf_file.pages
                pdf_content = ""
                for page in enumerate(pages):
                    pdf_content += page[1].extract_text()
                pdf_file.close()
                return pdf_content
            except PDFSyntaxError:
                raise PluginException(
                    cause="The type of the provided file is not supported.",
                    assistance="Supported file types: PDF, DOCX, PPTX, XLSX, ODT, ODP, ODF",
                )


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
    # The method is designed to reduce the number of false positives results. The domain regex has been extended to
    # include the path from the URL and the @ and = characters if they are at the end of the found domain.
    new_matches = []
    for match in enumerate(matches):
        # Here we remove the path, this solution allows to prevent the situation where the file names from the URL will
        # be extracted as domains, e.g. www.example.com/test.html
        split_match = match[1].split("/")[0]
        # Here we eliminate all domains that end with = or @. This avoids extracting two domains from an email address,
        # e.g. user.test@example.com, or extracting field names from an EML file as domains, e.g. two domains would be
        # extracted from "header.from=example.com"
        if not split_match.endswith("@") and not split_match.endswith("="):
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


def define_linux_date_time_format(date_format: str) -> str:
    return DateFormatStrings.human_to_linux_mapping.get(date_format)


def define_date_time_regex(date_format: str) -> str:
    return Regex.HumanToRegexPatterns.get(date_format)


def parse_time_all_date_formats(dates: list) -> list:
    for date in enumerate(dates):
        for linux_date_time_format in DateFormatStrings.human_to_linux_mapping.values():
            date_value_separators = regex.findall(
                r"[^(%b)(%d)(%m)(%y)(%h)(%s)(%D)(%M)(%Y)(%H)(%S)]", linux_date_time_format
            )
            # Alternatively insert date and separators into list that is then joined together as a string. Allows
            # for retrieved dates to be read in an extractable format and account for all future date format variations.
            date_string_list = list(range((len(date[1]) + len(date_value_separators))))
            date_string_list[::2] = date[1]
            date_string_list[1::2] = date_value_separators
            date_string = "".join(date_string_list)
            try:
                date_time_obj = datetime.strptime(date_string, linux_date_time_format)
                dates[date[0]] = date_time_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
                break
            except ValueError:
                continue
    return dates


def parse_time(dates: list, date_format: str) -> list:
    linux_date_time_format = define_linux_date_time_format(date_format)
    # Regex pattern used for identification of separators to handle date time formats in ISO format and all possible
    # cases of mixed separator format that can be converted to a datetime object
    date_value_separators = regex.findall(r"[^(%b)(%d)(%m)(%y)(%h)(%s)(%D)(%M)(%Y)(%H)(%S)]", linux_date_time_format)

    for date in enumerate(dates):
        # Alternatively insert date and separators into list that is then joined together as a string. Allows
        # for retrieved dates to be read in an extractable format and account for all future date format variations.
        date_string_list = list(range((len(date[1]) + len(date_value_separators))))
        date_string_list[::2] = date[1]
        date_string_list[1::2] = date_value_separators
        date_string = "".join(date_string_list)
        try:
            date_time_obj = datetime.strptime(date_string, linux_date_time_format)
            dates[date[0]] = date_time_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            raise PluginException(
                cause=f"The found date {date_string} could not be parsed as a real date",
                assistance="Please review selected date format input for date extraction",
            )
    return dates
