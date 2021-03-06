# https://blog.csdn.net/qq_40155090/article/details/107459046
# https://www.cnblogs.com/drewgg/p/14956274.html

from http import server
from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from myapi import app
from tornado.ioloop import IOLoop
import ssl



ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_ctx.load_cert_chain('C:\\SSL_TOOL\\secret\\certificate.crt',
                        'C:\\SSL_TOOL\\secret\\private.key')



s = HTTPServer(WSGIContainer(app),ssl_options=ssl_ctx)
s.listen(443) 
IOLoop.current().start()


