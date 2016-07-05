### Getting Twitter API keys
- Go [here](https://apps.twitter.com/) and log in with your Twitter user account. This step gives you a Twitter dev account under the same name as your user account.
- Click “Create New App”. 
- Fill out the form, agree to the terms, and click “Create your Twitter application”.
- In the next page, click on “Keys and Access Tokens” tab, and copy your “API key” and “API secret”. Scroll down and click “Create my access token”, and copy your “Access token” and “Access token secret”.


### Installing required libraries
- I have used a Python library called Python Twitter Tools to connect to Twitter API and downloading the data from Twitter. There are many other libraries in various programming languages that let you use Twitter API. But this one is simple to use, so I personally recommend this.
- Download the Python Twitter tools [here](https://pypi.python.org/pypi/twitter).
- To install the package, type this into your terminal
```
$ python setup.py build
$ python setup.py install
```
### Streaming API
The Streaming APIs give access to (usually a sample of) all tweets as they published on Twitter. On average, about 6,000 tweets per second are posted on Twitter and you (normal dev users) will get a small proportion (<=1%) of it. The Streaming APIs are one of the two types of Twitter APIs. The other one called REST APIs (we will talk about later in this tutorial), which is more suitable for singular searches, such as searching historic tweets, reading user profile information, or posting Tweets. The Streaming API only sends out real-time tweets, while the Search API (one of the popular REST APIs) gives historical tweets up to about a week with a max of a couple of hundreds. You may request elevated access (e.g. Firehose, Retweet, Link, Birddog or Shadow) for more data by contacting Twitter’s API support.

To learn more about Twitter's API with examples, start [here](https://github.com/ideoforms/python-twitter-examples).
