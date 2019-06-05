import komand
from .schema import GetHostIdFromHostnameInput, GetHostIdFromHostnameOutput, Input, Output, Component
# Custom imports below
from json import JSONDecodeError


class GetHostIdFromHostname(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_host_id_from_hostname',
            description=Component.DESCRIPTION,
            input=GetHostIdFromHostnameInput(),
            output=GetHostIdFromHostnameOutput())

    def run(self, params={}):
        hostname = params.get(Input.HOSTNAME)
        url = f"{self.connection.url}/hx/api/v3/hosts"

        response = self.connection.session.get(url=url, params={"search": hostname})

        if response.status_code != 200:
            try:
                details = response.json()["details"][0]
                code, message = details["code"], details["message"]

                raise Exception(f"Error: {message} (error code {code}")

            except JSONDecodeError as e:
                raise Exception(f"Error: Malformed response received from FireEye HX appliance. "
                                f"Got: {response.text}") from e
            except (KeyError, IndexError) as e:
                raise Exception("Error: Unknown error received from FireEye HX appliance "
                                "(no error cause reported).") from e
        try:
            response_json = response.json()
            entries = response_json["data"]["entries"]
            host_id = entries[0]["_id"]
        except (JSONDecodeError, KeyError) as e:
            raise Exception(f"Error: Malformed response received from FireEye HX appliance. "
                            f"Response was {response.text}") from e

        # IndexError from accessing an item in `entries` when one did not exist, so no matches. Return a failure.
        except IndexError:
            return {Output.SUCCESS: False}

        return {
            Output.SUCCESS: True,
            Output.HOST_ID: host_id
        }
