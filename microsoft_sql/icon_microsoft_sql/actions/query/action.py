import pyodbc as pyodbc

import komand
from .schema import QueryInput, QueryOutput, Input, Output, Component
from komand.exceptions import PluginException
# Custom imports below
from icon_microsoft_sql.util import db_exception
from pyodbc import Error
import datetime
import uuid


class Query(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='query',
                description=Component.DESCRIPTION,
                input=QueryInput(),
                output=QueryOutput())

    def run(self, params={}):
        query = params.get(Input.QUERY)
        parameters = params.get(Input.PARAMETERS)
        if not parameters:
            parameters = []
        cursor = self.connection.cnxn.cursor()

        parameter_tuple = tuple([value for param in parameters for value in param.values()])

        try:
            if parameters:
                cursor.execute(query, parameter_tuple)
            else:
                cursor.execute(query)
        except Error as e:
            self.connection.cnxn.rollback()
            self.connection.cnxn.close()
            db_exception.handle_exceptions(e, query)

        try:
            rows = cursor.fetchall()
            headers = cursor.description
        except pyodbc.ProgrammingError:
            rows = []
            headers = []

        self.connection.cnxn.commit()
        self.connection.cnxn.close()

        header_list = list()
        for name in headers:
            if len(name) > 0:
                header_list.append(name[0])
            else:
                raise PluginException(
                    cause='One or more columns in the selected table was not correctly configured.',
                    assistance='Please check that the table has been constructed properly.',
                    data=headers)

        row_list = []
        for row in rows:
            temp_dic = dict()
            for idx, item in enumerate(row):
                if isinstance(item, datetime.date):
                    item = item.strftime("%Y-%m-%d")
                if isinstance(item, datetime.time):
                    item = item.strftime("%H-%M-%s")
                if isinstance(item, datetime.datetime):
                    item = item.strftime("%Y-%m-%dT%H-%M-%S")
                if isinstance(item, uuid.UUID):
                    item = str(item)
                temp_dic[header_list[idx]] = item
            row_list.append(temp_dic)

        return {Output.HEADER: header_list, Output.RESULTS: row_list}
