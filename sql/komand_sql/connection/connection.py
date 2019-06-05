import komand
from .schema import ConnectionSchema
import sqlalchemy
from sqlalchemy.orm import sessionmaker


class SQLConnection(object):
    """SQLAlchemy database connection"""

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.session = None

    def __enter__(self):
        engine = sqlalchemy.create_engine(self.connection_string)
        Session = sessionmaker()
        self.session = Session(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.conn_str = None
        self.params = None
        self.connection = None

    def postgres_conn_string(self, params):
        self.logger.info('Using postgres connection string...')
        port = params.get("port", "")
        params['port'] = port if port != "" else 5432
        return "{type}://{user}:{password}@{host}:{port}/{db}".format(**params)

    def mssql_conn_string(self, params):
        self.logger.info('Using default connection string...')
        connection_string = "{type}+pymssql://{user}:{password}@{host}:{port}/{db}".format(**params)
        return connection_string

    def default_conn_string(self, params):
        self.logger.info('Using default connection string...')
        return "{type}+mxodbc://{user}:{password}@{host}:{port}/{db}".format(**params)

    def connect(self, params={}):
        username = params['credentials']['username']
        password = params['credentials']['password']
        del params['credentials']
        self.params = params
        self.params['user'] = username
        self.params['password'] = password
        
        type_connection_string = {
            'postgresql': Connection.postgres_conn_string,
            'postgres': Connection.postgres_conn_string,
            'mssql': Connection.mssql_conn_string,
            'MSSQL': Connection.mssql_conn_string
        }

        type = params.get("type", "unknown").lower()
        self.conn_str = type_connection_string.get(type, Connection.default_conn_string)(self, params)
        self.connection = SQLConnection(self.conn_str)
        self.connection.__enter__()
        self.logger.info("Connect: Connecting...")

    def test(self):
        session = self.connection.session
        if session:
            return {"status": "operation success"}
        else:
            raise Exception("Connection was not active. Please check your connection settings.")