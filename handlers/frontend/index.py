#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    pass

class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')

class AboutHandler(BaseHandler):
    def get(self):
        self.render('about.html')

class PageNotFoundHandler(BaseHandler):
    def get(self):
        self.render('error.html')