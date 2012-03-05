import urllib2
from pyPdf.pyPdf import PdfFileReader
from StringIO import StringIO

class DownloadHelper(object):
	""""""
	
	def download(self, url, filename):		
		"""Code coming from http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
		Returns the file name for further processing"""

		# proxy settings
		proxy_support = urllib2.ProxyHandler({"http": "localhost:3128"})
		proxy_opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
		urllib2.install_opener(proxy_opener)

		#file_name = url.split('/')[-1]
		file_name = filename
		u = urllib2.urlopen(url)
		f = open(file_name, 'wb')
		meta = u.info()
		file_size = int(meta.getheaders("Content-Length")[0])
		
		print "Downloading: %s Bytes: %s" % (file_name, file_size)

		file_size_dl = 0
		block_sz = 8192
		while True:
		    buffer = u.read(block_sz)
		    if not buffer:
		        break

		    file_size_dl += len(buffer)
		    f.write(buffer)
		    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		    status = status + chr(8)*(len(status)+1)
		    print status,

		f.close()

		return file_name
		
if __name__ == "__main__":
	dl = DownloadHelper()
	dl.download('http://www.inami.be/care/fr/infos/qualification/pdf/Q_doctor.pdf', 'q_doctor_fr.pdf')
	dl.download('http://www.inami.be/care/nl/infos/qualification/pdf/Q_doctor.pdf', 'q_doctor_nl.pdf')
	dl.download('http://www.inami.fgov.be/care/fr/infos/qualification/pdf/Q_dentist.pdf', 'q_dentist_fr.pdf')
	dl.download('http://www.inami.fgov.be/care/nl/infos/qualification/pdf/Q_dentist.pdf', 'q_dentist_nl.pdf')