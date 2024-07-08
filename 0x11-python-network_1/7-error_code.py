#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    status_code = req.status_code

    if status_code >= 400:
        print("Error code: {}".format(status_code))
    else:
        print(req.text)
