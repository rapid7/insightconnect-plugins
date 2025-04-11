from paramiko import MissingHostKeyPolicy, PKey, SSHClient


class CustomMissingKeyPolicy(MissingHostKeyPolicy):
    def missing_host_key(self, client: SSHClient, hostname: str, key: PKey) -> None:
        client.get_host_keys().add(hostname, key.get_name(), key)
