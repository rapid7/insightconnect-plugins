from json.decoder import JSONDecodeError
from komand_cherwell.connection.connection import Connection


def connectivity_test(connection: Connection) -> object:
    """
    Tests connectivity to the Cherwell server by way of the serviceinfo endpoint
    :param connection: Komand Connection object with a valid connection
    :return: Response from the Cherwell server
    """
    service_info_url = connection.base_url() + "/api/V1/serviceinfo"
    response = connection.session().get(service_info_url)

    if response.status_code not in range(200, 299):
        raise Exception(
            "Error: Received %d HTTP status code from Cherwell. Please verify your Cherwell server "
            "status and try again. If the issue persists please contact support. "
            "Server response was: %s" % (response.status_code, response.text))

    try:
        # This should be a JSON object containing information about their Cherwell server
        response_data = response.json()
    except JSONDecodeError:
        raise Exception("Error: Received an unexpected response from Cherwell "
                        "(non-JSON or no response was received). Response was: %s" % response.text)

    return response_data
