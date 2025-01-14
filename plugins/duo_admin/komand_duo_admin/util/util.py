from datetime import datetime


class Utils:
    @staticmethod
    def convert_epoch_to_readable(epoch_time: float) -> str:
        return datetime.utcfromtimestamp(epoch_time).strftime("%Y-%m-%d %H:%M:%S")
