import json
import paramiko
import base64
import grpc
import io
import time
from pyvelociraptor import api_pb2
from pyvelociraptor import api_pb2_grpc
import insightconnect_plugin_runtime
from .schema import RunInput, RunOutput, Input, Output, Component
# Custom imports below


class Run(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="run",
                description=Component.DESCRIPTION,
                input=RunInput(),
                output=RunOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        # TODO - If input bindings for connection can be done check to same if it you can do the same here
        """Runs a VQL query against the Velociraptor server.

        Args:
            config: A dictionary containing the configuration parameters for the Velociraptor server.
            query: The VQL query to run.

        Returns:
            A tuple containing the query, the response, and the query execution logs.
        """
        results = {}
        try:
            # Fill in the SSL params from the api_client config file. You can get such a file:
            # velociraptor --config server.config.yaml config api_client > api_client.conf.yaml
            api_connection_string = self.connection.api_connection_string
            root_certificates_decoded = self.connection.root_certificates_decoded
            private_key_decoded = self.connection.private_key_decoded
            certificate_chain_decoded = self.connection.certificate_chain_decoded
            query = params.get(Input.COMMAND)
            creds = grpc.ssl_channel_credentials(
            root_certificates = root_certificates_decoded,
            private_key = private_key_decoded,
            certificate_chain = certificate_chain_decoded)
            # This option is required to connect to the grpc server by IP - we
            # use self signed certs.
            options = (('grpc.ssl_target_name_override', "VelociraptorServer",),)
            # The first step is to open a gRPC channel to the server..
            with grpc.secure_channel(api_connection_string,
                                    creds, options) as channel:
                stub = api_pb2_grpc.APIStub(channel)
                                # The request consists of one or more VQL queries. Note that you can collect artifacts by simply naming them using the
                # "Artifact" plugin.
                request = api_pb2.VQLCollectorArgs(
                    max_wait=1,
                    max_row=100,
                    Query=[api_pb2.VQLRequest(
                        Name="ICON Plugin Request",
                        VQL=query,
                    )],
                )
                # This will block as responses are streamed from the
                # server. If the query is an event query we will run this loop
                # forever.
                logs_list = []
                for response in stub.Query(request):
                    if response.Response:
                        package = json.loads(response.Response)
                        logs_list.append(package)

                    elif response.log:
                        # Query execution logs are sent in their own messages.
                        package = time.ctime(response.timestamp / 1000000), response.log
            self.logger.info("Command Sent")
            results["logs_list"] = logs_list[0]
            return {Output.RESULTS: results}
        except grpc.RpcError as e:
            self.logger.info("Error: ",e)
            results["logs_list"] = e
            return {Output.RESULTS: results}

