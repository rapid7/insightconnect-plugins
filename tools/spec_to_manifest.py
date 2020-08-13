import json
import re
import sys
import yaml
import logging
import markdown
from bs4 import BeautifulSoup, NavigableString, Tag


def main():
    yaml = ""
    md = ""
    path = ""
    correct_params = False
    try:
        yaml = sys.argv[1]
        md = sys.argv[2]
        path = sys.argv[3]
        correct_params = True
    except IndexError:
        logging.warning("ERROR: Insufficient parameters")

    if correct_params:
        if verify_yaml(yaml) and verify_md(md):
            spec = open_and_read_spec(yaml)
            print("Read spec file at " + yaml)
            help_md = open_and_read_md(md)
            print("Read md file at " + md)
            json_obj = parse_fields(spec, help_md)
            print("Converted fields")
            write_to_json(json_obj, path)
            print("Wrote manifest at " + path)
        else:
            logging.warning("ERROR: Wrong file type(s) specified")


# noinspection DuplicatedCode,DuplicatedCode
def parse_fields(yaml_obj, md_obj):
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
    if extension_type == "plugin":
        extension_obj["externalPluginName"] = unique_name
        if cloud_ready:
            extension_obj["cloudReady"] = "true"
        else:
            extension_obj["cloudReady"] = "false"

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
    manifest_obj["description"] = md_obj.get("Description")

    # Key Features -- mandatory
    # From .md
    manifest_obj["key_features"] = md_obj.get("Key Features")

    # Requirements -- Optional
    # Tricky reading from .md, due to different formatting....
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
    version_number = ""
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
        version_obj = {"version": version_number, "date": "", "changes": version_changes}
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
            if not cloud_ready:
                manifest_obj["required_rapid7_features"] = ["orchestrator"]
            else:
                manifest_obj["required_rapid7_features"] = []

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

    # Processing Instructions -- optional
    # No sense of this in yaml...
    manifest_obj["processing_instructions"] = []

    return manifest_obj


def open_and_read_spec(file):
    spec_file = open(file)
    loaded_spec = yaml.safe_load(spec_file)
    return loaded_spec


def open_and_read_md(file):
    markdown_file = open(file)
    soup = md_convert_to_html(markdown_file)
    md_dict = html_convert_to_dict(soup)
    return md_dict


def md_convert_to_html(file):
    html = markdown.markdown(file.read())
    soup = BeautifulSoup(html, features="html.parser")
    return soup


def html_convert_to_dict(soup):
    header_dict = {}
    # Find all top level headers
    for header in soup.find_all("h1"):
        key = header.get_text().strip()
        text = ""
        next_tag_block = header
        while True:
            next_tag_block = next_tag_block.nextSibling
            # End of html
            if next_tag_block is None:
                break
            # If a section is empty
            # i.e. "Links"/"Requirements" section could be empty
            if check_blank_section(str(next_tag_block)):
                header_dict[key] = []
                break
            # If next node is text (usually does not add anything)
            if isinstance(next_tag_block, NavigableString):
                text += next_tag_block.strip()

            # If next node is a tag
            # ul tags are parsed out into strings accordingly
            # h1 tags denote the end of a header section
            # p tags include text that can be important for description/bullet points
            if isinstance(next_tag_block, Tag):
                if next_tag_block.name == "h1":
                    header_dict[key] = text.strip().replace("\n", " ")
                    break
                if next_tag_block.name == "ul":
                    is_list_with_links = False
                    for x in next_tag_block:
                        if isinstance(x, Tag):
                            if "<li><a href" in str(x) and key == "Links":
                                is_list_with_links = True
                                break
                    if is_list_with_links:
                        link_dict = handle_list_with_links(next_tag_block)
                        header_dict[key] = link_dict
                    else:
                        clean_text = handle_list(next_tag_block)
                        if text != "":
                            concat_string = text.lstrip(" ") + str(clean_text).replace("\'", "")
                            header_dict[key] = concat_string
                        else:
                            header_dict[key] = clean_text
                    break
                if next_tag_block.name == "p" or next_tag_block.name == "blockquote":
                    text += next_tag_block.get_text().replace(" \n", " ") + " "
    return header_dict


def handle_list_with_links(html):
    soup_node = BeautifulSoup(str(html), features="html.parser")
    link_dict = build_link_dict(soup_node)
    return link_dict


# Builds link data structure with url and description
def build_link_dict(element):
    return [{"text": li.get_text().split("\n")[0], "url": li.a.get("href")}
            for ul in element('ul', recursive=False)
            for li in ul('li', recursive=False)]


def handle_list(html):
    soup_node = BeautifulSoup(str(html), features="html.parser")
    html_list_tree = build_list_tree(soup_node)
    clean_text = clean_tree_to_string(html_list_tree)
    return clean_text


# Returns dictionary representing nested link structure
def build_list_tree(element):
    return [{li.get_text().split("\n")[0]: build_list_tree(li)}
            for ul in element('ul', recursive=False)
            for li in ul('li', recursive=False)]


# Cleans nested list dictionary into a nicer string
def clean_tree_to_string(d):
    string_list = []
    for list_element in d:
        for key, value in list_element.items():
            if len(value) != 0:
                cleaned_data = clean_tree_to_string(value)
                concat = key + " " + str(cleaned_data).replace("\'", "")
                string_list.append(concat)
            else:
                string_list.append(key)
    return string_list


def check_blank_section(node):
    return re.match(r"^.*This (plugin|workflow) does not contain any (requirements|references).", node)


def verify_yaml(file):
    return file and re.match(r"^\S*.spec.yaml$", file)


def verify_md(file):
    return file and re.match(r"^\S*help.md$", file)


def write_to_json(obj, path):
    with open(path + "/manifest.json", "w") as json_out:
        json.dump(obj, json_out, indent=4)


if __name__ == "__main__":
    main()
