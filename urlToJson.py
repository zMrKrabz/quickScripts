"""
Translates url encoded string into json object that is prettier
when creating requests objects. The path will be in the path key
in the returned json object
"""

from urllib.parse import unquote
import json

def urlToJson(url):
	split = encodedUrl.split("?")

	# If the user just submits a payload with no URL (such as from fiddler) just make body
	if len(split) > 1:
		path = encodedUrl.split("?")[0]
		decodedBody = unquote(encodedUrl.split("?")[1])
	else:
		path = 'Not Found'
		decodedBody = unquote(encodedUrl)

	obj = {}
	obj['path'] = path
	obj['body'] = {}

	params = decodedBody.split('&')

	for param in params:
		splitted = param.split('=')

		key = splitted[0]
		value = splitted[1]
		obj['body'][key] = value

	return obj

print("Please paste the URL you with to parse.")
encodedUrl = input()
print(urlToJson(encodedUrl))