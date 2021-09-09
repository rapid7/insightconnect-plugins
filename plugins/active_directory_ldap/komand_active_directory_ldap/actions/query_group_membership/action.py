import komand
from .schema import QueryGroupMembershipInput, QueryGroupMembershipOutput, Input, Output, Component

# Custom imports below
from komand.exceptions import PluginException
import json
import ldap3


class QueryGroupMembership(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query_group_membership",
            description=Component.DESCRIPTION,
            input=QueryGroupMembershipInput(),
            output=QueryGroupMembershipOutput(),
        )

    def run(self, params={}):
        base = params.get(Input.SEARCH_BASE)
        include_groups = params.get(Input.INCLUDE_GROUPS)
        expand_nested_groups = params.get(Input.EXPAND_NESTED_GROUPS)
        try:
            group = self.search_data(base=base, filter_query=f"(sAMAccountName={params.get(Input.GROUP_NAME)})").get(
                "entries"
            )
            if group and isinstance(group, list):
                group_dn = group[0].get("dn")
            else:
                raise PluginException(
                    cause="The specified group was not found.",
                    assistance="Please check that the provided group name and search base are correct and try again.",
                )
            if include_groups and expand_nested_groups:
                query = f"(memberOf:1.2.840.113556.1.4.1941:={group_dn})"
            elif include_groups:
                query = f"(memberOf:={group_dn})"
            elif expand_nested_groups:
                query = f"(&(objectClass=user)(memberOf:1.2.840.113556.1.4.1941:={group_dn}))"
            else:
                query = f"(&(objectClass=user)(memberOf:={group_dn}))"
            entries = self.search_data(base=base, filter_query=query).get("entries")
            return {Output.RESULTS: entries, Output.COUNT: len(entries)}
        except (AttributeError, IndexError) as e:
            raise PluginException(
                cause="LDAP returned unexpected response.",
                assistance="Check that the provided inputs are correct and try again. If the issue persists please "
                "contact support.",
                data=e,
            )

    def search_data(self, base: str, filter_query: str) -> dict:
        self.connection.conn.extend.standard.paged_search(
            search_base=base,
            search_filter=filter_query,
            attributes=[ldap3.ALL_ATTRIBUTES, ldap3.ALL_OPERATIONAL_ATTRIBUTES],
            paged_size=100,
            generator=False,
        )
        return json.loads(self.connection.conn.response_to_json())
