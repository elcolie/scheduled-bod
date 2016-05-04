# scheduled-bod
REST UIH portal
## Introduction :
This program will listen to `UIH-scheduler` to proceed the local function.

## System requirement
Python 3.5.1

## Installation :
pip-compile requirement.in
pip install -r requirement.txt

## Setup :
Change host and port from localhost and 9000.
To any number you want. Ex: app.run(host=www.mml.com, port=987)

## Usage :
python main.py

## Customization:
Replace `print()` by any function instead of you want to be run when receive request method is 'POST'