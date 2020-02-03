import komand
from .schema import FingerInput, FingerOutput, Input, Output, Component
# Custom imports below


class Finger(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='finger',
            description=Component.DESCRIPTION,
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
            f"finger: {params.get(Input.USER)}: no such user",
            'In real life: ???',
            'finger: connect: Connection refused'
        ]
        binary = "/usr/bin/finger"
        cmd = f"{binary} -l -m {params.get(Input.USER)}@{params.get(Input.HOST)}"
        r = komand.helper.exec_command(cmd)

        keys = [
            'Shell',
            'Home phone',
            'Work phone',
            'Room',
            'Project',
            'PGP key',
        ]

        # Did finger succeed in finding a user?
        stdout = r['stdout'].decode('utf-8')
        d['Found'], d['Plugin Status'] = self.found(stdout, r['stderr'].decode('utf-8'), errors)

        for key in keys:
            # Put value in dictionary with index as key.
            d[key] = komand.helper.extract_value(r'\s', key, r':\s(.*)\s', stdout)

        # Try to manually match everything that didn't before
        # Grab Login status/Never logged in
        if '\nNever logged in.\n' in stdout:
            d['Login Status'] = 'Never logged in'
            d['Login From'] = 'Never logged in'
        else:
            d['Login Status'] = komand.helper.extract_value(r'\n', 'On since', r'\s(.*)\n', stdout)
            d['Login From'] = komand.helper.extract_value(r'\n', 'On since', r'\s.* from (\S+)\n', stdout)

        # Grab Last mail read/No mail.
        mail = ['No mail.', 'No unread mail']
        for msg in mail:
            if '\n' + msg + '\n' in stdout:
                d['Mail Status'] = msg.rstrip('.')
                break
            d['Mail Status'] = komand.helper.extract_value(r'\n', 'Mail last read', r'\s(.*)\n', stdout)

        # Grab login name
        d['Login'] = komand.helper.extract_value(r'\n', '(?:Login|Login name)', r': (\S+)\s', stdout)
        # Grab full name
        d['Name'] = komand.helper.extract_value(r'\s', '(?:Name|In real life)', r':\s(.*)\s', stdout)
        # Grab home dself.irectory
        d['Directory'] = komand.helper.extract_value('\n', 'Directory', r':\s(\S+)\s+', stdout)
        # Grab forward maself.il address
        d['Mail forwarded to'] = komand.helper.extract_value(r'\n', 'Mail forwarded to', r'\s(\S+)\n', stdout)
        # Grab plan
        if '\nNo Plan.\n' in stdout:
            d['Plan'] = 'No plan'
        else:
            d['Plan'] = komand.helper.extract_value(r'\n', 'Plan', r':\n(.*)', stdout)

        output = {
            Output.FOUND: d['Found'],
            Output.LOGIN: d['Login'],
            Output.LOGINSTATUS: d['Login Status'],
            Output.LOGINFROM: d['Login From'],
            Output.HOME: d['Directory'],
            Output.FULLNAME: d['Name'],
            Output.SHELL: d['Shell'],
            Output.MAIL: d['Mail forwarded to'],
            Output.MAILSTATUS: d['Mail Status'],
            Output.PLAN: d['Plan'],
            Output.PROJECT: d['Project'],
            Output.PUBKEY: d['PGP key'],
            Output.WORKPHONE: d['Work phone'],
            Output.HOMEPHONE: d['Home phone'],
            Output.ROOM: d['Room'],
            Output.STATUS: d['Plugin Status'],
        }

        results = komand.helper.clean_dict(output)
        return results
