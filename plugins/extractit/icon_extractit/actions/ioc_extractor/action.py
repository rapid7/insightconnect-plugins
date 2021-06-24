import insightconnect_plugin_runtime
from .schema import IocExtractorInput, IocExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex, Extractor


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
        matches.extend(Extractor.clear_domains(Extractor.extract(Regex.Domain, provided_string, provided_file)))
        matches.extend(Extractor.parse_time(Extractor.extract(Regex.Date, provided_string, provided_file)))
        matches.extend(Extractor.extract_filepath(Regex.FilePath, provided_string, provided_file))
        matches.extend(Extractor.extract(Regex.Email, provided_string, provided_file))
        matches.extend(Extractor.extract(Regex.MACAddress, provided_string, provided_file))
        matches.extend(Extractor.extract(Regex.IPv4, provided_string, provided_file))
        matches.extend(Extractor.extract(Regex.IPv6, provided_string, provided_file))
        matches.extend(Extractor.extract(Regex.MD5, provided_string, provided_file))
        matches.extend(Extractor.extract(Regex.SHA1, provided_string, provided_file))
        matches.extend(Extractor.extract(Regex.SHA256, provided_string, provided_file))
        matches.extend(Extractor.extract(Regex.SHA512, provided_string, provided_file))
        matches.extend(Extractor.clear_urls(Extractor.extract(Regex.URL, provided_string, provided_file)))
        return {Output.IOCS: matches}
