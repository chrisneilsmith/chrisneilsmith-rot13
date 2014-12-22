#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

form = """
<html>
	<head>
		<title>Chris Smith's Rot 13 Cipher for Udacity CS 253</title>
	</head>
	<body>
		<h1>Enter some text to Rot13:</h1>
		<form method='post'>
			<textarea name="user_input" style="height: 100px; width: 400px;">%(user_input)s</textarea>
			<br>
			<br>
			<input type='submit'>
		</form>
	</body>
</html>
"""

def escape_html(s):
	return cgi.escape(s, quote=True)

def rot13(s):
	return

class MainHandler(webapp2.RequestHandler):
    def write_form(self, user_input=""):
        self.response.out.write(form % {"user_input": user_input})

    def get(self):
    	#self.response.write('Soon to be a Rot 13 cipher here!')
        self.write_form()

    def post(self):
	    user_input = self.request.get("user_input")
	    self.write_form(escape_html(user_input))



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
