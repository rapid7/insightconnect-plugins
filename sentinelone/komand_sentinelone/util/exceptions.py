from komand.exceptions import ConnectionTestException


# -*- coding: utf-8 -*-
class PluginException(ConnectionTestException):

    def __str__(self):
        return "An error occurred during plugin execution!\n\n{cause} {assistance}".format(
            cause=self.cause,
            assistance=self.assistance
        )
