#!/bin/bash

# Run this every time the game is updated
# ./listPlayers.sh > ./listPlayers.txt

grep -oP 'ask_character\("\K[^"]+(?="\))' game.py | sort -u
