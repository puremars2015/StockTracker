from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from myapi import app
from tornado.ioloop import IOLoop

s = HTTPServer(WSGIContainer(app))
s.listen(443) 
IOLoop.current().start()