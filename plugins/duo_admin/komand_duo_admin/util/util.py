from datetime import datetime
from logging import getLevelName


class Utils:
    @staticmethod
    def convert_epoch_to_readable(epoch_time: float) -> str:
        return datetime.utcfromtimestamp(epoch_time).strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_log_level(log_level: str) -> int:
        """
        To allow komand-props to make sense to the developer swap the intended debug vs info mode to our loggers to be
        flipped. This is because our plugins set the level to be INFO meaning only that level is returned from the
        container. When the value "debug" is specified in komand-props it means we want debug mode enabled -> therefore
        we want to turn these debug logs into "INGO" to be output.
        :param log_level: string of either info / debug to enable enhanced logging.
        :return: integer value to pass to self.logger.log()
        """

        log_level_mappings = {
            "INFO": "DEBUG",  # we want to keep logging to a minimal so don't print our debug logs
            "DEBUG": "INFO",  # we want to change loggers in this task to be of type "info" and included for traceability
        }

        return getLevelName(log_level_mappings.get(log_level.upper()))
