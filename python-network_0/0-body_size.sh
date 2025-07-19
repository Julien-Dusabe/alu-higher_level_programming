#!/bin/bash
# Displays the size (in bytes) of the body of the response from a given URL
curl -s -L -w "%{size_download}\n" "${1/#http:\/\/}" -o /dev/null
