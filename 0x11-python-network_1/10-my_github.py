#!/usr/bin/python3
"""
A script that takes your GitHub credentials (username
and password) and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    req = requests.get(url, auth=HTTPBasicAuth(username, token))
    json_req = req.json()

    if json_req:
        print("{}".format(json_req.get('id')))
