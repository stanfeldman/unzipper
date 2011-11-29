from mongoengine import *

connect('unzipper')

class Archive(Document):
    name = StringField(max_length=120, required=True)
    
class ArchiveItem(Document):
    name = StringField(max_length=300, required=True)
    archive = ReferenceField(Archive)
