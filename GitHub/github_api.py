# Access the github api

import requests

import json

def github_api(username):
	new_data = []
	api_endpoint = 'https://api.github.com/users/' + str(username)
	req_obj = requests.get(api_endpoint)
	if not req_obj:
		print("Invalid username! Try again.")
		exit(0)
	json_data = []
	content = req_obj.text
	retrieve_data = json.loads(req_obj.content)
	json_data.append(retrieve_data)
	user_data = {} # User data extracted from the api
	for data in json_data:
		user_data['name'] = data['name']
		user_data['blog'] = data['blog']
		user_data['email'] = data['email']
		user_data['public_gists'] = data['public_gists']
		user_data['public_repos'] = data['public_repos']
		user_data['avatar_urls'] = data['avatar_url']
		user_data['followers'] = data['followers']
		user_data['following'] = data['following']
	new_data.append(user_data)

	print new_data

if __name__ == "__main__":
	github_api(raw_input())

