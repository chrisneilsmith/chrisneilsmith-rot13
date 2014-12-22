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
		<h1>Welcome to Chris Smith's Rot13 Web App</h1>

		<p>When you hit submit, this web app will rotate each letter 13 places, but leave all other characters and spacing in tact.</p>
		<p>Give it a try. Enter some text and then hit submit.</p>

		<form method='post'>
			<textarea name="text" style="height: 100px; width: 400px;">%(text)s</textarea>
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
    output = ""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in s:
        if letter in lowercase and letter <= "m":
            output += chr(ord(letter) + 13)
        elif letter in lowercase and letter > "m":
            output += chr(ord(letter) - 13)
        elif letter in uppercase and letter <= "M":
            output += chr(ord(letter) + 13)
        elif letter in uppercase and letter > "M":
            output += chr(ord(letter) - 13)
        else:
            output += letter

    return output

class MainHandler(webapp2.RequestHandler):
    def write_form(self, text=""):
        self.response.out.write(form % {"text": text})

    def get(self):
    	#self.response.write('Soon to be a Rot 13 cipher here!')
        self.write_form()

    def post(self):
	    text = self.request.get("text")
	    self.write_form(escape_html(rot13(text)))

	

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
