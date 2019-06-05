import komand
from .schema import GetListInput, GetListOutput


class GetList(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_list',
                description='Get list of current blocks',
                input=GetListInput(),
                output=GetListOutput())

    def run(self, params={}):
        host = self.connection.host
        url = host + '/bhr/publist.csv'
        result = komand.helper.open_url(url)
        return { 'list': result.read().decode("utf-8") }

    def test(self):
        """TODO: Test action"""
        return {}
