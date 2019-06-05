import komand
from .schema import ReadInput, ReadOutput
# Custom imports below
import base64


class Read(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='read',
                description='Read contents from a PCAP file',
                input=ReadInput(),
                output=ReadOutput())

    def run(self, params={}):
        pcap = base64.b64decode(params.get('pcap'))
        try:
            f = open('input.pcap', 'wb')
            f.write(pcap)
        finally:
            f.close()
        cmd = "tcpdump -r input.pcap %s %s" % (params.get('options', ''), params.get('filter', ''))
        r = komand.helper.exec_command(cmd)
        stderr = r['stderr'].decode()
        if r['rcode'] != 0:
            self.logger.error('%s', stderr)
            raise Exception('Tcpdump Failed')
        dump_file = base64.b64encode(r['stdout'])
        stdout_list = komand.helper.clean_list(r['stdout'].decode().split('\n'))
        return {'dump_contents': stdout_list, 'dump_file': dump_file.decode(), 'stderr': stderr}
