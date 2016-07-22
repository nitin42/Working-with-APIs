'''Hacker-News API built on the top of firebaseio. To retreive the top stories, we generate a random id 
because each story is associated with a unique id. Uncomment the second method and comment the first one if 
you want to generate the news by specifying a particular id instead of randomly generating'''

from random import randint

import requests
import json

api_endpoint = 'https://hacker-news.firebaseio.com/v0/item/' + str(randint(1,100000)) + '.json?print=pretty' 
obj = requests.get(api_endpoint)
res = obj.content
data = json.loads(res)
print data

# def hacker_news(news_id):
	# api_endpoint = 'https://hacker-news.firebaseio.com/v0/item/' + str(news_id) + '.json?print=pretty' 
	# obj = requests.get(api_endpoint)
	# res = obj.content
	# data = json.loads(res)
	# print data


# if __name__ == '__main__':
	# hacker_news(int(raw_input()))
