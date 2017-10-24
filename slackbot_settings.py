#!/usr/bin/python
# -*- coding: utf-8 -*-

API_TOKEN = ""
DEFAULT_REPLY = "죄송합니다 무슨 말인지 모르겠어요"
PLUGINS = [
    'slackbot.plugins',
]
OOZIE_ADDR = "http://localhost:11000/oozie "
OOZIE_COMD = "/home/bpsec/oozie/bin/oozie "
OOZIE_JOBS = OOZIE_COMD + "jobs -oozie "  + OOZIE_ADDR
OOZIE_JOB  = OOZIE_COMD + "job -oozie "  + OOZIE_ADDR
IMG_URL    = "https://chart.googleapis.com/chart?chs=350x350&cht=lc&chco=0033FF&chxt=y&chd=t:"
