#!/usr/bin/env bash

semistandard --fix *.js
chmod u+x *.js

git add .
git commit -m "debug"
git push
