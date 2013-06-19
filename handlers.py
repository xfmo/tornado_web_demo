#!/usr/bin/env python
#-*-coding:utf-8-*-

#python import
import os
import re
import sys
import time
import json

#tornado import
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.web import url
from tornado.web import RequestHandler
from tornado.options import define
from tornado.options import options

#local import
from models.base import  *

#models
class BaseHandler(RequestHandler):
    @property
    def db(self):
        return self.application.db

    def render_json(self,obj):
        self.set_header('Content-Type','application/json')
        try:
            rc=json.dumps(obj)
            self.write(rc)
        except:
            raise tornado.web.HTTPError(500)

class IndexHandler(BaseHandler,UserMixin):
    def get(self):
        print self.get_user_count()
        self.render('index.html')
    def post(self):
        data=self.get_argument('id',None)
        print data
        res=json.loads(data)
        
        print 'result',res
        print ' ok',res[0]['name']
#        decodejson=json.loads(data)
#        print type(decodejson)

