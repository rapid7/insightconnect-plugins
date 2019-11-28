import os
from help_update import HelpUpdate


def main():
    subdirs = list(filter(lambda d: os.path.isdir(d), os.listdir(".")))
    base_path = os.getcwd()

    for d in subdirs:
        os.chdir(os.path.join(base_path, d))
        try:
            output = HelpUpdate.convert()
        except Exception:
            continue
        if output is not None:
            with open("./help.md", "w") as h:
                print("Writing for " + d)
                h.write(output)


if __name__ == '__main__':
    main()
