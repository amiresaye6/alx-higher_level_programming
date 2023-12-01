#!/usr/bin/env bash
# checking style and pusshing to github repo

pycodestyle *.py

git add .
git commit -m "init"
git push
