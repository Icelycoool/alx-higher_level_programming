#!/usr/bin/python3
"""
A script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    req = requests.post(url, data={'email': email})
    print(req.text)
