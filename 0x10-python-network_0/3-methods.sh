#!/bin/bash
# A script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" | grep -i 'Allow' | cut -d " " -f 2-
