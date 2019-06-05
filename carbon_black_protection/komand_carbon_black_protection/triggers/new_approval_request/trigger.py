import komand
import time
from .schema import NewApprovalRequestInput, NewApprovalRequestOutput
# Custom imports below


class NewApprovalRequest(komand.Trigger):
    starting_id = 0

    def __init__(self):
        super(self.__class__, self).__init__(
                name='new_approval_request',
                description='Triggers when a new approval request is created',
                input=NewApprovalRequestInput(),
                output=NewApprovalRequestOutput())

    def run(self, params={}):
        poll_rate = params.get("poll_rate", 10)
        self.logger.info("Looking for new approval requests...")

        url = self.connection.host + "/api/bit9platform/v1/approvalRequest?q=status:1&q=id>{id}"  # status:1 = submitted

        while True:
            with komand.helper.open_cachefile("cb_protection_new_approval_request") as cache_file:
                cache_file.seek(0)
                temporary_id = cache_file.readline().strip()
                if temporary_id is not '':
                    self.starting_id = int(temporary_id)

            try:
                request = self.connection.session.get(url=url.format(id=self.starting_id), verify=self.connection.verify)
                results = request.json()

                # Clean all the results before we do anything with them
                results = komand.helper.clean(results)

                for request in results:
                    self.logger.info("New approval request found, triggering...")
                    self.send({"approval_request": request})

                    # Write to cache as soon as we have it in case the trigger is killed mid-parse. This will prevent duplicate triggering
                    with komand.helper.open_cachefile("cb_protection_new_approval_request") as cache_file:
                        cache_file.seek(0)
                        cache_file.write(str(request["id"]))

                    self.starting_id = request["id"]

            except BaseException as e:
                raise Exception("Error occurred: %s" % e)
            except ValueError as e:
                raise e

            else:
                self.logger.info("Sleeping for %d seconds..." % poll_rate)
                time.sleep(poll_rate)

    def test(self):
        url = self.connection.host + "/api/bit9platform/v1/approvalRequest?limit=-1"  # -1 returns just the count (lightweight call)

        request = self.connection.session.get(url=url, verify=self.connection.verify)

        try:
            request.raise_for_status()
        except:
            raise Exception('Run: HTTPError: %s' % request.text)

        return {}