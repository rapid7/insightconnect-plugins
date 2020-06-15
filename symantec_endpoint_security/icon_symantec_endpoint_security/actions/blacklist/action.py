import insightconnect_plugin_runtime
from .schema import BlacklistInput, BlacklistOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import re
from icon_symantec_endpoint_security.util.api import APIException, HashType


class Blacklist(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='blacklist',
                description=Component.DESCRIPTION,
                input=BlacklistInput(),
                output=BlacklistOutput())

    def run(self, params={}):
        bl_name = params.get(Input.NAME)
        bl_desc = params.get(Input.DESCRIPTION)
        domain_id = params.get(Input.DOMAIN_ID)
        hashes = params.get(Input.HASHES)

        if not hashes:
            raise PluginException(cause="At least one hash must be provided for the blacklist!",
                                  assistance="Ensure at least one hash is provided as step input.")

        # Verify hashes are of the same type
        self._verify_hash_input(hashes=hashes)

        # Get the hash type
        hash_type = self._is_md5_or_sha256(hashes[0])

        try:
            self.connection.api_client.blacklist_file(blacklist_data=hashes,
                                                      blacklist_description=bl_desc,
                                                      domain_id=domain_id,
                                                      hash_type=hash_type,
                                                      name=bl_name)
        except APIException as e:
            raise PluginException(cause="An error occurred while attempting to blacklist hashes!",
                                  assistance=e.message)

        return {Output.BLACKLIST_ID}

    def _verify_hash_input(self, hashes: [str]) -> None:
        """
        Checks if multiple types of hashes have been provided as input. If multiple types are found an exception will
        be raised.
        :param hashes: Hashes input
        :return: None
        """
        if len(set(filter(self._is_md5_or_sha256, hashes))) > 1:
            raise PluginException(cause="Multiple types of hashes were found in the hashes input!",
                                  assistance="Only one type of hash can be provided in the hashes input per step."
                                             "Ensure only MD5 or only SHA256 hashes are being used as input.")

    @staticmethod
    def _is_md5_or_sha256(hash_: str) -> HashType:
        """
        Determines whether or not a hash is MD5 or SHA256
        :param hash_: Hash input by the user
        :return: HashType indicating the type of the hash
        """

        if re.match(r"^[a-zA-Z0-9]{32}$", hash_):
            return HashType.md5
        elif re.match(r"^[a-zA-Z0-9]{64}$", hash_):
            return HashType.sha256
        else:
            raise PluginException(cause=f"The hash {hash_} provided as input to the action was not an allowed type "
                                        f"by Symantec Endpoint Protection!",
                                  assistance="Ensure only MD5 or SHA256 hashes are provided to this action.")
