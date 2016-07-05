# Accessing Twitter API 
# Twitter has two APIs, Streaming APIs, and other one is RESTful APIs

try:
	import json
except ImportError:
	import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Authentication tokens for accessing the APIs
ACCESS_TOKEN = '3260949332-GsQhU60z94XZA012BbcgsJmT9EOFZEfbVW6zboW'
ACCESS_SECRET = 'NjxFN3dpdvmE4iZ0ci2wV5wfdeEqnmmMJssczSJv61fpf'
CONSUMER_KEY = 'NXXzhmDN1kcu3N7YPxf8y7qvp'
CONSUMER_SECRET = 'vViSlyPlHkueZCrEPTnQJ5PP8ET8iVHNmFh6G4RRSkcpDiCFPT'

# Create OAuth object
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Using Streaming API, so create a connection to this API
twitter_stream_api = TwitterStream(auth=oauth)

# Get the current data from the twitter
sample = twitter_stream_api.statuses.filter(track="twitter", locations="-74,40,-73,41")

# Set the tweet count
tweet_count = 50

for tweet in sample:

	# Decrement the tweet count
	tweet_count-=1

	print json.dumps(tweet)

	# Stop as soon as tweet_count becomes zero or no tweet to search for
	if tweet_count<=0:
		break

