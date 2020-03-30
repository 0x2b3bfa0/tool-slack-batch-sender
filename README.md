# Slack direct message sender
A simple script for privately sending the same message to lots of users.

## Installation

    pip3 install -r requirements.txt

## Configuration

1. Get your legacy token from https://api.slack.com/legacy/custom-integrations/legacy-tokens
2. Place the generated token into [`token.key`](/token.key)
3. Add newline-separated users inside[`users.list`](/users.list)
4. Copy the message into [`message.md`](/message.md)

## Execution

    python3 send.py
