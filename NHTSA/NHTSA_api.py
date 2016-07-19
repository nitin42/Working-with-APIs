from urllib2 import urlopen
from json import load

apiUrl = 'http://www.nhtsa.gov/webapi/api/SafetyRatings'

apiParam = '/VehicleId/7045' # Pass any valid paramters and check your results

outputFormat = '?format=json'

response = urlopen(apiUrl + apiParam + outputFormat)

json_obj = load(response)

print '------------------------------'
print '           Result			 '
print '------------------------------'
for objectCollection in json_obj['Results']:
	# Loop each vehicle in the vehicles collection
    for safetyRatingAttribute, safetyRatingValue in objectCollection.iteritems():
        print safetyRatingAttribute, ": ", safetyRatingValue
