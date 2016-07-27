import urllib

from json import load

def open_weather(location):
	api_endpoint = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&units=metric&appid=cb932829eacb6a0e9ee4f38bfbf112ed'
	obj = urllib.urlopen(api_endpoint)
	data = load(obj)
	json = []
	json.append(data)
	for item in json:
		print item['name']
		print item['weather']
		
if __name__ == '__main__':
	open_weather(raw_input())
