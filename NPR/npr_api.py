from urllib2 import urlopen
from json import load

url = "http://api.npr.org/query?apiKey="
key = "API_KEY"

url+=key
url+='&numResults=3&format=json&id='
npr_id = raw_input()
url+=npr_id

#print url

response = urlopen(url)
json_obj = load(response)

# Stories are present in the list dictionary
for story in json_obj['list']['story']:
    print story['title']['$text']

