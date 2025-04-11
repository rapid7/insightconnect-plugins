import os
from logging import Logger


class CacheFileManager:
    def __init__(self, logging: Logger, cache_file: str, append: bool = False):
        self.logging = logging
        self.append = append
        self.cache_dir = "/workspace/cache"
        self.file = None
        self.cache_file = cache_file

        if self.cache_dir not in self.cache_file:
            self.cache_file = os.path.join(self.cache_dir, self.cache_file)

        # Create the necessary directory if not exist
        cache_file_dir = os.path.dirname(self.cache_file)
        if not os.path.isdir(cache_file_dir):
            os.makedirs(cache_file_dir)

    def __enter__(self):
        mode = "a+" if self.append else "r+"

        if os.path.isfile(self.cache_file):
            self.file = open(self.cache_file, mode, encoding="utf-8")
            self.logging.info(f"Opened cache file {self.cache_file}")
        else:
            self.file = open(self.cache_file, "w+", encoding="utf-8")  # Open once to create the cache file
            self.file.close()
            self.logging.info(f"Cache file created {self.cache_file}")
            self.file = open(self.cache_file, mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
