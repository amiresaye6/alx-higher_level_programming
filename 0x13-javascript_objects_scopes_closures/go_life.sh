#!/usr/bin/env bash

// change mode to executable
chmod +x *.js

// checkign the styling of the code
semistandard *.js

// adding, commiting, and pushing to github.
git add .
git commit -m "inint commit"
git push
