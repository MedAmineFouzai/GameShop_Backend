
'''
The main server file
'''
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os
import torn

from routes import *
settings = dict(
		debug=torn.Debug(),
		cookie_secret="TODO",
		login_url="/login"
	)

application = Application(route, **settings)

if __name__ == "__main__":
	server = HTTPServer(application)
	server.listen(os.environ.get('PORT'))
	IOLoop.current().start()

					
