import os
import re


def main():
    subdirs = list(filter(lambda d: os.path.isdir(d), os.listdir(".")))
    base_path = os.getcwd()

    for d in subdirs:
        spec_path = os.path.join(base_path, d, "plugin.spec.yaml")
        try:
            output = update_source_url(spec_path, d)
        except Exception:
            continue
        if output is not None:
            with open(spec_path, "w") as h:
                print("Writing for " + d)
                h.write(output)


def update_source_url(spec_path, plugin_name):
    source_url = f"https://github.com/rapid7/insightconnect-plugins/tree/master/{plugin_name}"
    license_url = "https://github.com/rapid7/insightconnect-plugins/blob/master/LICENSE"
    new_resources = f"""resources:
  source_url: {source_url}
  license_url: {license_url}
"""
    pattern = "(resources:[\s\S]*)tags:"
    with open(spec_path, 'r') as spec:
        content = spec.read()
    match = re.findall(pattern, content)[0]
    content = content.replace(match, new_resources, 1)
    return content


if __name__ == '__main__':
    main()