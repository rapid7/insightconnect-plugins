import komand
from .schema import RunInput, RunOutput
from komand.exceptions import PluginException
# Custom imports below
import json
import base64
import requests
from komand_try_bro.util import utils


class Run(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run',
                description='Upload PCAP file',
                input=RunInput(),
                output=RunOutput())

    def run(self, params={}):
        server  = self.connection.server
        pcap    = base64.b64decode(params.get('pcap'))
        scripts = params.get('scripts')
        version = params.get('version', 'master')
        if pcap:
          checksum = utils.maybe_upload_pcap(server, pcap, self.logger)
        else:
          raise PluginException(cause='Error: No PCAP supplied')
        sources = utils.load_scripts(scripts, self.logger)
        self.logger.info('Run: Supplied Scripts: %s', sources)
        req     = { 'sources': sources, 'version': version, 'pcap': checksum }
        data    = json.dumps(req)
        headers = {'Content-type': 'application/json'}
        res     = requests.post(server  + "/run", data=data, headers=headers).json()
        if res['stdout'] != "":
          self.logger.info(res['stdout'])
        return { 'id': res['job'], 'url': '{server}/#/trybro/saved/{job}'.format(server=server, job=res['job']) }

    def test(self):
        server = self.connection.server
        res = requests.get(server)
        if res.status_code != 200:
          raise PluginException(cause='Test: Unsuccessful HTTP status code returned')
        return {}
