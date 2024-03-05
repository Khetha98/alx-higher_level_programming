#!/usr/bin/python3
"""
It a script takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of a response.
"""
from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    u = argv[1]
    r = Request(u)

    with urlopen(r) as response:
        print(dict(response.headers).get("X-Request-Id"))
