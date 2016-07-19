from urllib2 import urlopen
from urllib import quote

key = "API_KEY"
url = 'http://api.npr.org/query?apiKey='
url += key
url += '&numresults=3&action=Or&requiredAssets=audio&format=Podcast'

npr_id = raw_input("Enter comma-separated NPR IDs or leave blank.")
search_string = raw_input("Enter your search string or leave blank.")
feed_title = raw_input("What's your feed title?")

if npr_id or search_string:
    raw_input("Hit Enter to download your podcast.")

    if npr_id:
        url += '&id=' + npr_id

    if search_string:
        url += '&searchTerm=' + quote(search_string)

    if feed_title:
        url += '&title=' + quote(feed_title)
    
    response = urlopen(url)
    output = response.read()
    my_feed = open("feed.xml", 'w') 
    my_feed.write(output) # Write your custome podcasts into the feed.xml file and generate your podcasts.
    my_feed.close()

else:
    print "You must enter an NPR ID, a search term, or both."
    