#!/bin/bash
# Makes the request to 0.0.0.0:5000/catch_me which gets the message "You got me!".
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
