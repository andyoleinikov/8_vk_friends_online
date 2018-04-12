# Watcher of Friends Online

With this script you can see who of your VK friends is online right in the command line. To recieve **APP_ID** you need to create a standalone app on [VK apps page](https://vk.com/apps?act=manage).

# Quickstart

You need to enter login and password after starting the script. You can change **APP_ID** in **settings.py** file.

### Examples of script launch on Linux, Python 3.5:

```bash

$ python vk_friends_online.py
Login: <your login>
Password: <your password>
Your friends online:
Some One
Someone Else
And So On

```

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
