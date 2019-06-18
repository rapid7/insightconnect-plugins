import komand
from .schema import RunInput, RunOutput
# Custom imports below
import base64
import binascii


class Run(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='run',
                description='Run p0f on a PCAP',
                input=RunInput(),
                output=RunOutput())

    def run(self, params={}):
        _file = params.get('file').encode('UTF-8')

        # Verify string is base64
        try:
            base64.decodestring(_file)
        except binascii.Error:
            self.logger.error('Error: Invalid Base64 string')
            raise


        # Set file path to store file
        dir = "/tmp"
        file_name = "p0f.pcap"
        full_path = "%s/%s" % (dir, file_name)

        # Set variables needed when calling p0f
        binary = "/usr/sbin/p0f"
        cmd = "%s -s %s -tlv" % (binary, full_path)

        # Decode bas64 string and write to file
        with open(full_path, "wb") as fh:
            fh.write(base64.decodestring(_file))

        r = komand.helper.exec_command(cmd)
        encoded = r['stdout']
        encoded_split = encoded.splitlines(True)
        traffic = [i.decode('UTF-8').rstrip() for i in encoded_split]

        return {'traffic': traffic}

    def test(self):
        _file = "1MOyoQIABAAAAAAAAAAAAP//AAABAAAAfAFSWLu4BwBKAAAASgAAAAgAJ/3K6wgAJ07ZOQgARQAAPEfLQABABtroCgECBAoBAgOD8QBQL1y2bwAAAACgAnIQYcoAAAIEBbQEAggKAGvxpAAAAAABAwMHfAFSWO+4BwBKAAAASgAAAAgAJ07ZOQgAJ/3K6wgARQAAPAAAQABABiK0CgECAwoBAgQAUIPxtfoCHS9ctnCgEnEgGDcAAAIEBbQEAggKAHhDcABr8aQBAwMHfAFSWFm6BwBCAAAAQgAAAAgAJ/3K6wgAJ07ZOQgARQAANEfMQABABtrvCgECBAoBAgOD8QBQL1y2cLX6Ah6AEADlBbEAAAEBCAoAa/GkAHhDcHwBUlhrugcAkgAAAJIAAAAIACf9yusIACdO2TkIAEUAAIRHzUAAQAbangoBAgQKAQIDg/EAUC9ctnC1+gIegBgA5VkiAAABAQgKAGvxpQB4Q3BHRVQgL3Rlc3QuemlwIEhUVFAvMS4xDQpVc2VyLUFnZW50OiBjdXJsLzcuMzUuMA0KSG9zdDogMTAuMS4yLjMNCkFjY2VwdDogKi8qDQoNCnwBUlhrugcAQgAAAEIAAAAIACdO2TkIACf9yusIAEUAADRBbkAAQAbhTQoBAgMKAQIEAFCD8bX6Ah4vXLbAgBAA4xgvAAABAQgKAHhDcABr8aV8AVJYI74HAPABAADwAQAACAAnTtk5CAAn/crrCABFAAHiQW9AAEAG354KAQIDCgECBABQg/G1+gIeL1y2wIAYAOMZ3QAAAQEICgB4Q3EAa/GlSFRUUC8xLjEgMjAwIE9LDQpEYXRlOiBUaHUsIDE1IERlYyAyMDE2IDAyOjM1OjQwIEdNVA0KU2VydmVyOiBBcGFjaGUvMi40LjcgKFVidW50dSkNCkxhc3QtTW9kaWZpZWQ6IFdlZCwgMTQgRGVjIDIwMTYgMTg6NDQ6MDEgR01UDQpFVGFnOiAiYzUtNTQzYTJiODZhOWMyMCINCkFjY2VwdC1SYW5nZXM6IGJ5dGVzDQpDb250ZW50LUxlbmd0aDogMTk3DQpDb250ZW50LVR5cGU6IGFwcGxpY2F0aW9uL3ppcA0KDQpQSwMECgAAAAAAE5WOSbFVXfQfAAAAHwAAAAgAHAB0ZXN0LnR4dFVUCQADJZJRWCWSUVh1eAsAAQQAAAAABAAAAAB0aGlzIGlzIGEgdGVzdCBmb3IgY2hhb3NyZWFkZXIKUEsBAh4DCgAAAAAAE5WOSbFVXfQfAAAAHwAAAAgAGAAAAAAAAQAAAKSBAAAAAHRlc3QudHh0VVQFAAMlklFYdXgLAAEEAAAAAAQAAAAAUEsFBgAAAAABAAEATgAAAGEAAAAAAHwBUlj+vgcAQgAAAEIAAAAIACf9yusIACdO2TkIAEUAADRHzkAAQAba7QoBAgQKAQIDg/EAUC9ctsC1+gPMgBAA7QOpAAABAQgKAGvxpQB4Q3F8AVJY08kHAEIAAABCAAAACAAn/crrCAAnTtk5CABFAAA0R89AAEAG2uwKAQIECgECA4PxAFAvXLbAtfoDzIARAO0DqAAAAQEICgBr8aUAeENxfAFSWGjKBwBCAAAAQgAAAAgAJ07ZOQgAJ/3K6wgARQAANEFwQABABuFLCgECAwoBAgQAUIPxtfoDzC9ctsGAEQDjGC8AAAEBCAoAeENxAGvxpXwBUlheywcAQgAAAEIAAAAIACf9yusIACdO2TkIAEUAADRH0EAAQAba6woBAgQKAQIDg/EAUC9ctsG1+gPNgBAA7QOmAAABAQgKAGvxpgB4Q3E=".encode('UTF-8')

        # Set file path to store file
        dir = "/tmp"
        file_name = "p0f.pcap"
        full_path = "%s/%s" % (dir, file_name)

        # Decode bas64 string and write to file
        with open(full_path, "wb") as fh:
            fh.write(base64.decodestring(_file))

        # Set variables needed when calling p0f
        binary = "/usr/sbin/p0f"
        cmd = "%s -s %s"  % (binary, full_path)
        r = komand.helper.exec_command(cmd)

        # Test if p0f was successful
        if r['rcode'] != 0:
            raise Exception('p0f returned with non-zero status')

        return {}
