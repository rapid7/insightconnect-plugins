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
    home_page = page.get("space", {}).get("homepage", "")
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
