import komand
from .schema import LookupHashInput, LookupHashOutput


# Custom imports below


class LookupHash(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_hash",
            description="Lookup By Hash",
            input=LookupHashInput(),
            output=LookupHashOutput(),
        )

    def normalize(self, result):
        formatted = {"found": False, "threatscore": 0, "reports": []}
        if result.get("response_code"):
            return formatted

        response = result.get("response", [])
        if result and len(response) > 0:
            formatted["found"] = True
            formatted["reports"] = response
            if response and isinstance(response, list) and response[0] and isinstance(response[0], dict):
                formatted["threatscore"] = response[0].get("threatscore")
            else:
                formatted["threatscore"] = 0

        return formatted

    def lookup(self, hash_=""):
        r = self.connection.get(hash_)
        if r.status_code == 200:
            results = r.json()
            self.logger.debug("Got results %s", results)
            return self.normalize(results)
        return {"found": False, "threatscore": 0, "reports": []}

    def run(self, params={}):
        """Run action"""
        return self.lookup(params["hash"])
