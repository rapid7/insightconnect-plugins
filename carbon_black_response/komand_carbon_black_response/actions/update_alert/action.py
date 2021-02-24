import komand
from .schema import UpdateAlertInput, UpdateAlertOutput

# Custom imports below
from cbapi.response.models import Alert
from cbapi.errors import ApiError


class UpdateAlert(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_alert",
            description="Updates or Resolves an Alert in Carbon Black",
            input=UpdateAlertInput(),
            output=UpdateAlertOutput(),
        )

    def run(self, params={}):
        alert = self.connection.carbon_black.select(Alert, unique_id=params["id"])
        try:
            alert.status = params["status"]
            alert.save()
        except ApiError as ex:
            self.logger.error("Error: Unable to update alert. Error is: {error}".format(error=str(ex)))
            raise ex

        self.logger.info("Success: Updated alert!")

        return {"success": True}

    def test(self):
        if self.connection.test():
            return {}
