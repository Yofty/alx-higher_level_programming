#!/bin/bash
#ends a request
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
