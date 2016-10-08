#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.frontend.index import *

url = [
    (r'/', IndexHandler),
    (r'/about', AboutHandler),
    (r'/product', ProductHandler),
    (r'/recruit', RecruitHandler),
    (r'/job/([0-9a-fA-F]{8,})?', JobInfoHandler),
    (r'/software', SoftwareHandler),
    (r'/hardware', HardwareHandler),
    (r'.*', PageNotFoundHandler),
]
