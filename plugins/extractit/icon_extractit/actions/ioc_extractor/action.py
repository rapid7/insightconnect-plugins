import insightconnect_plugin_runtime
from .schema import IocExtractorInput, IocExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex
from icon_extractit.util import extractor


class IocExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ioc_extractor",
            description=Component.DESCRIPTION,
            input=IocExtractorInput(),
            output=IocExtractorOutput(),
        )

    def run(self, params={}):
        matches = []
        provided_string = params.get(Input.STR)
        provided_file = params.get(Input.FILE)
        matches.extend(extractor.clear_domains(extractor.extract(Regex.Domain, provided_string, provided_file)))
        matches.extend(extractor.parse_time(extractor.extract(Regex.Date, provided_string, provided_file)))
        matches.extend(extractor.extract_filepath(Regex.FilePath, provided_string, provided_file))
        matches.extend(extractor.clear_emails(extractor.extract(Regex.Email, provided_string, provided_file)))
        matches.extend(extractor.extract(Regex.MACAddress, provided_string, provided_file))
        matches.extend(extractor.extract(Regex.IPv4, provided_string, provided_file))
        matches.extend(extractor.extract(Regex.IPv6, provided_string, provided_file))
        matches.extend(extractor.extract(Regex.MD5, provided_string, provided_file))
        matches.extend(extractor.extract(Regex.SHA1, provided_string, provided_file))
        matches.extend(extractor.extract(Regex.SHA256, provided_string, provided_file))
        matches.extend(extractor.extract(Regex.SHA512, provided_string, provided_file))
        matches.extend(extractor.clear_urls(extractor.extract(Regex.URL, provided_string, provided_file)))
        return {Output.IOCS: matches}
