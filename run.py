#!/usr/bin/python
# -*- coding: utf-8 -*-

from slackbot.bot import Bot
from action import commonAction
from action import lunchAction


def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()


