#!/usr/bin/env bash

semistandard --fix *.js
betty *.c
pystypycodestyle *.py

git add .
git commit -m "debug"
git push
