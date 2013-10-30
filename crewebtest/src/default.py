import webapp2
import jinja2
import os
import TestForms.testForms
import HelloWorld.helloworld
import StaticFiles.template
import Templates.template

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):

    def get(self):
        
        template_values = {}

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
        ('/', MainPage),
        ('/testForms', TestForms.testForms.TestForms),
        ('/testForms/sign', TestForms.testForms.Guestbook),
        ('/helloWorld', HelloWorld.helloworld.HelloWorld),
        ('/staticFiles', StaticFiles.template.MainPage),
        ('/staticFiles/sign', StaticFiles.template.Guestbook),
        ('/templates', Templates.template.MainPage),
        ('/templates/sign', Templates.template.Guestbook)
        ], debug=True)
