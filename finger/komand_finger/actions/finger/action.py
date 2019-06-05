import komand
from .schema import FingerInput, FingerOutput
# Custom imports below


class Finger(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='finger',
            description='Ask finger about a username',
            input=FingerInput(),
            output=FingerOutput())

    def found(self, stdout, stderr, errors):
        '''Check for errors in output'''
        for msg in errors:
            self.logger.info(msg)
            if msg in stderr:
                return False, msg
            if msg in stdout:
                return False, msg
        return True, 'Success'

    def run(self, params={}):
        d = {}
        # GNU Finger's error messages from binary: $ strings /bin/finger
        errors = [
            'Finger online user list request denied',
            'Finger online user list denied',
            'Finger server disable',
            'Sorry, we do not support empty finger queries',
            'User not found',
            'finger: unknown host: ',
            'finger: connect: Connection timed out',
            'finger: fdopen: ',
            'finger: tcp/finger: unknown service',
            'finger: Out of space.',
            'finger: out of space.',
            'finger: socket: ',
            'usage: finger [-',
            'finger: {}: no such user'.format(params.get('user')),
            'In real life: ???',
            'finger: connect: Connection refused'
        ]
        binary = "/usr/bin/finger"
        cmd = "%s -l -m %s@%s" % (binary, params.get('user'), params.get('host'))
        r = komand.helper.exec_command(cmd)

        # Initialize list with keys for matching
        keys = [
            'Shell',
            'Home phone',
            'Work phone',
            'Room',
            'Project',
            'PGP key',
        ]

        # Did finger succeed in finding a user?
        d['Found'], d['Plugin Status'] = self.found(r['stdout'], r['stderr'], errors)

        for key in keys:
            # Put value in dictionary with index as key.
            d[key] = komand.helper.extract_value(r'\s', key, r':\s(.*)\s', r['stdout'])

        ## Try to manually match everything that didn't before
        # Grab Login status/Never logged in
        if '\nNever logged in.\n' in r['stdout']:
            d['Login Status'] = 'Never logged in'
            d['Login From'] = 'Never logged in'
        else:
            d['Login Status'] = komand.helper.extract_value(r'\n', 'On since', r'\s(.*)\n', r['stdout'])
            d['Login From'] = komand.helper.extract_value(r'\n', 'On since', r'\s.* from (\S+)\n', r['stdout'])

        # Grab Last mail read/No mail.
        mail = ['No mail.', 'No unread mail']
        for msg in mail:
            if '\n' + msg + '\n' in r['stdout']:
                d['Mail Status'] = msg.rstrip('.')
                break
            d['Mail Status'] = komand.helper.extract_value(r'\n', 'Mail last read', r'\s(.*)\n', r['stdout'])

        # Grab login name
        d['Login'] = komand.helper.extract_value(r'\n', '(?:Login|Login name)', r': (\S+)\s', r['stdout'])
        # Grab full name
        d['Name'] = komand.helper.extract_value(r'\s', '(?:Name|In real life)', r':\s(.*)\s', r['stdout'])
        # Grab home dself.irectory
        d['Directory'] = komand.helper.extract_value('\n', 'Directory', ':\s(\S+)\s+', r['stdout'])
        # Grab forward maself.il address
        d['Mail forwarded to'] = komand.helper.extract_value(r'\n', 'Mail forwarded to', r'\s(\S+)\n', r['stdout'])
        # Grab plan
        if '\nNo Plan.\n' in r['stdout']:
            d['Plan'] = 'No plan'
        else:
            d['Plan'] = komand.helper.extract_value(r'\n', 'Plan', r':\n(.*)', r['stdout'])

        output = {
            'found': d['Found'],
            'login': d['Login'],
            'loginstatus': d['Login Status'],
            'loginfrom': d['Login From'],
            'home': d['Directory'],
            'fullname': d['Name'],
            'shell': d['Shell'],
            'mail': d['Mail forwarded to'],
            'mailstatus': d['Mail Status'],
            'plan': d['Plan'],
            'project': d['Project'],
            'pubkey': d['PGP key'],
            'workphone': d['Work phone'],
            'homephone': d['Home phone'],
            'room': d['Room'],
            'status': d['Plugin Status'],
        }

        results = komand.helper.clean_dict(output)
        return results

    def test(self, params={}):
        """TODO: Test action"""
        return {}