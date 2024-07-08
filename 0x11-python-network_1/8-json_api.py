#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    req = requests.post(url, data={'q': q})

    try:
        json_req = req.json()
        if json_req:
            print("[{}] {}".format(json_req.get('id'), json_req.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
