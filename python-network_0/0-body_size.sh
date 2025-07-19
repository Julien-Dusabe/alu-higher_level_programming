#!/bin/bash
# Displays the size (in bytes) of the body of the response from a given URL
curl -s -L -w "%{size_download}\n" "http://localhost:$1/" -o /dev/null
