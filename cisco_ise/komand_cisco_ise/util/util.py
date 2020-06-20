import requests
import re
import json
from komand.exceptions import ConnectionTestException, PluginException

import aiohttp
import asyncio
from typing import Optional


# Class from https://github.com/bobthebutcher/ise/blob/master/cream.py
class ERS(object):
    def __init__(self, ise_node, ers_user, ers_pass, verify, timeout=2):
        """
        Class to interact with Cisco ISE via the ERS API
        :param ise_node: IP Address of the primary admin ISE node
        :param ers_user: ERS username
        :param ers_pass: ERS password
        :param timeout: Query timeout
        """
        self.ise_node = ise_node
        self.user_name = ers_user
        self.user_pass = ers_pass

        self.url_base = 'https://{0}:9060/ers'.format(self.ise_node)
        self.ise = requests.session()
        self.ise.auth = (self.user_name, self.user_pass)
        self.ise.verify = verify
        self.timeout = timeout
        self.ise.headers.update({'Connection': 'keep_alive'})

        requests.packages.urllib3.disable_warnings()

    @staticmethod
    def _mac_test(mac):

        if re.search(r'([0-9A-F]{2}[:]){5}([0-9A-F]){2}', mac.upper()) is not None:
            return True
        else:
            return False

    def get_endpoint_by_name(self, name):

        self.ise.headers.update({'ACCEPT': 'application/json', 'Content-Type': 'application/json'})

        resp = self.ise.get('{0}/config/endpoint/name/{1}'.format(self.url_base, name), verify=False)
        if resp.status_code == 401:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
        if resp.reason == 'Not Found':
            return 'Not Found'
        found_endpoint = resp.json()
        return found_endpoint

    def get_endpoint_by_id(self, endpoint_id):

        self.ise.headers.update({'ACCEPT': 'application/json', 'Content-Type': 'application/json'})

        resp = self.ise.get('{0}/config/endpoint/{1}'.format(self.url_base, endpoint_id), verify=False)
        if resp.status_code == 401:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
        if resp.reason == 'Not Found':
            return 'Not Found'
        found_endpoint = resp.json()
        return found_endpoint

    def get_endpoint(self):
        self.ise.headers.update({'Accept': 'application/json', 'Content-Type': 'application/json'})

        resp = self.ise.get('{0}/config/endpoint'.format(self.url_base), verify=False)
        found_endpoint = resp.json()
        return found_endpoint

    def get_anc_endpoint_all(self) -> str:

        self.ise.headers.update({'ACCEPT': 'application/json', 'Content-Type': 'application/json'})

        resp = self.ise.get('{0}/config/ancendpoint'.format(self.url_base), verify=False)
        if resp.status_code == 401:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
        if resp.reason == 'Not Found':
            return 'Not Found'

        found_endpoint = resp.json()
        return found_endpoint

    async def _get_anc_endpoint(self, session: aiohttp.ClientSession, endpoint_id: str = "") -> Optional[dict]:
        url = f"{self.url_base}/config/ancendpoint/{endpoint_id}"

        response = await session.get(url=url)
        if response.status == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
        if response.reason == "Not Found":
            return None

        found_endpoint = await response.json()

        return found_endpoint

    async def get_anc_endpoints(self, endpoint_ids: [str]) -> [Optional[dict]]:

        with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False),
                                   headers={"ACCEPT": "application/json", "Content-Type": "application/json"}) as sess:
            tasks: [asyncio.Task] = []
            for endpoint_id in endpoint_ids:
                tasks.append(asyncio.ensure_future(self._get_anc_endpoint(session=sess,
                                                                          endpoint_id=endpoint_id)))
            endpoints = asyncio.gather(*tasks)

        return endpoints

    def get_anc_endpoint(self, endpoint_id='') -> str:

        self.ise.headers.update({'ACCEPT': 'application/json', 'Content-Type': 'application/json'})

        resp = self.ise.get('{0}/config/ancendpoint/{1}'.format(self.url_base, endpoint_id), verify=False)
        if resp.status_code == 401:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
        if resp.reason == 'Not Found':
            return 'Not Found'

        found_endpoint = resp.json()
        return found_endpoint

    def apply_anc_endpoint_mac(self, mac_address: str, policy: str):

        is_valid = ERS._mac_test(mac_address)

        if not is_valid:
            raise Exception(
                'Mac Address is not valid {0}. Must be in the form of AA:BB:CC:00:11:22'.format(mac_address))
        else:
            self.ise.headers.update({'Accept': 'application/json', 'Content-Type': 'application/json'})

            payload = {'OperationAdditionalData':
                       {'additionalData': [{'name': 'macAddress', 'value': mac_address},
                        {'name': 'policyName', 'value': policy}]}}
            payload = json.dumps(payload)

            resp = self.ise.put('{0}/config/ancendpoint/apply'.format(self.url_base),
                                data=payload, verify=False)
            if resp.status_code == 401:
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.USERNAME_PASSWORD)

    def clean_anc_end_point(self, mac_address: str):

        is_valid = ERS._mac_test(mac_address)

        if not is_valid:
            raise Exception(
                'Mac Address is not valid {0}. Must be in the form of AA:BB:CC:00:11:22'.format(
                    mac_address))
        else:

            headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            payload = {'OperationAdditionalData':
                       {'additionalData': [{'name': 'macAddress', 'value': mac_address}]}}
            payload = json.dumps(payload)

            resp = self.ise.put('{0}/config/ancendpoint/clear'.format(self.url_base),
                                data=payload, headers=headers, verify=False)
            if resp.status_code == 401:
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
