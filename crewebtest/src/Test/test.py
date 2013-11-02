import webapp2
import jinja2
from google.appengine.ext import db
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Table (db.Model):
    element = db.StringProperty()

class Index(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
