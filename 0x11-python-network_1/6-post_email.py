#!/usr/bin/python3
"""
It a script that takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the body
of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":
    u = argv[1]
    value_ = {"email": argv[2]}
    r = requests.post(u, data=value_)

    print(r.text)
