from kiss.views.templates import TemplateResponse
from kiss.views.base import Response
import os
from zipfile import *
		
class Controller(object):
	def __init__(self):
		self.tmp_file_path = './tmp_file.zip'
		
	def get(self, request):
		return TemplateResponse("view.html")
	
	def post(self, request):
		file = request.files.get('zipfile')
		file.save(self.tmp_file_path)
		namelist = []
		with ZipFile(self.tmp_file_path, "r") as myzip:
			for item in myzip.namelist():
				namelist.append(item)
		os.remove(self.tmp_file_path)
		return TemplateResponse("view.html", {"files": namelist})
