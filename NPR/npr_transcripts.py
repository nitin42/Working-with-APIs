from urllib2 import urlopen
from json import load

key = "API_KEY"

url = 'http://api.npr.org/transcript?apiKey=API_KEY'
url += '&format=json&id=152248901'

response = urlopen(url)
j = load(response)


#print transcript paragraphs
for paragraph in j["paragraph"]:
	print paragraph["$text"] + "\n"