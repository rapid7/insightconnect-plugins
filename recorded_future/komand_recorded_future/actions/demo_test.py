import requests


def demo_test(token, logger):
    demo_url = "https://api.recordedfuture.com/v2/hash/demoevents?limit=1"
    try:
        test_headers = {'X-RFToken': token}
        response = requests.get(demo_url, headers=test_headers)
        response.raise_for_status()

        return {"status": "200 OK"}

    except requests.exceptions.HTTPError as e:
        logger.error("HTTP error occurred. Error: " + str(e))
    except requests.exceptions.ConnectionError as e:
        logger.error("A network problem occurred. Error: " + str(e))
    except requests.exceptions.Timeout as e:
        logger.error("Timeout occurred. Error: " + str(e))
    except requests.exceptions.TooManyRedirects as e:
        logger.error("Too many redirects! Error: " + str(e))
    except Exception as e:
        logger.error("Error: " + str(e))
