import urllib

import json

def map_api(address):
	api_endpoint = 'http://maps.googleapis.com/maps/api/geocode/json?'
	flag = True

	while flag:
	
		if len(address)<1:
			break
		url = api_endpoint + urllib.urlencode({'sensor': 'false', 'address': address})
		print 'Getting the information from', url
		obj = urllib.urlopen(url)
		data = obj.read()
		print 'Retrieved ', len(data), ' characters'
		try:
			js = json.loads(str(data))
		except:
			js = None

		if 'status' not in js or js['status']!='OK':
			print 'Error getting the information'
			print data
			continue

		print json.dumps(js, indent=4)
		lat = js["results"][0]["geometry"]["location"]["lat"] 
		lng = js["results"][0]["geometry"]["location"]["lng"] 
		print 'lat',lat,'lng',lng
		location = js['results'][0]['formatted_address'] 
		print location

if __name__ == '__main__':
	map_api(raw_input("Enter the location to search:"))
