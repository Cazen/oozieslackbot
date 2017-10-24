#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from slackbot.bot import respond_to

from action.commonUtil import *
from slackbot_settings import *


@respond_to('ocrlist', re.IGNORECASE)
@respond_to('Coordinator(.*)', re.IGNORECASE)
def slack_respont_ocrlist(message):
    outputRows = output_utf8(run_command(OOZIE_JOBS + "-jobtype coordinator -filter status=RUNNING | grep ooz"))
    fieldList = []
    for row in outputRows:
        fieldDict = {'title': row.split()[1].split("_201")[0], 'value': row.split()[0]}
        fieldList.append(fieldDict)

    attachments = assemble_attachment("fields", fieldList)
    message.send_webapi('실행중인 Coordinator List를 조회합니다', attachments)


@respond_to('owrlist', re.IGNORECASE)
@respond_to('Workflow(.*)', re.IGNORECASE)
def slack_respont_owrlist(message):
    outputRows = output_utf8(run_command(OOZIE_JOBS + "-jobtype wf -filter status=RUNNING | grep ooz"))
    fieldList = []
    for row in outputRows:
        fieldDict = {'title': row.split()[1].split("RUNNING")[0], 'value': row.split()[0]}
        fieldList.append(fieldDict)

    attachments = assemble_attachment("fields", fieldList)
    message.send_webapi('실행중인 Workflow List를 조회합니다', attachments)


@respond_to('oinfo (.*)', re.IGNORECASE)
def slack_respont_oinfo(message, jobId):
    outputRows = output_utf8(run_command(OOZIE_JOB + "-info " + jobId + " | grep -v '\-\-\-' | grep -v App"))
    fieldRows = """"""
    for row in outputRows:
        fieldRows = fieldRows + row[0:120].replace("  ", " ") + "\n"

    attachments = assemble_attachment("text", fieldRows)
    message.send_webapi("요청하신 " + jobId + " Log를 조회합니다", attachments)


@respond_to('occ (.*) (.*)', re.IGNORECASE)
def slack_respont_occ(message, jobId, concurrencyNum):
    output_utf8(run_command(OOZIE_JOB + "-change " + jobId + " -value concurrency=" + concurrencyNum))
    message.send_webapi("요청하신 " + jobId + " 의 Concurrency를 변경합니다. 변경 후 값 : " + concurrencyNum)


@respond_to('okill (.*)', re.IGNORECASE)
def slack_respont_okill(message, jobId):
    output_utf8(run_command(OOZIE_JOB + "-kill " + jobId))
    message.send_webapi("요청하신 " + jobId + " 를 Kill 진행하였습니다")


@respond_to('orerun (.*) (.*)', re.IGNORECASE)
def slack_respont_oinfo(message, jobId, jobNum):
    outputRows = output_utf8(run_command(OOZIE_JOB + "-rerun " + jobId + " -action " + jobNum + " | grep oozie"))
    for row in outputRows:
        message.send_webapi("요청하신 잡을 재수행하였습니다 = " + row)

@respond_to('cpu사용량(.*)', re.IGNORECASE)
def slack_respont_cpuutilization(message, given):
    outputRows = output_utf8(run_command("/usr/bin/sar -u | grep -Ev 'CPU|Average' | tail -n 20 | awk '{print $1\" \"100-$9}'"))
    fieldRows = """"""
    image_url = IMG_URL
    for row in outputRows:
        if len(str(row)) != 0:
            fieldRows = fieldRows + row.replace(":01", "        ") + "%\n"
            image_url = image_url + row.split(" ")[1] + ","

    attachments = assemble_attachment("image_url", image_url[:-1], "text", fieldRows)
    message.send_webapi("요청하신 최근 3시간 Cpu 사용량을 조회합니다", attachments)


@respond_to('mem사용량(.*)', re.IGNORECASE)
def slack_respont_memutilization(message, given):
    outputRows = output_utf8(run_command("/usr/bin/sar -r | grep -Ev 'mem|Average|Linux' | tail -n 20 | awk '{print $1\" \"$5}'"))
    fieldRows = """"""
    image_url = IMG_URL
    for row in outputRows:
        if len(str(row)) != 0:
            fieldRows = fieldRows + row.replace(":01", "        ") + "%\n"
            image_url = image_url + row.split(" ")[1] + ","

    attachments = assemble_attachment("image_url", image_url[:-1], "text", fieldRows)
    message.send_webapi("요청하신 최근 3시간 Memory 사용량을 조회합니다", attachments)


