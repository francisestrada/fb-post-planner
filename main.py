import webapp2
 import logging
 from google.appengine.api import urlfetch
+import json
 
 FACEBOOK_APP_ID = "839210319436433"
 FACEBOOK_APP_SECRET = "cbeeee3e0e9594e802d44a1016f23569"
 @@ -41,9 +42,15 @@ def post(self):
                 };
         form_data = urllib.urlencode(data)
         url = "https://graph.facebook.com/v2.1/me/feed"
-        result = urlfetch.fetch(url=url,payload=form_data,method=urlfetch.POST,headers={'Content-Type': 'application/x-www-form-urlencoded'})
-        self.redirect("/")
+        result = urlfetch.fetch(url=url,payload=form_data,method=urlfetch.POST)
+        content = json.loads(result.content)
         
+        if(content.get("id")):
+           self.response.write('<script>alert("Message posted to facebook.");window.location.assign("/")</script>')
+        elif content["error"]["error_user_title"]:
+            self.response.write('<script>alert("'+content["error"]["error_user_title"]+'");window.location.assign("/")</script>')
+        else:
+            self.response.write('<script>alert("An error occured.");window.location.assign("/")</script>')
        
 application = webapp2.WSGIApplication([
     ('/', MainHandler),
