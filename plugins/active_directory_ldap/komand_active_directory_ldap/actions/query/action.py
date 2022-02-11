import ldap3

import insightconnect_plugin_runtime

# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils
from .schema import QueryInput, QueryOutput, Input, Output


class Query(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query", description="Run a LDAP query", input=QueryInput(), output=QueryOutput()
        )

    def run(self, params={}):
        formatter = ADUtils()
        query = params.get(Input.SEARCH_FILTER)

        query = query.replace("\\>=", ">=")
        query = query.replace("\\<=", "<=")

        # replace ( and ) when they are part of a name rather than a search parameter
        escaped_query = formatter.escape_brackets_for_query(query)
        self.logger.info("Escaped query: %s", escaped_query)

        attributes = params.get(Input.ATTRIBUTES, [])
        if not attributes:
            attributes = [ldap3.ALL_ATTRIBUTES, ldap3.ALL_OPERATIONAL_ATTRIBUTES]

        entries = self.connection.client.query(params.get(Input.SEARCH_BASE), escaped_query, attributes)
        if entries:
            return {Output.RESULTS: entries, Output.COUNT: len(entries)}
        else:
            return {Output.RESULTS: [], Output.COUNT: 0}
