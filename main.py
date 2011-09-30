import cgi
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self): 
    	templates_values = {'greetings':'Hello!', 'url':'http://rizinami.appspot.com'}
    	path = os.path.join(os.path.dirname(__file__), 'index.html')
    	self.response.out.write(template.render(path,templates_values))

class Medic():
	def __init__(self, rizivnummer):
		self.riziv = rizivnummer

	def __unicode__(self):
		return self.riziv

	def __str__(self):
		return self.riziv

class PeerReview(webapp.RequestHandler):
	def post(self):
		activityNumber = cgi.escape(self.request.get('reviewName')).upper()
		activityDate = cgi.escape(self.request.get('reviewDate'))
		content = cgi.escape(self.request.get('content'))
		content = content.split()
		
		self.response.out.write('<html><body>Results:')
		self.response.out.write('<ul>')
		
		meds = [ Medic(rz) for rz in content]

		for r in meds:
			self.response.out.write('<li>' + activityNumber + ';' + unicode(r) + ';;1;1;' + activityDate + '</li>')
		
		self.response.out.write('</ul>')
		self.response.out.write('</pre></body></html>')
	
	def checkRIZIV(self, number):
		return True

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/peerReview', PeerReview)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()