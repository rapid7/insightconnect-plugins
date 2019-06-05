import komand
from .schema import RetrieveGlobalAclRulesInput, RetrieveGlobalAclRulesOutput


class RetrieveGlobalAclRules(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_global_acl_rules',
                description='Lists all global ACL rules with global ACL ID',
                input=RetrieveGlobalAclRulesInput(),
                output=RetrieveGlobalAclRulesOutput())

    def run(self, params={}):
        action = "security_policies"

        policy_id = params.get("policy_id")
        if not policy_id:
            self.connection.connector.raise_error("Policy ID can't be null")

        action = action + "/" + policy_id + "/global_acls"

        global_acl_id = params.get("global_acl_id")
        if global_acl_id:
            action = action + "/" + global_acl_id

        r = self.connection.connector.get(action)
        self.connection.connector.raise_error_when_not_in_status(200)

        r_data = []
        if 'data' not in r and global_acl_id:
            r_data = [r]
        elif 'data' not in r:
            self.connection.connector.raise_error("Empty returned value")
        else:
            r_data = r['data']

        data = []
        for k, val in enumerate(r_data):
            data.append({
                "action": r_data[k]["action"],
                "comments": r_data[k]["comments"],
                "extended_match": r_data[k]["extended_match"],
                "extended_match_sequence": r_data[k]["extended_match_sequence"],
                "id": r_data[k]["id"],
                "name": r_data[k]["name"],
                "redirect_url": r_data[k]["redirect_url"],
                "url_match": r_data[k]["url_match"]
            })

        return data

    def test(self):
        return [{
            "action": "",
            "comments": "",
            "extended_match": "",
            "extended_match_sequence": 0,
            "id": "",
            "name": "",
            "redirect_url": "",
            "url_match": ""
        }]
