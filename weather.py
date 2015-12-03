import urllib.parse
import urllib.request
import chartjs

start_year = 2981
end_year = 2013
weather_station = 5097

while start_year <= end_year:
	url = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID={0}&Year={1}".format(str(weather_station), str(start_year))
	start_year++
	req = urllib.request.Request(url)
	stream = urllib.request.urlopen(req)
	result = stream.read()
	charset = stream.info().get_param('charset', 'utf8')
	print(result.decode(charset))
