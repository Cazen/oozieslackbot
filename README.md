[![PyPI](https://badge.fury.io/py/slackbot.svg)](https://pypi.python.org/pypi/slackbot)

A chatbot for [Slack](https://slack.com) using [slackbot](https://github.com/lins05/slackbot)

## Features

* Based on slack [Real Time Messaging API](https://api.slack.com/rtm)
* Listing coordinator & workflow jobs
* Rerunning job and modify concurrency
* Monitoring cpu utilization and memory usage
* Python3 Support

## Installation & Start


```
pip install slackbot
python3 run.py
```

## Usage

### Generate the slack api token

First you need to get the slack api token for your bot. You have two options:

1. If you use a [bot user integration](https://api.slack.com/bot-users) of slack, you can get the api token on the integration page.
2. If you use a real slack user, you can generate an api token on [slack web api page](https://api.slack.com/web).


##### Configure the api token

Then you need to configure the `API_TOKEN` in a python module `slackbot_settings.py`, which must be located in a python import path. This will be automatically imported by the bot.

slackbot_settings.py:

```python
API_TOKEN = "<your-api-token>"
```

Alternatively, you can use the environment variable `SLACKBOT_API_TOKEN`.

