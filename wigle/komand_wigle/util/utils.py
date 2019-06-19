from logging import Logger

from requests import request

import komand


def clear_empty_values(params):
    return {k: v for k, v in params.items() if v}


def call_api_and_validate_response(
    method, endpoint, error_message='Invalid API call',
    logger=None, auth=None, *args, **kwargs
):
    if logger is None:
        logger = Logger('CallAPI')

    url = 'https://api.wigle.net/api/v2/' + endpoint
    logger.info('CallAPI: Calling {} ...'.format(url))
    response = request(method, url, auth=auth, *args, **kwargs)

    try:
        response.raise_for_status()
    except Exception as e:
        logger.error('CallAPI: {}: {} {}'.format(
            error_message, response.status_code, response.text
        ))
        raise e

    try:
        json = response.json()
        if 'success' in json:
            if not json['success']:
                message = json['message']
                logger.error('CallAPI: An error occured: {}'.format(message))
                raise Exception(message)
            del json['success']
        logger.info('CallAPI: API call successful')
        json = komand.helper.clean(json)
        return json
    except ValueError:
        logger.info(
            'CallAPI: API call successful, but response is not of type JSON'
        )
        return response
