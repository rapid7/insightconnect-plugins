import insightconnect_plugin_runtime
from .schema import CreateCaseObservableInput, CreateCaseObservableOutput, Component, Input, Output

# Custom imports below


class CreateCaseObservable(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_case_observable",
            description=Component.DESCRIPTION,
            input=CreateCaseObservableInput(),
            output=CreateCaseObservableOutput(),
        )

    def run(self, params={}):

        case_id = params.get(Input.ID)
        json_observable_data = params.get(Input.DATA)

        if json_observable_data:
            observable = json_observable_data
        else:
            observable = {
                "dataType": params.get(Input.DATATYPE),
                "message": params.get(Input.MESSAGE),
                "tlp": params.get(Input.TLP),
                "ioc": params.get(Input.IOC),
                "sighted": params.get(Input.SIGHTED),
                "tags": params.get(Input.TAGS),
            }

        self.logger.info(f"Input: {observable}")

        response = self.connection.client.create_observable_in_case(case_id=case_id, observable=observable)

        return {Output.CASE: response}
