#!/bin/bash

# Run this every time the game is updated
# ./listPlayers.sh > ./listPlayers.txt

grep -oP 'ask_character\(\s*"\K[^"]+(?="\s*\))' game.py | sort -u
