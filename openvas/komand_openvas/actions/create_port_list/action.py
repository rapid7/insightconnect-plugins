import komand
from .schema import CreatePortListInput, CreatePortListOutput
# Custom imports below
import sys


class CreatePortList(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_port_list',
                description='Create a new list of ports to scan in the OpenVAS server',
                input=CreatePortListInput(),
                output=CreatePortListOutput())

    def run(self, params={}):
        name = str(params.get('name'))
        port_list_tcp = list(params.get('port_list_TCP'))
        port_list_udp = list(params.get('port_list_UDP'))
        transform_tcp = ','.join(port_list_tcp)
        transform_udp = ','.join(port_list_udp)
        if not port_list_udp and not port_list_tcp:
            self.logger.error('No list of port ranges provided. Aborting.')
            return {'port_list_id': '', 'success': False, 'message': 'No list of port ranges provided. Aborting.'}
        elif transform_udp and transform_tcp:
            m_port_list = 'T: ' + transform_tcp + ', U: ' + transform_udp
        elif transform_udp and not transform_tcp:
            m_port_list = 'U: ' + transform_udp
        else:
            m_port_list = 'T: ' + transform_tcp

        m_port_list = str(m_port_list)
        try:
            port_list_id = self.connection.scanner.create_port_list(name, m_port_list, '')
        except:
            return {'port_list_id': '', 'success': False, 'message': 'Error creating port list: ' + ' | '.join(
                [str(sys.exc_info()[0]), str(sys.exc_info()[1])])}

        return {'port_list_id': port_list_id, 'success': True, 'message': 'Successfully created port list.'}

    def test(self):
        # TODO: Implement test function
        return {}
