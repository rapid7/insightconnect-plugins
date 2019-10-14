import komand
from .schema import ConnectionSchema, Input
from komand.exceptions import ConnectionTestException
# Custom imports below
import pyodbc


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        server = params.get(Input.HOST)
        user = params.get(Input.CREDENTIALS).get('username')
        password = params.get(Input.CREDENTIALS).get('password')
        db = params.get(Input.DB)
        port = params.get(Input.PORT)
        if port:
            server = f'{server},{port}'

        try:
            self.cnxn = pyodbc.connect(DRIVER='ODBC Driver 17 for SQL Server', SERVER=server, DATABASE=db, UID=user, PWD=password)
        except pyodbc.OperationalError as e:
            raise ConnectionTestException(cause='An error occurred when trying to log into the MSQSL database.',
                                          assistance='Ensure the connection information is correct and see the error data for more information.',
                                          data=e)

    def test(self):
        cursor = self.cnxn.cursor()
        self.cnxn.close()
        return {'Connection': 'Successful'}
