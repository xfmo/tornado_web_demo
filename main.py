#!/usr/bin/env python
#-*-coding:utf-8-*-
import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define
from tornado.options import options
from tornado.web import url

#local
from handlers import *

#options
define("port",default=8080,help="listen port",type=int)
define("debug",default=False,help="enable debug mode",type=bool)
define("process",default=0,help="fork process number",type=int)

CURRENT_PWD=os.path.dirname(__file__)
#application
class Application(tornado.web.Application):
    def __init__(self):
        handlers=[('/',IndexHandler),
                
                ]
        settings=dict(
                template_path=os.path.join(CURRENT_PWD,"templates"),
                static_path=os.path.join(CURRENT_PWD,"static"),
                debug=options.debug

                )
        tornado.web.Application.__init__(self,handlers,**settings)

def main():
    global http_server
    tornado.options.parse_command_line()
    
    http_server=tornado.httpserver.HTTPServer(Application(),xheaders=True)
    if options.debug==True:
        http_server.listen(options.port)
    else:
        http_server.bind(options.port)
        http_server.start(num_processes=options.process)

    tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
    main()
