import cgi
import datetime
import urllib
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Greeting(db.Model):
	"""Models an individual Guestbook entry with an author, content and datetime"""
	author = db.UserProperty()
	content = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)
	
def guestbook_key(guestbook_name = None):
	"""Constructs a datastore key for a Guestbook entity with guestbook_name."""
	return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')
	
class MainPage(webapp.RequestHandler):
	def get(self):
		self.response.out.write('<html><body>')
		guestbook_name = self.request.get('guestbook_name')