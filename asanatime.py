#def app(environ, start_response):
#      data = "Hello, World!\n"
#      start_response("200 OK", [
#          ("Content-Type", "text/plain"),
#          ("Content-Length", str(len(data)))
#      ])
#      return iter([data])

import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, world!"

application = web.application(urls, globals()).wsgifunc()
