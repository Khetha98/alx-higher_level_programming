#!/bin/bash
# sends the JSON POST request to URL, and displays the body of a response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
