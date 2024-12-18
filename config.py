#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8182324584:AAFy2bcf-IOZZvM6SkpSuXgxb3d4GsD_RM8")
    API_ID = int(os.environ.get("API_ID", "23671274"))
    API_HASH = os.environ.get("API_HASH", "09b9c07a023f7c13c2164f2b22bd937e")
    AUTH_USERS = "903077627"

