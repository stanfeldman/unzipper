from kiss.views.templates import TemplateResponse
from kiss.views.base import Response
import os
from zipfile import *
from models.models import *
		
class Controller(object):
	def __init__(self):
		self.tmp_file_path = './tmp_file.zip'
		
	def get(self, request):
		return TemplateResponse("view.html")
	
	def post(self, request):
		file = request.files.get('zipfile')
		file.save(self.tmp_file_path)
		archive = None
		with ZipFile(self.tmp_file_path, "r") as myzip:
			archive = Archive(name=file.filename)
			archive.save()
			for item in myzip.namelist():
				archive_item = ArchiveItem(name=item, archive=archive)
				archive_item.save()
		os.remove(self.tmp_file_path)
		return TemplateResponse("view.html", {"archive": archive, "items": ArchiveItem.objects(archive=archive)})
