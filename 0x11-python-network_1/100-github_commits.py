#!/usr/bin/python3
"""script lists 10 most recent commits at given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    u = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(u)
    commits = r.json()
    try:
        for j in range(10):
            print("{}: {}".format(
                commits[j].get("sha"),
                commits[j].get("commit").get("author").get("name")))
    except IndexError:
        pass