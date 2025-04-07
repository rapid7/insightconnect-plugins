import insightconnect_plugin_runtime
from .schema import (
    ThreatsFetchFileInput,
    ThreatsFetchFileOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from datetime import datetime


class ThreatsFetchFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="threats_fetch_file",
            description=Component.DESCRIPTION,
            input=ThreatsFetchFileInput(),
            output=ThreatsFetchFileOutput(),
        )

    def run(self, params={}):
        threat_id = params.get(Input.ID)
        password = params.get(Input.PASSWORD)

        if len(password) <= 10 or " " in password:
            raise PluginException(
                cause="Wrong password.",
                assistance="Password must have more than 10 characters and cannot contain whitespace.",
            )
        self.connection.client.check_if_threats_exist([threat_id])

        fetch_date = f"{datetime.utcnow().isoformat()}Z"
        self.connection.client.threats_fetch_file(params.get(Input.PASSWORD), {"ids": [threat_id]})

        return {Output.FILE: self.connection.client.download_file({"threatIds": threat_id}, fetch_date, password)}
