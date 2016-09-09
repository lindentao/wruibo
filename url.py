#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.frontend.index import *

url = [
    (r'/', IndexHandler),
    (r'/about', AboutHandler),
    (r'/error', ErrorHandler),
]
