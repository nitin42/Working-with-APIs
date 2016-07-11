# Foursquare API

import requests

import json

api_endpoint = 'https://api.foursquare.com/v2/venues/explore?v=20131016&ll=26.2684100%2C%2073.0059400&section=food&novelty=new&oauth_token=ANSS5YMO5OO0TDQNS4EHGZSFK4U2PBD4BPT2IV5QQOXK4ZDK'

obj = requests.get(api_endpoint)
data = json.loads(obj.content)

for item in data['response']:
	print item['groups']['venues']