import komand
from .schema import BlockUrlPolicyInput, BlockUrlPolicyOutput, Input, Output, Component
from komand.exceptions import PluginException
# Custom imports below
import fmcapi


class BlockUrlPolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='block_url_policy',
                description=Component.DESCRIPTION,
                input=BlockUrlPolicyInput(),
                output=BlockUrlPolicyOutput())

    def make_policy(self, fmc: fmcapi.FMC, policy_name: str):
        acp = fmcapi.AccessPolicies(fmc=fmc)
        acp.name = policy_name
        p = acp.get()
        if 'paging' in p:
            if p['paging']['count'] == 0:
                p = acp.post()
        self.logger.info(p)
        return p

    def make_url_object(self, fmc: fmcapi.FMC, name: str, fqdn: str) -> str:
        url = fmcapi.URLs(fmc=fmc)
        url.name = name
        url.url = fqdn
        url.post()
        url.get()
        return url.id

    def make_rule(self, fmc: fmcapi.FMC, policy: str, rule_name: str, urls: dict) -> str:
        acr = fmcapi.AccessRules(fmc=fmc)
        acr.name = rule_name
        acr.urls = urls
        acr.acp_id = policy['id']
        acr.URL = policy['rules']['links']['self']
        acr.action = 'BLOCK'
        acr.enabled = True
        acr.post()
        return acr.id

    def run(self, params={}):
        policy_name = params.get(Input.ACCESS_POLICY)
        rule_name = params.get(Input.RULE_NAME)

        with fmcapi.FMC(
            host=self.connection.host,
            username=self.connection.username,
            password=self.connection.password,
            autodeploy=True,limit=10
        ) as fmc1:
            urls = {'objects': []}
            for url in params.get(Input.URL_OBJECTS):
                if len(url['url']) > 400: 
                    raise PluginException(cause='URL exceeds max length of 400.',
                                      assistance='Please shorten the URL or try another.')

                url_id = self.make_url_object(fmc=fmc1, name=url['name'], fqdn=url['url'])
                urls['objects'].append({
                    'type': 'URL',
                    'id': url_id,
                    'name': url['name']
                })
            policy = self.make_policy(fmc=fmc1, policy_name=policy_name)
            acr_id = self.make_rule(fmc=fmc1, policy=policy, rule_name=rule_name, urls=urls)
        
        return {Output.SUCCESS: True}
