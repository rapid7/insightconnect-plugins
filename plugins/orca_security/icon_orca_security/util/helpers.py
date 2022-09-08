from urllib.parse import urlsplit

from insightconnect_plugin_runtime.exceptions import PluginException


def get_role_id(role_name: str, roles: list) -> str:
    for role in roles:
        if role_name.lower() == role.get("name").lower():
            role_id = role.get("id")
            if role_id:
                return role_id
    raise PluginException(
        cause=f"Role {role_name} not found.", assistance="Please check that provided role is correct and try again."
    )


def validate_filters(filters: list) -> list:
    new_filters = []
    for provided_filter in filters:
        field = provided_filter.get("field")
        includes = provided_filter.get("includes")
        excludes = provided_filter.get("excludes")
        if not field:
            raise PluginException(
                cause=f"The name of the field against which the alerts should be filtered was not specified in the "
                f"filter: {provided_filter}.",
                assistance="Please provide a field name and try again.",
            )
        if not includes and not excludes:
            raise PluginException(
                cause=f"No values were given for the field to include or exclude in the filter: {provided_filter}.",
                assistance="Please provide 'includes' or 'excludes' fields and try again.",
            )
        if field != "state.created_at":
            new_filters.append(provided_filter)
    return new_filters


def split_url(url: str) -> str:
    scheme, netloc, paths, queries, fragments = urlsplit(url.strip())  # pylint: disable=unused-variable
    return f"{scheme}://{netloc}"
