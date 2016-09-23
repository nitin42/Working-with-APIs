import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

def analyze(username):
	twitter_consumer_key = 'NXXzhmDN1kcu3N7YPxf8y7qvp'
	twitter_consumer_secret = 'vViSlyPlHkueZCrEPTnQJ5PP8ET8iVHNmFh6G4RRSkcpDiCFPT'
	twitter_access_token = '3260949332-GsQhU60z94XZA012BbcgsJmT9EOFZEfbVW6zboW'
	twitter_access_secret = 'NjxFN3dpdvmE4iZ0ci2wV5wfdeEqnmmMJssczSJv61fpf'

	twitter_api = twitter.Api(consumer_key=twitter_consumer_key, 
								consumer_secret=twitter_consumer_secret, 	
								access_token_key=twitter_access_token, 
								access_token_secret=twitter_access_secret)


	statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

	text = "" # Store the retrieved info 

	for status in statuses:
  		if (status.lang =='en'): # English tweets
  			text += status.text.encode('utf-8') 

	# The IBM Bluemix credentials for Personality Insights!
	pi_username = '91afa133-d7a9-469f-95e9-a38cb2c500f4'
	pi_password = 'EUiG6T4wGG7j'

	personality_insights = PersonalityInsights(username=pi_username, password=pi_password)

	result = personality_insights.profile(text)
	return result

def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                                data[c3['id']] = c3['percentage']
    return data
  
def compare(dict1, dict2):
	compared_data = {}
	for keys in dict1:
		if dict1[keys] != dict2[keys]:
			compared_data[keys]=abs(dict1[keys] - dict2[keys])
	return compared_data
 

user_handle = "@NTulswani"
celebrity_handle = "@narendramodi"

user_result = analyze(user_handle)
celebrity_result = analyze(celebrity_handle)

#First, flatten the results from the Watson PI API
user = flatten(user_result)
celebrity = flatten(celebrity_result)

#Then, compare the results of the Watson PI API by calculating the distance between traits
compared_results = compare(user,celebrity)

sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))

for keys, value in sorted_result:
    print keys,
    print(user[keys]),
    print ('->'),
    print (celebrity[keys]),
    print ('->'),
    print (compared_results[keys])


# Don't misuse my API keys. They have been provided for your convenience and I hope I can trust you!
