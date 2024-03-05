#!/usr/bin/python3
"""It a script fetching https://alx-intranet.hbtn.io/status."""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    r = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(r) as response:
        b = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(b)))
        print("\t- content: {}".format(b))
        print("\t- utf8 content: {}".format(b.decode("utf-8")))
