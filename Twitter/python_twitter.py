# Accessing Twitter API 
# Twitter has two APIs, Streaming APIs, and other one is RESTful APIs

try:
	import json
except ImportError:
	import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Authentication tokens for accessing the APIs
ACCESS_TOKEN = '**************************' # Your access token
ACCESS_SECRET = '************************' # Your secret key		
CONSUMER_KEY = '***************' # Your consumer key
CONSUMER_SECRET = '*********************************' # Your consumer secret

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

