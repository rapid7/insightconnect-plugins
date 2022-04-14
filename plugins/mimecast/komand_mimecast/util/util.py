from komand_mimecast.util.constants import BASE_HOSTNAME_MAP, DEFAULT_REGION


class Utils:
    @staticmethod
    def prepare_base_url(region: str = DEFAULT_REGION) -> str:
        return f"https://{BASE_HOSTNAME_MAP.get(region)}.mimecast.com"

    @staticmethod
    def normalize(key: str, value: str) -> dict:
        if "_" not in key:
            if value  and value != "none":
                return {key: value}
            return {}

        chunks = list(filter(lambda c: len(c), key.split("_")))

        for i in range(1, len(chunks)):
            chunks[i] = chunks[i].capitalize()
        if value and value != "none":
            return {"".join(chunks): value}
        return {}
