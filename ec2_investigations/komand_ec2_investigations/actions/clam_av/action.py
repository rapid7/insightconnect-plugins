import komand
from .schema import ClamAvInput, ClamAvOutput
# Custom imports below
import json
from boto.manage.cmdshell import sshclient_from_instance


class ClamAv(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='clam_av',
                description='Scan directory with ClamAV',
                input=ClamAvInput(),
                output=ClamAvOutput())

    def run(self, params={}):
        """TODO: Run action"""
        directory = params.get("directory")
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
        command = 'python clam_av_run.py ' + directory

        try:
           # Connect to AWS instance
           reservations = self.connection.aws.get_all_instances(filters={'instance_id' : instance_id})
           instance = reservations[0].instances[0]
           ssh_client = sshclient_from_instance(instance, './pk.pem', user_name=user)

           # Copy the mount.sh script to the instance and make it executable
           ssh_client.put_file("./komand_ec2_investigations/actions/clam_av_run.py", "./clam_av_run.py")
           # Execute the command and return the standard output
           status, stdout, stderr = ssh_client.run(command) 
           # Remove script after running
           ssh_client.run('rm ./clam_av_run.py')

           if stdout.decode("utf-8").rstrip() == "0":
              results = empty_json_output
              self.logger.error("Clam scan is not installed on host and is required to run")
           elif stderr.decode("utf-8") != "":
              results = empty_json_output
              self.logger.error(stderr.decode("utf-8").rstrip())
           else:
              results = json.loads(stdout.decode("utf-8").rstrip())
           
        except Exception:
           self.logger.error("Something went wrong, command probably failed to run")
           raise

        self.logger.info(results)
        return results

    def test(self):
        """TODO: Test action"""
        return {}
