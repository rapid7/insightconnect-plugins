from komand_thehive.connection.schema import Input as ConnectionInput
from komand_thehive.actions.create_case.schema import Input as CaseInput
from komand_thehive.actions.create_case_observable.schema import Input as CaseObservableInput
from komand_thehive.actions.create_case_task.schema import Input as CaseTaskInput

STUB_API_KEY = "9de5069c5afe602b2ea0a04b66beb2c0"
STUB_USERNAME = "username"
STUB_PASSWORD = "password"
STUB_PORT = "9000"
STUB_HOST = "10.10.10.10"
STUB_PROTOCOL = "http"
STUB_CONNECTION_API_KEY = {
    ConnectionInput.PORT: STUB_PORT,
    ConnectionInput.HOST: STUB_HOST,
    ConnectionInput.PROTOCOL: STUB_PROTOCOL,
    ConnectionInput.API_KEY: {"secretKey": STUB_API_KEY},
}
STUB_BASE_URL = "http://10.10.10.10:9000"
STUB_CASE_ID = "abcdef123"
STUB_USER_ID = "stubuserid"
STUB_CASE = {
    CaseInput.TITLE: "title",
    CaseInput.DESCRIPTION: "description",
    CaseInput.TLP: 2,
}
STUB_OBSERVABLE = {CaseObservableInput.ID: STUB_CASE_ID}
STUB_TASK = {CaseTaskInput.ID: STUB_CASE_ID, CaseTaskInput.TITLE: "title", CaseTaskInput.DESCRIPTION: "description"}
