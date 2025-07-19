#!/bin/bash
# Displays the size (in bytes) of the body of the response from a given URL
curl -s -w "%{size_download}" "$1" -o /dev/null
