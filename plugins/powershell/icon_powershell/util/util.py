import winrm
import base64
import subprocess  # noqa: B404
import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

DECODING_TYPE = "utf-8"


class FixWinrmSession(winrm.Session):
    def run_ps(self, script: str) -> winrm.Response:  # Fixes string bug in python 3 for NTLM connection
        encoded_ps = base64.b64encode(script.encode("utf_16_le")).decode("ascii")
        rs = self.run_cmd(f"powershell -encodedcommand {encoded_ps}")
        if len(rs.std_err):
            rs.std_err = self._clean_error_msg(rs.std_err)
        return rs


def run_powershell_script(
    auth: str,
    action: insightconnect_plugin_runtime.Action,
    host_ip: str,
    kdc: str,
    domain: str,
    host_name: str,
    powershell_script: str,
    password: str,
    username: str,
    port: int,
) -> dict:
    if auth == "None" or not host_ip:
        data = run_script_locally(action=action, powershell_script=powershell_script)

    elif auth == "NTLM":
        data = run_script_using_ntlm(
            action=action,
            host_ip=host_ip,
            powershell_script=powershell_script,
            username=username,
            password=password,
            port=port,
        )

    elif auth == "Kerberos":
        data = run_script_using_kerberos(
            action=action,
            host_ip=host_ip,
            kdc=kdc,
            domain=domain,
            host_name=host_name,
            powershell_script=powershell_script,
            password=password,
            username=username,
            port=port,
        )

    elif auth == "CredSSP":
        data = run_script_using_credssp(
            action=action,
            host_ip=host_ip,
            powershell_script=powershell_script,
            username=username,
            password=password,
            port=port,
        )

    else:
        raise PluginException(
            cause="No valid Authentication type was chosen.",
            assistance="Make sure that you choose a correct Authentication type based on documentation.",
        )

    stdout = data.get("stdout")
    stderr = data.get("stderr")

    if stdout:
        stdout = action.safe_encode(stdout)
    if stderr:
        stderr = action.safe_encode(stderr)
    if "ParserError" in stderr:
        raise PluginException(
            cause="Error parsing script.",
            assistance="Refer to help.md. Ensure you are not using special characters such as quotes in your password.",
        )
    return {"stdout": stdout, "stderr": stderr}


def run_script_locally(action: insightconnect_plugin_runtime.Action, powershell_script: str) -> dict:
    action.logger.info("Running on local VM")
    action.logger.debug("PowerShell script: " + powershell_script)
    with subprocess.Popen(
        powershell_script,
        shell="true",  # noqa: B602
        executable="pwsh",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ) as process:
        stdout, error = process.communicate()
        try:
            stdout = stdout.decode(DECODING_TYPE)
        except AttributeError:
            pass
        try:
            error = error.decode(DECODING_TYPE)
        except AttributeError:
            pass

        return {"stdout": stdout, "stderr": error}


def run_script_using_ntlm(
    action: insightconnect_plugin_runtime.Action,
    host_ip: str,
    powershell_script: str,
    username: str,
    password: str,
    port: int,
) -> dict:
    # Adds needed https and port number to host IP
    action.logger.info("Running a NTLM connection")
    prefix = "http" if port == 5985 else "https"
    host_connection = f"{prefix}://{host_ip}:{port}/wsman"
    action.logger.debug("Host Connection: " + host_connection)
    action.logger.debug("PowerShell script: " + powershell_script)
    powershell_session = FixWinrmSession(host_connection, auth=(username, password), transport="ntlm")

    # Forces the Protocol to not fail with self signed certs
    powershell_session.protocol = winrm.Protocol(
        endpoint=host_connection,
        transport="ntlm",
        username=username,
        password=password,
        server_cert_validation="ignore",
        message_encryption="auto",
    )

    error_value, stdout = run_powershell_session(action, powershell_script, powershell_session)

    return {"stdout": stdout, "stderr": error_value}


def run_script_using_credssp(
    action: insightconnect_plugin_runtime.Action,
    host_ip: str,
    powershell_script: str,
    username: str,
    password: str,
    port: int,
) -> dict:

    # Adds needed https and port number to host IP
    action.logger.info("Running a CredSSP connection")
    host_connection = f"https://{host_ip}:{port}/wsman"
    action.logger.debug("Host Connection: " + host_connection)
    action.logger.debug("PowerShell script: " + powershell_script)

    powershell_session = FixWinrmSession(host_connection, auth=(username, password), transport="credssp")

    # Forces the Protocol to not fail with self signed certs
    powershell_session.protocol = winrm.Protocol(
        endpoint=host_connection,
        transport="credssp",
        username=username,
        password=password,
        server_cert_validation="ignore",
        message_encryption="auto",
    )

    error_value, stdout = run_powershell_session(action, powershell_script, powershell_session)

    return {"stdout": stdout, "stderr": error_value}


def run_script_using_kerberos(
    action: insightconnect_plugin_runtime.Action,
    host_ip: str,
    kdc: str,
    domain: str,
    host_name: str,
    powershell_script: str,
    password: str,
    username: str,
    port: int,
) -> dict:
    action.logger.info("Running Kerberos connection")
    # Adds needed https and port number to host IP
    prefix = "http" if port == 5985 else "https"
    host_address = f"{prefix}://{host_ip}:{port}/wsman"
    configure_machine_for_kerberos_connection(
        action, domain, host_ip, host_name, kdc, password, powershell_script, username
    )

    # Runs the script on the host
    powershell_session = FixWinrmSession(host_address, auth=(username, password), transport="kerberos")

    # Forces the protocol to not fail with self signed certs
    powershell_session.protocol = winrm.Protocol(
        endpoint=host_address,
        transport="kerberos",
        username=username,
        password=password,
        server_cert_validation="ignore",
    )
    error_value, stdout = run_powershell_session(action, powershell_script, powershell_session)

    return {"stdout": stdout, "stderr": error_value}


def configure_machine_for_kerberos_connection(
    action: insightconnect_plugin_runtime.Action,
    domain: str,
    host_ip: str,
    host_name: str,
    kdc: str,
    password: str,
    powershell_script: str,
    username: str,
):
    action.logger.debug("PowerShell script: " + powershell_script)
    udomain = domain.upper()
    # Config for krb5 file to the domain
    krb_config = (
        f"[libdefaults]\n"
        f"default_realm = {udomain}\n"
        f"forwardable = true\n"
        f"proxiable = true\n"
        f"\n"
        f"[realms]\n"
        f"{udomain} = {{\n"
        f"kdc = {kdc}\n"
        f"admin_server = {kdc}\n"
        f"default_domain = {udomain}\n"
        f"}}\n"
        f"\n"
        f"[domain_realm]\n"
        f".{domain} = {udomain}\n"
        f"{domain} = {udomain}\n"
    )

    action.logger.debug(krb_config)
    # Config for DNS
    dns = f"search {domain}\r\nnameserver {kdc}"
    action.logger.debug(dns)
    # Sends output from stdout on shell commands to logging. Preventing errors
    subprocess.call("mkdir -p /var/lib/samba/private", shell="true")  # noqa: B607,B602
    subprocess.call("systemctl enable sssd", shell="true")  # noqa: B607,B602
    # Setup realm to join the domain
    with open("/etc/krb5.conf", "w", encoding="utf-8") as file:
        file.write(krb_config)

    # Creates a Kerberos ticket
    kinit = f"""echo '{password}' | kinit {username}@{domain.upper()}"""
    response = subprocess.Popen(kinit, shell="true", stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # noqa: B602
    (stdout, stderr) = response.communicate()
    stdout = stdout.decode(DECODING_TYPE)
    stderr = stderr.decode(DECODING_TYPE)
    action.logger.info("Attempt to make Kerberos ticket stdout: " + stdout)
    action.logger.info("Attempt to make Kerberos ticket stderr: " + stderr)
    # DNS info so the plugin knows where to find the domain
    with open("/etc/resolv.conf", "w", encoding="utf-8") as f:
        f.write(dns)
    realm = f"""echo '{password}' | realm --install=/ join --user={username} {domain}"""
    response = subprocess.Popen(realm, shell="true", stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # noqa: B602
    (stdout, stderr) = response.communicate()
    stdout = stdout.decode(DECODING_TYPE)
    stderr = stderr.decode(DECODING_TYPE)
    action.logger.info("Attempt to join domain stdout: " + stdout)
    action.logger.info("Attempt to join domain stderr: " + stderr)
    # Allows resolution if A name not set for host
    with open("/etc/hosts", "a", encoding="utf-8") as f:
        f.write("\r\n" + host_ip + " " + host_name)


def run_powershell_session(
    action: insightconnect_plugin_runtime.Action, powershell_script: str, powershell_session: winrm.Session
) -> tuple:
    run_script = powershell_session.run_ps(powershell_script)
    exit_code = run_script.status_code
    error_value = run_script.std_err
    output = run_script.std_out
    try:
        error_value = error_value.decode(DECODING_TYPE)
    except AttributeError:
        pass
    output = output.decode(DECODING_TYPE)
    if exit_code != 0:
        action.logger.error(error_value)
        raise PluginException(
            cause="An error occurred in the PowerShell script.", assistance="See logging for more info."
        )
    return error_value, output


def add_credentials_to_script(powershell_script: str, credentials: dict) -> str:
    credentials_definition = ""
    username = credentials.get("username")
    password = credentials.get("password")
    secret_key = credentials.get("secret_key")

    if username:
        credentials_definition += f"$username = '{username}'\n"
    if password:
        credentials_definition += f"$password = '{password}' | ConvertTo-SecureString -asPlainText -Force\n"
    if secret_key:
        credentials_definition += f"$secret_key = '{secret_key}'\n"

    return credentials_definition + powershell_script
