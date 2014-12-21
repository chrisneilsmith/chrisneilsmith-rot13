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
			<input type='textarea' style="height: 100; width: 400">
			</input>
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
    def get(self):
        self.response.write('Soon to be a Rot 13 cipher here!')
        self.response.write(form)

    #def post(self):
    	

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
