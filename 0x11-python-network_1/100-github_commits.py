#!/usr/bin/python3
"""list the 10 most recent commits on given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    u = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(u)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
