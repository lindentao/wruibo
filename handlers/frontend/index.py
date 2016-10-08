#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

from optsql.models import *

class BaseHandler(tornado.web.RequestHandler):
    pass

class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')

class AboutHandler(BaseHandler):
    def get(self):
        self.render('about.html')

class ProductHandler(BaseHandler):
    def get(self):
        self.render('product.html')

class RecruitHandler(BaseHandler):
    def get(self):
        jobs = []
        for job in Job.objects.order_by('-time'):
            jobs.append(job)
        self.render('recruit.html', jobs=jobs)

class JobInfoHandler(BaseHandler):
    def get(self, jid=None):
        job = Job.objects.get(pk=jid)
        self.render('job.html', job=job)

class SoftwareHandler(BaseHandler):
    def get(self):
        self.render('software.html')

class HardwareHandler(BaseHandler):
    def get(self):
        self.render('hardware.html')

class PageNotFoundHandler(BaseHandler):
    def get(self):
        self.render('error.html')


