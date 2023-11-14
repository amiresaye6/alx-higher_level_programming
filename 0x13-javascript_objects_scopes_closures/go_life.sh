#!/usr/bin/env bash

semistandard --fix *.js
chmod u+x *.js
pystypycodestyle *.py
betty *.c

git add .
git commit -m "debug"
git push
