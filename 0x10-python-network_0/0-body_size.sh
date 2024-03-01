#!/bin/bash
# Used to Get the byte size of the HTTP response header for the given URL.
curl -s "$1" | wc -c
