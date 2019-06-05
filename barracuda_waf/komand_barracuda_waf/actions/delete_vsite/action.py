import komand
from .schema import DeleteVsiteInput, DeleteVsiteOutput


class DeleteVsite(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_vsite',
                description='Deletes the given vsite',
                input=DeleteVsiteInput(),
                output=DeleteVsiteOutput())

    def run(self, params={}):
        action = "vsites/" + params.get("id")
        self.connection.connector.delete(action)

        if self.connection.connector.get_code() == 404:
            return {"status": False}
        else:
            return {"status": True}

    def test(self):
        return {"status": True}
