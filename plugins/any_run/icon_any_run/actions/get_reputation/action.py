import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetReputationInput, GetReputationOutput, Input, Output, Component

# Custom imports below
from anyrun import RunTimeException
from anyrun.connectors import LookupConnector
from insightconnect_plugin_runtime.helper import clean

from icon_any_run.util.config import Config
from icon_any_run.util.tools import get_report_name, check_hash_type


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
        entity_type = params.get(Input.ENTITY_TYPE, "url")
        entity_value = params.get(Input.ENTITY_VALUE, "")
        lookup_depth = params.get(Input.LOOKUP_DEPTH, 180)
        # END INPUT BINDING - DO NOT REMOVE
        final_report = dict()

        try:
            if entity_type == "hash":
                hash_type = check_hash_type(entity_value)
                query_params = {hash_type: entity_value}
            else:
                query_params = {entity_type: entity_value}

            with LookupConnector(self.connection.lookup_api_key, integration=Config.VERSION) as connector:
                summary = connector.get_intelligence(**query_params, lookup_depth=lookup_depth, parse_response=True)

            final_report[Output.VERDICT] = summary.verdict()
            final_report[Output.LOOKUP_URL] = summary.intelligence_url(entity_value)
            final_report[Output.LAST_MODIFIED] = summary.last_modified()
            final_report[Output.INDUSTRIES] = summary.industries()
            final_report[Output.TAGS] = summary.tags()
            final_report[Output.ASOWNER] = summary.asn()
            final_report[Output.GEO] = summary.country()

            if tasks := summary.tasks(tasks_range=20):
                final_report[Output.LAST_ANALYSES] = tasks

            if file_meta := summary.file_meta():
                final_report[Output.FILE_EXTENSION] = file_meta.filepath.split(".")[-1]
                final_report[Output.FILENAME] = file_meta.filename
                final_report[Output.FILEPATH] = file_meta.filepath
                final_report[Output.SHA1] = file_meta.hashes.sha1
                final_report[Output.SHA256] = file_meta.hashes.sha256
                final_report[Output.MD5] = file_meta.hashes.md5
                final_report[Output.SSDEEP] = file_meta.hashes.ssdeep

            return clean(final_report)
        except RunTimeException as error:
            raise PluginException(
                cause="Failed to get reputation.",
                assistance=error.description,
                data=error.json,
            )
