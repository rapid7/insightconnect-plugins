import komand
from .schema import ConnectionSchema
# Custom imports below
import subprocess


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_host = None
        self.api_port = None
        self.f = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.api_host = params.get('api_host')
        self.api_port = params.get('api_port')
        self.f = open("sqlmap_logs.txt", "w")
        if not self.api_host and not self.api_port:
            subprocess.Popen(['python /python/src/sqlmap-master/sqlmapapi.py -s'],
                             stdout=self.f, stderr=self.f, shell=True)
            self.api_host = '127.0.0.1'
            self.api_port = '8775'
        if self.api_host and self.api_port:
            subprocess.Popen(['python /python/src/sqlmap-master/sqlmapapi.py -s --host=%s --port=%s' % (self.api_host,
                                                                                                        self.api_port)],
                             stdout=self.f, stderr=self.f, shell=True)
