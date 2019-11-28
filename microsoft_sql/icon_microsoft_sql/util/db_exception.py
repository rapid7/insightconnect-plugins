import pyodbc
from komand.exceptions import PluginException


def handle_exceptions(e: pyodbc.Error, query: str):
    """
    This method takes a pyodbc.Error object and raises a specific error type Along with appropriate messaging
    :param e: A pyodbc.Error object to be raised and give context
    :param query: The query that the plugin attempted to run
    """
    _ASSISTANCE = 'Double-check the query string and refer to the error code for additional information.'
    _DATA = f'Error code: {e}\nQuery string: {query}'

    cause = {pyodbc.OperationalError: 'An operational error occurred. This can be related to the database\'s operation'
                                      ' and not necessarily under the control of the programmer, e.g. an unexpected disconnect occurs,'
                                      ' the data source name is not found, a transaction could not be processed,'
                                      ' a memory allocation error occurred during processing, etc.',
             pyodbc.ProgrammingError: 'A programing error occurred. This can be caused by \'table not found\' or \'already exists\','
                                      ' syntax error in the SQL statement, wrong number of parameters specified, etc.',
             pyodbc.DataError: 'A data error occurred. This can be caused by problems with the processed data such as division by zero,'
                               ' numeric value out of range, etc.',
             pyodbc.IntegrityError: 'An integrity error occurred. This can happen'
                                    ' when the relational integrity of the database is affected, e.g. a foreign key check fails.',
             pyodbc.InternalError: 'An internal error occurred. This can be caused when the database encounters an internal error, e.g. the '
                                   'cursor is invalid, the transaction is out of sync, etc.',
             pyodbc.NotSupportedError: 'A \'not supported\' error occurred. This can be caused by a method or database API was used'
                                       ' which is not supported by the database, e.g.'
                                       ' requesting a .rollback() on a connection that does not support transactions or has transactions turned off.',
             pyodbc.InterfaceError: 'An interface error occurred. This is an error related to the database interface rather than the database itself.'}

    raise PluginException(cause=cause[type(e)],
                          assistance=_ASSISTANCE,
                          data=_DATA)
