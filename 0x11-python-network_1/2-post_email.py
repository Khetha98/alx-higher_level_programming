#!/usr/bin/python3
""" It a script that takes in a URL and an email, sends a POST request
 And displays the body of the response
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    u = sys.argv[1]
    value_ = {"email": sys.argv[2]}
    data_ = urllib.parse.urlencode(value_).encode("ascii")

    request = urllib.request.Request(u, data_)
    with urllib.request.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))
