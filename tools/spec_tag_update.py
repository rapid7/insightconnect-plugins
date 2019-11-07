import os
import re


def main():
    subdirs = list(filter(lambda d: os.path.isdir(d), os.listdir(".")))
    base_path = os.getcwd()

    for d in subdirs:
        spec_path = os.path.join(base_path, d, "plugin.spec.yaml")
        try:
            output = update_tags(spec_path)
        except Exception:
            continue
        if output is not None:
            with open(spec_path, "w") as h:
                print("Writing for " + d)
                h.write(output)


def update_tags(spec_path):
    pattern = "tags:\n(?:-[^-^\n]*\n)*"
    with open(spec_path, 'r') as spec:
        content = spec.read()
    match = re.findall(pattern, content)[0]
    tags = ", ".join([tag.strip() for tag in match.split("-")[1:]])
    addition = f'''hub_tags:
  use_cases: []
  key_words: [{tags}]
  features: []
'''
    content = content.replace(match, match + addition, 1)
    return content


if __name__ == '__main__':
    main()
