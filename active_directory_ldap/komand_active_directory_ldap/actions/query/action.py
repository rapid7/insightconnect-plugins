import komand
from .schema import QueryInput, QueryOutput
# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils
import json
import ldap3


class Query(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='query',
                description='Run a LDAP query',
                input=QueryInput(),
                output=QueryOutput())

    def run(self, params={}):
        conn = self.connection.conn
        query = params.get('search_filter')

        query = ADUtils.dn_normalize(query)
        temp_list = ADUtils.dn_escape_and_split(query)
        query_list = [s for s in temp_list if 'DC' in s]
        query = ','.join(query_list)
        escaped_query = ','.join(temp_list)
        escaped_query = escaped_query.replace("\\>=", ">=")
        escaped_query = escaped_query.replace("\\<=", "<=")

        # find pars of `(` `)`
        pairs = ADUtils.find_parentheses_pairs(escaped_query)

        # replace ( and ) when they are part of a name rather than a search parameter
        for key, value in pairs.items():
            tempstring = escaped_query
            if tempstring.find('=', key, value) == -1:
                escaped_query = escaped_query[:value] + '\\29' + escaped_query[value + 1:]
                escaped_query = escaped_query[:key] + '\\28' + escaped_query[key + 1:]
        self.logger.info(f"Escaped query: {escaped_query}")

        conn.search(search_base=params.get('search_base'),
                    search_filter=escaped_query,
                    attributes=[ldap3.ALL_ATTRIBUTES, ldap3.ALL_OPERATIONAL_ATTRIBUTES]
                    )

        result_list_json = conn.response_to_json()
        result_list_object = json.loads(result_list_json)
        entries = result_list_object["entries"]

        for entry in entries:
            if entry.get("dn"):
                entry["dn"] = entry["dn"].replace("\\", "")

            if entry.get("attributes") and entry.get("attributes").get("distinguishedName"):
                entry.get("attributes")["distinguishedName"] = \
                    entry.get("attributes").get("distinguishedName").replace("\\", "")

        return {'results': entries}
