import time


class Util:

    @staticmethod
    def now_ms():
        return int(time.time() * 1000)
