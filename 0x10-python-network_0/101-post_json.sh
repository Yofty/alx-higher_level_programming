#!/bin/bash
# sends a JSON POST req
curl -sL -H "content-type:application/json" -d @"$2" -X POST "$1"
