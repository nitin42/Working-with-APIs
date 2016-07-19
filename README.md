# Python-APIs

Access the third party APIs using Python, JavaScript and Ruby.

Popular APIs

1. [GitHub](https://developer.github.com/)
2. [Twitter](https://dev.twitter.com/)
3. [Youtube](https://www.youtube.com/yt/dev/)
4. [Locu](https://dev.locu.com/)
5. [Foursquare](https://developer.foursquare.com/)
6. [NPR](www.npr.org/api/index)
7. [Evernote](https://dev.evernote.com/)
8. [DWOLLA](https://developers.dwolla.com/)
9. [WePay](https://www.wepay.com/developer)
10. [SoundCloud](https://developers.soundcloud.com/docs/api/guide)
11. [box](https://developer.box.com/)
12. [NHTSA](www.nhtsa.gov/webapi/Default.aspx?Recalls/API/83)
13. [SendGrid](https://sendgrid.com/docs/API_Reference/Web_API/)
14. [Facebook(Graph API)](https://developers.facebook.com/)

## Using APIs with Python

- **Making a request**
To make a HTTp request, we use ```urlopen()``` method for GET request and then read the response as ```response_object.read()```. Remember the four verbs when dealing with HTTP request i.e GET, POST, PUT and DELETE.
To post or get the data as response from an API, always remember about the endpoints of the API.

- **The Response**
When we get the response from the server, it will be in the form of three digit code status indicating about the situation.
Below are some status code:
> 
- 1xx - Server is working on something!
- 2xx - Success
- 3xx - Incase the url requested is changed, the server responds after getting the response from the new or altered url
- 4xx - Mistake made by client
- 5xx - Mistake made by server or some obfuscated request to the server.

- **Parsing JSON**
To parse the response which is either received in JSON or XML format we import json and xml.dom. To work with JSON,
use ```load()``` to load the JSON response. To work with XML, consider this example,
> 
from xml.dom import minidom

f = open('example.txt', 'r')
pets = minidom.parseString(f.read())
f.close()

names = pets.getElementsByTagName('name')
for name in names:
	print name.firstChild.nodeValue



