#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

def getTime():
    year = time.localtime(time.time()).tm_year
    print year

getTime()