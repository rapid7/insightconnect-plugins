import insightconnect_plugin_runtime
import ldap3

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.util.utils import ADUtils
from .schema import QueryInput, QueryOutput, Input, Output


class Query(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query",
            description="Run a LDAP query",
            input=QueryInput(),
            output=QueryOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        query = (
            params.get(Input.SEARCH_FILTER, "")
            .replace("\\>=", ">=")
            .replace("\\<=", "<=")
        )
        search_base = params.get(Input.SEARCH_BASE)
        attributes = params.get(Input.ATTRIBUTES, [])
        # END INPUT BINDING - DO NOT REMOVE

        # replace ( and ) when they are part of a name rather than a search parameter
        escaped_query = ADUtils.escape_brackets_for_query(query)
        self.logger.info(f"Escaped query: {escaped_query}")

        if not attributes:
            attributes = [ldap3.ALL_ATTRIBUTES, ldap3.ALL_OPERATIONAL_ATTRIBUTES]

        try:
            entries = self.connection.client.query(
                search_base, escaped_query, attributes
            )
        except PluginException:
            self.logger.info("Escaping non-ascii characters...")
            entries = self.connection.client.query(
                search_base,
                ADUtils.escape_non_ascii_characters(escaped_query),
                attributes,
            )

        if entries:
            return {Output.RESULTS: entries, Output.COUNT: len(entries)}
        return {Output.RESULTS: [], Output.COUNT: 0}
