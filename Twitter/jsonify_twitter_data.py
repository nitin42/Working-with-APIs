# Accessing Twitter API 
# Twitter has two APIs, Streaming APIs, and other one is RESTful APIs

try:
	import json
except ImportError:
	import simplejson as json

filename = "twitter_data.txt" # Open the file in which data was stored

open_file = open(filename, 'r') # Open the file in read mode

for line in open_file:
	try: # If the line is in JSON format
		tweet_obj = json.loads(line.strip()) # Create the json object of the file and read the text in one line

		if 'text' in tweet_obj: # Because tweet is present in text field
			print tweet_obj['id']
			print tweet_obj['created_at']
			print tweet_obj['text']

			print tweet_obj['user']['id']
			print tweet_obj['user']['name']
			print tweet_obj['user']['screen_name']

			hashes = [] # Storing the hashtags

			for i in tweet_obj['entities']['hashtags']: # Present inside this nested dictionary
				hashes.append(i['text']) # Present in the text field
			print hashes

	except: # If the line is not in JSON format
		continue
