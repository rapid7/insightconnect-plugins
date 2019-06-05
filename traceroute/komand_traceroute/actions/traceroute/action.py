import komand
from .schema import TracerouteInput, TracerouteOutput
# Custom imports below
import subprocess
import re


class Traceroute(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='traceroute',
                description='Traceroute to a host returns the route used to comunicate with the host',
                input=TracerouteInput(),
                output=TracerouteOutput())

    def run(self, params={}):
        host = params.get('host')
        count = params.get('count')
        max_ttl = params.get('max_ttl')
        time_out = params.get('time_out')
        set_ack = params.get('set_ack')
        resolve_hostname = params.get('resolve_hostname')
        port = params.get('port')

        if count == 0:
            count = 3
        if max_ttl == 0:
            max_ttl = 30
        if time_out == 0:
            time_out = 3
        if port < 1 or port > 65535:
            port = 80

        count = str(count)
        max_ttl = str(max_ttl)
        time_out = str(time_out)
        port = str(port)

        if set_ack and resolve_hostname:
            # both set_ack and resolve_hostname are true
            request = '-m {max_ttl} -q {count} '.format(max_ttl=max_ttl, count=count) +\
                      '-w {time_out} -A {host} {port}'.format(time_out=time_out, host=host, port=port)
        elif set_ack:
            # set_ack is true but resolve_hostname is false
            request = '-n -m {max_ttl} -q {count} '.format(max_ttl=max_ttl, count=count) + \
                      '-w {time_out} -A {host} {port}'.format(time_out=time_out, host=host, port=port)
        elif resolve_hostname:
            # resolve_hostname is true but set_ack is false
            request = '-m {max_ttl} -q {count} '.format(max_ttl=max_ttl, count=count) + \
                      '-w {time_out} {host} {port}'.format(time_out=time_out, host=host, port=port)
        else:
            # both set_ack and resolve_hostname are false
            request = '-n -m {max_ttl} -q {count} '.format(max_ttl=max_ttl, count=count) + \
                      '-w {time_out} {host} {port}'.format(time_out=time_out, host=host, port=port)

        response = subprocess.Popen(['tcptraceroute ' + request], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, shell=True)
        (output, err) = response.communicate()

        output = output.decode('utf-8')
        err = err.decode('utf-8')

        self.logger.info('Standard Error: %s', err)

        if response.returncode == 0:
            ip = []
            path = []
            temp_path = output.splitlines()
            # remove white space from the start of each path line
            for x in temp_path:
                temp = x.lstrip(' ')
                path.append(temp)
            # parse out IP addresses
            try:
                for x in path:
                    temp = re.search(r'\d*\.\d*\.\d*\.\d*', x)
                    ip.append(temp.group())

                temp = re.search(r'open', output)
                # if the work open found it means the final IP address responded.
                if temp:
                    return {'reply': True, 'response': output, 'path': path, 'ip': ip}
                return {'reply': False, 'response': output, 'path': path, 'ip': ip}
            except AttributeError:
                self.logger.error('The regular expression search for IP addresses failed')
                self.logger.error('Standard Output: %s', output)
                raise
            except:
                self.logger.error('Return Code: %s' % response.returncode)
                self.logger.error('Standard Output: %s' % output)
                self.logger.error('Standard Error: %s' % err)
                raise Exception('Something went wrong, see self.logger')
        else:
            self.logger.error('Return Code: %s' % response.returncode)
            self.logger.error('Standard Output: %s' % output)
            self.logger.error('Standard Error: %s' % err)
            raise Exception('Something went wrong, see self.logger')

    def test(self):
        request = 'tcptraceroute 127.0.0.1'
        response = subprocess.Popen([request], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, shell=True)
        (output, err) = response.communicate()
        self.logger.info('Standard Error: %s', err)

        output = output.decode('utf-8')

        if response.returncode == 0:
            ip = []
            path = []
            temp_path = output.splitlines()
            for x in temp_path:
                temp = x.lstrip(' ')
                path.append(temp)
            try:
                for x in path:
                    temp = re.search(r'\d*\.\d*\.\d*\.\d*', x)
                    ip.append(temp.group())

                temp = re.search(r'open', output)
                if temp:
                    return {'reply': True, 'response': output, 'path': path, 'ip': ip}
                return {'reply': False, 'response': output, 'path': path, 'ip': ip}
            except AttributeError:
                self.logger.error('The regular expression search for IP addresses failed')
                self.logger.error('Standard Output: %s', output)
                raise
            except:
                self.logger.error('Return Code: %s' % response.returncode)
                self.logger.error('Standard Output: %s' % output)
                self.logger.error('Standard Error: %s' % err)
                raise Exception('Something went wrong, see self.logger')
        else:
            self.logger.error('Return Code: %s' % response.returncode)
            self.logger.error('Standard Output: %s' % output)
            self.logger.error('Standard Error: %s' % err)
            raise Exception('Something went wrong, see self.logger')
