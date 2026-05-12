#!/bin/bash

THEME_DIRECTORY=$(dirname $0)
echo $THEME_DIRECTORY

# Create buildinfo
GIT_COMMIT=$(git rev-parse HEAD)
GIT_COMMIT_THEME=$(git -C $THEME_DIRECTORY rev-parse HEAD)
BUILD_TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

cat > content/buildinfo.md <<EOF
+++
title = "Build Info"
template = "buildinfo.html"
[extra]
site_commit = "$GIT_COMMIT"
theme_commit = "$GIT_COMMIT_THEME"
timestamp = "$BUILD_TIME"
+++
EOF

# Function to kill background processes when the script exits
cleanup() {
  echo "Cleaning up..."
  # Kill all background processes
  kill $(jobs -p)
}
trap cleanup EXIT

# Start services as background processes
python3 $THEME_DIRECTORY/renderserver/main.py &

sleep 1

zola build
