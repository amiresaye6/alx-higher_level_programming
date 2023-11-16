#!/usr/bin/env bash

chmod +x *.py
pycodestyle *.py


git add .
git commit -m "init mandatory"
git push
