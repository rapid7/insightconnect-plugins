import komand
from .schema import ConnectionSchema
# Custom imports below
import ftplib
import ftputil.session


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        host = params.get('host')
        username = params.get('credentials').get('username', 'anonymous')
        password = params.get('credentials').get('password', 'test@test.com')
        # Use secure mode?
        secure = params.get('secure', False)
        # Use passive mode?
        passive = params.get('passive', False)

        # Either ftplib.FTP or ftplib.FTP_TLS
        base_ftp_class = ftplib.FTP
        if secure:
            base_ftp_class = ftplib.FTP_TLS
        my_session_factory = ftputil.session.session_factory(
            base_class=base_ftp_class,
            use_passive_mode=passive)
        try:
            self.ftp_host = ftputil.FTPHost(host, username,
                                            password, session_factory=my_session_factory)
        except ftputil.error.PermanentError as e:
            raise e

