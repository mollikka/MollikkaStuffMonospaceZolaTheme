#!/bin/bash

THEME_DIRECTORY=$(dirname $0)
echo $THEME_DIRECTORY

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

zola serve &

wait
