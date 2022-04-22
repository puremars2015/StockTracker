# https://blog.csdn.net/qq_40155090/article/details/107459046
# https://www.cnblogs.com/drewgg/p/14956274.html

from http import server
from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
import app
from tornado.ioloop import IOLoop
import ssl



ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_ctx.load_cert_chain('C:\\SSL_TOOL\\secret\\certificate.crt',
                        'C:\\SSL_TOOL\\secret\\private.key')



a = HTTPServer(WSGIContainer(app.app))

s = HTTPServer(a,ssl_options=ssl_ctx)


# a.bind(5000,"0.0.0.0")
s.listen(443) 



IOLoop.current().start()