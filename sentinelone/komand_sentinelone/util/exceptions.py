from komand.exceptions import ConnectionTestException


class PluginException(ConnectionTestException):

    def __str__(self):
        return "An error occurred during plugin execution!\n\n{cause} {assistance}".format(
            cause=self.cause,
            assistance=self.assistance
        )
