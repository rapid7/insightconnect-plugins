import komand
from .schema import QueryInput, QueryOutput, Input, Output

# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils
import json
import ldap3


class Query(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query", description="Run a LDAP query", input=QueryInput(), output=QueryOutput()
        )

    def run(self, params={}):
        formatter = ADUtils()
        conn = self.connection.conn
        query = params.get(Input.SEARCH_FILTER)

        query = query.replace("\\>=", ">=")
        query = query.replace("\\<=", "<=")

        # find pars of `(` `)`
        pairs = formatter.find_parentheses_pairs(query)

        # replace ( and ) when they are part of a name rather than a search parameter
        escaped_query = formatter.escape_brackets_for_query(query, pairs)
        self.logger.info(f"Escaped query: {escaped_query}")

        attributes = params.get(Input.ATTRIBUTES)
        if not attributes:
            attributes = [ldap3.ALL_ATTRIBUTES, ldap3.ALL_OPERATIONAL_ATTRIBUTES]

        conn.extend.standard.paged_search(
            search_base=params.get(Input.SEARCH_BASE),
            search_filter=escaped_query,
            attributes=attributes,
            paged_size=100,
            generator=False,
        )

        result_list_json = conn.response_to_json()
        result_list_object = json.loads(result_list_json)
        entries = result_list_object["entries"]

        return {Output.RESULTS: entries, Output.COUNT: len(entries)}
