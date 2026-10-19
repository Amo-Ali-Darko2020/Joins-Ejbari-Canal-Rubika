#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "Installing Rubika Force Join Bot..."

pkg update -y
pkg install python -y

python -m pip install --upgrade pip
python -m pip install maxrubika

echo "Installation completed."
echo "Run the bot with: python bot.py"
