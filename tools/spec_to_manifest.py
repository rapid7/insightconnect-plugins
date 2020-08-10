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
        logging.warning('ERROR: Insufficient parameters')

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

    # Extension -- mandatory
    # In this case, only workflows
    extension_type = yaml_obj.get("extension")
    extension_obj = {"type": extension_type}
    if extension_type == "workflow":
        extension_obj[extension_type] = yaml_obj.get("name") + ".icon"
    # if extension_type == plugin....

    manifest_obj["extension"] = extension_obj

    # ID -- mandatory
    # From yaml
    manifest_obj["id"] = yaml_obj.get("name")

    # Title -- mandatory
    # From yaml
    manifest_obj["title"] = yaml_obj.get("title")

    # Description -- Mandatory
    # from yaml
    manifest_obj["tagline"] = yaml_obj.get("description")

    # Overview -- mandatory
    # Tricky extraction of overview from .md
    # For now, keep as blank
    manifest_obj["overview"] = ""

    # Key Features -- mandatory
    # From .md, for now, keep as blank
    manifest_obj["key_features"] = []

    # Requirements -- Optional
    # Tricky reading from .md, due to different formatting....
    # Keep blank for now
    manifest_obj["requirements"] = []

    # Resources -- optional
    # Don't know where to pull this info from.....
    manifest_obj["resources"] = []

    # Version -- optional
    # Directly from yaml, parsed as string in manifest
    manifest_obj["version"] = str(yaml_obj.get("version"))

    # Version History....
    # Should be from .md -- need to parse
    manifest_obj["version_history"] = []

    # Publisher -- mandatory
    # "Vendor" field from yaml
    manifest_obj["publisher"] = yaml_obj.get("vendor")

    # Support -- mandatory
    # from yaml if R7, where to get info on "community" support?
    if yaml_obj.get("support") == "rapid7":
        support_obj = {"type": "publisher", "url": "http://www.rapid7.com/discuss"}
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
    # Different rules for workflows, plugins, etc....Workflows --> need orchestrator
    if extension_type == 'workflow' or extension_type == 'plugin':
        cloud_ready = yaml_obj.get("cloud_ready")
        if not yaml_obj.get('cloud_ready'):
            manifest_obj["required_rapid7_features"] = ["orchestrator"]
        else:
            manifest_obj["required_rapid7_features"] = []

    # Status -- optional
    # From yaml
    manifest_obj["status"] = yaml_obj.get("status")

    # Logos -- optional
    # Not sure what this would mean for a workflow....
    manifest_obj["logos"] = {}

    # Display Options -- mandatory
    # No sense of this in spec.....
    manifest_obj["display_options"] = []

    # Tags -- Mandatory
    # Converting from yaml
    hub_tags = yaml_obj.get("hub_tags")

    # Tags.categories -- Mandatory
    categories = hub_tags.get("use_cases")

    # Tags.third_party_products -- optional
    # Is this in tha YAML????
    third_party_products = []

    # Tags.keywords -- optional
    keywords = hub_tags.get("keywords")
    manifest_obj["tags"] = {"categories": categories, "third_party_products": third_party_products,
                            "keywords": keywords}

    # Documentation -- optional
    # Not entirely sure how to handle this either, not in yaml
    manifest_obj["documentation"] = []

    # Media -- optional
    # Small conversions from yaml
    screenshots = yaml_obj.get("resources").get("screenshots")
    if screenshots:
        media_list = []
        for media in yaml_obj.get("resources").get("screenshots"):
            image_pattern = r'\S+\.(?:png|jpe?g)'
            video_pattern = r'\S+\.(?:mp4)'
            type_of_media = ""
            if re.match(image_pattern, media['name']):
                type_of_media = "image"
            if re.match(video_pattern, media['name']):
                type_of_media = "video"
            media_info = {"source": media.get('name'), "title": media.get('title'), 'type': type_of_media}
            media_list.append(media_info)
        manifest_obj['media'] = media_list

    # Links -- optional
    # Conversion from yaml
    src = ""
    lic = ""
    if yaml_obj.get('resources'):
        resources = yaml_obj.get('resources')
        if resources.get('source_url'):
            src = resources['source_url']
        if resources.get('license_url'):
            lic = yaml_obj['resources']['license_url']

        manifest_obj['links'] = {'source_url': src, 'license_url': lic}

    # Processing Instructions -- optional
    # No sense of this in yaml...
    manifest_obj['processing_instructions'] = []

    return manifest_obj


def verify_yaml(file):
    return file and re.match(r'^\S*workflow.spec.yaml$', file)


def open_and_read_spec(file):
    spec_file = open(file)
    loaded_spec = yaml.safe_load(spec_file)
    return loaded_spec


def write_to_json(obj, path):
    with open(path + "/manifest.json", 'w') as json_out:
        json.dump(obj, json_out, indent=4)


if __name__ == '__main__':
    main()
