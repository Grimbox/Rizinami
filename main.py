import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/peerReview" method="post">
		<div>Activity number <input type="text" name="reviewName" cols="60" /></div>
		<div>Activity Date (format YYYY-MM-DD)<input type="text" name="reviewDate" cols="60" /></div>
                <div><textarea name="content" rows="10" cols="60"></textarea></div>
                <div><input type="submit" value="Send data"></div>
              </form>
            </body>
          </html>""")


class PeerReview(webapp.RequestHandler):
	def post(self):
		activityNumber = cgi.escape(self.request.get('reviewName')).upper()
		activityDate = cgi.escape(self.request.get('reviewDate'))
		content = cgi.escape(self.request.get('content'))
		content = content.split()
		
		self.response.out.write('<html><body>You wrote:')
		self.response.out.write('<ul>')
		
		for rz in content:
			self.response.out.write('<li>' + activityNumber + ';' + rz + ';;1;1;' + activityDate + '</li>')
		
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