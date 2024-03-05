#!/usr/bin/python3
"""
It a script that takes in a URL, send a request to URL, and dispaly body
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as r:
            print(r.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
