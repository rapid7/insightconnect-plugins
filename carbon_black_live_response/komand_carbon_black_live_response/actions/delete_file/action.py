import komand
from .schema import DeleteFileInput, DeleteFileOutput
# Custom imports below
import cbapi
from cbapi.response.models import Sensor


class DeleteFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_file',
                description='Delete a file from the endpoint',
                input=DeleteFileInput(),
                output=DeleteFileOutput())

    def run(self, params={}):
        try:
            sensor = self.connection.carbon_black.select(Sensor).where("hostname:%s" % params.get("hostname")).first()
            if sensor is None:
                self.logger.info("Failed to delete %s" % params.get("object_path"))
                return {"success": False}

            self.logger.info("Connected to sensor...")
            with sensor.lr_session() as session:
                self.logger.info("Session created...")
                session.delete_file(params.get("object_path"))

                return {"success": True}

        except cbapi.live_response_api.LiveResponseError as e:
            self.logger.error("Error occurred: %s" % e)
            raise
        except cbapi.errors.TimeoutError:
            self.logger.error(
                "Error occurred: timeout encountered when waiting for a response for a Live Response API request")
            raise
        except cbapi.response.live_response_api.LiveResponseError as e:
            self.logger.error(
                "Error occurred: error during the execution of a Live Response command on an endpoint. Details: %s" % e)
            raise
        except cbapi.errors.ApiError as e:
            self.logger.error(
                "Error occurred: attempted to execute a command that is not supported by the sensor. Details: %s" % e)
            raise
        except cbapi.errors.ServerError as e:
            self.logger.error("Error occurred: server error occurred. Details: %s" % e)
            raise

    def test(self):
        # TODO: Implement test function
        return {}
