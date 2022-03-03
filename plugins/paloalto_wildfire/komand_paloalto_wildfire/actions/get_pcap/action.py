# Custom imports below
import base64

import insightconnect_plugin_runtime

from .schema import GetPcapInput, GetPcapOutput, Input, Output


class GetPcap(insightconnect_plugin_runtime.Action):
    platform = {
        "Windows XP, Adobe Reader 9.3.3, Office 2003": 1,
        "Windows XP, Adobe Reader 9.4.0, Flash 10, Office 2007": 2,
        "Windows XP, Adobe Reader 11, Flash 11, Office 2010": 3,
        "Windows 7 32‐bit, Adobe Reader 11, Flash 11, Office 2010": 4,
        "Windows 7 64bit, Adobe Reader 11, Flash 11, Office 2010": 5,
        "Mac OS X Mountain Lion": 50,
        "Android 2.3, API 10, avd2.3.1": 201,
    }

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_pcap",
            description="Query for a PCAP",
            input=GetPcapInput(),
            output=GetPcapOutput(),
        )

    def run(self, params={}):
        return {
            Output.FILE: base64.b64encode(
                self.connection.client.get_pcap(
                    params.get(Input.HASH), platform=self.platform.get(params.get(Input.PLATFORM))
                )
            ).decode()
        }
