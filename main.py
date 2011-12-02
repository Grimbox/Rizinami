import cgi
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from django.http import HttpResponse

import datetime

class MainPage(webapp.RequestHandler):
    def get(self): 
    	templates_values = {'version':'0.1'}
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
		
		meds = [ Medic(rz) for rz in content.split()]

		content = ''

		for med in meds:
			content += unicode(activityNumber) + ';' + unicode(med) + ';;1;1;' + unicode(activityDate) + '\r\n'

		self.response.headers['Content-Type'] = 'text/csv'
		self.response.headers['Content-Disposition'] = 'attachment; filename=%s'%self.generateFilename()
		self.response.out.write(content)
	
	""" Verifies a Riziv/Inami number against the check digit.
	"""
	def checkRIZIV(self, number):
		pass

	""" return a representation of 'now' according to file name standard.
		eg. 
			1st of december 2011 @ 2h00 will result in 'PeerReview_2011-12-01_0200.txt'
	"""
	def generateFilename(self):
		return datetime.datetime.now().strftime("PeerReview_%Y-%m-%d_%H%M.txt")

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/peerReview', PeerReview)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()