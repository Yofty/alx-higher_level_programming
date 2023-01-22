#!/usr/bin/python3
"""takes in url and send a request"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(arv[1]) as response:
            s = response.read()
            print(s.decode('UTF-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
