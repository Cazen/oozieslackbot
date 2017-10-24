#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess, json


# Using python pipe(sh)
def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True).splitlines()
    except subprocess.CalledProcessError as e:
        output = ["아이디를확인해주십시오 데이터가존재하지않습니다".encode()]
    return output


# For pre-processing the rows
def output_utf8(inputlist):
    for inputRow in inputlist:
        yield inputRow.decode("UTF-8")


# For assembling attachment
def assemble_attachment(*args):
    attachments = []
    attachmentsDict = {
        'fallback': 'A textual representation of your table data',
        "color": "#36a64f"
    }
    for arg1, arg2 in zip(args[::2], args[1::2]):
        attachmentsDict[arg1] = arg2
    attachments.append(attachmentsDict)
    return json.dumps(attachments)


