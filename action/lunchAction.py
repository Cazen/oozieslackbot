#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from slackbot.bot import respond_to

from action.commonUtil import *
from slackbot_settings import *
import urllib.request, json

@respond_to('메뉴', re.IGNORECASE)
@respond_to('menu', re.IGNORECASE)
def slack_respont_lunchmenu(message, *args):
    outputJson = json.loads(urllib.request.urlopen("https://dela-mini.firebaseio.com/delacourt/jamsil.json").read())
    attachments = []
    for rowJson in outputJson["menus"]:
        if rowJson["zoneId"] == "B1":
            attachmentsDict = {
                "title": rowJson["name"]
            }
            if "imgSrc" in rowJson:
                attachmentsDict["thumb_url"] = rowJson["imgSrc"]
            attachments.append(attachmentsDict)

    message.send_webapi(outputJson["time"] + 'B1층 메뉴를 출력합니다', attachments)

    attachments = []
    for rowJson in outputJson["menus"]:
        if rowJson["zoneId"] == "B2":
            attachmentsDict = {
                "title": rowJson["name"]
            }
            if "imgSrc" in rowJson:
                attachmentsDict["thumb_url"] = rowJson["imgSrc"]
            attachments.append(attachmentsDict)
    if len(attachments) != 0:
        message.send_webapi(outputJson["time"] + 'B2층 메뉴를 출력합니다', attachments)


