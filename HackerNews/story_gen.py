import requests

import json

def hacker_news(news_id):
	api_endpoint = 'https://hacker-news.firebaseio.com/v0/item/' + news_id + '.json?print=pretty' 
	obj = requests.get(api_endpoint)
	data = json.loads(obj.content)
	for item in data:
		print item[0] # By
		print item[5] # score
		print item[7] # title
		print item[8] # type
		print item[9] # url to the story

if __name__ == '__main__':
	hacker_news(int(raw_input()))