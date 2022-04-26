import os.path

from komand_paloalto_wildfire.util.constants import SUPPORTED_FILES


class Utils:
    @staticmethod
    def check_link_for_supported_file_type(url: str) -> bool:
        filename = os.path.basename(url)
        return filename.lower().endswith(SUPPORTED_FILES)
