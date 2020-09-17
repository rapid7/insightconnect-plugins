import requests
import time
from komand.exceptions import PluginException


def get_user_info(connection, user_id, logger):
    endpoint = f"https://graph.microsoft.com/v1.0/{connection.tenant}/users/{user_id}"
    headers = connection.get_headers(connection.get_auth_token())

    result = None
    try:
        result = requests.get(endpoint, headers=headers)
    except Exception:
        counter = 0; # We are going to try this 5 times and give up.
        for counter in range(1, 6):
            logger.info(f"Get user info failed, trying again, attempt {counter}.")
            logger.info(f"Sleeping for 5 seconds...")
            time.sleep(5)
            try:
                logger.info(f"Attempting to get user info.")
                result = requests.get(endpoint, headers=headers)
                break # We didn't get an exception, so break the loop
            except Exception:
                logger.info(f"Get user info failed.")
                pass # we got an exception, force pass and try again

    if result and not result.status_code == 200:
        time.sleep(5)  # adding retry
        result = requests.get(endpoint, headers=headers)
        if not result.status_code == 200:
            raise PluginException(cause="Get User Info failed.",
                                  assistance="Unexpected return code from server.",
                                  data=result.text)
    return result
