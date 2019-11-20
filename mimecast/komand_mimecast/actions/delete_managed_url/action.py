import komand
from .schema import DeleteManagedUrlInput, DeleteManagedUrlOutput, Component
# Custom imports below
from komand_mimecast.util import util


class DeleteManagedUrl(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_managed_url',
                description=Component.DESCRIPTION,
                input=DeleteManagedUrlInput(),
                output=DeleteManagedUrlOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        get_uri = self.connection.GET_MANAGED_URL_URI
        delete_uri = self.connection.DELETE_MANAGED_URL_URI
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        # Generate payload dictionary
        plugin_arguments = {}
        for key, value in params.items():
            temp = util.normalize(key, value)
            plugin_arguments.update(temp)

        # Mimecast request for get_managed_urls (we need to get the ID, and we can only get the entire table of urls
        #   back, not just the one)
        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=get_uri,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=None)

        get_data = {}
        if 'data' in response:
            get_data = response['data']
        delete_all_entries_boolean = bool(plugin_arguments['deleteAllEntries'])

        # get the IDS of only the ones that pertain to the URL we want blocked
        url_to_block = plugin_arguments['url']
        url_comparer = util.UrlMimecastFinder(url_to_block)
        ids_of_items_to_delete = []
        for json_block in get_data:
            if url_comparer.does_mimecast_json_object_match(json_block):
                ids_of_items_to_delete.append(str(json_block['id']))

        # maximum of 1 deletion if not delete_all_entries_boolean
        if not delete_all_entries_boolean and len(ids_of_items_to_delete) > 1:
            ids_of_items_to_delete = ids_of_items_to_delete[:1]

        # Mimecast request for delete
        total_deleted_ids = 0
        for id_to_delete in ids_of_items_to_delete:
            mimecast_request = util.MimecastRequests()
            response = mimecast_request.mimecast_post(url=url, uri=delete_uri,
                                                      access_key=access_key, secret_key=secret_key,
                                                      app_id=app_id, app_key=app_key, data={'id': id_to_delete})
            total_deleted_ids += 1

        return {'response': [{'number_of_deletions': str(total_deleted_ids)}]}
