import urllib2, json, pprint

url = "http://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&sensor=false"

# send address to google
googleResponse = urllib2.urlopen(url)
# convert google response from json to python object
jsonResponse = json.loads(googleResponse.read())

# walk through google response indices to get lat & lng, converting to strings
lat = str(json.dumps([s['geometry']['location']['lat'] for s in jsonResponse['results']]))[1:-1]
lng = str(json.dumps([s['geometry']['location']['lng'] for s in jsonResponse['results']]))[1:-1]

# insert lat and lng into fcc api call
fccurl = 'http://data.fcc.gov/api/block/find?format=json&latitude=' + lat + '&longitude=' + lng

# send lat & lng request to fcc, get fips code back
fccResponse = urllib2.urlopen(fccurl)
# convert fcc response from json to python object
fccjsonResponse = json.loads(fccResponse.read())

# walk through fcc response indices to retrieve fips code
fips = str(fccjsonResponse['Block']['FIPS'])

# positions within fips http://www.geolytics.com/USCensus,Geocode,Data,Geography,Products.asp
state = fips[0:2]
county = fips[2:5]
tract = fips[5:11]

# census api key
census_key = 'b6665d8653b770fd34a25cb60c6cfdc2343f4f5d'

# census table
census_table = 'B00001_001E'

# census year (most recent available)
census_year = '2011'

# acs_period
acs_period = 'acs5'

# census api call http://api.census.gov/data/2011/acs5/geo.html
census_url = 'http://api.census.gov/data/' + census_year + '/' + acs_period + '?key=' + census_key + '&get=' + census_table + '&for=tract:' + tract + '&in=state:' + state + '+county:' + county

print(census_url)

# send state/county/tract, table to census and get data back
census_response = urllib2.urlopen(census_url)
# convert census response from json to python object
census_json_response = json.loads(census_response.read())[1]
census_data = census_json_response + '123 fake street'

pprint.pprint(census_data)

# walk through fcc response indices to retrieve fips code
# fips = str(fccjsonResponse['Block']['FIPS'])

