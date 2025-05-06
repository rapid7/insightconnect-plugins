import insightconnect_plugin_runtime
import sqlalchemy
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from sqlalchemy.orm import sessionmaker

from .schema import ConnectionSchema, Input


class SQLConnection(object):
    """SQLAlchemy database connection"""

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.session = None

    def __enter__(self):
        engine = sqlalchemy.create_engine(self.connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.conn_str = None
        self.params = None
        self.connection = None
        self.user = None
        self.password = None
        self.type = None

    def postgres_conn_string(self, params):
        self.logger.info("Using PostgreSQL connection string...")
        params[Input.PORT] = params.get(Input.PORT) or 5432
        return f"postgres://{self.user}:{self.password}@{params[Input.HOST]}:{params[Input.PORT]}/{params[Input.DB]}"

    def mssql_conn_string(self, params):
        self.logger.info("Using MSSQL connection string...")
        params[Input.PORT] = params.get(Input.PORT) or 1433
        return (
            f"mssql+pymssql://{self.user}:{self.password}@{params[Input.HOST]}:{params[Input.PORT]}/{params[Input.DB]}"
        )

    def default_conn_string(self, params):
        self.logger.info("Using MySQL connection string...")
        params[Input.PORT] = params.get(Input.PORT) or 3306
        return (
            f"mysql+mysqldb://{self.user}:{self.password}@{params[Input.HOST]}:{params[Input.PORT]}/{params[Input.DB]}"
        )

    def connect(self, params={}):
        self.user = params.get(Input.CREDENTIALS).get("username")
        self.password = params.get(Input.CREDENTIALS).get("password")
        self.type = params[Input.TYPE]

        del params[Input.CREDENTIALS]

        type_connection_string = {
            "MSSQL": Connection.mssql_conn_string,
            "MySQL": Connection.default_conn_string,
            "PostgreSQL": Connection.postgres_conn_string,
        }

        self.conn_str = type_connection_string.get(params[Input.TYPE])(self, params)

    def test(self):
        with SQLConnection(self.conn_str) as conn:
            try:
                conn.session.execute("select 1")
                return {"status": "Success"}
            except Exception as error:
                raise ConnectionTestException(
                    cause="Unable to connect to the server.",
                    assistance="Check connection credentials.",
                    data=error,
                )
            finally:
                conn.session.close()
