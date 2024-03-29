#!/usr/bin/python3
"""takes in a URL, sends a request to the URL"""
from sys import argv
import requests


if __name__ == '__main__':
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
