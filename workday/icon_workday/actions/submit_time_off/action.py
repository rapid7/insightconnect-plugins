import komand
from .schema import SubmitTimeOffInput, SubmitTimeOffOutput, Input, Output, Component
# Custom imports below
from zeep import Client
from zeep.wsse.username import UsernameToken


class SubmitTimeOff(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='submit_time_off',
            description=Component.DESCRIPTION,
            input=SubmitTimeOffInput(),
            output=SubmitTimeOffOutput())

    def run(self, params={}):
        wsdl_url = f"https://{self.connection.environment + '.' if self.connection.environment else ''}" \
                   f"workday.com/ccx/service/{self.connection.tenant}/Absence_Management/v32.0?wsdl"

        client = Client(wsdl_url,
                        wsse=UsernameToken(
                            username=f"{self.connection.username}@{self.connection.tenant}",
                            password=self.connection.password)
                        )

        try:
            client.service.Enter_Time_Off(Enter_Time_Off_Data={
                'Worker_Reference': {
                    'ID': {
                        'type': 'Employee_ID',
                        '_value_1': f"{params[Input.EMPLOYEE_ID]}"
                    }
                },
                'Enter_Time_Off_Entry_Data': {
                    'Date': f"{params[Input.DATE]}",
                    'Requested': f"{params[Input.DAYS]}",
                    'Time_Off_Type_Reference': {
                        'ID': {
                            'type': 'Time_Off_Type_ID',
                            '_value_1': f"{params[Input.TIME_OFF_TYPE]}"
                        }
                    },
                    'Comment': f"{params[Input.COMMENT]}"
                }
            })
            return True
        except Exception:
            return {Output.SUCCESS: False}
