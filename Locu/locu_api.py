# Locu API

import requests

import json


def search_restaurant(locality):
	api_key = "bb5f92fb7f236891948704449f13f083ce2c1978"
	api_endpoint = "http://api.locu.com/v1_0/venue/search/"
	#locality = 'Delhi'
	category = "restaurant"
	api_url = api_endpoint + "?locality=" + str(locality) + "&category=" + category + "&api_key=" + api_key

	res = requests.get(api_url)
	data = json.loads(res.content)
	for item in data["objects"]:
		print (item["name"]) #+ " --> " + item["phone"])
		print venue_details(item["id"])

def venue_details(venue_id):
	api_key = "bb5f92fb7f236891948704449f13f083ce2c1978"
	api_endpoint = "http://api.locu.com/v1_0/venue/"
	#locality = 'Delhi'
	#category = "restaurant"
	api_url = api_endpoint  + venue_id + "/" +"?api_key=" + api_key

	res = requests.get(api_url)
	data = res.json()
	return data["objects"][0]["name"], data["objects"][0]["has_menu"], data["objects"][0]["phone"]


if __name__ == "__main__":
	search_restaurant(raw_input())	
