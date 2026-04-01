import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetReputationInput, GetReputationOutput, Input, Output, Component

# Custom imports below
from anyrun import RunTimeException
from anyrun.connectors import LookupConnector

from icon_any_run.util.config import Config
from icon_any_run.util.tools import get_report_name


class GetReputation(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_reputation",
            description=Component.DESCRIPTION,
            input=GetReputationInput(),
            output=GetReputationOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        entity_type = params.get(Input.ENTITY_TYPE)
        entity_value = params.get(Input.ENTITY_VALUE)
        lookup_depth = params.get(Input.LOOKUP_DEPTH)
        # END INPUT BINDING - DO NOT REMOVE
        try:
            if entity_type == "hash":
                hash_type = {32: "md5", 40: "sha1", 64: "sha256"}.get(len(entity_value))
                if not hash_type:
                    raise RunTimeException("Unsupported hash type. Allowed: sha1, sha256, md5")
                query_params = {hash_type: entity_value}
            else:
                query_params = {entity_type: entity_value}

            with LookupConnector(self.connection.lookup_api_key, integration=Config.VERSION) as connector:
                summary = connector.get_intelligence(**query_params, lookup_depth=lookup_depth, parse_response=True)

            return {
                Output.ASOWNER: summary.asn() if summary.asn() else "",
                Output.FILE_EXTENSION: summary.file_meta().file_extension if summary.file_meta() else "",
                Output.FILENAME: summary.file_meta().filename if summary.file_meta() else "",
                Output.FILEPATH: summary.file_meta().filepath if summary.file_meta() else "",
                Output.GEO: summary.country() if summary.country() else "",
                Output.INDUSTRIES: summary.industries() if summary.industries() else "",
                Output.LAST_ANALYSES: summary.tasks() if summary.tasks() else "",
                Output.LAST_MODIFIED: summary.last_modified() if summary.last_modified() else "",
                Output.LOOKUP_URL: summary.intelligence_url(entity_value),
                Output.MD5: summary.file_meta().hashes.md5 if summary.file_meta() else "",
                Output.PORT: summary.port() if summary.port() else "",
                Output.SHA1: summary.file_meta().hashes.sha1 if summary.file_meta() else "",
                Output.SHA256: summary.file_meta().hashes.sha256 if summary.file_meta() else "",
                Output.SSDEEP: summary.file_meta().hashes.ssdeep if summary.file_meta() else "",
                Output.TAGS: summary.tags() if summary.tags() else "",
                Output.VERDICT: summary.verdict(),
            }
        except RunTimeException as error:
            raise PluginException(
                cause="Failed to get reputation.",
                assistance=error.description,
                data=error.json,
            )
