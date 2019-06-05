import komand
from .schema import QueryInput, QueryOutput
# Custom imports below
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

        conn.search(search_base=params.get('search_base'),
                    search_filter=params.get('search_filter'),
                    attributes=[ldap3.ALL_ATTRIBUTES, ldap3.ALL_OPERATIONAL_ATTRIBUTES]
                    )

        result_list_json = conn.response_to_json()
        result_list_object = json.loads(result_list_json)
        entries = result_list_object["entries"]

        return {'results': entries}
