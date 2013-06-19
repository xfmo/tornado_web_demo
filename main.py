#!/usr/bin/env python
#-*-coding:utf-8-*-
#python
import os

#tornado 
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define
from tornado.options import options
from tornado.web import url

#sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

#local
from databases  import  database 
from handlers import *
from config import *

#options
define("port",default=8080,help="listen port",type=int)
define("debug",default=False,help="enable debug mode",type=bool)
define("process",default=0,help="fork process number",type=int)
define("init",default=False,help="init tables",type=bool)
define("clean",default=False,help="clean tables",type=bool)

CURRENT_PWD=os.path.dirname(__file__)
#database engine
engine=create_engine(DATABASE_URL,encoding="utf-8",echo=options.debug)

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
        #db 
        self.db=scoped_session(sessionmaker(bind=engine))

def main():
    global http_server
    tornado.options.parse_command_line()
    
    if options.clean==True:
        database.clean_db(engine)
        return 
    
    if options.init==True:
        database.init_db(engine)
        return

    http_server=tornado.httpserver.HTTPServer(Application(),xheaders=True)
    if options.debug==True:
        http_server.listen(options.port)
    else:
        http_server.bind(options.port)
        http_server.start(num_processes=options.process)

    tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
    main()
