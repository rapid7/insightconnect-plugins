import komand
from .schema import CreateWorkspaceInput, CreateWorkspaceOutput, Component, Input, Output

# Custom imports below
from komand.exceptions import PluginException


class CreateWorkspace(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_workspace',
            description=Component.DESCRIPTION,
            input=CreateWorkspaceInput(),
            output=CreateWorkspaceOutput())

    def run(self, params={}):
        directory_id = params.get(Input.DIRECTORY_ID)
        username = params.get(Input.USERNAME)
        bundle_id = params.get(Input.BUNDLE_ID)
        volume_encryption_key = params.get(Input.VOLUME_ENCRYPTION_KEY)
        user_volume_encryption_enabled = params.get(Input.USER_VOLUME_ENCRYPTION_ENABLED)
        root_volume_encryption_enabled = params.get(Input.ROOT_VOLUME_ENCRYPTION_ENABLED)
        workspace_properties = params.get(Input.WORKSPACE_PROPERTIES)
        tags = params.get(Input.TAGS)
        result = {}

        payload = {
            'DirectoryId': directory_id,
            'UserName': username,
            'BundleId': bundle_id,
            'Tags': tags,
            'WorkspaceProperties': {
                'ComputeTypeName': workspace_properties['compute_type_name'],
                'RootVolumeSizeGib': workspace_properties['root_volume_size'],
                'RunningMode': workspace_properties['running_mode'],
                'RunningModeAutoStopTimeoutInMinutes': workspace_properties['running_mode_auto_stop_time_out'],
                'UserVolumeSizeGib': workspace_properties['user_volume_size']
            }
        }

        if user_volume_encryption_enabled and root_volume_encryption_enabled:
            raise PluginException(cause="Both user and root volume encrypted flags are set.",
                                  assistance="Only one of the encryption flags can be set.")

        if user_volume_encryption_enabled:
            payload['UserVolumeEncryptionEnabled'] = user_volume_encryption_enabled
        if root_volume_encryption_enabled:
            payload['RootVolumeEncryptionEnabled'] = root_volume_encryption_enabled
        if user_volume_encryption_enabled or root_volume_encryption_enabled:
            if volume_encryption_key:
                payload['VolumeEncryptionKey'] = volume_encryption_key
            else:
                raise PluginException(cause="Invalid value for Volume Encryption Key input.",
                                      assistance='Please provide a valid value for the input.')

        try:
            result = self.connection.aws.client('workspaces').create_workspaces(Workspaces=[payload])
        except:
            raise PluginException(cause="An unknown error occurred",
                                  data=result)

        try:
            if result['FailedRequests']:
                raise PluginException(cause=result['FailedRequests'][0].get('ErrorCode'),
                                      assistance=result['FailedRequests'][0].get('ErrorMessage'),
                                      data=result)
        except KeyError:
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=result)

        try:
            if result['PendingRequests'][0].get('ErrorCode'):
                raise PluginException(cause=result['PendingRequests'][0].get('ErrorCode'),
                                      assistance=result['PendingRequests'][0].get('ErrorMessage'),
                                      data=result)
            else:
                result = {'id': result['PendingRequests'][0].get('WorkspaceId'),
                          'state': result['PendingRequests'][0].get('State')}
        except (IndexError, KeyError):
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=result)

        return { Output.WORKSPACE_ID_STATE: result}
