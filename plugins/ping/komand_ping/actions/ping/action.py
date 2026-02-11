import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

import subprocess  # noqa: B404
import re
import ipaddress
import unicodedata

from .schema import PingInput, PingOutput


class Ping(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ping",
            description="Ping a host to check for connectivity",
            input=PingInput(),
            output=PingOutput(),
        )

    # pylint: disable=too-many-branches,too-many-statements
    def run(self, params={}):  # noqa: MC0001
        host = self._validate_host(params.get("host"))
        count = params.get("count")
        resolve_hostname = params.get("resolve_hostname")

        if count == 0:
            count = 4
        count = str(count)

        # build command with appropriate options
        cmd = ["ping", "-c", count]
        if not resolve_hostname:
            cmd.append("-n")
        cmd.append(host)

        try:
            result = subprocess.run(  # nosec B603 - cmd is an argv list (shell=False) and `host` is validated in _validate_host()
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=60,
                check=False,
            )
            output, err = result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            raise PluginException(cause="Ping timed out.", assistance="Check network connectivity.")
        except Exception as error:
            self.logger.error(f"Ping execution failed: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

        if result.returncode == 0:
            try:
                temp = re.search(r"\d* packets t", output)
                sub = temp.group()
                transmitted = sub[:-10]
                transmitted = int(transmitted)
            except AttributeError:
                self.logger.error("The regular expression search for transmitted packets failed")
                self.logger.error("Standard Output: %s", output)
                raise PluginException(cause="An AttributeError occurred.", assistance="Please see log for details.")
            except ValueError:
                self.logger.error(f"The transmitted packets value is not valid. The value was {transmitted}")
                self.logger.error(f"Standard Output: {output}")
                raise PluginException(cause="A ValueError occurred.", assistance="Please see log for details.")
            except:
                self.logger.error(f"Standard Output: {output}")
                self.logger.error(f"Return form regex {temp}")
                self.logger.error(f"Substring built by regex {sub}")
                raise PluginException(preset=PluginException.Preset.UNKNOWN, assistance="Please see log for details.")

            try:
                temp = re.search(r"\d* packets r", output)
                if temp is None:
                    temp = re.search(r"\d* received", output)
                    sub = temp.group()
                    received = sub[:-9]
                else:
                    sub = temp.group()
                    received = sub[:-10]
                received = int(received)
            except AttributeError:
                self.logger.error("The regular expression search for received packets failed")
                self.logger.error("Standard Output: %s", output)
                raise PluginException(cause="An AttributeError occurred.", assistance="Please see log for details.")
            except ValueError:
                self.logger.error("The received packets value is not valid. The value was %s", received)
                self.logger.error("Standard Output: %s", output)
                raise PluginException(cause="A ValueError occurred.", assistance="Please see log for details.")
            except:
                self.logger.error("Standard Output: %s", output)
                self.logger.error("Return form regex %s", temp)
                self.logger.error("Substring built by regex %s", sub)
                raise PluginException(preset=PluginException.Preset.UNKNOWN, assistance="Please see log for details.")

            packet_loss = None
            try:
                temp = re.search(r"received.* packet loss", output)
                sub = temp.group()
                sub = sub[:-13]
                sub = sub[10:]
                packet_loss = float(sub)
            except AttributeError:
                self.logger.error("The regular expression search for % packet loss failed")
                self.logger.error("Standard Output: %s", output)
                raise PluginException(cause="An AttributeError occurred.", assistance="Please see log for details.")
            except ValueError:
                self.logger.error("The % packet loss value is not valid. The value was %s", packet_loss)
                self.logger.error("Standard Output: %s", output)
                raise PluginException(cause="A ValueError occurred.", assistance="Please see log for details.")
            except:
                self.logger.error("Standard Output: %s", output)
                self.logger.error("return form regex %s", temp)
                self.logger.error("substring built by regex %s", sub)
                raise PluginException(preset=PluginException.Preset.UNKNOWN, assistance="Please see log for details.")

            try:
                temp = re.search(r"mdev.*", output)
                sub = temp.group()
                sub = sub[7:]
                sub = sub[:-3]
                values = sub.split("/")
                if sub == "":
                    self.logger.error("Standard Output: %s", output)
                    self.logger.error("Return form regex %s", temp)
                    raise PluginException(
                        cause="The value for average latency was not found.",
                        assistance="Please see log for details.",
                    )
                try:
                    average_latency = values[1] + "ms"
                    minimum_latency = values[0] + "ms"
                    maximum_latency = values[2] + "ms"
                    standard_deviation = values[3] + "ms"
                except IndexError:
                    self.logger.error(f"Failed to find min avg max and mdev {sub}")

            except AttributeError:
                self.logger.error("The regular expression search for average latency failed")
                self.logger.error("Standard Output: %s", output)
                raise PluginException(cause="An AttributeError occurred.", assistance="Please see log for details.")
            except:
                self.logger.error("Standard Output: %s", output)
                self.logger.error("Return form regex %s", temp)
                self.logger.error("Substring built by regex %s", sub)
                raise PluginException(preset=PluginException.Preset.UNKNOWN, assistance="Please see log for details.")

            return {
                "reply": True,
                "response": output,
                "packets_percent_lost": packet_loss,
                "average_latency": average_latency,
                "packets_transmitted": transmitted,
                "packets_received": received,
                "minimum_latency": minimum_latency,
                "maximum_latency": maximum_latency,
                "standard_deviation": standard_deviation,
            }
        elif result.returncode < 3:
            return {"reply": False, "response": output}
        else:
            self.logger.error("Standard Output: %s", output)
            self.logger.error("Standard Error: %s", err)
            raise PluginException(preset=PluginException.Preset.UNKNOWN, assistance="Please see log for details.")

    @staticmethod
    def _validate_host(host: str) -> str:  # noqa: MC0001
        """
        Validate user-supplied host. Allow FQDN hostnames and IP addresses, but disallow:
        - empty values
        - any whitespace/control characters
        - values starting with '-' (could be interpreted as ping options)

        Returns the stripped host.
        """
        if host is None:
            raise PluginException(cause="Host is required.", assistance="Provide a hostname or IP address.")

        host = str(host).strip()
        if not host:
            raise PluginException(cause="Host is required.", assistance="Provide a hostname or IP address.")

        if host.startswith("-"):
            raise PluginException(
                cause="Invalid host value.",
                assistance="Host must not start with '-' (it can be interpreted as a command-line option).",
            )

        # Disallow any whitespace/control characters
        for ch in host:
            if ch.isspace() or unicodedata.category(ch)[0] == "C":
                raise PluginException(
                    cause="Invalid host value.",
                    assistance="Host must not contain whitespace or control characters.",
                )

        # If it's an IP address, ensure that it is valid
        try:
            ipaddress.ip_address(host)
            return host
        except ValueError:
            pass

        # Validate hostname: must be 1-253 chars, consist of letters, digits, hyphens, and dots
        if not re.fullmatch(r"[A-Za-z0-9._-]{1,253}", host):
            raise PluginException(
                cause="Invalid host value.",
                assistance="Host must be a valid hostname or IP address.",
            )

        # Validate each label: must not start/end with hyphen, and must be 1-63 chars.
        for label in host.split("."):
            if not label:
                continue  # Allow trailing dot (FQDN)
            if len(label) > 63:
                raise PluginException(
                    cause="Invalid host value.",
                    assistance="Hostname labels must be 63 characters or less.",
                )
            if label.startswith("-") or label.endswith("-"):
                raise PluginException(
                    cause="Invalid host value.",
                    assistance="Hostname labels must not start or end with a hyphen.",
                )

        return host
