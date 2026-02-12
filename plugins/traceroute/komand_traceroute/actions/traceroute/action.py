import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import TracerouteInput, TracerouteOutput

# Custom imports below
import subprocess  # noqa: B404
import re


class Traceroute(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="traceroute",
            description="Traceroute to a host returns the route used to comunicate with the host",
            input=TracerouteInput(),
            output=TracerouteOutput(),
        )

    def run(self, params={}):
        host = self._validate_host(params.get("host"))
        count, max_ttl, time_out, set_ack, resolve_hostname, port = self._get_inputs(params)

        cmd = ["tcptraceroute", "-m", f"{max_ttl}", "-q", f"{count}", "-w", f"{time_out}", host, f"{port}"]
        if set_ack:
            cmd.insert(-2, "-A")
        if not resolve_hostname:
            cmd.insert(1, "-n")

        with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as response:  # nosec B603
            (output, err) = response.communicate()
            output = output.decode("utf-8")
            err = err.decode("utf-8")
            resp_code = response.returncode
            self.logger.info("Standard Error: %s", err)

        if resp_code != 0:
            self.logger.error(f"Received a non-zero exit code, please see error. status_code={resp_code}")
            raise PluginException(
                preset=PluginException.Preset.UNKNOWN, data=f"Return code={resp_code}, output={output}, error={err}"
            )

        try:
            ip, path = [], [p.lstrip(" ") for p in output.splitlines()]
            ip = re.findall(r"\d*\.\d*\.\d*\.\d*", output)

            if not ip:
                self.logger.error("No IP addresses found in the output.")
                raise PluginException(
                    cause="Unable to find any IP addresses in the output.",
                    assistance="Please check output of traceroute command.",
                    data=output,
                )

            # if the work open found it means the final IP address responded.
            reply = re.search(r"open", output) is not None
            return {"reply": reply, "response": output, "path": path, "ip": ip}
        except:
            self.logger.error("Unexpected error occurred while parsing output.")
            raise PluginException(
                cause=PluginException.Preset.UNKNOWN,
                data=f"Return code={resp_code}, output={output}, error={err}",
            )

    @staticmethod
    def _validate_host(host: str):
        if not re.match(r"^[a-zA-Z0-9][a-zA-Z0-9\-\.]+$", host):
            raise PluginException(
                cause="Invalid hostname format, please check input.",
                assistance="Hostname can only contain alphanumeric characters, hyphens, and dots.",
                data=f"Supplied hostname: {host}",
            )
        return host

    @staticmethod
    def _get_inputs(params: dict) -> tuple[int, int, int, bool, bool, int]:
        # ensure customer hasn't provided a zero value for these inputs
        count = params.get("count")
        max_ttl = params.get("max_ttl")
        time_out = params.get("time_out")

        if count == 0:
            count = 3
        if max_ttl == 0:
            max_ttl = 30
        if time_out == 0:
            time_out = 3

        set_ack = params.get("set_ack")
        resolve_hostname = params.get("resolve_hostname")

        port = params.get("port")
        if port < 1 or port > 65535:
            port = 80

        return count, max_ttl, time_out, set_ack, resolve_hostname, port
