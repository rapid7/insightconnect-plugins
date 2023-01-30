import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import UpdateSharedCredentialInput, UpdateSharedCredentialOutput, Input, Output, Component
from ...util import endpoints
from ...util.resource_requests import ResourceRequests
from ...util.util import check_not_null, check_in_enum, make_payload


def ssh_setup(account: dict):
    permission_elevation = account.get("permission_elevation", "none")
    check_in_enum(permission_elevation, ["none", "sudo", "sudosu", "su", "pbrun", "privileged-exec"])
    if permission_elevation not in ("none", "pbrun"):
        permission_elevation_username = check_not_null(account, "permission_elevation_username")
        permission_elevation_password = check_not_null(account, "permission_elevation_password")
    else:
        permission_elevation_username = ""
        permission_elevation_password = ""
    return permission_elevation, permission_elevation_username, permission_elevation_password


def usr_and_pass(account: dict):
    return check_not_null(account, "username"), check_not_null(account, "password")


def as400_cifs_cvs(account: dict, service: str) -> dict:
    domain = account.get("domain", "")
    username, password = usr_and_pass(account)
    return {"service": service, "domain": domain, "username": username, "password": password}


def cifs_hash(account: dict, service: str) -> dict:
    domain = account.get("domain", "")
    username = check_not_null(account, "username")
    ntlm_hash = check_not_null(account, "ntlm_hash")
    return {"service": service, "domain": domain, "username": username, "ntlmHash": ntlm_hash}


def db2_mysql_postgresql(account: dict, service: str) -> dict:
    database = account.get("database", "")
    username, password = usr_and_pass(account)
    return {"service": service, "database": database, "username": username, "password": password}


def ftp_pop_remote_exec_telnet(account: dict, service: str) -> dict:
    username, password = usr_and_pass(account)
    return {"service": service, "username": username, "password": password}


def http(account: dict, service: str) -> dict:
    realm = account.get("realm", "")
    username, password = usr_and_pass(account)
    return {"service": service, "realm": realm, "username": username, "password": password}


def ms_sql_sybase(account: dict, service: str) -> dict:
    database = account.get("database", "")
    username, password = usr_and_pass(account)
    use_windows_authentication = account.get("use_windows_authentication", False)
    if use_windows_authentication:
        domain = check_not_null(account, "domain")
        return {"service": service, "database": database, "domain": domain, "username": username, "password": password}
    else:
        return {"service": service, "database": database, "username": username, "password": password}


def notes(account: dict, service: str) -> dict:
    notes_id_password = check_not_null(account, "notes_id_password")
    return {"service": service, "notesIDPassword": notes_id_password}


def oracle(account: dict, service: str) -> dict:
    sid = account.get("sid", "")
    username, password = usr_and_pass(account)
    enumerate_sids = account.get("enumerate_sids", False)
    oracle_listener_password = account.get("oracle_listener_password", "")
    return {"service": service, "sid": sid, "enumerateSids": enumerate_sids, "username": username,
            "password": password, "oracleListenerPassword": oracle_listener_password}


def snmp(account: dict, service: str) -> dict:
    community_name = check_not_null(account, "community_name")
    return {"service": service, "communityName": community_name}


def snmpv3(account: dict, service: str) -> dict:
    authentication_type = check_not_null(account, "authentication_type")
    check_in_enum(authentication_type, ["no-authentication", "md5", "sha"])
    username, password = usr_and_pass(account)
    privacy_type = account.get("privacy_type", "")
    if privacy_type != "":
        check_in_enum(privacy_type, ["no-privacy", "des", "aes-128", "aes-192", "aes-192-with-3-des-key-extension",
                                     "aes-256", "aes-265-with-3-des-key-extension"])
    privacy_password = account.get("privacy_password", "")
    if authentication_type == "no-authentication" and privacy_type == "no-privacy" and privacy_password == "":
        raise PluginException(
            cause="Privacy_password is required when authentication_type is no-authentication and privacy_type is no-privacy.",
            assistance="Enter privacy_password"
        )
    return {"service": service, "authenticationType": authentication_type, "privacyType": privacy_type,
            "username": username, "password": password}


def ssh(account: dict, service: str) -> dict:
    username, password = usr_and_pass(account)
    permission_elevation, permission_elevation_username, permission_elevation_password = ssh_setup(account)
    return {"service": service, "username": username, "password": password, "permissionElevation": permission_elevation,
            "permissionElevationUsername": permission_elevation_username,
            "permissionElevationPassword": permission_elevation_password}


def ssh_key(account: dict, service: str) -> dict:
    username = check_not_null(account, "username")
    private_key_password = check_not_null(account, "private_key_password")
    pem_key = check_not_null(account, "pem_key")
    permission_elevation, permission_elevation_username, permission_elevation_password = ssh_setup(account)
    return {"service": service, "username": username, "privateKeyPassword": private_key_password, "pemKey": pem_key,
            "permissionElevation": permission_elevation, "permissionElevationUsername": permission_elevation_username,
            "permissionElevationPassword": permission_elevation_password}


class UpdateSharedCredential(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='update_shared_credential',
            description=Component.DESCRIPTION,
            input=UpdateSharedCredentialInput(),
            output=UpdateSharedCredentialOutput())

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.SharedCredential.update_shared_credential(self.connection.console_url,
                                                                       params.get(Input.ID))
        account = params.get("account")
        description = params.get("description", "")
        host_restriction = params.get("host_restriction", "")
        id_ = check_not_null(params, "id")
        name = check_not_null(params, "name")
        port_restriction = params.get("port_restriction", "")
        site_assignment = check_not_null(params, "site_assignment")
        check_in_enum(site_assignment, ["all-sites", "specific-sites"])

        if site_assignment == "all-sites":
            sites = None
        else:
            sites = check_not_null(params, "sites")

        service = check_not_null(account, "service")
        service_dict = {"as400": as400_cifs_cvs, "cifs": as400_cifs_cvs, "cvs": as400_cifs_cvs, "cifs_hash": cifs_hash,
                        "ftp": ftp_pop_remote_exec_telnet, "pop": ftp_pop_remote_exec_telnet,
                        "db2": db2_mysql_postgresql, "mysql": db2_mysql_postgresql, "postgresql": db2_mysql_postgresql,
                        "remote-exec": ftp_pop_remote_exec_telnet, "telnet": ftp_pop_remote_exec_telnet, "snmp": snmp,
                        "http": http, "ms-sql": ms_sql_sybase, "sybase": ms_sql_sybase, "notes": notes,
                        "snmpv3": snmpv3, "ssh": ssh, "sshKey": ssh_key}

        account_input = service_dict[service](account, service)
        payload = make_payload(account_input, description, host_restriction, id_, name, port_restriction,
                               site_assignment, sites)
        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=payload)

        return {"links": response["links"]}
