import winrm
import base64
import subprocess


def fix_run_ps(self, script):  # Fixes string bug in python 3 for NTLM connection
    encoded_ps = base64.b64encode(script.encode('utf_16_le')).decode('ascii')
    rs = self.run_cmd('powershell -encodedcommand {0}'.format(encoded_ps))
    if len(rs.std_err):
        rs.std_err = self._clean_error_msg(rs.std_err.decode('utf-8'))
    return rs


winrm.Session.run_ps = fix_run_ps


def local(action, powershell_script):
    action.logger.info('Running on local VM')
    action.logger.debug('PowerShell script: ' + powershell_script)
    process = subprocess.Popen(powershell_script, shell='true', executable='pwsh', stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output, error = process.communicate()
    try:
        output = output.decode('utf-8')
    except AttributeError:
        pass
    try:
        error = error.decode('utf-8')
    except AttributeError:
        pass

    return {'output': output, 'stderr': error}


def ntlm(action, host_ip, powershell_script, username, password, port):
    # Adds needed https and port number to host IP
    action.logger.info('Running a NTLM connection')
    host_connection = 'https://{host_ip}:{port}/wsman'.format(host_ip=host_ip, port=port)
    action.logger.debug('Host Connection: ' + host_connection)
    action.logger.debug('PowerShell script: ' + powershell_script)

    powershell_session = winrm.Session(host_connection, auth=(username, password), transport='ntlm')
    # Forces the Protocol to not fail with self signed certs
    p = winrm.Protocol(endpoint=host_connection,
                       transport='ntlm',
                       username=username,
                       password=password,
                       server_cert_validation='ignore',
                       message_encryption='auto')
    powershell_session.protocol = p
    run_script = powershell_session.run_ps(powershell_script)
    exit_code = run_script.status_code
    error_value = run_script.std_err
    output = run_script.std_out

    try:
        error_value = error_value.decode('utf-8')
    except AttributeError:
        pass
    output = output.decode('utf-8')

    if exit_code != 0:
        action.logger.error(error_value)
        raise Exception('An error occurred in the PowerShell script, see logging for more info')

    return {'output': output, 'stderr': error_value}


def kerberos(action, host_ip, kdc, domain, host_name, powershell_script, password, username, port):
    action.logger.info('Running Kerberos connection')
    # Adds needed https and port number to host IP
    host_connection = 'https://{host_ip}:{port}/wsman'.format(host_ip=host_ip, port=port)
    action.logger.debug('PowerShell script: ' + powershell_script)

    udomain = domain.upper()
    # Config for krb5 file to the domain
    krb_config = '''[libdefaults]
default_realm = {udomain}
forwardable = true
proxiable = true

[realms]
{udomain} = {{
kdc = {kdc}
admin_server = {kdc}
default_domain = {udomain}
}}

[domain_realm]
.{domain} = {udomain}
{domain} = {udomain}'''.format(udomain=udomain, domain=domain, kdc=kdc)
    action.logger.debug(krb_config)
    # Config for DNS
    dns = 'search %s\r\nnameserver %s' % (domain, kdc)
    action.logger.debug(dns)
    # Sends output from stdout on shell commands to logging. Preventing errors
    subprocess.call('mkdir -p /var/lib/samba/private', shell='true')
    subprocess.call('systemctl enable sssd', shell='true')
    # Setup realm to join the domain
    with open('/etc/krb5.conf', 'w') as f:
        f.write(krb_config)
    # Creates a Kerberos ticket
    kinit = '''echo '%s' | kinit %s@%s''' % (password, username, domain.upper())
    response = subprocess.Popen(kinit, shell='true', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = response.communicate()
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')
    action.logger.info('Attempt to make Kerberos ticket stdout: ' + stdout)
    action.logger.info('Attempt to make Kerberos ticket stderr: ' + stderr)
    # DNS info so the plugin knows where to find the domain
    with open('/etc/resolv.conf', 'w') as f:
        f.write(dns)
    # Joins Komand to domain
    realm = '''echo '%s' | realm --install=/ join --user=%s %s''' % (
                                                                     password, username, domain)
    response = subprocess.Popen(realm, shell='true', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = response.communicate()
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')
    action.logger.info('Attempt to join domain stdout: ' + stdout)
    action.logger.info('Attempt to join domain stderr: ' + stderr)
    # Allows resolution if A name not set for host
    with open('/etc/hosts', 'a') as f:
        f.write('\r\n' + host_ip + ' ' + host_name)

    # Runs the script on the host
    powershell_session = winrm.Session(host_connection, auth=(username, password),
                                       transport='kerberos')

    # Forces the protocol to not fail with self signed certs
    p = winrm.Protocol(endpoint=host_connection,
                       transport='kerberos',
                       username=username,
                       password=password,
                       server_cert_validation='ignore')
    powershell_session.protocol = p
    run_script = powershell_session.run_ps(powershell_script)
    exit_code = run_script.status_code
    error_value = run_script.std_err
    output = run_script.std_out

    try:
        error_value = error_value.decode('utf-8')
    except AttributeError:
        pass
    output = output.decode('utf-8')

    if exit_code != 0:
        action.logger.error(error_value)
        raise Exception('An error occurred in the PowerShell script, see logging for more info')

    return {'output': output, 'stderr': error_value}


def credssp(action, host_ip, powershell_script, username, password, port):
    # Adds needed https and port number to host IP
    action.logger.info('Running a CredSSP connection')
    host_connection = 'https://{host_ip}:{port}/wsman'.format(host_ip=host_ip, port=port)
    action.logger.debug('Host Connection: ' + host_connection)
    action.logger.debug('PowerShell script: ' + powershell_script)

    powershell_session = winrm.Session(host_connection, auth=(username, password), transport='credssp')
    # Forces the Protocol to not fail with self signed certs
    p = winrm.Protocol(endpoint=host_connection,
                       transport='credssp',
                       username=username,
                       password=password,
                       server_cert_validation='ignore',
                       message_encryption='auto')
    powershell_session.protocol = p
    run_script = powershell_session.run_ps(powershell_script)
    exit_code = run_script.status_code
    error_value = run_script.std_err
    output = run_script.std_out

    try:
        error_value = error_value.decode('utf-8')
    except AttributeError:
        pass
    output = output.decode('utf-8')

    if exit_code != 0:
        action.logger.error(error_value)
        raise Exception('An error occurred in the PowerShell script, see logging for more info')

    return {'output': output, 'stderr': error_value}
