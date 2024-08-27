import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from datetime import datetime, timedelta, timezone

# Custom imports below
from komand_proofpoint_tap.util.api import ProofpointTapApi
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from komand_proofpoint_tap.util.exceptions import ApiException
from komand_proofpoint_tap.util.api import Endpoint
from komand_proofpoint_tap.util.util import SiemUtils


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None
        self.is_authorized = False

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.client = ProofpointTapApi(
            params.get(Input.SERVICEPRINCIPAL, {}), params.get(Input.SECRET, {}), self.logger
        )

    def test(self):
        if self.client.authorized:
            try:
                self.client.get_top_clickers({"window": 14})
            except PluginException:
                raise ConnectionTestException(
                    cause="Connection error.",
                    assistance="Please check that your service principal and secret are correct.",
                )
        return {"status": "Success"}

    def test_task(self):
        self.logger.info("Running a connection test to Proofpoint")
        return_message = "The connection test to Proofpoint was unsuccessful \n"
        try:
            end_time = datetime.now(timezone.utc) - timedelta(minutes=1)
            start_time = datetime.now(timezone.utc) - timedelta(minutes=6)

            parameters = SiemUtils.prepare_time_range(start_time.isoformat(), end_time.isoformat(), {"format": "JSON"})

            _ = self.client.siem_action(Endpoint.get_all_threats(), parameters)
            message = "The connection test to Proofpoint was successful"
            self.logger.info(message)
            return {"success": True}, message
        except ApiException as error:
            cause_msg = f"The connection test to Proofpoint failed because: {error.cause}"
            return_message += f"{cause_msg} \n"
            self.logger.info(cause_msg)
            self.logger.info(error.assistance)
            return_message += f"{error.assistance} \n"
            self.logger.error(error)

            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=return_message)
