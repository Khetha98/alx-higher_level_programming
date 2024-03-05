#!/usr/bin/python3
"""script that sends a POST request to a given URL with a given email.
"""
import sys
import requests


if __name__ == "__main__":
    u = sys.argv[1]
    value_ = {"email": sys.argv[2]}

    r = requests.post(u, data=value_)
    print(r.text)
