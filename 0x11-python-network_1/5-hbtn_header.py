#!/usr/bin/python3
"""
It a script that takes in a URL, sends a request to a URL and displays the
value of the variable X-Request-Id in the response header.
"""
import requests
from sys import argv


if __name__ == "__main__":
    u = argv[1]
    r = requests.get(u)

    print(r.headers.get("X-Request-Id"))
