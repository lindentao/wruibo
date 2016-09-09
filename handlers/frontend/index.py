#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('about.html')

class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('error.html')