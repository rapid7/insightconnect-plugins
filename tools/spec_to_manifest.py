import json
import re
import sys
import yaml
import logging
import markdown
from bs4 import BeautifulSoup, NavigableString, Tag
import glob
from pprint import pprint


"""
Input: path to workflow directory
Output: manifest.json file within specified directory
"""


def main():
    logging.basicConfig(format='%(message)s')
    path = sys.argv[1]
    yaml, md, icon = find_files(path)
    if yaml and md and icon:
        spec = open_and_read_spec(yaml)
        print("Read spec file at " + yaml)

        help_md = open_and_read_md(md)
        print("Read md file at " + md)

        workflow_time = find_workflow_time(icon)
        json_obj = parse_fields(spec, help_md, workflow_time)
        print("Converted fields")

        write_to_json(json_obj, path)
        print("Wrote manifest at " + path)
    else:
        logging.warning("ERROR: A file was not found")


def parse_fields(yaml_obj, md_obj, time_saved):
    # Manifest Version -- mandatory
    manifest_obj = {"manifest_version": 1}

    resources = yaml_obj.get("resources")
    if resources:
        vendor_url = resources.get("vendor_url")
    cloud_ready = yaml_obj.get("cloud_ready")
    unique_name = yaml_obj.get("name")
    publisher = yaml_obj.get("vendor")
    support = yaml_obj.get("support")

    # Extension -- mandatory
    # From yaml, other info changes based on extension
    extension_type = yaml_obj.get("extension")
    extension_obj = {"type": extension_type}
    if extension_type == "workflow":
        extension_obj[extension_type] = unique_name + ".icon"
        extension_obj["workflowTime"] = time_saved
        extension_obj["pluginsUsed"] = md_obj.get("Plugins Used", [])

    # if extension_type == "plugin":
    #     extension_obj["externalPluginName"] = unique_name
    #     if cloud_ready:
    #         extension_obj["cloudReady"] = "true"
    #     else:
    #         extension_obj["cloudReady"] = "false"

    manifest_obj["extension"] = extension_obj

    # ID -- mandatory
    # From yaml
    manifest_obj["id"] = unique_name

    # Title -- mandatory
    # From yaml
    manifest_obj["title"] = yaml_obj.get("title")

    # Overview -- Mandatory
    # from yaml
    manifest_obj["overview"] = yaml_obj.get("description")

    # Description -- mandatory
    # Tricky extraction of description from .md
    manifest_obj["description"] = clean_chars(md_obj.get("Description"))

    # Key Features -- mandatory
    # From .md
    manifest_obj["key_features"] = md_obj.get("Key Features")

    # Requirements -- Optional
    # Tricky reading from .md, due to different formatting....
    if md_obj.get("Requirements") == "None":
        manifest_obj["requirements"] = []
    else:
        manifest_obj["requirements"] = md_obj.get("Requirements")

    # Resources -- optional
    # Equivalent to Links --> References from .md
    manifest_obj["resources"] = md_obj.get("Links")

    # Version -- optional
    # Directly from yaml, parsed as string in manifest
    manifest_obj["version"] = str(yaml_obj.get("version"))

    # Version History....
    # Should be from .md -- small normalizations
    versions = md_obj.get("Version History")
    converted_versions_obj = []
    version_changes = ""
    for version in versions:
        version_info = version.split(" - ")
        if version_info:
            version_number = version_info[0].strip()
            if len(version_info) >= 2:
                version_changes = " - ".join(version_info[1:]).strip()
            else:
                version_changes = ""
        else:
            version_number = ""
        version_obj = {"version": version_number, "date": "", "changes": clean_chars(version_changes)}
        converted_versions_obj.append(version_obj)
    manifest_obj["version_history"] = converted_versions_obj

    # Publisher -- mandatory
    # "Vendor" field from yaml
    manifest_obj["publisher"] = publisher

    # Support -- mandatory
    # from yaml if R7, where to get info on "community" support?
    if support == "rapid7":
        support_obj = {"type": "publisher", "url": "http://www.rapid7.com"}
    else:
        if vendor_url:
            support_obj = {"type": "community", "url": vendor_url}
        else:
            support_obj = {"type": "community", "url": ""}
    manifest_obj["support"] = support_obj

    # Rapid7 Products -- mandatory
    # Products key from yaml, we don't have an understanding of primary/secondary....
    product_listings = yaml_obj.get("products")
    r7_products = []
    for x in range(len(product_listings)):
        if x == 0:
            r7_products.append({"name": product_listings[x], "role": "primary"})
        else:
            r7_products.append({"name": product_listings[x], "role": "secondary"})
    manifest_obj["rapid7_products"] = r7_products

    # Required R7 Features -- Required
    # Different rules for workflows, plugins, etc...

    if extension_type == "workflow" or extension_type == "plugin":
        if unique_name == "rapid7_insight_agent":
            manifest_obj["required_rapid7_features"] = ["orchestrator", "agent"]
        else:
            if cloud_ready or "cloud_enabled" in yaml_obj.get("hub_tags").get("keywords"):
                manifest_obj["required_rapid7_features"] = []
            else:
                manifest_obj["required_rapid7_features"] = ["orchestrator"]

    # Status -- optional
    # From yaml
    manifest_obj["status"] = yaml_obj.get("status")

    # Logos -- optional
    manifest_obj["logos"] = {"primary": "extension.png", "secondary": []}

    # Display Options -- mandatory
    # No sense of this in spec/md -- only "credit_author" is valid
    manifest_obj["display_options"] = []

    # Tags -- Mandatory
    # Converting from yaml
    hub_tags = yaml_obj.get("hub_tags")

    # Tags.categories -- Mandatory
    categories = hub_tags.get("use_cases")

    # Tags.third_party_products -- optional
    # This info is not readily available yet
    third_party_products = []

    # Tags.keywords -- optional
    keywords = hub_tags.get("keywords")
    manifest_obj["tags"] = {"categories": categories, "third_party_products": third_party_products,
                            "keywords": keywords}

    # Documentation -- optional
    documentation_obj = {}
    if resources.get("docs_url"):
        documentation_obj["type"] = "url"
        documentation_obj["source"] = resources.get("docs_url")
    else:
        documentation_obj["type"] = "file"
        documentation_obj["source"] = "help.md"

    manifest_obj["documentation"] = documentation_obj

    # Media -- optional
    # Conversions from yaml -- plugins don't have screenshots
    if resources:
        screenshots = resources.get("screenshots")
        if screenshots:
            media_list = []
            for media in yaml_obj.get("resources").get("screenshots"):
                image_pattern = r"\S+\.(?:png|jpe?g)"
                video_pattern = r"\S+\.(?:mp4)"
                type_of_media = ""
                if re.match(image_pattern, media["name"]):
                    type_of_media = "image"
                if re.match(video_pattern, media["name"]):
                    type_of_media = "video"
                media_info = {"source": media.get("name"), "title": media.get("title"), "type": type_of_media}
                media_list.append(media_info)
            manifest_obj["media"] = media_list

    # Links -- optional
    # Conversion from yaml
    src = ""
    lic = ""
    if resources:
        if resources.get("source_url"):
            src = resources["source_url"]
        if resources.get("license_url"):
            lic = yaml_obj["resources"]["license_url"]

        manifest_obj["links"] = {"source_url": src, "license_url": lic}

    manifest_obj["metadata"] = []

    # Processing Instructions -- optional
    manifest_obj["processing_instructions"] = []

    return manifest_obj


def html_convert_to_dict(soup):
    header_dict = {}
    # Look through all top level headers ("Description, Key Features, Requirements, etc.)
    for header in soup.find_all("h1"):
        key = header.get_text().strip()
        text = ""
        html_node = header
        p_links = []
        while True:
            html_node = html_node.nextSibling

            # End of html, fill dictionary based on what has been filled in
            if html_node is None:
                if text:
                    header_dict[key] = text
                elif p_links:
                    header_dict[key] = p_links
                else:
                    header_dict[key] = []
                break

            # If a section is empty
            # i.e. "Links"/"Requirements" section could be empty
            if check_blank_section(str(html_node)):
                header_dict[key] = []
                break

            # If next node is only text, add and move on (rare)
            if isinstance(html_node, NavigableString):
                text += html_node.strip()

            # If next node has a tag
            # h1 tags denote the end of a header section
            # ul tags are parsed out into strings accordingly
            # h2 tag may have plugin info
            # p tags include text that can be important for description/bullet points

            if isinstance(html_node, Tag):
                if html_node.name == "h1":
                    header_dict[key] = clean_chars(text.strip().replace("\n", " "))
                    break
                if html_node.name == "ul":
                    is_list_with_links = False
                    if key == "Documentation":
                        text += html_node.get_text().replace(" \n", " ") + " "
                    else:
                        for x in html_node:
                            if isinstance(x, Tag):
                                if "<li><a href" in str(x) and key == "Links":
                                    is_list_with_links = True
                                    break
                        if is_list_with_links:
                            link_dict = handle_list_with_links(html_node)
                            header_dict[key] = link_dict
                        else:
                            clean_text = handle_list(html_node)
                            if text != "":
                                concat_string = text.lstrip(" ") + str(clean_text).replace("\"", "").rstrip(" ")
                                header_dict[key] = concat_string
                            else:
                                header_dict[key] = clean_text
                        break
                if html_node.name == "h2":
                    if html_node.text == "Technical Details":
                        header_dict["Plugins Used"], html_node = get_used_plugins(html_node)
                if html_node.name == "p" or html_node.name == "blockquote":

                    # Found that some of the links section is not a list (instead a p tag)
                    if "<a href=" in str(html_node.next) and key == "Links":
                        p_links.append(get_p_link(html_node.next))
                    else:
                        text += html_node.get_text().replace(" \n", " ") + " "
    return header_dict


def open_and_read_spec(file):
    spec_file = open(file)
    loaded_spec = yaml.safe_load(spec_file)
    return loaded_spec


def open_and_read_md(file):
    markdown_file = open(file)
    soup = md_convert_to_html(markdown_file)
    md_dict = html_convert_to_dict(soup)
    md_dict = validate_dict(md_dict, ["Description", "Documentation", "Key Features", "Requirements", "Version History", "Links"])
    return md_dict


def find_workflow_time(icon):
    with open(icon) as file:
        dic = json.loads(file.read())
        seconds = dic.get("kom").get("workflowVersions")[0].get("humanCostSeconds")
        return str(seconds) + " seconds"


def md_convert_to_html(file):
    html = markdown.markdown(file.read(), extensions=["tables"])
    soup = BeautifulSoup(html, features="html.parser")
    return soup


def get_p_link(string):
    soup_node = BeautifulSoup(str(string), features="html.parser")
    return {"text": soup_node.get_text(), "url": soup_node.a.get("href")}


def handle_list_with_links(html):
    soup_node = BeautifulSoup(str(html), features="html.parser")
    link_dict = build_link_dict(soup_node)
    return link_dict


# Builds link data structure with url and description
def build_link_dict(element):
    try:
        return [{"text": li.get_text().split("\n")[0], "url": li.a.get("href")}
                for ul in element('ul', recursive=False)
                for li in ul('li', recursive=False)]
    except AttributeError:
        logging.warning("List with hyperlinks is not formatted correctly. Please check the help.md file.")
        return []


def handle_list(html):
    soup_node = BeautifulSoup(str(html), features="html.parser")
    html_list_tree = build_list_tree(soup_node)
    clean_text = clean_tree_to_string(html_list_tree)
    return clean_text


# Returns dictionary representing nested link structure
def build_list_tree(element):
    return [{clean_chars(li.get_text().split("\n")[0]): build_list_tree(li)}
            for ul in element('ul', recursive=False)
            for li in ul('li', recursive=False)]


# Cleans nested list dictionary into a nicer string
def clean_tree_to_string(d):
    string_list = []
    for list_element in d:
        for key, value in list_element.items():
            if len(value) != 0:
                cleaned_data = clean_tree_to_string(value)
                concat = key + " " + str(cleaned_data)
                string_list.append(concat)
            else:
                string_list.append(str(key).rstrip(" ").replace("\"", "'"))
    return string_list


def check_blank_section(node):
    return re.match(r"^.*This (plugin|workflow) does not contain any (requirements|references).", node)


def validate_dict(md, sections):
    keys = md.keys()
    for section in sections:
        if section not in keys:
            logging.warning(f"WARNING: Markdown dictionary does not have %s key, an empty section will be added. This "
                            f"warning is due to the help.md being improperly formatted. " % section)
            if section in ["Description", "Documentation"]:
                md[section] = ""
            if section in ["Key Features", "Requirements", "Version History", "Links"]:
                md[section] = []
    return md


def get_used_plugins(table):
    node = table
    while node.find('td') == -1 or not node.find('td'):
        node = node.nextSibling
        if isinstance(node, Tag):
            if node.getText() == "Troubleshooting":
                break
    entries = node.findAll('td')
    plugin_list = []
    for i in range(0, len(entries), 3):
        plugin = {"plugin:": entries[i].text, "version": entries[i+1].text}
        plugin_list.append(plugin)
    return plugin_list, node


def clean_chars(text):
    text = text.replace("\u2019", "'")
    text = text.replace("\u2018", "'")
    text = text.replace("\"", "'")
    return text


def find_files(path):
    try:
        yaml = glob.glob(path + "/*.spec.yaml")[0]
        md = glob.glob(path + "/help.md")[0]
        icon = glob.glob(path + "/*.icon")[0]
        return yaml, md, icon
    except IndexError:
        logging.warning(f"ERROR: One of the necessary files was not found. "
                        f"Please check to see if your directory has the necessary files.")


def write_to_json(obj, path):
    with open(path + "/manifest.json", "w") as json_out:
        json.dump(obj, json_out, indent=4)


if __name__ == "__main__":
    main()
