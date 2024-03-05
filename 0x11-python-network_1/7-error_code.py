#!/usr/bin/python3
"""script that sends a request to a given URL and displays the response body.
"""
import sys
import requests


if __name__ == "__main__":
    u = sys.argv[1]

    req = requests.get(u)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
