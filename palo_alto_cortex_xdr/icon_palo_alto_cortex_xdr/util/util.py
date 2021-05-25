import time


class Util:
    @staticmethod
    def now_ms():
        # Return the current epoch time in ms
        return int(time.time() * 1000)
