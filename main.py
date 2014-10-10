import os
import urllib
import datetime
 
from google.appengine.api import users
from google.appengine.ext import ndb
 
import jinja2
import webapp2
import logging
from google.appengine.api import urlfetch
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

 
FACEBOOK_APP_ID = "839210319436433"
FACEBOOK_APP_SECRET = "cbeeee3e0e9594e802d44a1016f23569"
class User(ndb.Model):
 	user_id = ndb.StringProperty(required=True)
 	access_token = ndb.StringProperty(required=True)
 
class Posts(ndb.Model):
     user_id = ndb.StringProperty(required=True)
     access_token = ndb.StringProperty(required=True)
     message = ndb.StringProperty(required=True)
     date_to_post = ndb.DateProperty()
     date_created = ndb.DateProperty()
 
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/main.html')
        self.response.write(template.render())
    def post(self):
         data = {
                     "method": "post",
                     "message": self.request.get("message"),
                     "access_token": self.request.get("access_token")
                 };
         form_data = urllib.urlencode(data)
         url = "https://graph.facebook.com/v2.1/me/feed"
         result = urlfetch.fetch(url=url,payload=form_data,method=urlfetch.POST,headers={'Content-Type': 'application/x-www-form-urlencoded'})
         self.redirect("/")
         result = urlfetch.fetch(url=url,payload=form_data,method=urlfetch.POST)
         content = json.loads(result.content)
         
         if(content.get("id")):
           self.response.write('<script>alert("Message posted to facebook.");window.location.assign("/")</script>')
         elif content["error"]["error_user_title"]:
            self.response.write('<script>alert("'+content["error"]["error_user_title"]+'");window.location.assign("/")</script>')
         else:
            self.response.write('<script>alert("An error occured.");window.location.assign("/")</script>')
     	
application = webapp2.WSGIApplication([
     ('/', MainHandler),
], debug=True)