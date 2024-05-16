# Zendesk Time Tracker

A way to track time spent on effort around zendesk objects.

## Features

### Normal Operation

1. If not logged in, present a login screen.
2. Pull active 'X' objects to track (X is configurable to a field, in config file)
3. Draw into multiple buttons.
4. To start tracking time, click on a button.
5. Unclick to stop tracking time.

### Edit time tracked

1. Click on EDIT
2. Checkbox a time you want to remove.
3. CLick remove to confirm

### Refreshing Objects

1. A "refresh" button to get latest "X" objects.
2. That refresh button re-draws the homepage.
3. It does not disturb the ongoing timer if exists
4. Redirects to log in to Zendesk if existing session is broken

## Installation

...

## Configuration

1. Need config file OR an env variable. $ZENDESK_API_TOKEN
2. Config File
    1. URL of Zendesk tenant
    2. Object to track (X)