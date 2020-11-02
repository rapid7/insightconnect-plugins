import json
import re
import sys
import yaml
import logging
import markdown
from bs4 import BeautifulSoup, Tag
import glob

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
        logging.info("Read spec file at " + yaml)

        help_md = open_and_read_md(md)
        logging.info("Read md file at " + md)

        workflow_meta_info = find_workflow_meta_info(icon)
        json_obj = fill_fields(spec, help_md, workflow_meta_info)
        logging.info("Converted fields")

        write_to_json(json_obj, path)
        logging.info("Wrote manifest at " + path)
    else:
        logging.warning("ERROR: A file was not found")


# Create a dictionary with keys being h1 headers and values being the text within those h1 sections
# This includes any tags as well (h2, p, etc)
def get_html_chunks(html: str, tag: str, exceptions=None) -> dict:
    """
    Splits up html into chunks based on tag provided
    :param html: html to parse through
    :param tag: The target tag to act as a "delimiter" to split html on
    :param exceptions: Names of sections that should be excluded when splitting
    :return: dictionary where key = name of section and value = all html contained in that section
    """
    soup = BeautifulSoup(html, features="html.parser")
    if exceptions is None:
        exceptions = []

    html_chunks = dict()

    # Gets the first line of the html
    line = soup.find()

    # Key acts as the header for the section
    key = line.get_text().strip()

    line = line.nextSibling
    html_block = ""
    while line is not None:
        # Once you've hit your target tag, fill in dictionary with the respective header as key and html as value
        if isinstance(line, Tag) and line.name == tag and line.get_text() not in exceptions:
            html_block = html_block.strip("\n")
            html_chunks[key] = html_block
            key = line.get_text().strip()
            html_block = ""
        else:
            html_block += str(line)
        line = line.nextSibling
    html_chunks[key] = html_block

    return html_chunks


def html_convert_to_dict(html):
    """
    Fills in help.md info in a dict
    :param html: The html that was converted from help.md
    :return: Dictionary with all relevant info from help.md
    """
    info_dict = dict()

    # Breaks up html (i.e. markdown file) based on its headers
    h1_blocks = get_html_chunks(html, "h1", ["Usage"])

    info_dict["Description"] = clean_to_plaintext(h1_blocks.get("Description"))

    info_dict["Plugins Used"] = handle_documentation(h1_blocks.get("Documentation"))
    info_dict["Key Features"] = handle_key_features(h1_blocks.get("Key Features"))
    info_dict["Requirements"] = handle_requirements(h1_blocks.get("Requirements"))
    info_dict["Version History"] = handle_version_history(h1_blocks.get("Version History"))
    info_dict["Links"] = handle_links(h1_blocks.get("Links"))

    return info_dict


def handle_documentation(documentation: str) -> [dict]:
    """
    Gathers information needed from Documentation section of help.md
    :param documentation: Documentation text to parse through
    :return: Text with documentation instructions and list of plugins used in workflow
    """

    if not documentation:
        return ""
    # Documentation section is split up into 3 parts -- setup, technical details/plugins and troubleshooting
    # Currently, only the technical details section is used in the manifest
    h2_blocks = get_html_chunks(documentation, "h2")

    # Grab only the tech details section to get plugins from
    plugins = get_plugins_list(h2_blocks.get("Technical Details"))

    return plugins


def handle_key_features(key_features: str) -> list:
    """
    Gathers info for the Key Features section
    :param key_features: Key Features section of the help.md
    :return: A list of key features
    """
    if not key_features:
        return []
    kf_list = get_list_items(key_features, "ul")
    return kf_list


def handle_requirements(requirements: str) -> list:
    """
    Gathers info the Requirements section
    :param requirements: Requirements section of the help.md
    :return: A list of requirements
    """

    if not requirements:
        return []

    soup = BeautifulSoup(requirements, features="html.parser")

    # Due to the requirements section being formatted differently,
    # sometimes this section will have some text, tagged with <p>
    # to preserve this text, check if there is a p tag
    p_block = soup.find("p")
    if p_block:
        p_text = p_block.getText()
        if p_text == "None":
            return []

        # If there is a p tag: use that p's text
        # Then look for a html list (links removed)
        else:
            # The next line after a p tag block is a "\n"
            # The line after that will include a list
            if p_block.nextSibling and p_block.nextSibling.nextSibling:
                list_elements = str(p_block.nextSibling.nextSibling)
                list_elements = remove_links(list_elements)
                requirements_list = get_list_items(str(list_elements), "ul")
                return [f"{p_text.strip()} {requirements_list}"]
            else:
                return []

    # If no p element, grab the list with links removed
    else:
        removed_links = remove_links(str(soup))
        req_list = get_list_items(removed_links, "ul")
        return req_list


def handle_version_history(version_history: str) -> [dict]:
    """
    Gathers info for the Version History section
    :param version_history: Version History section of the help.md
    :return: A list of version history objects
    """
    if not version_history:
        return []

    # Remove any formatting from version history
    plaintext_versions = clean_to_plaintext(version_history)

    versions = get_list_items(plaintext_versions, "ul")

    # Get each version, which is split by a dash
    all_versions_list = []
    for version in versions:
        version_info = version.split(" - ")
        if version_info:
            version_obj = {"version": version_info[0], "date": "", "changes": version_info[1]}
            all_versions_list.append(version_obj)

    return all_versions_list


def handle_links(links_block: str) -> [dict]:
    """
    Gathers info for the Links section
    :param links_block: Links section of the help.md
    :return: A list of link objects
    """
    if not links_block:
        return []

    links = links_block.strip("\n")

    # All the links are contained under the "References" subheader
    references_only = get_html_chunks(links, "h2").get("References")

    references_only = references_only.strip("\n")
    list_with_links = get_list_items_with_links(references_only)

    return list_with_links


def get_plugins_list(table: str) -> [dict]:
    """
    Creates a plugin list from an html table
    :param table: The html table to parse through
    :return: A list of plugins and their versions
    """
    soup = BeautifulSoup(table, features="html.parser")

    # Denotes the start of a html table
    entries = soup.findAll('td')

    if entries:
        plugin_list = []
        for i in range(0, len(entries), 3):
            plugin = {"plugin:": entries[i].text, "version": entries[i + 1].text}
            plugin_list.append(plugin)
        return plugin_list

    # No plugins were used
    else:
        return []


def get_list_items(html_list: str, list_tag: str) -> list:
    """
    Create a python list from an html list block
    :param html_list: html list object to create a python list from
    :param list_tag: html tag element to create lists from, typically "ul" or "ol"
    :return: A python list that the items contained in the html list
    """
    soup = BeautifulSoup(html_list, features="html.parser")
    multiple_tags = soup.findAll(list_tag)

    # If a tag is found multiple times, you have a nested list
    if len(multiple_tags) > 1:
        entire_html_list = str(multiple_tags[0])
        inner_html_list = str(multiple_tags[1])

        # Grabs the text that introduces the inner list
        outer_text = entire_html_list.splitlines()[1]
        leading_text = BeautifulSoup(outer_text, features="html.parser").getText()

        # Recursively get python list from the inner html list
        nested_list_string = get_list_items(inner_html_list, list_tag)

        return [f"{leading_text} {nested_list_string}"]

    start_of_list = soup.find(list_tag)

    # Find each list element in the html list and strip out the tag
    list_elements = start_of_list.findAll()
    text_only_list = []
    for element in list_elements:
        text_only_list.append(element.getText().strip())

    return text_only_list


def get_list_items_with_links(list_with_links: str) -> [dict]:
    """
    Create a python list of link objects from an html list block
    :param list_with_links: Html list containing links (i.e. <a> tags)
    :return: List of objects with link and name of link
    """
    # No links
    if not list_with_links:
        return []

    soup = BeautifulSoup(list_with_links, features="html.parser")

    start_of_list = soup.find("ul")

    # Handles case where lists were not bulleted correctly
    if not start_of_list:
        if soup.find("p"):
            start_of_list = soup.find("p")
        else:
            return []

    # Grab each list element (i.e. <a> tag)
    list_elements = start_of_list.findAll("a", href=True)
    links_obj_list = []
    for element in list_elements:
        url = element["href"]
        text = element.getText()
        link_obj = {"title": text, "source": url}
        links_obj_list.append(link_obj)

    return links_obj_list


def clean_to_plaintext(text: str) -> str:
    """
    Strip formatting tags from html
    :param text: Text to strip formatting tags from
    :return: Text with common formatting tags stripped
    """
    text = re.sub(
        "(<p>)|(</p>)|(<i>)|(</i>)|(<strong>)|(</strong>)|(<code>)|(</code>)|(<blockquote>)|(</blockquote>)", "",
        text)
    return text


def remove_links(text: str) -> str:
    """
    Removes links from html (for requirements section)
    :param text: html chunk
    :return: html chunk with links removed
    """
    text = re.sub("(<a href=\".*\">)|</a>", "", text)
    return text


def find_workflow_meta_info(icon: str) -> dict:
    """
    Gathers info from .icon file as meta data
    :param icon: Path to .icon file
    :return: Dictionary with relevant meta data
    """
    meta_info = dict()
    try:
        with open(icon) as file:
            dic = json.loads(file.read())
            seconds = dic.get("kom").get("workflowVersions")[0].get("humanCostSeconds")
            steps = dic.get("kom").get("workflowVersions")[0].get("steps")
            meta_info["Seconds"] = f"{str(seconds)} seconds"
            meta_info["Steps"] = len(steps)
    except FileNotFoundError:
        logging.warning(f"No such file {icon}")
    return meta_info


def fill_fields(yaml_obj: dict, md_obj: dict, meta_info: dict) -> dict:
    """
    Brings together info from help.md, spec and other sources to create a manifest obj
    :param yaml_obj: Information contained in the spec.yaml file
    :param md_obj: Information from help.md, processed and standardized for manifest
    :param meta_info: Meta information about the extension type (only supports workflows at time of writing)
    :return: Manifest obj
    """
    manifest_obj = dict()

    # Properties that are used multiple times
    yaml_resources = yaml_obj.get("resources", "")
    cloud_ready = yaml_obj.get("cloud_ready", "")
    extension_name = yaml_obj.get("name", "")

    manifest_obj["manifestVersion"] = "1"

    # Extension object changes based on extension type
    extension_type = yaml_obj.get("extension")
    extension_obj = dict()
    if extension_type == "workflow" and meta_info:
        plugins_used = md_obj.get("Plugins Used", [])
        extension_obj = create_workflow_extension(extension_name, meta_info, plugins_used)

    # if extension_type == "plugin":
    #     extension_obj["type"] = "plugin"
    #     extension_obj["externalPluginName"] = unique_name
    #     if cloud_ready:
    #         extension_obj["cloudReady"] = "true"
    #     else:
    #         extension_obj["cloudReady"] = "false"

    manifest_obj["extension"] = extension_obj

    # Globally unique ID (in dashes, not underscores)
    manifest_obj["id"] = extension_name.replace("_", "-")

    # Title of extension for the listing page
    manifest_obj["title"] = yaml_obj.get("title")

    # Overview for extension for the listing page
    manifest_obj["overview"] = yaml_obj.get("description")

    # High level description of what extension does, used on details page
    manifest_obj["description"] = yaml_obj.get("description")

    # Important features of the extension to display
    manifest_obj["keyFeatures"] = md_obj.get("Key Features")

    # Requirements for extension to work
    manifest_obj["requirements"] = md_obj.get("Requirements")

    # Resources that could be useful for the extension
    manifest_obj["resources"] = md_obj.get("Links")

    # Current version of extension
    manifest_obj["version"] = str(yaml_obj.get("version"))

    # Version history for display on details page -- "date" property will have to be addressed
    manifest_obj["versionHistory"] = md_obj.get("Version History")

    # Company / person responsible for the extension
    manifest_obj["publisher"] = yaml_obj.get("vendor")

    # Specifies what support and where support can be found
    if yaml_obj.get("support") == "rapid7":
        support_obj = {"type": "publisher", "url": "http://www.rapid7.com"}
    else:
        if yaml_resources:
            vendor_url = yaml_resources.get("vendor_url", "")
            support_obj = {"type": "community", "url": vendor_url}
        else:
            support_obj = {"type": "community", "url": ""}
    manifest_obj["support"] = support_obj

    # List of R7 products this extension interacts with -- need to address primary/secondary roles...
    product_listings = yaml_obj.get("products")
    r7_products = []
    for x in range(len(product_listings)):
        if x == 0:
            r7_products.append({"name": product_listings[x], "role": "primary"})
        else:
            r7_products.append({"name": product_listings[x], "role": "secondary"})
    manifest_obj["rapid7Products"] = r7_products

    # Rapid7 specific tools for the extension to work
    if extension_type == "workflow" or extension_type == "plugin":
        if extension_name == "rapid7_insight_agent":
            manifest_obj["required_rapid7_features"] = ["orchestrator", "agent"]
        else:
            if cloud_ready or "cloud_enabled" in yaml_obj.get("hub_tags").get("keywords"):
                manifest_obj["required_rapid7_features"] = []
            else:
                manifest_obj["required_rapid7_features"] = ["orchestrator"]

    # Statuses that apply to the extension (ex. "obsolete")
    manifest_obj["status"] = yaml_obj.get("status")

    # Logos to represent the extension for display
    manifest_obj["logos"] = {"primary": "extension.png", "secondary": []}

    # Flags to customized way extension is displayed
    manifest_obj["display_options"] = []

    # Tags from spec to be displayed in details section
    manifest_obj["tags"] = create_tags(yaml_obj.get("hub_tags"))

    # Specifies what kind of documentation style will be used for the extension
    documentation_obj = dict()
    if yaml_resources.get("docs_url"):
        documentation_obj["type"] = "url"
        documentation_obj["source"] = yaml_resources.get("docs_url")
    else:
        documentation_obj["type"] = "file"
        documentation_obj["source"] = "help.md"

    manifest_obj["documentation"] = documentation_obj

    # List of media items for the extension (images, videos, etc.)
    if yaml_resources and yaml_resources.get("screenshots"):
        manifest_obj["media"] = create_media_list(yaml_resources.get("screenshots"))
    else:
        manifest_obj["media"] = []

    # Specific links related to the extension for display on details page
    if yaml_resources:
        src = yaml_resources.get("source_url", "")
        lic = yaml_resources.get("license_url", "")
        manifest_obj["links"] = {"source_url": src, "license_url": lic}
    else:
        manifest_obj["links"] = dict()

    # For ad-hoc requirements
    manifest_obj["metadata"] = []

    # Internal-only instructions
    manifest_obj["processing_instructions"] = []

    return manifest_obj


def create_workflow_extension(workflow_name: str, meta_info: dict, plugins: [dict]) -> dict:
    """
    Creates a workflow extension object, as proposed by hub team
    :param workflow_name: Name of workflow as specified in spec
    :param meta_info: Obtained from the .icon file, contains additional info
    :param plugins: Plugins used by the workflow
    :return: Manifest extension object
    """
    obj = dict()
    obj["type"] = "workflow"
    obj["file"] = workflow_name + ".icon"
    obj["workflowTime"] = meta_info["Seconds"]
    obj["pluginsUsed"] = plugins
    obj["workflowSteps"] = meta_info["Steps"]

    # This is an arbitrary threshold, will likely be determined by hub team
    if meta_info["Steps"] < 15:
        obj["workflowComplexity"] = "Low"
    else:
        obj["workflowComplexity"] = "High"

    return obj


def create_media_list(media_items: dict) -> [dict]:
    """
    Creates a list of media items for hub display
    :param media_items: List of screenshots, videos, etc. specified in spec.yaml
    :return: List of all media objects for the extension
    """
    image_pattern = r"\S+\.(?:png|jpe?g)"
    video_pattern = r"\S+\.(?:mp4)"
    media_list = []
    for media in media_items:
        type_of_media = ""
        if re.match(image_pattern, media.get("name")):
            type_of_media = "image"
        if re.match(video_pattern, media.get("name")):
            type_of_media = "video"
        media_info = {"source": media.get("name"), "title": media.get("title"), "type": type_of_media}
        media_list.append(media_info)

    return media_list


def create_tags(hub_tags: dict) -> dict:
    """
    Creates dict of tags for hub display
    :param hub_tags: The data held in the "hub_tags" field in the spec.yaml
    :return: Dict of tags
    """
    # Tags.categories -- Mandatory
    categories = hub_tags.get("use_cases")

    # Tags.third_party_products -- optional
    third_party_products = []

    # Tags.keywords -- optional
    keywords = hub_tags.get("keywords")

    obj = {"categories": categories, "third_party_products": third_party_products, "keywords": keywords}

    return obj


def open_and_read_spec(file):
    spec_file = open(file)
    loaded_spec = yaml.safe_load(spec_file)
    return loaded_spec


def open_and_read_md(markdown_file):
    with open(markdown_file) as md:
        # Converts markdown into html for easier parsing
        html_text = markdown.markdown(md.read(), extensions=["tables"])

        md_dict = html_convert_to_dict(html_text)
    return md_dict


def find_files(path):
    try:
        yaml_file = glob.glob(path + "/*.spec.yaml")[0]
        md_file = glob.glob(path + "/help.md")[0]
        icon_file = glob.glob(path + "/*.icon")[0]
        return yaml_file, md_file, icon_file
    except IndexError:
        logging.warning(f"ERROR: One of the necessary files was not found. "
                        f"Please check to see if your directory has the necessary files.")


def write_to_json(obj, path):
    with open(f"{path}/manifest.json", "w") as json_out:
        json.dump(obj, json_out, indent=4)


if __name__ == "__main__":
    main()
