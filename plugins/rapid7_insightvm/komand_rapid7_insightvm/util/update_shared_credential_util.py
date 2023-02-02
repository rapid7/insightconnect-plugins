from typing import Union, Tuple, Dict

from insightconnect_plugin_runtime.exceptions import PluginException

from komand_rapid7_insightvm.util.util import check_not_null


def ssh_setup(account: Dict[str, any]) -> Tuple[str, str, str]:
    """
    checks permission elevation to see if permission_elevation_username and password is needed
    :param account: user input
    :return: permission_elevation, permission_elevation_username, permission_elevation_password
    """
    permission_elevation = account.get("permission_elevation", "none")

    if permission_elevation not in ("none", "pbrun"):
        permission_elevation_username = check_not_null(account, "permission_elevation_username")
        permission_elevation_password = check_not_null(account, "permission_elevation_password")
    else:
        permission_elevation_username = ""
        permission_elevation_password = ""  # nosec
    return permission_elevation, permission_elevation_username, permission_elevation_password


def usr_and_pass(account: Dict[str, any]) -> Tuple[str, str]:
    """
    gets username and password from account
    :param account: where username and password is stored
    :return: username and password
    """
    return check_not_null(account, "username"), check_not_null(account, "password")


def as400_cifs_cvs(account: Dict[str, any], service: str) -> Dict[str, str]:
    """
    Gets inputs required for the as400, cifs, or cvs services
    :param account: where all potential inputs are stored
    :param service: service
    :return: dictionary of all required variables for the as400, cifs, or cvs services
    """
    domain = account.get("domain", "")
    username, password = usr_and_pass(account)
    return {"service": service, "domain": domain, "username": username, "password": password}


def cifshash(account: Dict[str, any], service: str) -> Dict[str, str]:
    """
    Gets inputs required for cifshash service
    :param account: where all potential inputs are stored
    :param service: service
    :return: dictionary of all required variables for cifshash
    """
    domain = account.get("domain", "")
    username = check_not_null(account, "username")
    ntlm_hash = check_not_null(account, "ntlm_hash")
    return {"service": service, "domain": domain, "username": username, "ntlmHash": ntlm_hash}


def db2_mysql_postgresql(account: Dict[str, any], service: str) -> Dict[str, str]:
    """
    Gets inputs required for the db2, mysql, or postgresql services
    :param account: where all potential inputs are stored
    :param service: service
    :return: dictionary of all required variables the db2, mysql, or postgresql services
    """
    database = account.get("database", "")
    username, password = usr_and_pass(account)
    return {"service": service, "database": database, "username": username, "password": password}


def ftp_pop_remote_exec_telnet(account: Dict[str, any], service: str) -> Dict[str, str]:
    """
    Gets inputs required for the ftp, pop, remote-exec or telnet services
    :param account: where all potential inputs are stored
    :param service: service
    :return: dictionary of all required variables for the ftp, pop, remote-exec or telnet service
    """
    username, password = usr_and_pass(account)
    return {"service": service, "username": username, "password": password}


def http(account: Dict[str, any], service: str) -> Dict[str, str]:
    """
    Gets inputs required for http service
    :param account: where all potential inputs are stored
    :param service: service
    :return: dictionary of all required variables for http
    """
    realm = account.get("realm", "")
    username, password = usr_and_pass(account)
    return {"service": service, "realm": realm, "username": username, "password": password}


def ms_sql_sybase(account: Dict[str, any], service: str) -> Union[Dict[str, any], Dict[str, any]]:
    """
    Gets inputs required for the ms-sql or sybase service
    :param account: where all potential inputs are stored
    :param service: service
    :return: dictionary of all required variables for the ms-sql or sybase service
    """
    database = account.get("database", "")
    username, password = usr_and_pass(account)
    use_windows_authentication = account.get("use_windows_authentication", False)
    if use_windows_authentication:
        domain = check_not_null(account, "domain")
        return {
            "service": service,
            "database": database,
            "useWindowsAuthentication": use_windows_authentication,
            "domain": domain,
            "username": username,
            "password": password,
        }
    else:
        return {
            "service": service,
            "database": database,
            "useWindowsAuthentication": use_windows_authentication,
            "username": username,
            "password": password,
        }


def notes(account: Dict[str, any], service: str) -> Dict[str, str]:
    """
    Gets inputs required for notes service
    :param account: where all potential inputs are stored
    :param service: service
    :return: dictionary of all required variables for notes
    """
    notes_id_password = check_not_null(account, "notes_id_password")
    return {"service": service, "notesIDPassword": notes_id_password}


def oracle(account: Dict[str, any], service: str) -> Union[Dict[str, any], Dict[str, any]]:
    """
    Gets inputs required for oracle service
    :param account: where all potential inputs are stored
    :param service: service
    :return: dictionary of all required variables for oracle
    """
    sid = account.get("sid", "")
    username, password = usr_and_pass(account)
    enumerate_sids = account.get("enumerate_sids", False)
    if enumerate_sids:
        oracle_listener_password = account.get("oracle_listener_password", "")
        return {
            "service": service,
            "sid": sid,
            "enumerateSids": enumerate_sids,
            "username": username,
            "password": password,
            "oracleListenerPassword": oracle_listener_password,
        }
    else:
        return {
            "service": service,
            "sid": sid,
            "enumerateSids": enumerate_sids,
            "username": username,
            "password": password,
        }


def snmp(account: Dict[str, any], service: str) -> Dict[str, str]:
    """
    Gets inputs required for snmp service
    :param account: where all potential inputs are stored
    :param service: service
    :return: dictionary of all required variables for snmp
    """
    community_name = check_not_null(account, "community_name")
    return {"service": service, "communityName": community_name}


def snmpv3(account: Dict[str, any], service: str) -> Dict[str, str]:
    """
    Gets inputs required for snmpv3 service
    :param account: where all potential inputs are stored
    :param service: service
    :return: dictionary of all required variables for snmpv3
    """
    authentication_type = check_not_null(account, "authentication_type")
    username, password = usr_and_pass(account)
    privacy_type = account.get("privacy_type", "no-privacy")
    privacy_password = account.get("privacy_password", "")
    if authentication_type == "no-authentication" and privacy_type == "no-privacy" and privacy_password == "":  # nosec
        raise PluginException(
            cause="Privacy_password is required when authentication_type is no-authentication and privacy_type is no-privacy.",
            assistance="Enter privacy_password",
        )
    return {
        "service": service,
        "authenticationType": authentication_type,
        "privacyType": privacy_type,
        "username": username,
        "password": password,
    }


def ssh(account: Dict[str, any], service: str) -> Dict[str, str]:
    """
    Gets inputs required for ssh service
    :param account: where all potential inputs are stored
    :param service: service
    :return: dictionary of all required variables for ssh
    """
    username, password = usr_and_pass(account)
    permission_elevation, permission_elevation_username, permission_elevation_password = ssh_setup(account)
    return {
        "service": service,
        "username": username,
        "password": password,
        "permissionElevation": permission_elevation,
        "permissionElevationUsername": permission_elevation_username,
        "permissionElevationPassword": permission_elevation_password,
    }


def ssh_key(account: Dict[str, any], service: str) -> Dict[str, any]:
    """
    Gets inputs required for ssh-key service
    :param account: where all potential inputs are stored
    :param service: service
    :return: dictionary of all required variables for ssh-key
    """
    username = check_not_null(account, "username")
    private_key_password = check_not_null(account, "private_key_password")
    pem_key = check_not_null(account, "pem_key")
    permission_elevation, permission_elevation_username, permission_elevation_password = ssh_setup(account)
    return {
        "service": service,
        "username": username,
        "privateKeyPassword": private_key_password,
        "pemKey": pem_key,
        "permissionElevation": permission_elevation,
        "permissionElevationUsername": permission_elevation_username,
        "permissionElevationPassword": permission_elevation_password,
    }


def get_account_input(account: Dict[str, any]):
    """
    finds which service user wants to use and runs function specific to that service
    :param account: account input
    :return: returns the output of a function that takes variables from account depending on the service chosen
    """
    service = check_not_null(account, "service")
    service_dict = {
        "as400": as400_cifs_cvs,
        "cifs": as400_cifs_cvs,
        "cvs": as400_cifs_cvs,
        "cifshash": cifshash,
        "ftp": ftp_pop_remote_exec_telnet,
        "pop": ftp_pop_remote_exec_telnet,
        "oracle": oracle,
        "db2": db2_mysql_postgresql,
        "mysql": db2_mysql_postgresql,
        "postgresql": db2_mysql_postgresql,
        "remote-exec": ftp_pop_remote_exec_telnet,
        "telnet": ftp_pop_remote_exec_telnet,
        "snmp": snmp,
        "http": http,
        "ms-sql": ms_sql_sybase,
        "sybase": ms_sql_sybase,
        "notes": notes,
        "snmpv3": snmpv3,
        "ssh": ssh,
        "ssh-key": ssh_key,
    }
    return service_dict[service](account, service)


def make_payload(params: Dict[str, any], account_input: Dict[str, any]) -> Dict[str, any]:
    """
    creates a payload for the put request
    :param params: user input
    :param account_input: required variables collected from user input
    :return: dictionary of entire payload that will be sent to the api
    """
    site_assignment = params.get(check_not_null(params, "site_assignment"))
    if site_assignment == "all-sites":
        sites = None
    else:
        sites = check_not_null(params, "sites")
    payload = {
        "account": account_input,
        "description": params.get("description", ""),
        "hostRestriction": params.get("host_restriction", ""),
        "id": check_not_null(params, "id"),
        "name": check_not_null(params, "name"),
        "portRestriction": params.get("port_restriction", ""),
        "siteAssignment": site_assignment,
        "sites": sites,
    }
    return payload
