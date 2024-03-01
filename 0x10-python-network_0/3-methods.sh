#!/bin/bash
# Used to Display all HTTP methods the server of given URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
