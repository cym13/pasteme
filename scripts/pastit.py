#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pasteme's client

Usage: pastit [-u url] [FILE]

Arguments:
    FILE    File to send
            If missing, reads from stdin
            If FILE is an url, then the corresponding file
            is downloaded and written on stdout.

Options:
    -u, --url url   Alternate url of the pasteme
                    Default is http://paste.devys.org/
"""

import sys
import requests
from docopt import docopt


def post(text, url):
    try:
        req = requests.post(url, data={"content":text})
    except BaseException as e:
        manage(e, url)
    return req.url


def get(url):
    if not url.endswith("/raw"):
        url += "/raw"

    try:
        req = requests.get(url)
    except BaseException as e:
        manage(e, url)

    if req.status_code == 404:
        return "Paste not found"
    elif not req.ok:
        return "An error occured (%s)" % req.status_code

    return req.text


def manage(excep, url=None):
    try:
        raise excep
    except requests.exceptions.ConnectionError as e:
        sys.exit(e)
    except (requests.exceptions.InvalidURL,
            requests.exceptions.InvalidSchema) as e:
        print("Invalid URL: %s" % url, file=sys.stderr)
        if not url.startswith("http"):
            print("Perhaps you meant http://%s" % url, file=sys.stderr)
        sys.exit(1)



def main():
    args = docopt(__doc__)

    if args["FILE"] and '://' in args["FILE"]:
        print(get(args["FILE"]))
        return


    url = args["--url"] or "http://paste.devys.org/"

    if args["FILE"]:
        try:
            text = open(args["FILE"]).read()
        except (FileNotFoundError,PermissionError) as e:
            exit(e)
    else:
        text = sys.stdin.read()

    print(post(text, url))


if __name__ == "__main__":
    main()
