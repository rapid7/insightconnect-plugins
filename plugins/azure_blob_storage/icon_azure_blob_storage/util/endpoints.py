# Connection endpoints
O365_AUTH_ENDPOINT = "https://login.microsoftonline.com/{}/oauth2/token"
O365_AUTH_RESOURCE = "https://storage.azure.com"

COMMON_URI = "https://{account}.blob.core.windows.net"
# Actions endpoints
CONTAINER_ENDPOINT = "/{container_name}?restype=container"
LIST_CONTAINERS_ENDPOINT = "/?comp=list"
LIST_BLOBS_ENDPOINT = "/{container_name}/?restype=container&comp=list"
BLOB_ENDPOINT = "/{container_name}/{blob_name}"
