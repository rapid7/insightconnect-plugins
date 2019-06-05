import komand
from .schema import PingInput, PingOutput
# Custom imports below
import subprocess
import re


class Ping(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ping',
                description='Ping a host to check for connectivity',
                input=PingInput(),
                output=PingOutput())

    def run(self, params={}):
        host = params.get('host')
        count = params.get('count')
        resolve_hostname = params.get('resolve_hostname')

        if count == 0:
            count = 4
        count = str(count)

        if resolve_hostname:
            response = subprocess.Popen(['ping -c ' + count + ' ' + host], stdout=subprocess.PIPE, shell=True)
            (output, err) = response.communicate()
        else:
            response = subprocess.Popen(['ping -n -c ' + count + ' ' + host], stdout=subprocess.PIPE, shell=True)
            (output, err) = response.communicate()

        output = output.decode("utf-8")

        if response.returncode == 0:
            try:
                temp = re.search(r'\d* packets t', output)
                sub = temp.group()
                transmitted = sub[:-10]
                transmitted = int(transmitted)
            except AttributeError:
                self.logger.error('The regular expression search for transmitted packets failed')
                self.logger.error('Standard Output: %s', output)
                raise Exception('A AttributeError occurred,see log for details')
            except ValueError:
                self.logger.error('The transmitted packets value is not valid. The value was %s' % transmitted)
                self.logger.error('Standard Output: %s' % output)
                raise Exception('A ValueError occurred,see log for details')
            except:
                self.logger.error('Standard Output: %s', output)
                self.logger.error('Return form regex %s' % temp)
                self.logger.error('Substring built by regex %s' % sub)
                raise Exception('Unknown error occurred, see log for details')

            try:
                temp = re.search(r'\d* packets r', output)
                sub = temp.group()
                received = sub[:-10]
                received = int(received)
            except AttributeError:
                self.logger.error('The regular expression search for received packets failed')
                self.logger.error('Standard Output: %s', output)
                raise Exception('A AttributeError occurred,see log for details')
            except ValueError:
                self.logger.error('The received packets value is not valid. The value was %s', received)
                self.logger.error('Standard Output: %s', output)
                raise Exception('A ValueError occurred,see log for details')
            except:
                self.logger.error('Standard Output: %s', output)
                self.logger.error('Return form regex %s', temp)
                self.logger.error('Substring built by regex %s', sub)
                raise Exception('Unknown error occurred, see log for details')

            try:
                temp = re.search(r'received.*', output)
                sub = temp.group()
                sub = sub[:-13]
                sub = sub[10:]
                packet_loss = float(sub)
            except AttributeError:
                self.logger.error('The regular expression search for % packet loss failed')
                self.logger.error('Standard Output: %s', output)
                raise Exception('A AttributeError occurred,see log for details')
            except ValueError:
                self.logger.error('The % packet loss value is not valid. The value was %s', packet_loss)
                self.logger.error('Standard Output: %s', output)
                raise Exception('A ValueError occurred,see log for details')
            except:
                self.logger.error('Standard Output: %s', output)
                self.logger.error('return form regex %s', temp)
                self.logger.error('substring built by regex %s', sub)
                raise Exception('Unknown error occurred, see log for details')

            try:
                temp = re.search(r'stddev.*', output)
                sub = temp.group()
                sub = sub[9:]
                sub = sub[:-3]
                values = sub.split('/')

                if sub == '':
                    self.logger.error('Standard Output: %s', output)
                    self.logger.error('Return form regex %s', temp)
                    raise Exception('The value for average latency was not found, see log for details')
                try:
                    average_latency = values[1] + 'ms'
                    minimum_latency = values[0] + 'ms'
                    maximum_latency = values[2] + 'ms'
                    standard_deviation = values[3] + 'ms'
                except IndexError:
                    self.logger.error('Failed to find min avg max and stdev %s' % sub)

            except AttributeError:
                self.logger.error('The regular expression search for average latency failed')
                self.logger.error('Standard Output: %s', output)
                raise Exception('A AttributeError occurred,see log for details')
            except:
                self.logger.error('Standard Output: %s', output)
                self.logger.error('Return form regex %s', temp)
                self.logger.error('Substring built by regex %s', sub)
                raise Exception('Unknown error occurred, see log for details')

            return {'reply': True, 'response': output,
                    'packets_percent_lost': packet_loss,
                    'average_latency': average_latency, 'packets_transmitted': transmitted,
                    'packets_received': received, 'minimum_latency': minimum_latency,
                    'maximum_latency': maximum_latency, 'standard_deviation': standard_deviation}
        elif response.returncode < 3:

            return {'reply': False, 'response': output}
        else:
            self.logger.error('Standard Output: %s', output)
            self.logger.error('Standard Error: %s', err)
            raise Exception('Unknown error occurred, see log for details')

    def test(self):
        response = subprocess.Popen(['ping -c 4 127.0.0.1'], stdout=subprocess.PIPE, shell=True)
        (output, err) = response.communicate()

        output = output.decode("utf-8")

        if response.returncode == 0:
            return {'reply': True, 'response': output}

        return {'reply': False, 'response': output}
