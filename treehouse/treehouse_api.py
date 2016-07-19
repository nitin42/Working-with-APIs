# Access the treehouse api

import requests

import json

def treehouse(username):
	api_endpoint = "http://teamtreehouse.com/" + str(username) + ".json"
	req_obj = requests.get(api_endpoint)
	if not req_obj:
		print ("Invalid username! Try again")

	content = req_obj.text
	data = []
	json_data = json.loads(req_obj.content)
	data.append(json_data)
	user_data = {}
	dumps = []

	for item in data:
		user_data['name'] = item['name']
		user_data['profile_name'] = item['profile_name']
		user_data['profile_url'] = item['profile_url']
		user_data['badges'] = item['badges']
	dumps.append(user_data)

if __name__ == "__main__":
	treehouse(raw_input())