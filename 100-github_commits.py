#!/usr/bin/python3
"""
A script that prints the commit of a repository
and the person that commited them
"""
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]

    url = f"https://api.github.com/repos/{user}/{repo}/commits?per_page=10"

    request = requests.get(url)
    commits = request.json()

    for commit in commits:
        commit_data = commit['commit']
        author = commit_data['author']['name']
        sha = commit['sha']
        print("{}: {}".format(sha, author))
