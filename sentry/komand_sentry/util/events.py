import re
import time

from requests import post


def parse_dsn(logger, dsn):
    """
    Parses given DSN configuration and extracts:
        - public_key
        - secret_key
        - host
        - protocol
        - project_id

    Returns extracted data as a dict
    """

    protocol = r'(?P<protocol>\w+)'
    public_key = r'(?P<public_key>\w+)'
    secret_key = r'(?P<secret_key>\w+)'
    host = r'(?P<host>[^/]+)'
    project_id = r'(?P<project_id>\w+)'

    dsn_format = r'^{}://{}:{}@{}/{}$'.format(
        protocol, public_key, secret_key, host, project_id
    )

    logger.info('ParseDSN: Extracting information from DSN configuration')

    dsn_data = re.match(dsn_format, dsn)

    if not dsn_data:
        logger.error('ParseDSN: Could not parse DSN configuration')
        raise Exception('Invalid DSN configuration')

    logger.info('ParseDSN: DSN configuration parsed successfully')

    return dsn_data.groupdict()


def submit_event(logger, event_json, dsn, sentry_version):
    """
    Submits new event data using auth keys from DSN configuration.
    Returns the ID of a newly created event.
    """
    dsn_data = parse_dsn(logger, dsn)

    api_url = '{}://{}/api/{}/store/'.format(
        dsn_data['protocol'], dsn_data['host'], dsn_data['project_id']
    )

    sentry_auth_header = (
        'Sentry sentry_version={}, sentry_timestamp={}, sentry_key={}, '
        'sentry_secret={}, sentry_client=komand/1.0.0'
    ).format(
        sentry_version, int(time.time()),
        dsn_data['public_key'], dsn_data['secret_key']
    )

    response = post(api_url, json=event_json, headers={
        'X-Sentry-Auth': sentry_auth_header,
    })

    try:
        response.raise_for_status()
    except Exception as e:
        logger.error(
            'Requests: Exception: Failed to submit an event: {} {}'.format(
                response.status_code, response.headers['X-Sentry-Error']
            )
        )
        raise e

    return response.json()['id']
