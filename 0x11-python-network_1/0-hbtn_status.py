#!/usr/bin/python3
"""A script that 
    - fetches https:intranet.htbn.io/status
    - uses urlib package
"""
import urllib.request
import urllib.parse


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.htbn.io/status') as response:
        content = response.read()
        print("Body response:")
        print('\t- type:', type(html))
        print('\t- content:', html)
        print('\t- utf8 content:' , html.decode('utf-8'))
