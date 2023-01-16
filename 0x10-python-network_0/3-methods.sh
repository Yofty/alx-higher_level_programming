#!/bin/bash
# display all HTTP
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
