import json
from pprint import pprint
import sys
from xml.etree import ElementTree

def extract_from_opml(filename):
    results = []
    with open(filename, 'rt') as f:
        tree = ElementTree.parse(f)
    for node in tree.findall('.//outline'):
        url = node.attrib.get('xmlUrl')
        title = node.attrib.get('title')
        if url:
            results.append({"url":url,
                            "title":title})

    return json.dumps({"sources-rss": results}, indent=4)


if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print("No file supplied, exiting")
        exit()

    sources = extract_from_opml(sys.argv[1])
    print(sources)
