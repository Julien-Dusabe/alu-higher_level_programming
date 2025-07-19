#!/bin/bash
# 0-body_size.sh

# Takes a URL as first argument
url="$1"

# Use curl with -s for silent and -w '%{size_download}' to output body size
# We discard the actual body by redirecting output to /dev/null
curl -s -w "%{size_download}" "$url" -o /dev/null
echo
