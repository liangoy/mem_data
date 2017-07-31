import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import urllib
import base64
import json

from tornado.options import define, options

import requests
import mem_data

define("port", default=1320, help="run on the given port", type=int)

table=mem_data.Mem_table()
table=table.mem_table
var={}


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        parameter=self.get_argument("parameter")
        
        self.data='OK'
        shell=base64.urlsafe_b64decode(parameter.encode('utf-8')).decode('utf-8')
        exec(shell)
        print(table)
        self.write(self.data)



        
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
