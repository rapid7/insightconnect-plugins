from atlassian.errors import ApiPermissionError, ApiNotFoundError, ApiValueError, ApiConflictError
from insightconnect_plugin_runtime.exceptions import PluginException


def normalize_page(p):
    p["created"] = p["created"].value + "Z"
    p["modified"] = p["modified"].value + "Z"
    if p["homePage"] == "false":
        p["homePage"] = False
    else:
        p["homePage"] = True

    if p["current"] == "false":
        p["current"] = False
    else:
        p["current"] = True

    return p


def extract_page_data(page):

    url_base = page.get("_links").get("base")
    endpoint = page.get("_links").get("webui")
    home_page = page.get("space", {}).get("_expandable").get("homepage", "")
    id = page.get("id")
    is_home_page = id in home_page
    ancestors = page.get("ancestors")

    page = {
        "title": page.get("title"),
        "space": page.get("space").get("name"),
        "modifier": page.get("version", {}).get("publicName"),
        "created": page.get("history", {}).get("createdDate"),
        "content": page.get("body", {}).get("view", {}).get("value"),
        "url": f"{url_base}{endpoint}",
        "permissions": page.get("space", {}).get("permissions"),
        "creator": page.get("history", {}).get("createdBy", {}).get("publicName"),
        "parentId": ancestors[0].get("id") if ancestors else None,
        "version": f'{page.get("version", {}).get("number")}',
        "homePage": is_home_page,
        "id": id,
        "current": page.get("status").lower() == "current",
        "contentStatus": page.get("status"),
        "modified": page.get("version", {}).get("when"),
    }
    return page

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ApiPermissionError as exception:
            raise PluginException(
                "Something unexpected occurred. See error log for details.",
                "Please check your input and connection details.",
                data=exception)
        except ApiNotFoundError as exception:
            raise PluginException(
                preset=PluginException.Preset.NOT_FOUND,
                data=exception)
        except ApiValueError as exception:
            raise PluginException(
                preset=PluginException.Preset.BAD_REQUEST,
                data=exception)
        except ApiConflictError as exception:
            raise PluginException(
                "A conflict occurred. See error log for details.",
                "Please check your input and connection details.",
                data=exception)
        except Exception as exception:
            raise PluginException(
                "Something unexpected occurred. See error log for details.",
                "Please check your input and connection details.",
                data=exception)
    return wrapper
