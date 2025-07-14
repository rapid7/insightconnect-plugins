import insightconnect_plugin_runtime
from .schema import ExtractAllInput, ExtractAllOutput, Input, Output, Component

# Custom imports below

from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import (
    extract,
    parse_time,
    clear_emails,
    extract_filepath,
    clear_urls,
    clear_domains,
    clear_filenames,
    define_date_time_regex,
    extract_all_date_formats,
    parse_time_all_date_formats,
)


class ExtractAll(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="extract_all",
            description=Component.DESCRIPTION,
            input=ExtractAllInput(),
            output=ExtractAllOutput(),
        )

    def run(self, params={}):
        string = params.get(Input.STR)
        file = params.get(Input.FILE)
        date_format = params.get(Input.DATE_FORMAT)
        indicators = {
            "cves": extract(Regex.CVE, string, file),
            "dates": (
                parse_time(extract(define_date_time_regex(date_format), string, file), date_format)
                if date_format != "All Formats"
                else parse_time_all_date_formats(
                    extract_all_date_formats(
                        string,
                        file,
                    )
                )
            ),
            "email_addresses": clear_emails(extract(Regex.Email, string, file)),
            "filepaths": extract_filepath(Regex.FilePath, string, file),
            "mac_addresses": extract(Regex.MACAddress, string, file),
            "hashes": {
                "md5_hashes": extract(Regex.MD5, string, file),
                "sha1_hashes": extract(Regex.SHA1, string, file),
                "sha256_hashes": extract(Regex.SHA256, string, file),
                "sha512_hashes": extract(Regex.SHA512, string, file),
            },
            "ip_addresses": {
                "ipv4_addresses": extract(Regex.IPv4, string, file),
                "ipv6_addresses": extract(Regex.IPv6, string, file),
            },
            "urls": clear_urls(extract(Regex.URL, string, file)),
            "uuids": extract(Regex.UUID, string, file),
            "domains": clear_domains(extract(Regex.Domain, string, file)),
            "filenames": clear_filenames(extract(Regex.Filename, string, file)),
        }

        return {Output.INDICATORS: indicators}
