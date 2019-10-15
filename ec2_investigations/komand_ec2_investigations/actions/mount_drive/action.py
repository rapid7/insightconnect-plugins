import komand
from .schema import MountDriveInput, MountDriveOutput
# Custom imports below
import json
from boto.manage.cmdshell import sshclient_from_instance


class MountDrive(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='mount_drive',
                description='Mount drive',
                input=MountDriveInput(),
                output=MountDriveOutput())

    def run(self, params={}):
        """TODO: Run action"""
        directory = params.get("directory")
        device = params.get("device")
        instance_id = params.get("instance_id")
        private_key = params.get("private_key")
        user = params.get("user")
        region = params.get("region")
        empty_json_output = {}

        # Create private key file
        f = open('./pk.pem', 'w')
        f.write(private_key)
        f.close()

        # Create command from user input
        command = 'sudo ./mount.sh ' + directory + ' ' + device

        try:
           # Connect to AWS instance
           reservations = self.connection.aws.get_all_instances(filters={'instance_id' : instance_id})
           instance = reservations[0].instances[0]
           ssh_client = sshclient_from_instance(instance, './pk.pem', user_name=user)

           # Copy the mount.sh script to the instance and make it executable
           ssh_client.put_file("./komand_ec2_investigations/actions/mount.sh", "./mount.sh")
           ssh_client.run('chmod +x mount.sh')

           # Execute the command and return the standard output
           status, stdout, stderr = ssh_client.run(command)
           # Remove script after running
           ssh_client.run('rm ./mount.sh')

           if stdout.decode("utf-8").rstrip() == "0":
              result = empty_json_output
              self.logger.error("Unable to mount device: %s. Verify volume is attached", device)
           elif stdout.decode("utf-8").rstrip() == "1":
              result = json.loads('{"directory": "%s", "status": "Directory already mounted"}' % directory)
              self.logger.info("Unable to mount directory: %s. Directory already mounted", directory)
           elif stdout.decode("utf-8").rstrip() == "2":
              result = empty_json_output
              self.logger.error("Unable to mount directory: %s. Invalid directory", directory)
           else:
              result = json.loads(stdout.decode("utf-8").rstrip())

        except Exception:
           self.logger.error("No address associated with hostname %s. Verify instance is running and credentials are valid", instance_id)
           raise

        return result

    def test(self):
        """TODO: Test action"""
        return {}
