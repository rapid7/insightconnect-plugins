import json
import re
import sys
import yaml
import logging


def main():
    filename = ""
    path = ""
    correct_params = False
    try:
        filename = sys.argv[1]
        path = sys.argv[2]
        correct_params = True
    except IndexError:
        logging.warning("ERROR: Insufficient parameters")

    if correct_params:
        if verify_yaml(filename):
            spec = open_and_read_spec(filename)
            print("Read spec file at " + filename)
            json_obj = parse_fields(spec)
            print("Converted fields")
            write_to_json(json_obj, path)
            print("Wrote manifest at " + path)
        else:
            logging.warning("ERROR: Wrong file type specified")


def parse_fields(yaml_obj):
    # Manifest Version -- mandatory
    manifest_obj = {"manifest_version": 1}

    resources = yaml_obj.get("resources")
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
    manifest_obj["description"] = ""

    # Key Features -- mandatory
    # From .md
    manifest_obj["key_features"] = []

    # Requirements -- Optional
    # Tricky reading from .md, due to different formatting....
    manifest_obj["requirements"] = []

    # Resources -- optional
    # Pull from .md
    if resources:
        vendor_url = resources.get("vendor_url")
        if vendor_url:
            manifest_obj["resources"] = [{"text": "Vendor Website", "url":vendor_url}]
        else:
            # Append references --> links from .md
            manifest_obj["resources"] = []

    # Version -- optional
    # Directly from yaml, parsed as string in manifest
    manifest_obj["version"] = str(yaml_obj.get("version"))

    # Version History....
    # Should be from .md -- need to parse
    manifest_obj["version_history"] = []

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
            manifest_obj ["required_rapid7_features"] = ["orchestrator", "agent"]
        else:
            if not cloud_ready:
                manifest_obj["required_rapid7_features"] = ["orchestrator"]
            else:
                manifest_obj["required_rapid7_features"] = []

    # Status -- optional
    # From yaml
    manifest_obj["status"] = yaml_obj.get("status")

    # Logos -- optional
    manifest_obj["logos"] = {"primary": "extension.png", "secondary":[]}

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


def verify_yaml(file):
    return file and re.match(r"^\S*.spec.yaml$", file)


def open_and_read_spec(file):
    spec_file = open(file)
    loaded_spec = yaml.safe_load(spec_file)
    return loaded_spec


def write_to_json(obj, path):
    with open(path + "/manifest.json", "w") as json_out:
        json.dump(obj, json_out, indent=4)


if __name__ == "__main__":
    main()
