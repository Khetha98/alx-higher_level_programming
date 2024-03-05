#!/usr/bin/python3
"""
It a script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    u = "https://intranet.hbtn.io/status"
    r = requests.get(u)
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
