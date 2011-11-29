import sys
sys.path.append("/home/stanislavfeldman/projects/python/kiss.py/")
sys.path.append(".")
from kiss.core.application import Application
from settings import options

app = Application(options)
app.start()
