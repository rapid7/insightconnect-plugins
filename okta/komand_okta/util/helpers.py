import urllib.parse
import requests
from komand.exceptions import PluginException


def group_response(response, user_id):
    try:
        data = response.json()
    except ValueError:
        if response.status_code == 204:
            return {'userid': user_id, 'success': True}
        return {'success': False}

    if 'errorSummary' in data:
        # 405: {u'errorCode': u'E0000022', u'errorSummary': u'The endpoint does not support the provided HTTP method', u'errorLink': u'E0000022', u'errorCauses': [], u'errorId': u'oaexVslu0CIQCWH63QtUs4kSw'}
        raise PluginException(cause='Wrong HTTP method', assistance=data['errorSummary'])

    return {'success': False}


def get_user_id(email, connection, logger):
    url = requests.compat.urljoin(connection.okta_url, f'/api/v1/users/{urllib.parse.quote(email)}')

    """ Search for the user by email to get the id """
    response = connection.session.get(url)
    data = response.json()

    if response.status_code != 200:
        summary = data['errorSummary']
        logger.error(f'Okta: Lookup User by Email failed: {summary}')
        return None

    return data['id']


def raise_based_on_error_code(response):
    error_code = response["errorCode"]
    error_summary = response["errorSummary"]
    error_causes = response["errorCauses"]
    raise PluginException(
        cause=f"Okta returned a {response.status_code} status code, and an error code of {error_code}.",
        assistance=f"Summary: {error_summary}. Possible causes: {error_causes}.",
        data=response.text)
