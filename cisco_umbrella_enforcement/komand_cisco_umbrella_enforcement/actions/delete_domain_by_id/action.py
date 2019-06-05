import komand
from .schema import DeleteDomainByIdInput, DeleteDomainByIdOutput
# Custom imports below


class DeleteDomainById(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_domain_by_id',
                description='Delete domain from user domain list by ID',
                input=DeleteDomainByIdInput(),
                output=DeleteDomainByIdOutput())

    def run(self, params={}):
        ID = params.get("ID")
        
        try:
            status_code = self.connection.api.delete_domains_by_id(ID)
            self.logger.info(status_code)
        except Exception:
            self.logger.error("DeleteDomainById: run: Problem with request")
            raise Exception("DeleteDomainById: run: Problem with request")

        return {"status": "success"}

    def test(self):
        return {"status": "success"}
