#!/usr/bin/env python3
import contextlib
import json
import gzip
import os
import re
from collections import Counter
from nltk.tag import pos_tag
from nltk.tokenize import RegexpTokenizer


def load_files(dirname):
    files = list()
    for dirpath, dirnames, filenames in os.walk(dirname):
        for filename in [f for f in filenames if f.endswith(".md") or f.endswith(".yaml")]:
            print("found " + os.path.join(dirpath, filename))
            files.append(os.path.join(dirpath, filename))
    return files


@contextlib.contextmanager
def load_file(filename, encoding="utf-8"):
    if filename[-3:].lower() == ".gz":
        with gzip.open(filename, mode="rt", encoding=encoding) as file:
            yield file
    else:
        with open(filename, mode="r", encoding=encoding) as file:
            yield file


def export_word_frequency(filepath, word_frequency):
    with open(filepath, "w") as f:
        json.dump(word_frequency, f, indent="", sort_keys=True, ensure_ascii=False)


def build_word_frequency(dirpath, output_path):
    word_frequency = Counter()
    tok = RegexpTokenizer(r"\w+")

    rows = 0

    files = load_files(dirpath)

    for filepath in files:
        with load_file(filepath, "utf-8") as file:
            for line in file:
                line = re.sub("[^0-9a-zA-Z]+", " ", line)
                parts = tok.tokenize(line)
                tagged_sent = pos_tag(parts)
                words = [word[0].lower() for word in tagged_sent if word[0] and word[0][0].isalpha()]
                if words:
                    word_frequency.update(words)

                rows += 1

                if rows % 100000 == 0:
                    print("completed: {} rows".format(rows))

    print("completed: {} rows".format(rows))
    export_word_frequency(output_path, word_frequency)
    print("exported custom dictionary to {}".format(output_path))
    return word_frequency


def _parse_args():
    import argparse

    parser = argparse.ArgumentParser(description="Build a new custom dictionary for an InsightConnect Plugin")
    parser.add_argument("-p", "--path", help="The path to the plugin to build a custom dictionary for")

    args = parser.parse_args()

    # validate that we have a path, if needed!
    if not args.path:
        raise Exception("A path is required to generate a custom dictionary")

    if args.path:
        args.path = os.path.abspath(os.path.realpath(args.path))
        if not os.path.exists(args.path):
            raise FileNotFoundError("A valid path is required to generate a custom dictionary")

    return args


if __name__ == "__main__":
    args = _parse_args()
    script_path = os.path.dirname(os.path.abspath(__file__))
    export_path = os.path.abspath("{}/custom_dict.json".format(args.path))
    word_frequency = build_word_frequency(args.path, export_path)
