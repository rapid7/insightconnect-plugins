import insightconnect_plugin_runtime
from .schema import CreateServiceRequestInput, CreateServiceRequestOutput, Input, Output, Component

# Custom imports below


class CreateServiceRequest(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_service_request",
            description=Component.DESCRIPTION,
            input=CreateServiceRequestInput(),
            output=CreateServiceRequestOutput(),
        )

    def run(self, params={}):
        urgency = params.get(Input.URGENCY)

        payload = {
            "SvcReqTmplLink": self.connection.ivanti_service_manager_api.search_service_request_template(
                params.get(Input.SERVICE_REQUEST_TEMPLATE)
            ).get("RecId"),
            "ProfileLink": self.connection.ivanti_service_manager_api.search_employee(params.get(Input.CUSTOMER)).get(
                "RecId"
            ),
            "Symptom": params.get(Input.DESCRIPTION),
            "Status": params.get(Input.STATUS),
        }

        if urgency:
            payload["Urgency"] = urgency

        return {Output.SERVICE_REQUEST: self.connection.ivanti_service_manager_api.post_service_request(payload)}
